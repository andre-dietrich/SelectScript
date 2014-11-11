from Interpreter import Interpreter
from SelectScript import SelectScript

def compile(prog, debug=False):
    try:
        return SelectScript(None, None).compile(prog, debug)
    except:
        print "Error"