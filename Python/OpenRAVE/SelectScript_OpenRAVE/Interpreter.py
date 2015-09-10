import operator, threading
import numpy as np
import ssFunction
from openravepy import *

import SelectScript
import SelectScript.Interpreter


class Interpreter(SelectScript.Interpreter):
    def __init__(self):
        SelectScript.Interpreter.__init__(self)
        self.initFunctions()
        self.timer_list = {}

        self.environment = None

    def initFunctions(self):
        self.addFunction('id', ssFunction._identifer, "Returns the identifier of a sensor, robot, or kinbody.\nUsage: id(object) -> string")
        self.addFunction('type', ssFunction._type, "Returns the type of an object.\nUsage: type(object)")
        self.addFunction('position', ssFunction._position, "Returns a list of the x,y,z coordinates of an object.\nUsage: position(object, begin, end)\n       position(object) -> [x,y,z]\n       position(object, 0,2) -> [x,y]")
        self.addFunction('pose', ssFunction._pose, "Returns the pose of an object.\nUsage: pose(object) -> XXX")
        self.addFunction('distance', ssFunction._distance, "Calculates the euclidian distance of two objects.\nUsage: distance(object1, object2) -> float")

        self.addFunction('volume', ssFunction._volumeAABB, "Approximates the volume of an object by using AABB.\nUsage: volume(object) -> float")

        self.addFunction('isRobot', ssFunction._isRobot, "Checks if object is of type Robot.\nUsage: isRobot(object) -> bool")
        self.addFunction('isSensor', ssFunction._isSensor, "Checks if object is of type Sensor.\nUsage: isSensor(object) -> bool")
        self.addFunction('isKinbody', ssFunction._isKinbody, "Checks if object is of type Kinbody.\nUsage: isKinbody(object) -> bool")

        self.addFunction('robot', ssFunction._robot)
        self.addFunction('sensor', ssFunction._sensor)
        self.addFunction('kinbody', ssFunction._kinbody)

        self.addFunction('obj', ssFunction._object, "Returns the object itself.\nUsage: obj(object) -> object")

        self.addFunction('x', ssFunction._positionX, "Returns only the x position.\nUsage: x(object) -> float")
        self.addFunction('y', ssFunction._positionY, "Returns only the y position.\nUsage: y(object) -> float")
        self.addFunction('z', ssFunction._positionZ, "Returns only the z position.\nUsage: z(object) -> float")

        self.addFunction('isEnabled', ssFunction._isEnabled, "Checks if object is enabled.\nUsage: isEnabled(object) -> bool")
        self.addFunction('isVisible', ssFunction._isVisible, "Checks if object is visable.\nUsage: isVisable(object) -> bool")

        self.addFunction('isSensing', ssFunction._isSensing, "Checks if a sensor is currently sensing a certain object.\nUsage: isSensing(sensor, object) -> bool")
        self.addFunction('environmentID', ssFunction._getEnvironmentID, "Returns the OpenRAVE environment id of an object.\nUsage: environmentID(object) -> XXX")

        self.addFunction('sensingAmount', ssFunction._sensingAmount, "Calculates how much of XXX")
        self.addFunction('sensingEnvIDs', ssFunction._sensingEnvironmentIDs)

        self.addFunction('above', ssFunction._above, "Checks if the position of an object (o2) is above object (o1), by using the axis-aligned bounding box of o1.\nUsage: above(o1, o2) -> bool")
        self.addFunction('below', ssFunction._below, "Checks if the position of an object (o2) is below object (o1), by using the axis-aligned bounding box of o1.\nUsage: below(o1, o2) -> bool")
        self.addFunction('within', ssFunction._within, "Checks if the position of an object (o2) is within object (o1), by using the axis-aligned bounding box of o1.\nUsage: within(o1, o2) -> bool")

        self.addFunction('oFrom', ssFunction._objectFrom, "todo\nUsage: oFrom(id, environment) -> object")

        self.addFunction('checkCollision', ssFunction._checkCollision, "Checks if a collision with the entity has occured.\nUsage: checkCollision(object) -> bool")
        self.addFunction('move', ssFunction._moveObjectToPosition, "")

        self.addFunction('getTime', self.getTime )

    def callFunction(self, name, params):

        try:
            #if "env" in self.fct_list[name].func_code.co_varnames:
            return self.fct_list[name](*params, env=self.environment)
        except:
            return self.fct_list[name](*params)

    def callVariable(self, name, age=0):
        if name == "environment":
            return self.environment

        return SelectScript.Interpreter.callVariable(self, name, age)

    def getListFrom(self, obj):
        if isinstance(obj, openravepy_int.Environment):
            return obj.GetSensors() + obj.GetBodies()
        else:
            return SelectScript.Interpreter.getListFrom(self, obj)

    def trigger(self, name, prog, t, callback):
        if self.timer_list.has_key(name):
            #prog, t, callback, old = self.timer_list[name]
            #print self.callVariable('env').GetSimulationTime() /200000.
            #print self.callVariable('env').IsSimulationRunning()

            old_result = self.timer_list[name]

            threading.Timer(t, self.trigger, [name, prog, t, callback]).start()

            result=self.eval(prog)

            if result != old_result:
                self.timer_list[name] = result
                callback(result)

    def addEnvironment(self, env):
        self.environment = env

    def addTrigger(self, name, prog, t, callback):
        self.timer_list[name] = None #[prog, t, callback, None]
        self.trigger(name, prog, t, callback)

    def delTrigger(self, name):
        self.timer_list.pop(name)

    def getTime(self):
        return self.callVariable('env').GetSimulationTime()/200000.

    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == "environment":
            results = self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
            return self.evalAs_environment(PARAMS, results)
        elif AS == "occupancygrid":
            results = self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
            results = self.evalAs_environment(PARAMS, results)
            #results = self.evalAs("environment", [], SELECT, FROM_n, RESULTS)
            return self.evalAS_OccupancyGrid(PARAMS, results)
        elif AS == "sensorgrid":
            results = self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
            results = self.evalAs_environment(PARAMS, results)
            return self.evalAS_SensorGrid(PARAMS, results)
        elif AS == "sensorrangegrid":
            results = self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
            results = self.evalAs_environment(PARAMS, results)
            return self.evalAS_SensorRangeGrid(PARAMS, results)
        elif AS == "prolog":
            return self.evalAs_Prolog(PARAMS, SELECT, FROM_n, RESULTS)
        else:
            return SelectScript.Interpreter.evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS)

    def evalAs_environment(self, PARAMS, RESULTS):

        RESULTS = list(set(RESULTS))

        if RESULTS == []:
            return openravepy_int.Environment()

        newEnv = RESULTS[0].GetEnv().CloneSelf(0b11111111)
        ids = []
        for elem in RESULTS:
            if type(elem) in [openravepy_int.Robot, openravepy_int.KinBody, openravepy_int.Sensor]:
                ids.append(elem.GetName())

        # remove sensors
        for elem in newEnv.GetSensors():
            if not elem.GetName() in ids:
                if not newEnv.Remove( newEnv.GetSensor(elem.GetName()) ):
                    elem.Configure(Sensor.ConfigureCommand.PowerOff)
                    elem.Configure(Sensor.ConfigureCommand.RenderDataOff)
        # remove robots
        for elem in newEnv.GetRobots():
            if not elem.GetName() in ids:
                newEnv.Remove( newEnv.GetRobot(elem.GetName()) )
        # remove bodies
        for elem in newEnv.GetBodies():
            if not elem.GetName() in ids:
                #print elem.GetName()
                newEnv.Remove( newEnv.GetKinBody(elem.GetName()) )

        return newEnv

    def evalAS_OccupancyGrid(self, PARAMS, RESULTS):
        openravepy_int.RaveInitialize()

        z_pos     = PARAMS[0]
        grid_size = PARAMS[1]

        pos, size = self._calcSize(RESULTS, grid_size)

        ogMap = RaveCreateModule(RESULTS, 'occupancygridmap')
        ogMap.SendCommand('SetTranslation %f %f %f' % (pos[0], pos[1], z_pos))
        ogMap.SendCommand('SetSize %i %i %f' %(size[0]+1, size[1]+1, grid_size) )

        render = ogMap.SendCommand('Scan')

        return np.fromstring(render, dtype=bool, count=-1, sep='').reshape(int(size[0]+1), int(size[1]+1))


    def evalAS_SensorGrid(self, PARAMS, RESULTS):
        openravepy_int.RaveInitialize()

        z_pos = PARAMS[0]
        grid_size = height = PARAMS[1]
        if len(PARAMS) == 3:
            height    = PARAMS[2]

        pos, size = self._calcSize(RESULTS, grid_size)
        #print RESULTS.GetSensors()
        ogMap = RaveCreateModule(RESULTS, 'sensorcubemap')
        print 'SetTranslation %f %f %f' % (pos[0], pos[1], z_pos)
        print 'SetSize %i %f %i %f 1 %f' % (size[0]+1, grid_size, size[1]+1, grid_size, height)
        ogMap.SendCommand('SetTranslation %f %f %f' % (pos[0], pos[1], z_pos))
        ogMap.SendCommand('SetSize %i %f %i %f 1 %f' % (size[0]+1, grid_size, size[1]+1, grid_size, height) )
        render = ogMap.SendCommand('Scan')

        return np.fromstring(render, dtype=int, count=-1, sep=' ').reshape(int(size[0]+1), int(size[1]+1))

    def evalAS_SensorRangeGrid(self, PARAMS, RESULTS):
        openravepy_int.RaveInitialize()

        z_pos     = PARAMS[0]
        grid_size = PARAMS[1]

        pos, size = self._calcSize(RESULTS, grid_size)

        ogMap = RaveCreateModule(RESULTS, 'rangegridmap')
        ogMap.SendCommand('SetTranslation %f %f %f' % (pos[0], pos[1], z_pos))
        ogMap.SendCommand('SetSize %i %i %f' %(size[0]+1, size[1]+1, grid_size) )

        render = ogMap.SendCommand('Scan')
        #return (render, pos[0], pos[1], grid_size, size[0], size[1])
        return np.fromstring(render, dtype=float, count=-1, sep=' ').reshape(int(size[0]+1), int(size[1]+1))

    def _calcSize(self, env, grid_size):
        envmin = envmax = []
        for b in env.GetBodies():
            ab = b.ComputeAABB()
            envmin.append((ab.pos()-ab.extents())[0:2])
            envmax.append((ab.pos()+ab.extents())[0:2])

        envmin = np.floor(np.min(np.array(envmin), 0)*100.) / 100
        envmax = np.ceil( np.max(np.array(envmax), 0)*100.) / 100
        size   = ((envmax - envmin) / grid_size)

        return (envmin, size)

    def evalAs_Prolog(self, PARAMS, SELECT, FROM_n, RESULTS):
        results = set()
        for elem in RESULTS:

            for f in SELECT:

                if f[1] == 'to' :
                    result, relation = self.eval(f, elem, FROM_n)
                    pp = f[2][0][2]
                else:
                    relation = f[1]
                    result = self.eval(f, elem, FROM_n)

                    if f[0] == SelectScript.SelectScript.types['phrase']:
                        pp = [[SelectScript.SelectScript.types['this'], '']]
                    else:
                        pp = f[2]

                if result != False:
                        clause = relation + "("
                        for p in pp:
                            p = self.eval(p, elem, FROM_n)
                            if isinstance(p, (openravepy_int.Robot, openravepy_int.Sensor, openravepy_int.KinBody)):
                                p = p.GetName()
                            clause += str(p) + ","
                        clause = clause[:-1] + ")"

                        if result != True:
                            clause = clause[:-1] + ","+str(result)+")"

                        results.add(clause)

        return sorted(results)
