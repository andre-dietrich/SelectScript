#!/usr/bin/env python
#__builtins__.__openravepy_version__ = '0.9'
import os
from openravepy import *
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import SelectScript
import SelectScript_OpenRAVE.Interpreter as ssRAVE

class interpeter_extended(ssRAVE):
    def __init__(self):
        ssRAVE.__init__(self)
    
    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == "environment":
            results = ssRAVE.evalAS_list(self, [], SELECT, FROM_n, RESULTS)
            return self.environment(PARAMS, results)
        elif AS == "OccupancyGrid":
            results = ssRAVE.evalAS_list(self, [], SELECT, FROM_n, RESULTS)
            results = self.environment([], results)
            #results = self.evalAS("environment", PARAMS, SELECT, FROM_n, RESULTS)
            return self.OccupancyGrid(PARAMS, results)
        else:
            return ssRAVE.evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS)
  
    def OccupancyGrid(self, PARAMS, RESULTS):
        z_pos     = PARAMS[0]
        grid_size = PARAMS[1]
        
        # only for visualizing:
        #env = RESULTS.next()[0].GetEnv()
        
        envmin = envmax = []
        for b in RESULTS.GetBodies():
            ab = b.ComputeAABB()
            envmin.append(ab.pos()-ab.extents())
            envmax.append(ab.pos()+ab.extents())
            
        envmin = np.floor(np.min(np.array(envmin), 0)*100.) / 100
        envmax = np.ceil( np.max(np.array(envmax), 0)*100.) / 100 
        size   = np.ceil((envmax - envmin) / grid_size)
                
        ogMap = RaveCreateModule(RESULTS,'occupancygridmap')
        ogMap.SendCommand('SetTranslation %f %f %f' % (envmin[0], envmin[1], z_pos))
        ogMap.SendCommand('SetSize %i %i %f' %(size[0]+1, size[1]+1, grid_size) )
        ogMap.SendCommand('SetLineWidth 2.0')
    
        render = ogMap.SendCommand('Scan')
        
        #ogMap.SendCommand('Render')
        #sleep(10)
        
        return np.fromstring(render, dtype=bool, count=-1, sep='').reshape(int(size[0]+1), int(size[1]+1))
        
    def environment(self, PARAMS, RESULTS):
        
        newEnv = RESULTS[0].GetEnv().CloneSelf(1|8)
        ids = []
        for elem in RESULTS:
            if type(elem) in [Robot, KinBody, Sensor]:
                ids.append(elem.GetName())
        
        # remove sensors
        for elem in newEnv.GetSensors():
            if not elem.GetName() in ids:
                newEnv.Remove( newEnv.GetSensor(elem.GetName()) )
        # remove robots
        for elem in newEnv.GetRobots():
            if not elem.GetName() in ids:
                newEnv.Remove( newEnv.GetRobot(elem.GetName()) )
        # remove bodies
        for elem in newEnv.GetBodies():
            if not elem.GetName() in ids:
                newEnv.Remove( newEnv.GetKinBody(elem.GetName()) )
        
        return newEnv

def start():
    RaveInitialize()    
    
    kitchen_env = os.path.dirname(__file__)+"/resources/kitchen.env.xml"
    env = Environment()     # create the environment
    env.SetViewer('qtcoin') # start the viewer
    env.Load(kitchen_env)   # load a model

    ssRave = interpeter_extended()
    ssRave.addVariable('kitchen', env)
        
    ## Example 1: Generate a map from the enitre environment 
    expr = "SELECT obj FROM kitchen AS OccupancyGrid ( z_pos=0.22, grid_size=0.025 );"
    print "query:", expr
    prog = SelectScript.compile(expr)
    map = ssRave.eval(prog)    
    
    # plot the map
    plt.imshow(map.astype(numpy.float), cmap=plt.cm.gray)
    plt.show()    
    
    ## Example 2: Generate a map from all objects that are close to roomba 
    expr  = "roomba = SELECT obj FROM kitchen WHERE id(this)=='roomba_625x' AS value;"
    expr += "SELECT obj FROM kitchen WHERE distance(roomba, this) <= 1.6 AS OccupancyGrid (z_pos=0.22, grid_size=0.025 );"
    print "query:", expr
    prog = SelectScript.compile(expr)
    map = ssRave.eval(prog)    
    
    plt.imshow(map.astype(numpy.float), cmap=plt.cm.gray)
    plt.show()
    
if __name__ == "__main__":
    start()
    
    raw_input("\nPress Enter to exit ...")