import SelectScript
import SelectScript_ODE.Interpreter as ssODE

from odeViz.examples.chaos import Simulation

class my_ode_sim(Simulation):
    def __init__(self, dt=0.01, dx=10):
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

def log(msg): pass

if __name__ == "__main__":
    
    sim = my_ode_sim(0.02)
    
    expr = """ SELECT mul(velocity(a.this),mass(a.this))
               FROM a=space, b=space
               WHERE collision(a.this, b.this) and hasBody(a.this)
               AS sound; // OMG """                
    prog = SelectScript.compile(expr)
    sim.addCallback(prog, log)
    
    sim.start()    