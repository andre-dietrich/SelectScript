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

problem = """ colors = ['red', 'green', 'blue', 'yellow'];

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
              AS dict;
              """

bytecode = SelectScript.compile(problem, debug = True)

ss = SelectScript.Interpreter()

for i, result in enumerate(ss.eval(bytecode)):
    print "=========",i,"========="
    pprint(result)
