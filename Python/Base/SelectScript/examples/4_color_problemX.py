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

              neighbours = [["a", "b"], ["a", "c"], ["a", "d"], ["a", "e"], 
                            ["b", "c"], ["b", "d"], ["c", "d"], ["d", "e"]];

              SELECT a.this,   b.this,   c.this,   d.this,   e.this
              FROM   a=colors, b=colors, c=colors, d=colors, e=colors                     
              WHERE  [] == SELECT a.this 
                           FROM neighbours
                           WHERE eval(this[0]+".this;") == eval(this[1]+".this;")
                           AS list
              AS dict;              
              """
#problem = """eval("2*2;");"""

bytecode = SelectScript.compile(problem, debug = True)

#print bytecode

def get(obj, n):
  return obj[n]

ss = SelectScript.Interpreter()
ss.addFunction('get', get)

for i, result in enumerate(ss.eval(bytecode)):
    print "=========",i,"========="
    pprint(result)
