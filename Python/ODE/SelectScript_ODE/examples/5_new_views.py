import SelectScript
import SelectScript_ODE.Interpreter as ssODE

from odeViz.examples.chaos import Simulation

import matplotlib.pyplot as plt
import numpy as np

class my_ode_sim(Simulation):
    def __init__(self, dt=0.001, dx=10):
        Simulation.__init__(self, dt, dx)
        
        self.callbacks = []
        
        self.ss = ssODE()
        self.ss.addVariable('space', self.space[0])
        self.ss.addVariable('world', self.world)
        
    def execute(self, caller, event):
        Simulation.execute(self, caller, event)
        self.executeSQL()
            
    def executeSQL(self):
        self.ss.setTime(self.simulationTime)
        
        for i in range(len(self.callbacks)) :
            eval_time = self.callbacks[i][2]
            if (self.simulationTime % eval_time) <= self.dt:
                callback  = self.callbacks[i][1]
                prog      = self.callbacks[i][0]
                result    = self.ss.eval(prog)

                callback(self, result)
    
    def addCallback(self, prog, callback, eval_time):       
        self.callbacks.append( [prog, callback, eval_time, []] )


def matrix(sim, m):
    plt.clf()
    plt.subplot(121)
    plt.title("Mass XY-projection")
    plt.imshow(m[0])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar(orientation='horizontal')
      
    plt.subplot(122)
    plt.title("Linear Velocity XY-projection")
    plt.imshow(abs(m[1]))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar(orientation='horizontal')
    
    plt.draw()

if __name__ == "__main__":
    
    plt.ion()
    plt.set_cmap('Spectral')
    
    sim = my_ode_sim(dt=0.002)

    sim.setParam(seed=42, gravity=(0,0,0),
             bounce=0.3, Mu=500, minmaxForce=2000,
             probExplode=0.2, probInsert=1,
             minSize=0.2,
             maxSize=0.5,
             minDensity=10,
             maxDensity=100)
    
    expr = """ Mass     = SELECT mass FROM space WHERE hasBody(this) AS plane ('XY', [-5,-5], [100,100,0.1], 3);
               Velocity = SELECT linearVelocity(this, 2) FROM space WHERE hasBody(this) AS plane('XY', [-5,-5], [100,100,0.1], 3);
               [Mass, Velocity]; """
    
    prog = SelectScript.compile(expr)
    
    sim.addCallback(prog, matrix, eval_time=1)
    
    sim.start()
