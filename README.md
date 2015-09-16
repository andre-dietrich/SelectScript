# Moved to:
# https://gitlab.com/OvGU-ESS/SelectScript

#SelectScript

SelectScript a querying language intended to serve as a general and generic interface to
any kind of discrete simulation. Similar to LUA, scripts are interpreted within foreign
programming languages. Currently there is only support for Python, which means, that there
is a SelectScript-compiler and a basic interpreter. The creation of new extensions for
different simulation environments requires only to extend the basic interpreter in an
object oriented manner. There are currently two "dialects", one for the Open Dynamics
Engine (ODE) and one for the robotic simulator OpenRAVE. The compiler can be interpreted
as fixed, it only generates some kind of simplified bytecode. What position, mass, and
velocity stand for, has to be resolved by the interpreter, whereby all functions are
implemented within the original programming language.

The example below shows a (not fully) the syntax of an query script. It is possible to
define persistent variables, timely variables (which keep the results over a certain
period of time and can be used as a source for further queries), evaluate any kind of
expressions, and last but not least query running simulations online and extract any
kind of information in any kind of representation.


``` sql
V0 = ((22^2 * 12.12 - 2) / 2) == 2932.04; # ... True
V1 = SELECT ...; # SELECT anything ... in any format ...

V2 = SELECT position(a.this), mass(a.this), (velocity(a.this, dirction=1))^2, ...
     FROM a = simulation_environment, b = simulation_environment
     WHERE mass(a.this) < 12 and mass(b.this) != 0 and isColliding(a.this, b.this)
     GROUP BY round(mass(a.this), 0.01)
     ORDER BY ...
     AS 2D-Projection(XY); # or as an ordinary list, dictionary, an OccupancyGridMap, ...

[V1, V2, getTime()]; # the result is a list of three elements
```

# Media

The videos are screencasts of the examples provide within every (currently available
dialect) and shall provide a first insight on the application of SelectScript.

## SelectScript_ODE

[![SelectScript_ODE](http://img.youtube.com/vi/F1XNch1JC9Y/0.jpg)](http://www.youtube.com/watch?v=F1XNch1JC9Y)

## SelectScript_OpenRAVE

See also the tutorial at: https://pythonhosted.org/SelectScript_OpenRAVE
#### simple (interactive) queries:

[![SelectScript_OpenRAVE demo0](http://img.youtube.com/vi/R_PThP0gwOc/0.jpg)](http://www.youtube.com/watch?v=R_PThP0gwOc)

#### user defined relations:
Query for all objects that are "on" the table and in reachable distance to the
manipulator. And use the result as input for trajectory planning.

[![SelectScript_OpenRAVE demo1](http://img.youtube.com/vi/jSaoCXRNVNg/0.jpg)](http://www.youtube.com/watch?v=jSaoCXRNVNg)

#### defining situations by using triggers and callbacks:
Which sensor had perceived a robot during the last 2 seconds)? The result set is
used as input for the defined callback function, whereby the callback is only
executed, if the result has changed. The result set in this video is visualized
by the sensor beams.

[![SelectScript_OpenRAVE demo2](http://img.youtube.com/vi/Bk8TaOQQdZM/0.jpg)](http://www.youtube.com/watch?v=Bk8TaOQQdZM)

#### query for a sub-environment:

[![SelectScript_OpenRAVE demo3](http://img.youtube.com/vi/k5NXVv6O3tU/0.jpg)](http://www.youtube.com/watch?v=k5NXVv6O3tU)

#### query for an OccupancyGridMap:

[![SelectScript_OpenRAVE demo4](http://img.youtube.com/vi/MYQppe9E9Es/0.jpg)](http://www.youtube.com/watch?v=MYQppe9E9Es)

## Links

OpenRAVE: http://openrave.org/docs/latest_stable/

SelectScript_OpenRAVE: https://pythonhosted.org/SelectScript_OpenRAVE

Open Dynamics Engine: http://www.ode.org/


## Contact

| André Dietrich |                                           |
| -------------- | ----------------------------------------- |
| web:           | http://eos.cs.ovgu.de/crew/dietrich/      |
| eMail:         | dietrich@ivs.cs.uni-magdeburg.de          |
| YoutTube:      | https://www.youtube.com/user/ivsmagdeburg |
