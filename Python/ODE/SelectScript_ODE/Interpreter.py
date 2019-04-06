import threading
import ode
from functions import *
import SelectScript.Interpreter

import numpy as np
import pygame

class Interpreter(SelectScript.Interpreter):

    def __init__(self):
        self.current_time = 0
        SelectScript.Interpreter.__init__(self)
        self.initFunctions()

    def initFunctions(self):
        self.addFunction('pos',            Sode_position,     "Returns a list of the x,y,z coordinates of an object.\nUsage: pos(object, begin, end)\n       pos(object) -> [x,y,z]\n       pos(object, 0,2) -> [x,y]")
        self.addFunction('posX',           Sode_posX,         "Returns only the x coordinate of an object.\nUsage: posX(object) -> float")
        self.addFunction('posY',           Sode_posY,         "Returns only the y coordinate of an object.\nUsage: posY(object) -> float")
        self.addFunction('posZ',           Sode_posZ,         "Returns only the z coordinate of an object.\nUsage: posZ(object) -> float")
        self.addFunction('rot',            Sode_rotation,     "Returns ")
        self.addFunction('quat',           Sode_quaternion)
        self.addFunction('aabb',           Sode_aabb)
        self.addFunction('obj',            Sode_obj,           "Returns the object itself.\nUsage: obj(object) -> object")
        self.addFunction('type',           Sode_type)
        self.addFunction('torque',         Sode_torque)
        self.addFunction('force',          Sode_force)
        self.addFunction('velocity',       Sode_velocity)
        self.addFunction('linearVelocity', Sode_LinearVel)

        self.addFunction('id',             Sode_identifer)

        self.addFunction('isEnabled',      Sode_isEnabled)
        self.addFunction('isSpace',        Sode_isSpace)
        self.addFunction('gravityMode',    Sode_gravityMode)

        self.addFunction('isGeom',         Sode_isGeom)
        self.addFunction('isBox',          Sode_isBox)
        self.addFunction('isCapsule',      Sode_isCapsule)
        self.addFunction('isCCylinder',    Sode_isCCylinder)
        self.addFunction('isCylinder',     Sode_isCylinder)
        self.addFunction('isHeightfield',  Sode_isHeightfield)
        self.addFunction('isPlane',        Sode_isPlane)
        self.addFunction('isRay',          Sode_isRay)
        self.addFunction('isSphere',       Sode_isSphere)
        self.addFunction('isTransform',    Sode_isTransform)
        self.addFunction('isTriMesh',      Sode_isTriMesh)

        self.addFunction('collision',      Sode_collision)
        self.addFunction('uniq',           Sode_unique)
        self.addFunction('distance',       Sode_distance)

        self.addFunction('getTime',        self.getTime)

        self.addFunction('mass',           Sode_mass,    "Returns the mass of an object.\nUsage: mass(object) -> float")
        self.addFunction('volume',         Sode_volume,  "Returns the volume of an object.\nUsage: volume(object) -> float")
        self.addFunction('hasBody',        Sode_hasBody)
        self.addFunction('quantum',        Sode_quantum)

        self.addFunction('sum',   sum, "Calculate the sum values within a list.\nUsage: sum([float, int, ...]) -> float")
        self.addFunction('max',   max)
        self.addFunction('min',   min)
        self.addFunction('count', len)


    def getListFrom(self, obj):
        if isinstance(obj, ode.SimpleSpace):
            return self.getSpaceGenerator(obj)
        else:
            return SelectScript.Interpreter.getListFrom(self, obj)

    def getSpaceGenerator(self, obj):
        for i in range(obj.getNumGeoms()):
            yield obj.getGeom(int(i))

    def getTime(self):
        return self.current_time

    def setTime(self, curr_time):
        self.current_time = curr_time

    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == "sound":
            results = self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
            return self.evalAs_sound(PARAMS, results)

        elif AS == "plane":
            SELECT.append( [0, 'to', [[0, 'pos', [[5, '']]], [3, '__pos']]] ) # to(pos(this),'__pos')
            results = self.evalAS_dict([], SELECT, FROM_n, RESULTS)
            return self.evalAs_plane(PARAMS, results)

        return SelectScript.Interpreter.evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS)

    def evalAs_sound(self, PARAMS, RESULTS):
        pygame.init()
        effect = pygame.mixer.Sound('beep.wav')

        count = len(RESULTS)

        for _ in range(RESULTS.count(None)):
            RESULTS.remove(None)

        if isinstance(RESULTS, list):
            value = sum(RESULTS)
        else:
            value = RESULTS

        if count > 0:
            effect.set_volume(value)
            effect.play(count)

        return []

    def evalAs_plane(self, PARAMS, RESULTS):
        plane = PARAMS[0].lower() # 'XY', 'XZ', 'YZ'
        start = PARAMS[1]         # [x, y]
        dim   = PARAMS[2]         # [width, height, resolution]
        blur  = False             # like gaussian filter

        if len(PARAMS) == 4:
            if PARAMS[3] > 1:
                blur = PARAMS[3]
                blur_matrix = np.matrix([[(1.+blur-abs(i)-abs(j)) for j in range(-blur+1, blur, 1) ] for i in range(-blur+1, blur, 1)])
                blur_matrix = blur_matrix/blur_matrix.sum()

        result = np.zeros((dim[0], dim[1]))

        _pos = lambda o: o[0:2]
        if isinstance(plane, str):
            if plane.find('y') and plane.find('z'):
                _pos = lambda o: o[1:3]
            elif plane.find('x') and plane.find('z'):
                _pos = lambda o: [o[0], o[2]]
            else:  # xy
                _pos = lambda o: o[0:2]

        for val in RESULTS:
            position = _pos(val['__pos'])

            if start[0] <= position[0] < start[0] + dim[0]*dim[2]:
                if start[1] <= position[1] < start[1] + dim[1]*dim[2]:
                    sum_values = 0
                    for k in val.keys():
                        if k=='__pos': continue
                        if isinstance(val[k], list):
                            for _ in range(val[k].count(None)):
                                val[k].remove(None)
                            sum_values += sum(val[k])
                        elif isinstance(val[k], (int, float)):
                            sum_values += val[k]

                    x = int((position[0]-start[0])/dim[2])
                    y = int((position[1]-start[1])/dim[2])

                    if blur != False:

                        filtered = blur_matrix * sum_values
                        for x_ in range(x-blur, x+blur, 1):
                            for y_ in range(y-blur, y+blur, 1):
                                if 0 <= x_ < dim[0] and 0 <= y_ < dim[1]:
                                    result[x_,y_] += filtered[x-blur-x_, y-blur-y_]
                    else:
                        result[x,y] += sum_values

        return result
