# Map
# =============================
#  ______________________
# |     |                |
# |     |____________  b |
# |  a  |            |   |
# |     |      c     |   |
# |     |____________|___|
# |_____|                |
# |     |                |
# |  e  |        d       |
# |_____|________________|


import SelectScript
import SelectScript.Interpreter
from pprint import pprint

problem = """ colors     = ['red', 'green', 'blue', 'yellow'];

              neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this], 
                            [b.this, c.this], [b.this, d.this], [c.this, d.this], [d.this, e.this]];

              SELECT a.this,   b.this,   c.this,   d.this,   e.this
              FROM   a=colors, b=colors, c=colors, d=colors, e=colors                     
              WHERE  [] == SELECT this
                           
                           FROM neighbours
                                 
                           WHERE this[0] == this[1]
                           AS list
              AS dict;              
              """
#problem = """eval("2*2;");"""

bytecode = SelectScript.compile(problem, debug = True)

print bytecode

def get(obj, n):
  return obj[n]

ss = SelectScript.Interpreter()
ss.addFunction('get', get)

for i, result in enumerate(ss.eval(bytecode)):
 #   pass
    print "=========",i,"========="
    pprint(result)
