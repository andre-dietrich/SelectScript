#!/usr/bin/env python
#__builtins__.__openravepy_version__ = '0.9'
import os
from openravepy import *
from time import sleep
import numpy as np
import SelectScript
import SelectScript_OpenRAVE.Interpreter as ssRAVE

from pyswip import Prolog

class interpeter_extended(ssRAVE):
    def __init__(self):
        ssRAVE.__init__(self)
                
    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == "prolog":
            return self.prolog(PARAMS, SELECT, FROM_n, RESULTS)
        return ssRAVE.evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS)        
        
    def prolog(self, PARAMS, SELECT, FROM_n, RESULTS):
        results = set()
        for elem in RESULTS:
            
            for f in SELECT:
                if f[1] == 'to' :
                    result, relation = self.eval(f, elem, FROM_n)
                    pp = f[2][0][2]
                else:
                    relation = f[1]
                    result = self.eval(f, elem, FROM_n)
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

def start():
    kitchen_env = "resources/kitchen.env.xml"
    env = Environment()     # create the environment
    env.SetViewer('qtcoin') # start the viewer
    env.Load(kitchen_env)   # load a model

    ssRave = interpeter_extended()
    ssRave.addVariable('kitchen', env)
        
    ## Example 1: Generate a map from the enitre environment 
    expr = """SELECT  above(a.this, b.this), 
                      below(a.this, b.this), 
                      isEnabled(a.this),     
                      volume(a.this),        
                      position(a.this),      
                      isRobot(a.this),       
                      isKinbody(a.this)      
            FROM a=kitchen, b=kitchen      
            WHERE not (isSensor(a.this) or isSensor(b.this)) 
            AS prolog;"""
            
    print "query:", expr
    prog = SelectScript.compile(expr)
    prolog = Prolog()
    for result in ssRave.eval(prog):
        print result
        prolog.assertz(result)
        
    print list(prolog.query("above(table, X)"))
    print list(prolog.query("volume(Obj, V), V > 1.0"))
    print list(prolog.query("position(_, P)"))
    
    
if __name__ == "__main__":
    start()
    
    raw_input("\nPress Enter to exit ...")