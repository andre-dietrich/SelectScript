# Map, with first calculated solution
# =============================
#  ___________________________
# |             |             |
# | e=g ________|________ f=b |
# |    |  \__  a=r  __/  |    |
# |    |     \__ __/     |    |
# |----| d=y  __X__  b=g |----|
# |    |   __/ c=b \__   |    |
# |    |__/___________\__|    |
# | h=r         |         g=y |
# |_____________|_____________|
#

import SelectScript
import SelectScript.Interpreter
from pprint import pprint
from time import time

ss = SelectScript.Interpreter()

####################################################################################
####################################################################################
problem1 = """# standard probably most intuitive problem definition
colors = ['red', 'green', 'blue', 'yellow'];

SELECT a.this,   b.this,   c.this,   d.this,
       e.this,   f.this,   g.this,   h.this
                     
FROM   a=colors, b=colors, c=colors, d=colors,
       e=colors, f=colors, g=colors, h=colors
                     
WHERE  a.this != b.this AND a.this != c.this AND
       a.this != d.this AND a.this != e.this AND
       a.this != f.this AND 
       b.this != c.this AND b.this != d.this AND
       b.this != f.this AND b.this != g.this AND
       c.this != d.this AND c.this != g.this AND
       c.this != h.this AND
       d.this != e.this AND d.this != h.this AND
       e.this != f.this AND e.this != h.this AND
       f.this != g.this AND g.this != h.this
AS dict; """

bytecode = SelectScript.compile(problem1)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem1
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "# results:", len(result)
print "1. result:", result[0]
# time: 5.05048203468
# # results: 48
# 1. result: {'a': 'red', 'c': 'blue', 'b': 'green', 'e': 'green', 'd': 'yellow', 'g': 'yellow', 'f': 'blue', 'h': 'red'}
####################################################################################
####################################################################################
problem2 = """# encapsulate the neighbors into a nested SELECT-statement
colors = ['red', 'green', 'blue', 'yellow'];

SELECT a.this,   b.this,   c.this,   d.this,
       e.this,   f.this,   g.this,   h.this
                     
FROM   a=colors, b=colors, c=colors, d=colors,
       e=colors, f=colors, g=colors, h=colors
                     
WHERE  [] == SELECT this
             FROM [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this], [a.this, f.this],
                  [b.this, c.this], [b.this, d.this], [b.this, f.this], [b.this, g.this],
                  [c.this, d.this], [c.this, g.this], [c.this, h.this],
                  [d.this, e.this], [d.this, h.this],
                  [e.this, f.this], [e.this, h.this],
                  [f.this, g.this], [g.this, h.this]]
             WHERE this[0] == this[1]
             AS list
AS dict; """

bytecode = SelectScript.compile(problem2)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem2
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "# results:", len(result)
print "1. result:", result[0]
# time: 13.9889478683
# # results: 48
# 1. result: {'a': 'red', 'c': 'blue', 'b': 'green', 'e': 'green', 'd': 'yellow', 'g': 'yellow', 'f': 'blue', 'h': 'red'}
####################################################################################
####################################################################################
problem3 = """# making it a bit nicer for the eye
colors = ['red', 'green', 'blue', 'yellow'];

neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this],
              [a.this, f.this], [b.this, c.this], [b.this, d.this], [b.this, f.this],
              [b.this, g.this], [c.this, d.this], [c.this, g.this], [c.this, h.this],
              [d.this, e.this], [d.this, h.this], [e.this, f.this], [e.this, h.this],
              [f.this, g.this], [g.this, h.this]];

SELECT a.this,   b.this,   c.this,   d.this,   e.this,   f.this,   g.this,   h.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors, f=colors, g=colors, h=colors
WHERE  [] == SELECT this
             FROM neighbours
             WHERE this[0] == this[1]
             AS list
AS dict; """

bytecode = SelectScript.compile(problem3)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem3
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "# results:", len(result)
print "1. result:", result[0]
# time: 14.1401050091
# # results: 48
# 1. result: {'a': 'red', 'c': 'blue', 'b': 'green', 'e': 'green', 'd': 'yellow', 'g': 'yellow', 'f': 'blue', 'h': 'red'}
####################################################################################
####################################################################################
problem4 = """# probably even nicer, but much slower due to the application of internal eval
# see the where-clause ... use with caution
colors     = ['red', 'green', 'blue', 'yellow'];

neighbours = [["a", "b"], ["a", "c"], ["a", "d"], ["a", "e"],
              ["a", "f"], ["b", "c"], ["b", "d"], ["b", "f"],
              ["b", "g"], ["c", "d"], ["c", "g"], ["c", "h"],
              ["d", "e"], ["d", "h"], ["e", "f"], ["e", "h"],
              ["f", "g"], ["g", "h"]];

SELECT a.this,   b.this,   c.this,   d.this,   e.this,   f.this,   g.this,   h.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors, f=colors, g=colors, h=colors            
WHERE  [] == SELECT this 
             FROM neighbours
             WHERE eval(this[0]+".this;") == eval(this[1]+".this;")
             AS list
AS dict; """

def get(obj, n):
    return obj[n]
ss.addFunction('get', get)

bytecode = SelectScript.compile(problem4)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem4
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "# results:", len(result)
print "1. result:", result[0]
# time: 1552.77478504
# # results: 48
# 1. result: {'a': u'red', 'c': 'blue', 'b': 'green', 'e': 'green', 'd': 'yellow', 'g': 'yellow', 'f': 'blue', 'h': 'red'}
