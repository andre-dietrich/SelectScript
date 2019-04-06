import SelectScript
import SelectScript_ODE.Interpreter as ssODE

from odeViz.examples import chaos
from thread import start_new_thread
import time

def wait(seconds):
	print "wait (", seconds, ") ",
	for _ in range(seconds):
		time.sleep(1)
		print ".",
	print

sim = chaos.Simulation(dt=0.01, dx=1)
sim.setParam(seed=18, gravity=(0,0,0),
             bounce=0.3, Mu=500, minmaxForce=10000,
             probExplode=0.1, probInsert=0.5)

ssODE = ssODE()
ssODE.addVariable('space', sim.space[0])

start_new_thread(sim.start, ()) #  

##################################################################
wait(10)
expr = "SELECT id(this, space), mass, velocity FROM space WHERE isSphere(this) AS dict;"
prog = SelectScript.compile(expr)  # generate byte-code
result = ssODE.eval(prog)

print "------------------------------- Example 1 -------------------------------"
print "expr = \"", expr, '"'
print "prog = SelectScript.compile(expr)"
#print prog
print "result = ssODE.eval(prog)"
for result in ssODE.eval(prog):
    print result

##################################################################
wait(10)
expr = "SELECT id(this, space), type, volume FROM space WHERE isSphere(this) AS dict;"
prog = SelectScript.compile(expr)  # generate byte-code

print "------------------------------- Example 2 -------------------------------"
print "expr = \"", expr, '"'
print "prog = SelectScript.compile(expr)"
#print prog
print "result = ssODE.eval(prog)"
for result in ssODE.eval(prog):
    print result

##################################################################
wait(10)
expr = "max(SELECT mass FROM space AS list);"
prog = SelectScript.compile(expr)  # generate byte-code
result = ssODE.eval(prog)

print "------------------------------- Example 3 -------------------------------"
print "expr = \"", expr, '"'
print "prog = SelectScript.compile(expr)"
#print prog
print "result = ssODE.eval(prog)"
print result

##################################################################
wait(10)
expr = "SELECT obj FROM space WHERE mass(this) < " +str(result)+ " AS list;"
prog = SelectScript.compile(expr)  # generate byte-code
result = ssODE.eval(prog)

print "------------------------------- Example 4 -------------------------------"
print "expr = \"", expr, '"'
print "prog = SelectScript.compile(expr)"
#print prog
print "result = ssODE.eval(prog)"

for geom in result:
	print geom
	sim.GetProperty(geom).SetOpacity(0.1)
	
wait(20)

