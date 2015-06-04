import SelectScript
import SelectScript.Interpreter

def place(row, colum, checkboard):
    if checkboard == []: return []
    if checkboard[row,colum] != 0:
        pass
    elif towers[step[1]] == []:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    elif towers[step[1]][-1] > towers[step[0]][-1]:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    return []
  
problem = """
SELECT to([mov.this, tower], "move"+str(level))
FROM row=[0,1,2,3,4,5,6,7], column=[0,1,2,3,4,5,6,7]
WHERE checkboard == put(row.this, column.this, checkboard )
              
START WITH level = 1, checkboard = [[0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0,0]]
CONNECT BY checkboard = place(row.this, column.this, checkboard ), level=level+1
STOP WITH level == 8 or checkerboard == []

AS list; """

bytecode = SelectScript.compile(problem)

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

result = ss.eval(bytecode)


for step in result[0]:
  print step

