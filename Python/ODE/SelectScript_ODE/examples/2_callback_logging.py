import SelectScript
import SelectScript_ODE.Interpreter as ssODE

from odeViz.examples.chaos import Simulation

import numpy as np
import matplotlib.pyplot as plt

class my_ode_sim(Simulation):
    def __init__(self, dt=0.001, dx=10):
        Simulation.__init__(self, dt, dx)
        
        self.callbacks = []
        
        self.ssODE = ssODE()
        self.ssODE.addVariable('space', self.space[0])
        self.ssODE.addVariable('world', self.world)
        
    def execute(self, caller, event):
        Simulation.execute(self, caller, event)
        self.executeSQL()
            
    def executeSQL(self):
        self.ssODE.setTime(self.simulationTime)
        
        for i in range(len(self.callbacks)) :
            prog = self.callbacks[i][0]
            callback = self.callbacks[i][1]
            result = self.ssODE.eval(prog)

            if result != self.callbacks[i][2]:
                self.callbacks[i][2] = result
                callback(self, result)
    
    def addCallback(self, prog, callback):       
        self.callbacks.append( [prog, callback, []] )

def logInfo(sim, msg):
    
    dat['time'  ].append(msg[0])
    dat['count1'].append(msg[1])
    dat['mean1' ].append(msg[2])
    dat['count2'].append(msg[3])
    dat['mean2' ].append(msg[4])
    
    # plot results only every second
    if msg[0] % 1 > sim.dt:
      return
    
    if msg[0] % 10 > sim.dt:
      dat['col'   ].append(msg[5])
      dat['colt'  ].append(msg[0])
    
    plt.subplots_adjust(wspace=0.5)
    
    plt.clf()
    
    plt.subplot(223)
    plt.plot(dat['time'], dat['mean1'], '-', label="white", linewidth=2.0, color="black")
    plt.plot(dat['time'], dat['mean2'], '--', label="colored", linewidth=2.0, color="black")
    plt.ylabel('volume')
    plt.xlabel('time')
    plt.grid(True)    
    
    plt.subplot(211)
    plt.plot(dat['time'], dat['count1'], '-', label="white", linewidth=2.0, color="black")
    plt.plot(dat['time'], dat['count2'], '--', label="colored", linewidth=2.0, color="black")
    plt.xlabel('time')
    plt.ylabel('amount')
    plt.grid(True)

    plt.legend(loc=7)
    
    plt.subplot(224)
    plt.bar(dat['colt'],dat['col'], color='red', edgecolor='black', width=10)
    plt.xlabel('collisions per 10sec')

    plt.draw()

def color(obj):
    return list(sim.GetProperty(obj).GetColor())

def average(obj):
    for _ in range(obj.count(None)):
        obj.remove(None)
    if obj == []:
        return 0
    if isinstance(obj, list):
        return sum(obj)/len(obj)
    return 0

if __name__ == "__main__":
    
    dat = {'time':[0], 'count1': [0] , 'mean1': [0], 'count2': [0], 'mean2': [0], 'col':[0.0001], 'colt':[0]}

    plt.ion()
    
    sim = my_ode_sim(dt=0.01)    
    sim.setParam(seed=42, gravity=(0,0,0),
             bounce=0.3, Mu=500, minmaxForce=5000,
             probExplode=0.3, probInsert=0.5,
             minSize=0.2,
             maxSize=0.5)
    
    sim.ssODE.addFunction('color', color)
    sim.ssODE.addFunction('average', average)
    
    expr = """ white = [1,1,1];
               
               G_1 = SELECT volume FROM space WHERE color(this) == white and hasBody(this) AS list;
               G_2 = SELECT volume FROM space WHERE color(this) != white and hasBody(this) AS list;
               
               col{10} = sub(count(uniq(SELECT obj(a.this) FROM a=space, b=space 
               WHERE collision(a.this, b.this) AS list)), 6);
               
               [getTime(), count(G_1), sum(G_1), count(G_2), sum(G_2), sum(col{-10})]; """
                                
    prog = SelectScript.compile(expr)
    sim.addCallback(prog, logInfo)
    
    sim.start()
