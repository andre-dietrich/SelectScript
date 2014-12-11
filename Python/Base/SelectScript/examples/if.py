import SelectScript
import SelectScript.Interpreter

problem = """ IF(False; "fuck", 2, 55; 22, "fffuck"); """

bytecode = SelectScript.compile(problem, debug = True)

ss = SelectScript.Interpreter()

print ss.eval(bytecode)

