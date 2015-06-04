from pprint import pprint

import SelectScript
import SelectScript.Interpreter

def move(step, towers):
    if towers == [] or towers[step[0]] == []:
        pass
    elif towers[step[1]] == []:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    elif towers[step[1]][-1] > towers[step[0]][-1]:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    return []
  
problem = """
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT to([mov.this, tower], "move"+str(level))
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]], level=1
CONNECT BY NO CYCLE
        tower = move( mov.this, tower ), level=level+1
STOP WITH level==7 or [] == move( mov.this, tower )
              
AS dict; """

bytecode = SelectScript.compile(problem, debug=True)

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

result = ss.eval(bytecode)

pprint(result)

