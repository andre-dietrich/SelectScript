from operator import and_, not_, xor, or_, lt, le, eq, ne, ge, gt, \
                     add, sub, mul, div, mod, neg, pos, pow, contains, \
                     itemgetter

from itertools import product, chain, groupby
from SelectScript import SelectScript

from copy import deepcopy 
 
class Interpreter():
    
    def __init__(self):
        self = self
        self.fct_list = {}
        self.var_list = {}
        
        self.fct_desc = {}
        
        self.addFunction('and', and_, "", True),  self.addFunction('not', not_, "", True)
        self.addFunction('xor', xor,  "", True),  self.addFunction('or',  or_ , "", True)
        
        self.addFunction('lt', lt,    "", True),  self.addFunction('le', le,    "", True)
        self.addFunction('eq', eq,    "", True),  self.addFunction('ne', ne,    "", True)
        self.addFunction('ge', ge,    "", True),  self.addFunction('gt', gt,    "", True)
        
        self.addFunction('add', add,  "", True),  self.addFunction('sub', sub,  "", True)
        self.addFunction('mul', mul,  "", True),  self.addFunction('div', div,  "", True)
        self.addFunction('mod', mod,  "", True),  self.addFunction('neg', neg,  "", True)
        self.addFunction('pos', pos,  "", True),  self.addFunction('pow', pow,  "", True)
        
        self.addFunction('in',  contains, "", True)
        self.addFunction('assign', self.addVariable, "", True)
        
        self.addFunction('to',    self._to, "Translates the function-name of an SELECT-clause.\nUsage: to(fct(...), 'new_name')")
        self.addFunction('clear', self.clearMemory, "Delete all defined variables.\nUsage: clear()")        
        self.addFunction('var',   self.debugVariable )        
        self.addFunction('help',  self.help , "Lists all callable functions: help()\nGet help for a specific function: help('function_name')")
        
        self.addFunction('print',    self.ssprint , "Print the result of an expression and return its value.\n Usage: print( ... expr ...)")
        
        self.ss = SelectScript(None, None)
        
        #self.addFunction('getTime', self.getTime )
    ####################################################################################################################
    def _to(self, value, name):
        return value
    ####################################################################################################################
    def help(self, function=None):
        if function == None:
            return [fct for fct in self.fct_desc.keys()]
        if self.fct_desc.has_key(function):
            return function + "\n" + self.fct_desc[function]
        return function + " not found"        
    ####################################################################################################################
    def addVariable(self, name, value, age=0):
        # first instantiation
        if not self.var_list.has_key(name):
            self.var_list[name] = [[], age]
        # add value to not timed variable
        if self.var_list[name][1] == 0:
            self.var_list[name][0] = value
        # add value to timed variable
        else:
            self.var_list[name][0].append([self.getTime(), value])
            # remove the oldest ones ...
            if self.var_list[name] > 0:
                max_age = self.getTime() - self.var_list[name][1]
                self.var_list[name][0] = filter(lambda t: t[0] >= max_age, self.var_list[name][0])
        
        return value
    ####################################################################################################################
    def callVariable(self, name, age=0):
        if self.var_list[name][1] == 0:
            return self.var_list[name][0]
        elif age > 0: # a certain point in time
            for result in self.var_list[name][0]:
                if result[0] == age:
                    return result[1]
            return []
        elif age < 0: # a time period from now on
            t_min = self.getTime() + age
            return [res[1] for res in filter(lambda t: t[0]>=t_min, self.var_list[name][0])]
        elif age == None: # all values
            return map(lambda e: e[1], self.var_list[name][0])        
        else:
            return self.var_list[name][0][-1][1]
    ####################################################################################################################
    def debugVariable(self, name):
        print "age: ", self.var_list[name][1]
        print "val: ", self.var_list[name][0]
    ####################################################################################################################
    def addFunction(self, name, ptr, description="", internal=False):
        self.fct_list[name] = ptr
        if not internal:
            self.fct_desc[name] = description
    ####################################################################################################################
    def callFunction(self, name, params):
        return self.fct_list[name](*params)
    ####################################################################################################################
    def clearMemory(self):
        self.var_list = {}
    ####################################################################################################################
    def getTime(self):
        return 0
    def ssprint(self, value, info=""):
        print info+str(value)
        return value
    ####################################################################################################################
    def eval(self, prog, this=None, ids=None):        
        if isinstance(prog[0], list):
            for stmt in prog:
                res = self.eval(stmt, this, ids)
            return res
                
        elif prog[0] == SelectScript.types['fct']:
            return self.callFunction( prog[1], [ self.eval(elem, this, ids) for elem in prog[2] ] )

        elif prog[0] == SelectScript.types['eval']:
            return self.eval(self.ss.compile(self.eval(prog[1], this, ids)), this, ids)            
        
        elif prog[0] == SelectScript.types['phrase']:
            if type(this[0]) == dict and this[0].has_key(prog[1]):
                return this[0][prog[1]]
            elif self.var_list.has_key(prog[1]):
                return self.callVariable(prog[1])
            else:
                return self.callFunction( prog[1], [ this[0] ] )
        
        elif prog[0] == SelectScript.types['val']:
            return prog[1]
            
        elif prog[0] == SelectScript.types['var']:
            return self.callVariable(prog[1], self.eval(prog[2], this, ids))
            
        elif prog[0] == SelectScript.types['this']:
            return this[ids[prog[1]]]
        
        elif prog[0] == SelectScript.types['list']:
            return [ self.eval(elem, this, ids) for elem in prog[1]]
        
        elif prog[0] == SelectScript.types['sel']:
            return self.evalSelect(prog[1:], this, ids)
            
        else:
            return prog
    ####################################################################################################################
    def evalSelect(self, prog, this=None, ids=None):
        SELECT  = prog[0]
        #########################################################################################
        FROM, FROM_n = self.evalFrom(prog[1], this, ids)
        #########################################################################################
        RECURSION = prog[7]
        if RECURSION != [[],[],[]]:
            self.unique = set()
            return self.evalRecursion(prog, FROM_n, list(FROM))
        #########################################################################################
        else:
            WHERE   = prog[2]
            results = self.evalWhere(FROM, FROM_n, WHERE)
        #########################################################################################
        ORDER   = prog[5]
        if ORDER != []: 
            results = self.evalOrder(ORDER, FROM_n, results)
        #########################################################################################
        GROUP   = prog[3]        
        if GROUP != []: 
            results = self.evalGroup(GROUP, FROM_n, results)
        #########################################################################################
        #HAVING = prog[4]
        #if HAVING != []:
        #    results = self.evalGroup(GROUP, FROM_n, results)
                    
        #########################################################################################
        AS      = [prog[6][0], [ self.eval(elem, this, ids) for elem in prog[6][1] ]]
        
        #########################################################################################
        # get trough all groups
        if isinstance(results, dict):
            results = { key: self.evalAs(AS[0], AS[1], SELECT, FROM_n, elem) for key, elem in results.items() }
        else:
            results = self.evalAs(AS[0], AS[1], SELECT, FROM_n, results)
        
        return results    
    ####################################################################################################################
    def evalFrom(self, prog, this, ids):
        FROM   = []
        FROM_n = {'':0}
        start  = 0
        
        if this != None:
            FROM = [[elem] for elem in this]
            FROM_n = ids
            start  = len(this)
            FROM_n[''] = start
        
        for n, p in enumerate(prog):
            FROM.append( self.getListFrom(self.eval( p, this, ids )) )
            # Variable
            if p[0] == SelectScript.types['var']:
                FROM_n[p[1]] = n+start
            # Assignement
            elif p[0] == SelectScript.types['fct']:
                FROM_n[self.eval(p[2][0])] = n+start
                
        return (product(*FROM), FROM_n)
    ####################################################################################################################
    def evalRecursion(self, prog, FROM_n, FROM):
        #print "Start recursion"
        start_with = deepcopy(prog[7][0])
        connect_by = deepcopy(prog[7][1])
        stop_with  = deepcopy(prog[7][2])
        
        prog[7][0] = []                 # remove start with
        
        sub_prog = deepcopy(prog)
        sub_prog[7] = [[],[],[]]
        
        result = []
        
        # create inital variable configuration
        for e in start_with:
            self.eval(e)
        initial_var_list = deepcopy(self.var_list)
        
        for elem in FROM:
            
                
            #print "1---------", self.callVariable('tower')
            # if final step ...
            if self.eval(stop_with, elem, FROM_n):
                self.var_list = deepcopy(initial_var_list)
                #print "FINAL level: ", self.callVariable('level'), self.callVariable('tower'), elem
                if self.evalWhere([elem], FROM_n, prog[2]) != []:
                    sub = self.evalAs(prog[6][0], prog[6][1], prog[0], FROM_n, [elem])
               
                    self.unique.add(hash(str(sub)))
                    result.append(sub)
                    
            # step in further into recursion
            else:
                self.var_list = deepcopy(initial_var_list)
                #print "2---------", self.callVariable('tower')
                
                sub = self.evalAs(prog[6][0], prog[6][1], prog[0], FROM_n, [elem])
                
                #print hash(str(sub)), sub, 
                if hash(str(sub)) in self.unique:
                    #print sub, cycle
                #    print "NOT"
                    continue
                #print "IN"
                self.unique.add(hash(str(sub)))
                
                if self.evalWhere([elem], FROM_n, prog[2]) != []:
                    #print "where"
                    result+=sub
                self.var_list = deepcopy(initial_var_list)
                #print "NOT FINAL level: ", self.callVariable('level'), self.callVariable('tower'), elem
                
                for e in connect_by:
                    self.eval(e, elem, FROM_n)
                sub_2 = self.evalRecursion(prog, FROM_n, FROM)
                self.var_list = deepcopy(initial_var_list)
                                    
                #print "XXXXXXXXXXXXXXXXXNOT FINAL level: ", self.callVariable('level'), self.callVariable('tower'), elem
                
                if sub_2 != []:
                    for ss in sub_2:
                        if not isinstance(ss, list):
                            result.append(sub+[ss])
                        else:
                            result.append(sub+ss)
            
            self.var_list = deepcopy(initial_var_list)
        #print "END recursion"
        return result
            
#            
#            
#            
#            res_bool, res_eval = self.evalRecursion(prog, FROM_n, FROM)
#            
#            if res_bool:
#                AS = [prog[6][0], [ self.eval(elem, this, ids) for elem in prog[6][1] ]]
#                                
#                sub_results.append(self.evalAs(AS[0], AS[1], prog[0], FROM_n, [elem]))
#                sub_results += res_eval
#                
#            result
        return result
        
    def evalWhere(self, FROM, FROM_n, WHERE):
        if WHERE == []:
            return FROM
        return [ elem for elem in FROM if self.eval(WHERE, elem, FROM_n) ]
    ####################################################################################################################
    def evalGroup(self, GROUP, FROM_n, RESULTS):
        matrix = map( lambda elem:  list(chain( map(lambda g: self.eval(g, elem, FROM_n), GROUP), [elem])), RESULTS )  
        for i in range(len(GROUP)-1, -1, -1):
            matrix = sorted(matrix, key=itemgetter(i))        
        return { key: map(lambda e: e[-1], val) for key, val in groupby( matrix, lambda g: str(g[:-1])[1:-1]) }
    ####################################################################################################################
    def evalOrder(self, ORDER, FROM_n, RESULTS):        
        matrix = map( lambda elem:  list(chain( map(lambda o: self.eval(o[0], elem, FROM_n), ORDER), [elem])), RESULTS )        
        for i in range(len(ORDER)-1, -1, -1):
            matrix.sort(key=itemgetter(i), reverse = ORDER[i][1])
        return map(lambda x: x[-1], matrix)        
    ####################################################################################################################
    def evalAs(self, AS, PARAMS, SELECT, FROM_n, RESULTS):
        if AS == SelectScript.asTypes['list']:
            return self.evalAS_list(PARAMS, SELECT, FROM_n, RESULTS)
        elif AS == SelectScript.asTypes['dict']:
            return self.evalAS_dict(PARAMS, SELECT, FROM_n, RESULTS)
        elif AS == SelectScript.asTypes['value']:
            return self.evalAS_value(PARAMS, SELECT, FROM_n, RESULTS)
        return None
    ####################################################################################################################
    def evalAS_value(self, PARAMS, SELECT, FROM_n, RESULTS):
        if RESULTS != []:
            return self.eval( SELECT[0] , RESULTS[0], FROM_n )
        return []
    ####################################################################################################################
    def evalAS_list(self, PARAMS, SELECT, FROM_n, RESULTS):
        return [ self.eval(fct, elem, FROM_n) for elem in RESULTS for fct in SELECT]
    ####################################################################################################################
    def evalAS_dict(self, PARAMS, SELECT, FROM_n, RESULTS):
        return [ { self.eval(f[2][1], elem, FROM_n) if f[1] == "to" else f[1] :
                       self.eval(f, elem, FROM_n)
                    for f in SELECT }
                   for elem in RESULTS  ]
    ####################################################################################################################
    def getListFrom(self, obj):
        return obj if isinstance(obj, list) else [obj]
