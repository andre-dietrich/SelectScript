import SelectScript
import SelectScript_ODE.Interpreter as ssODE

from odeViz.examples.chaos import Simulation

############################################################
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
                callback(result)

    def addCallback(self, prog, callback):
        self.callbacks.append( [prog, callback, []] )

############################################################
def color(obj):
    return list(sim.GetProperty(obj).GetColor())

############################################################
def callbackPush(output):
    for elem in output:
        [x,y,z] = elem['pos']
        odeBody = elem['obj'].getBody()
        odeBody.addForce((cmp(x, 0) * 4 - x,
                          cmp(y, 0) * 4 - y,
                          cmp(z, 0) * 4 - z))

############################################################

sim = my_ode_sim(0.005, dx=11)

sim.setParam(seed=18, gravity=(0,0,0),
             bounce=0.3, Mu=500, minmaxForce=10000,
             probExplode=0.1, probInsert=0.5)

sim.ssODE.addFunction('color', color)

expr = """SELECT obj, pos FROM space 
          WHERE color(this)==[1,1,1] AND distance([0,0,0], this) < 4
          AS dict;"""

prog = SelectScript.compile(expr)
sim.addCallback(prog, callbackPush)

sim.start()






