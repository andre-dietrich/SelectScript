from Interpreter import Interpreter
from SelectScript import SelectScript

def compile(prog):
    try:
        return SelectScript(None, None).compile(prog)
    except:
        print "Error"