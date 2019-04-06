# SelectScript_OpenRAVE

It is an implementation of the SelectScript query language for robotics
simulation environment OpenRAVE.

## Installation

First of all you need to install the SelectScript_Base!

via Python setuptools:
```
$ sudo python setup.py build
$ sudo python setup.py install
```

If the Installation was successful can be checked from an IPython
interactive shell:

``` pyhton
# should work also for demo1, demo2, ...
import SelectScript_OpenRAVE.examples.demo0 as demo0
demo0.start()
```

## Tutorial

Please visit the package information site:

http://pythonhosted.org//SelectScript_OpenRAVE

## Media

The videos are screencasts of the examples provide within this project and shall
provide a first insight on the application of SelectScript.

#### examples/demo0.py : simple (interactive) queries

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/R_PThP0gwOc/0.jpg)](http://www.youtube.com/watch?v=R_PThP0gwOc)

#### examples/demo1.py : user defined relations:
Query for all objects that are "on" the table and in reachable distance to the
manipulator. And use the result as input for trajectory planning.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/jSaoCXRNVNg/0.jpg)](http://www.youtube.com/watch?v=jSaoCXRNVNg)

#### examples/demo2.py : defining situations by using triggers and callbacks:
Which sensor had perceived a robot during the last 2 seconds)? The result set is
used as input for the defined callback function, whereby the callback is only
executed, if the result has changed. The result set in this video is visualized
by the sensor beams.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/Bk8TaOQQdZM/0.jpg)](http://www.youtube.com/watch?v=Bk8TaOQQdZM)

#### examples/demo3.py : query for a sub-environment

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/k5NXVv6O3tU/0.jpg)](http://www.youtube.com/watch?v=k5NXVv6O3tU)

#### examples/demo4.py : query for an OccupancyGridMap

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/MYQppe9E9Es/0.jpg)](http://www.youtube.com/watch?v=MYQppe9E9Es)

## Contact

If you change the code, improve this project, fix bugs, or just have comments,
feel free to contact me...

| André Dietrich |                                           |
| -------------- | ----------------------------------------- |
| web:           | http://eos.cs.ovgu.de/crew/dietrich/      |
| eMail:         | dietrich@ivs.cs.uni-magdeburg.de          |


