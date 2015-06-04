from pprint import pprint
from time import time

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

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

####################################################################################
####################################################################################
problem1 = """# Basic nested functions ...
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];

SELECT mov1.this, mov2.this, mov3.this, mov4.this, mov5.this, mov6.this, mov7.this
FROM mov1=moves, mov2=moves, mov3=moves, mov4=moves, mov5=moves, mov6=moves, mov7=moves
WHERE [[],[],[3,2,1]] == move( mov7.this,
                               move( mov6.this,
                                     move( mov5.this,
                                           move( mov4.this,
                                                 move( mov3.this,
                                                       move( mov2.this,
                                                             move( mov1.this, [[3,2,1],[],[]] )))))))
AS list; """

bytecode = SelectScript.compile(problem1)

t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem1
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result

####################################################################################
####################################################################################
problem2 = """# Basic recursive query
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT mov.this
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]], level=1
CONNECT BY tower = move(mov.this, tower), level=level+1
STOP WITH  level==7 or []==move(mov.this, tower)
              
AS list; """

bytecode = SelectScript.compile(problem2)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem2
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result

####################################################################################
####################################################################################
problem3 = """# Recursive query with no cycles allowed ... reduces the search space
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]], level=1
CONNECT BY NO CYCLE
           tower = move( mov.this, tower ), level=level+1
STOP WITH  level==7 or [] == move( mov.this, tower )
              
AS dict; """

bytecode = SelectScript.compile(problem3)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem3
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result

####################################################################################
####################################################################################
problem4 = """# 
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT to([mov.this, tower], "config"+str(level))
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]], level=1
CONNECT BY UNIQUE
           tower = move( mov.this, tower ), level=level+1
STOP WITH  level==7 or [] == move( mov.this, tower )
              
AS dict; """

bytecode = SelectScript.compile(problem4)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem4
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result

####################################################################################
####################################################################################
problem5 = """# 
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT to([mov.this, tower], "config"+str(level))
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]], level=1
CONNECT BY NO CYCLE UNIQUE
           tower = move( mov.this, tower ), level=level+1
STOP WITH  level==7 or [] == move( mov.this, tower )
              
AS dict; """

bytecode = SelectScript.compile(problem5)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem5
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result

####################################################################################
####################################################################################
problem6 = """# 
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[3,2,1],[],[]]
CONNECT BY MEMORIZE 7
           tower = move( mov.this, tower )
STOP WITH  [] == move( mov.this, tower )
              
AS dict; """

bytecode= SelectScript.compile(problem6)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem6
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result
