import SelectScript
import SelectScript.Interpreter

problem = """ IF(False==True; "fuck", 2, 55; 22, 33,33,"fffuck"); """

bytecode = SelectScript.compile(problem)

ss = SelectScript.Interpreter()

print ss.eval(bytecode)

