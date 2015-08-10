from pprint import pprint
from time import time

import SelectScript
import SelectScript.Interpreter

def move(step, towers):
    if not towers or not towers[step[0]]:
        pass
    elif not towers[step[1]] or towers[step[1]][-1] > towers[step[0]][-1]:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    return []

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

####################################################################################
####################################################################################
problem1 = """# Basic nested functions iterating over all combinations, not very effective
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
# time: 10.0932531357
# result: [[0, 2], [0, 1], [2, 1], [0, 2], [1, 0], [1, 2], [0, 2]]
####################################################################################
####################################################################################
problem2 = """# Basic recursive query
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];

SELECT mov.this
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )

START WITH tower = [[3,2,1],[],[]], level=1                # the local level variable
CONNECT BY tower = move(mov.this, tower), level=level+1    # is required to prevent
STOP WITH  level==7 or []==move(mov.this, tower)           # an infinite recursion

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
# time: 0.885102987289
# result: [[[0, 2], [0, 1], [2, 1], [0, 2], [1, 0], [1, 2], [0, 2]]]
####################################################################################
####################################################################################
problem3 = """# Recursive query with no cycles allowed ... reduces the search space
# because one moves can be applied a couple of times, the tower is included as
# an additional result parameter
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
# time: 0.324506998062
# result: [[{'tower': [[3, 2], [],     [1]],       'mov': [0, 2]},
#           {'tower': [[3],    [2],    [1]],       'mov': [0, 1]},
#           {'tower': [[3],    [2, 1], []],        'mov': [2, 1]},
#           {'tower': [[],     [2, 1], [3]],       'mov': [0, 2]},
#           {'tower': [[1],    [2],    [3]],       'mov': [1, 0]},
#           {'tower': [[1],    [],     [3, 2]],    'mov': [1, 2]},
#           {'tower': [[],     [],     [3, 2, 1]], 'mov': [0, 2]}]]

####################################################################################
####################################################################################
problem4 = """# a result can only appear once in a search, note the changed SELECT-statement
# the "to" function is used to format/name the titles in the dictionary
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
# time: 0.194886922836
# result: [[{'config1': [[0, 2], [[3, 2], [],     [1]]]},
#           {'config2': [[0, 1], [[3],    [2],    [1]]]},
#           {'config3': [[2, 1], [[3],    [2, 1], []]]},
#           {'config4': [[0, 2], [[],     [2, 1], [3]]]},
#           {'config5': [[1, 0], [[1],    [2],    [3]]]},
#           {'config6': [[1, 2], [[1],    [],     [3, 2]]]},
#           {'config7': [[0, 2], [[],     [],     [3, 2, 1]]]}]]
####################################################################################
####################################################################################
problem5 = """# both options can also be applied in combination
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
# time: 0.201504945755
# result: [[{'config1': [[0, 2], [[3, 2], [],     [1]]]},
#           {'config2': [[0, 1], [[3],    [2],    [1]]]},
#           {'config3': [[2, 1], [[3],    [2, 1], []]]},
#           {'config4': [[0, 2], [[],     [2, 1], [3]]]},
#           {'config5': [[1, 0], [[1],    [2],    [3]]]},
#           {'config6': [[1, 2], [[1],    [],     [3, 2]]]},
#           {'config7': [[0, 2], [[],     [],     [3, 2, 1]]]}]]
####################################################################################
####################################################################################
problem6 = """# The memorize option generates a graph structure in the background
# with a certain depth, which can speed-up a query ...
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];

SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )

START WITH tower = [[3,2,1],[],[]]
CONNECT BY MEMORIZE 
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
# time: 0.0428931713104
# result: [[[{'tower': [[3, 2], [],     [1]],       'mov': [0, 2]}],
#           [{'tower': [[3],    [2],    [1]],       'mov': [0, 1]}],
#           [{'tower': [[3],    [2, 1], []],        'mov': [2, 1]}],
#           [{'tower': [[],     [2, 1], [3]],       'mov': [0, 2]}],
#           [{'tower': [[1],    [2],    [3]],       'mov': [1, 0]}],
#           [{'tower': [[1],    [],     [3, 2]],    'mov': [1, 2]}],
#           [{'tower': [[],     [],     [3, 2, 1]], 'mov': [0, 2]}]]]
####################################################################################
####################################################################################
problem7 = """# stop at a certain number of results... note the changed graph-size
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];

SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[3,2,1]] == move( mov.this, tower )

START WITH tower = [[3,2,1],[],[]]
CONNECT BY MEMORIZE 10 MAXIMUM 3
           tower = move( mov.this, tower )
STOP WITH  [] == move( mov.this, tower )

AS dict; """

bytecode= SelectScript.compile(problem7)
t_start = time()
result  = ss.eval(bytecode)
t_end   = time()

print "----------------------------------------------------------------------------"
print problem7
print "----------------------------------------------------------------------------"
print "time:", t_end - t_start
print "result:", result
# time: 0.075532913208
# result: [[[{'tower': [[3, 2], [1],    []],        'mov': [0, 1]}],
#           [{'tower': [[3],    [1],    [2]],       'mov': [0, 2]}],
#           [{'tower': [[3],    [],     [2, 1]],    'mov': [1, 2]}],
#           [{'tower': [[],     [3],    [2, 1]],    'mov': [0, 1]}],
#           [{'tower': [[],     [3, 1], [2]],       'mov': [2, 1]}],
#           [{'tower': [[2],    [3, 1], []],        'mov': [2, 0]}],
#           [{'tower': [[2, 1], [3],    []],        'mov': [1, 0]}],
#           [{'tower': [[2, 1], [],     [3]],       'mov': [1, 2]}],
#           [{'tower': [[2],    [1],    [3]],       'mov': [0, 1]}],
#           [{'tower': [[],     [1],    [3, 2]],    'mov': [0, 2]}],
#           [{'tower': [[],     [],     [3, 2, 1]], 'mov': [1, 2]}]],
#
#          [[{'tower': [[3, 2], [],     [1]],       'mov': [0, 2]}],
#           [{'tower': [[3],    [2],    [1]],       'mov': [0, 1]}],
#           [{'tower': [[3],    [2, 1], []],        'mov': [2, 1]}],
#           [{'tower': [[],     [2, 1], [3]],       'mov': [0, 2]}],
#           [{'tower': [[1],    [2],    [3]],       'mov': [1, 0]}],
#           [{'tower': [[1],    [],     [3, 2]],    'mov': [1, 2]}],
#           [{'tower': [[],     [],     [3, 2, 1]], 'mov': [0, 2]}]],
#
#          [[{'tower': [[3, 2], [],     [1]],       'mov': [0, 2]}],
#           [{'tower': [[3],    [2],    [1]],       'mov': [0, 1]}],
#           [{'tower': [[3, 1], [2],    []],        'mov': [2, 0]}],
#           [{'tower': [[3],    [2, 1], []],        'mov': [0, 1]}],
#           [{'tower': [[3],    [2, 1], []],        'mov': [0, 1]}],
#           [{'tower': [[],     [2, 1], [3]],       'mov': [0, 2]}],
#           [{'tower': [[1],    [2],    [3]],       'mov': [1, 0]}],
#           [{'tower': [[1],    [],     [3, 2]],    'mov': [1, 2]}],
#           [{'tower': [[],     [],     [3, 2, 1]], 'mov': [0, 2]}]]]
