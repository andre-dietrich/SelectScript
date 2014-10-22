from odeViz.examples import chaos

sim = chaos.Simulation(dt=0.0025, dx=10)
sim.setParam(seed=18, gravity=(0,0,0),
             bounce=0.3, Mu=500, minmaxForce=10000,
             probExplode=0.1, probInsert=0.5)

sim.start()



