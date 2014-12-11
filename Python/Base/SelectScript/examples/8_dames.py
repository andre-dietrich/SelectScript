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
  
problem = """ place = [0,1,2,3,4,5,6,7];
              
              SELECT to([mov.this, tower], "move"+str(level))
              FROM row=place, column=place
              WHERE allcheckboard == put(row.this, column.this, checkboard )
              
              START WITH level = 1, checkboard = [[0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0],
                                                  [0,0,0,0,0,0,0,0]]
              CONNECT BY checkboard = put( row.this, column.this, checkboard ), level=level+1
              STOP WITH level == 8
              
              AS list;
              """

bytecode = SelectScript.compile(problem, debug=True)

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

result = ss.eval(bytecode)


for step in result[0]:
  print step

