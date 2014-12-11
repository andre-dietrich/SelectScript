import SelectScript
import SelectScript.Interpreter

def move(step, towers):
    new_towers = []
    if towers == []:
        pass
    elif towers[step[0]] == []:
        pass
    elif towers[step[1]] == []:
        towers[step[1]].append( towers[step[0]].pop() )
        new_towers = towers
    elif towers[step[1]][-1] > towers[step[0]][-1]:
        towers[step[1]].append( towers[step[0]].pop() )
        new_towers = towers
    return new_towers

problem = """ moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];

              SELECT mov1.this, mov2.this, mov3.this, mov4.this, mov5.this, mov6.this, mov7.this
              FROM mov1=moves, mov2=moves, mov3=moves, mov4=moves, mov5=moves, mov6=moves, mov7=moves
              WHERE [[],[],[3,2,1]] == move( mov7.this,
                                             move( mov6.this,
                                                   move( mov5.this,
                                                         move( mov4.this,
                                                               move( mov3.this,
                                                                     move( mov2.this,
                                                                           move( mov1.this, [[3,2,1],[],[]] )))))))
              AS list;
              """

bytecode = SelectScript.compile(problem, debug = True)

ss = SelectScript.Interpreter()
ss.addFunction('move', move)

print ss.eval(bytecode)

