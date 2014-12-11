import SelectScript
import SelectScript.Interpreter

def put(x, y, number, sudoku):
    if sudoku[x][y] == 0 and
       not number in sudoku[x] and
       not number in [l[y] for l in sudoku] and
       not number in [sudoku[i][j] for i in range(x/3*3, x/3*3+3, 1) for j in range(y/3*3, y/3*3+3, 1) ]:
        sudoku[x][y] = number
        return sudoku
        
    return []
  
problem = """ pos = [0,1,2,3,4,5,6,7,8];
              num = [1,2,3,4,5,6,7,8,9];
              
              SELECT to([mov.this, tower], "move"+str(level))
              FROM r=pos, c=pos, n=num 
              WHERE allcheckboard == put(row.this, column.this, checkboard )
              
              START WITH level = 1, sudoku = [[7,0,0,  9,2,1,  0,0,8],
                                              [0,0,3,  0,0,0,  6,2,9],
                                              [0,0,2,  3,0,0,  0,0,0],
                                              
                                              [0,4,1,  8,3,0,  0,7,0],
                                              [3,0,6,  0,7,0,  9,0,5],
                                              [0,7,0,  0,5,0,  0,1,0],
                                              
                                              [0,0,0,  2,0,3,  0,0,0],
                                              [4,9,7,  0,0,0,  3,0,0],
                                              [2,0,0,  7,0,6,  8,0,1]]
                                              
              CONNECT BY sudoku = put( r.this, c.this, n.this, sudoku ), level=level+1
              STOP WITH level == 8
              
              AS list;
              """
              


bytecode = SelectScript.compile(problem, debug=True)

ss = SelectScript.Interpreter()
ss.addFunction('put', put)

result = ss.eval(bytecode)


for step in result[0]:
  print step

