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

problem = """ ########################################################################
colors = ['red', 'green', 'blue', 'yellow'];

neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this],
              [a.this, f.this], [b.this, c.this], [b.this, d.this], [b.this, f.this],
              [b.this, g.this], [c.this, d.this], [c.this, g.this], [c.this, h.this],
              [d.this, e.this], [d.this, h.this], [e.this, f.this], [e.this, h.this],
              [f.this, g.this], [g.this, h.this]];

######################################################################################
SELECT a.this,   b.this,   c.this,   d.this,   e.this,   f.this,   g.this,   h.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors, f=colors, g=colors, h=colors
WHERE  [] == SELECT this
             FROM neighbours
             WHERE this[0] == this[1]
             AS list
AS dict;
"""

bytecode = SelectScript.compile(problem, debug = True)

ss = SelectScript.Interpreter()

for i, result in enumerate(ss.eval(bytecode)):
    print "=========",i,"========="
    pprint(result)
