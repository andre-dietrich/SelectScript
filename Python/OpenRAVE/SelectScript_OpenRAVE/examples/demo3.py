#!/usr/bin/env python
#__builtins__.__openravepy_version__ = '0.9'
import os, time, sys
from openravepy import *
from time import sleep

import SelectScript
import SelectScript_OpenRAVE.Interpreter as ssRAVE


class interpeter_extended(ssRAVE):
    def __init__(self):
        ssRAVE.__init__(self)
                
    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == "environment":
            results = ssRAVE.evalAS_list(self, [], SELECT, FROM_n, RESULTS)
            return self.environment(PARAMS, results)
        else:
            return ssRAVE.evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS)
        
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
    kitchen_env = "resources/kitchen.env.xml"
    env = Environment()     # create the environment
    #env.SetViewer('qtcoin') # start the viewer
    env.Load(kitchen_env)   # load a model

    ssRaveX = interpeter_extended()
    ssRaveX.addVariable('kitchen', env)
    
    ## Example 1: Query for information about sensors and robots 
    expr  = "roomba = SELECT obj FROM kitchen WHERE id(this)=='roomba_625x' AS value;"
    expr += "SELECT obj FROM kitchen WHERE distance(roomba, this) <= 1.6 AS environment;"
    print "query:", expr
    prog = SelectScript.compile(expr)
    
    newEnv = ssRaveX.eval(prog)
    
    #env.Reset()
    env = newEnv
    
    newEnv.SetViewer('qtcoin') # start the viewer
    
if __name__ == "__main__":
    start()
    
    raw_input("\nPress Enter to exit ...")