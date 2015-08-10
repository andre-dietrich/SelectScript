# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectScript.g 2015-08-10 19:05:46

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
        
import sys

import antlr3
import antlr3.tree

import operator

from SelectExprLexer import SelectExprLexer
from SelectExprParser import SelectExprParser



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
VAL=6
VAR=5
LIST_BEGIN=49
ELSE=14
PHRASE=105
IF=46
CYCLE=81
GRAPH=84
SUB=40
IN=31
STOP=78
MAXIMUM=87
DOT=15
WHERE=62
AS=73
LINE_COMMENT=96
POS=9
FCT=4
POW=44
THEN=13
XOR=26
SEP=16
A=19
B=70
C=56
D=21
E=54
F=45
G=64
H=61
I=30
CONNECT=76
J=106
K=107
ASSIGN=32
L=55
M=58
N=20
COMMENT=95
O=24
P=66
ORDER=63
GROUP=67
Q=82
ASC=88
R=25
S=53
T=28
U=65
V=68
W=60
BY=72
X=23
Y=71
Z=85
CHARACTER=103
SQ=47
SELECT=57
DIV=42
NEG=10
MEMORIZE=86
ELEMENT=8
LIST_END=50
LE=35
STRING=97
ADD=39
LT=37
FROM=59
DQ=48
SPECIAL=104
DESC=89
INTEGER=99
MUL=41
NEWLINE=93
UNIQUE=83
TRUE=101
EQ=33
NOT=29
AND=22
NE=34
THIS=74
END=17
HAVING=69
LIST=7
NO=80
FLOAT=100
AS_VALUE=91
AGE_END=52
AS_DICT=92
WS=94
EOF=-1
GE=36
AGE=11
OR=27
MOD=43
AGE_BEGIN=51
STMT_SELECT=12
COLON=18
TIME=75
GT=38
DIGIT=98
WITH=79
T__108=108
START=77
FALSE=102
T__109=109
AS_LIST=90

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FCT", "VAR", "VAL", "LIST", "ELEMENT", "POS", "NEG", "AGE", "STMT_SELECT", 
    "THEN", "ELSE", "DOT", "SEP", "END", "COLON", "A", "N", "D", "AND", 
    "X", "O", "R", "XOR", "OR", "T", "NOT", "I", "IN", "ASSIGN", "EQ", "NE", 
    "LE", "GE", "LT", "GT", "ADD", "SUB", "MUL", "DIV", "MOD", "POW", "F", 
    "IF", "SQ", "DQ", "LIST_BEGIN", "LIST_END", "AGE_BEGIN", "AGE_END", 
    "S", "E", "L", "C", "SELECT", "M", "FROM", "W", "H", "WHERE", "ORDER", 
    "G", "U", "P", "GROUP", "V", "HAVING", "B", "Y", "BY", "AS", "THIS", 
    "TIME", "CONNECT", "START", "STOP", "WITH", "NO", "CYCLE", "Q", "UNIQUE", 
    "GRAPH", "Z", "MEMORIZE", "MAXIMUM", "ASC", "DESC", "AS_LIST", "AS_VALUE", 
    "AS_DICT", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT", "STRING", "DIGIT", 
    "INTEGER", "FLOAT", "TRUE", "FALSE", "CHARACTER", "SPECIAL", "PHRASE", 
    "J", "K", "'('", "')'"
]




class SelectScript(TreeParser):
    grammarFileName = "SelectScript.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SelectScript, self).__init__(input, state, *args, **kwargs)

        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )






                


        

             

    fct_list = {'=' : 'assign', 'in' : 'in',
                'and' : 'and', 'not' : 'not',
                'xor' : 'xor', 'or'  : 'or',
                'lt'  : 'lt',  'le'  : 'le',
                'eq'  : 'eq',  'ne'  : 'ne',
                'ge'  : 'ge',  'gt'  : 'gt' }

    simplify_ops = {'or':  operator.or_,	'xor':operator.xor,
    		'and': operator.and_,	'not': operator.not_,
    		'eq':  operator.eq,	'ne':  operator.ne,
    		'ge':  operator.ge, 	'gt':  operator.gt,
    		'le':  operator.le, 	'lt':  operator.lt,
    		'mul': operator.mul, 	'div': operator.div,
    		'mod': operator.mod, 	'sub': operator.sub,
    		'add': operator.add, 	'pow': operator.pow,
    		'neg': operator.neg, 	'pos': operator.pos}

    types = {'fct' :   0, 'var' : 1,
             'list':   2, 'val' : 3,
             'sel' :   4, 'this': 5,
             'phrase': 6, 'eval': 7,
             'elem':   8, 'id':   9,
             'if'  : 10 }

    asTypes = {'dict' :'d', 'list' :'l', 'value':'v'}

    def _fct(self, name, params):
    	return [self.types['fct'], name, params]

    def _var(self, var_name, age=0) :
    	return [self.types['var'], var_name, age]

    def _val(self, value) :
    	return [self.types['val'], value]

    def _list(self, l) :
    	return [self.types['list'], l]

    def _sel(self, s, f, w, g, h, o, a, rec) :
    	return [self.types['sel'], s, f, w, g, h, o, a, rec]

    def _this(self, name='') :
    	return [self.types['this'], name]

    def _phrase(self, name) :
    	return [self.types['phrase'], name]

    def _eval(self, string):
    	return [self.types['eval'], string]

    def _elem(self, atom, params):
    	return [self.types['elem'], atom, params]

    def _if(self, expr, params1, params2):
        #print expr, "---",params1, "---" ,params2
        return [self.types['if'], expr, params1, params2]

    def Simplify(self, prog) :

    	if prog == []:
    		pass
    	# program
    	elif isinstance(prog[0], list):
    		for i in range(len(prog)):
    			prog[i] = self.Simplify(prog[i])
    	# functions
    	elif prog[0] == self.types['fct']:
    		params = []
    		reduce = True
    		for param in prog[2]:
    			params.append( self.Simplify(param) )
    			if params[-1][0] != self.types['val']:
    				reduce = False
    		if reduce and (prog[1] in self.simplify_ops.keys()):
    			prog = self._val( self.simplify_ops[prog[1]](*[p[1] for p in params]) )
    		else :
    			prog[2] = params
    	# lists
    	elif prog[0] == self.types['list']:
    		for i in range(len(prog[1])):
    			prog[1][i] = self.Simplify(prog[1][i])
    	# select
    	elif prog[0] == self.types['sel']:
    		S, F, W, G, H, O, A, R = prog[1:]

    		S = [self.Simplify(expr) for expr in S]
    		F = [self.Simplify(expr) for expr in F]
    		W =  self.Simplify(W)
    		G = [self.Simplify(expr) for expr in G]
    		H = [self.Simplify(expr) for expr in H]
    		if O != []:
    			O = [[self.Simplify(expr[0]), expr[1]] for expr in O]
    		A[1] = [self.Simplify(expr) for expr in A[1]]

    		R[0] = [self.Simplify(expr) for expr in R[0]]
    		R[1] = [self.Simplify(expr) for expr in R[1]]
    		R[2] = [self.Simplify(expr) for expr in R[2]]

    		prog = self._sel(S, F, W, G, H, O, A)

    	return prog

    def compile(self, source, debug=False) :
    	char_stream = antlr3.ANTLRStringStream(source)
    	lexer = SelectExprLexer(char_stream)
    	tokens = antlr3.CommonTokenStream(lexer)
    	parser = SelectExprParser(tokens)
    	r = parser.eval()

    	# this is the root of the AST
    	root = r.tree

    	nodes = antlr3.tree.CommonTreeNodeStream(root)
    	nodes.setTokenStream(tokens)
    	self.__init__(nodes)
    	if debug:
    		return self.eval()

    	return self.Simplify(self.eval())

    def prettyPrint(self, prog, depth=0):

    	if prog == []:
    		return

    	treE = "   "*depth

    	if isinstance(prog[0], list):
    		for stmt in prog:
    			print treE, "["
    			self.prettyPrint( stmt, depth+1 )
    			print treE, "]"

    	elif prog[0] == self.types['fct']:
    		print treE, "[ func,", prog[1], "[ "
    		for param in prog[2]:
    			self.prettyPrint( param, depth+1 )
    		print treE, "]"

    	elif prog[0] == self.types['val']:
    		print treE, "[ val,", prog[1], "]"

    	elif prog[0] == self.types['this']:
    		print treE, "[ this,", prog[1], "]"

    	elif prog[0] == self.types['var']:
    		print treE, "[ var,", prog[1], ", age, ["
    		self.prettyPrint( prog[2], depth+1 )
    		print treE, "] ]"

    	elif prog[0] == self.types['list']:
    		print treE, "[ list, ["
    		self.prettyPrint( prog[1], depth+1 )
    		print treE, "]"

    	elif prog[0] == self.types['phrase']:
    		print treE, "[ phrase, ", prog[1], "]"

    	elif prog[0] == self.types['sel']:
    		print treE, "[ SELECT-statement, "
    		treE += "   "

    		print treE, "[ select,",
    		self.prettyPrint( prog[1], depth+2 )

    		print treE, "[ from, ",
    		self.prettyPrint( prog[2], depth+2 )

    		if prog[3] != []:
    			print treE, "[ where, ",
    			self.prettyPrint( [prog[3]], depth+2 )

    		if prog[4] != []:
    			print treE, "[ group by, ",
    			self.prettyPrint( prog[4], depth+2 )

    		if prog[6] != []:
    			print treE, "[ order by, ",
    			self.prettyPrint( prog[6], depth+2 )

    		if prog[7] != []:
    			print treE, "[ as,", prog[7][0], # "]"
    			self.prettyPrint( prog[7][1], depth+2 )

    		if prog[8] != [[],[],[]]:
    			print treE, "[ start with,",
    			self.prettyPrint( prog[8][0], depth+2 )
    			print treE, "[ connect by,",
    			self.prettyPrint( prog[8][1], depth+2 )
    			print treE, "[ stop with,",
    			self.prettyPrint( prog[8][2], depth+2 )
    	else:
    		print ""



    # $ANTLR start "eval"
    # SelectScript.g:247:1: eval returns [stmt_list] : p= prog ;
    def eval(self, ):

        stmt_list = None

        p = None


        try:
            try:
                # SelectScript.g:247:25: (p= prog )
                # SelectScript.g:248:5: p= prog
                pass 
                self._state.following.append(self.FOLLOW_prog_in_eval72)
                p = self.prog()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stmt_list = p





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stmt_list

    # $ANTLR end "eval"


    # $ANTLR start "prog"
    # SelectScript.g:251:1: prog returns [stmt_list] : (stmt= statement )+ ;
    def prog(self, ):

        stmt_list = None

        stmt = None


        stmt_list = []
        try:
            try:
                # SelectScript.g:252:22: ( (stmt= statement )+ )
                # SelectScript.g:253:2: (stmt= statement )+
                pass 
                # SelectScript.g:253:2: (stmt= statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((FCT <= LA1_0 <= NEG) or LA1_0 == STMT_SELECT or LA1_0 == AND or (XOR <= LA1_0 <= OR) or LA1_0 == NOT or (IN <= LA1_0 <= POW) or LA1_0 == IF or LA1_0 == THIS or LA1_0 == 108) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectScript.g:253:3: stmt= statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_prog94)
                        stmt = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stmt_list.append( stmt )



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stmt_list

    # $ANTLR end "prog"


    # $ANTLR start "statement"
    # SelectScript.g:256:1: statement returns [stmt] : (s= statement_select | e= expr );
    def statement(self, ):

        stmt = None

        s = None

        e = None


        try:
            try:
                # SelectScript.g:256:25: (s= statement_select | e= expr )
                alt2 = 2
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectScript.g:257:2: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_statement113)
                    s = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stmt = s



                elif alt2 == 2:
                    # SelectScript.g:258:4: e= expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_statement123)
                    e = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stmt = e




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stmt

    # $ANTLR end "statement"


    # $ANTLR start "statement_select"
    # SelectScript.g:261:1: statement_select returns [selection] : ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? ) ;
    def statement_select(self, ):

        selection = None

        s = None

        f = None

        w = None

        g = None

        h = None

        o = None

        a = None

        rec_start = None

        rec_connect = None

        rec_stop = None


        s=[]; f=[]; w=[]; g=[]; h=[]; o=[]; a=[self.asTypes['dict'],[]]; rec_start=[]; rec_connect=[[],[0,0]]; rec_stop=[]; 
        try:
            try:
                # SelectScript.g:264:1: ( ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? ) )
                # SelectScript.g:265:2: ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? )
                pass 
                self.match(self.input, STMT_SELECT, self.FOLLOW_STMT_SELECT_in_statement_select150)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_select__in_statement_select154)
                s = self.select_()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_from__in_statement_select158)
                f = self.from_()

                self._state.following.pop()
                # SelectScript.g:265:34: (w= where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    alt3 = 1
                if alt3 == 1:
                    # SelectScript.g:265:36: w= where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select164)
                    w = self.where_()

                    self._state.following.pop()



                # SelectScript.g:265:48: (g= group_ (h= having_ )? )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == GROUP) :
                    alt5 = 1
                if alt5 == 1:
                    # SelectScript.g:265:50: g= group_ (h= having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select173)
                    g = self.group_()

                    self._state.following.pop()
                    # SelectScript.g:265:59: (h= having_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == HAVING) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectScript.g:265:60: h= having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select178)
                        h = self.having_()

                        self._state.following.pop()






                # SelectScript.g:265:74: (o= order_ )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ORDER) :
                    alt6 = 1
                if alt6 == 1:
                    # SelectScript.g:265:76: o= order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select188)
                    o = self.order_()

                    self._state.following.pop()



                # SelectScript.g:265:88: (a= as_ )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == AS) :
                    alt7 = 1
                if alt7 == 1:
                    # SelectScript.g:265:90: a= as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select197)
                    a = self.as_()

                    self._state.following.pop()



                # SelectScript.g:265:99: ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((CONNECT <= LA9_0 <= START)) :
                    alt9 = 1
                if alt9 == 1:
                    # SelectScript.g:265:100: (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_
                    pass 
                    # SelectScript.g:265:100: (rec_start= start_ )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == START) :
                        alt8 = 1
                    if alt8 == 1:
                        # SelectScript.g:265:101: rec_start= start_
                        pass 
                        self._state.following.append(self.FOLLOW_start__in_statement_select206)
                        rec_start = self.start_()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_connect__in_statement_select212)
                    rec_connect = self.connect_()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_stop__in_statement_select216)
                    rec_stop = self.stop_()

                    self._state.following.pop()




                self.match(self.input, UP, None)



                if self._state.backtracking == 0:
                    selection = self._sel(s, f, w, g, h, o, a, [rec_start, rec_connect[0], rec_stop, rec_connect[1]]); 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return selection

    # $ANTLR end "statement_select"


    # $ANTLR start "select_"
    # SelectScript.g:268:1: select_ returns [types] : ^( SELECT (type= PHRASE | f= function | t= this_ | e= expr )* ) ;
    def select_(self, ):

        types = None

        type = None
        f = None

        t = None

        e = None


        types = []
        try:
            try:
                # SelectScript.g:269:19: ( ^( SELECT (type= PHRASE | f= function | t= this_ | e= expr )* ) )
                # SelectScript.g:270:2: ^( SELECT (type= PHRASE | f= function | t= this_ | e= expr )* )
                pass 
                self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_240)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:271:3: (type= PHRASE | f= function | t= this_ | e= expr )*
                    while True: #loop10
                        alt10 = 5
                        alt10 = self.dfa10.predict(self.input)
                        if alt10 == 1:
                            # SelectScript.g:272:3: type= PHRASE
                            pass 
                            type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_250)
                            if self._state.backtracking == 0:
                                types.append( self._phrase (type.getText()) ); 



                        elif alt10 == 2:
                            # SelectScript.g:273:5: f= function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_select_262)
                            f = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( f ); 



                        elif alt10 == 3:
                            # SelectScript.g:274:5: t= this_
                            pass 
                            self._state.following.append(self.FOLLOW_this__in_select_273)
                            t = self.this_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( t ); 



                        elif alt10 == 4:
                            # SelectScript.g:275:5: e= expr
                            pass 
                            self._state.following.append(self.FOLLOW_expr_in_select_286)
                            e = self.expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( e ); 



                        else:
                            break #loop10

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return types

    # $ANTLR end "select_"


    # $ANTLR start "from_"
    # SelectScript.g:280:1: from_ returns [env] : ^( FROM (e= expr )+ ) ;
    def from_(self, ):

        env = None

        e = None


        env=[]; 
        try:
            try:
                # SelectScript.g:281:17: ( ^( FROM (e= expr )+ ) )
                # SelectScript.g:282:2: ^( FROM (e= expr )+ )
                pass 
                self.match(self.input, FROM, self.FOLLOW_FROM_in_from_318)

                self.match(self.input, DOWN, None)
                # SelectScript.g:282:9: (e= expr )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((FCT <= LA11_0 <= NEG) or LA11_0 == STMT_SELECT or LA11_0 == AND or (XOR <= LA11_0 <= OR) or LA11_0 == NOT or (IN <= LA11_0 <= POW) or LA11_0 == IF or LA11_0 == THIS or LA11_0 == 108) :
                        alt11 = 1


                    if alt11 == 1:
                        # SelectScript.g:282:10: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_from_323)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            env.append(e); 



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return env

    # $ANTLR end "from_"


    # $ANTLR start "as_"
    # SelectScript.g:285:1: as_ returns [rep] : ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) );
    def as_(self, ):

        rep = None

        v = None
        p = None


        p=[]; 
        try:
            try:
                # SelectScript.g:286:15: ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) )
                alt13 = 4
                LA13_0 = self.input.LA(1)

                if (LA13_0 == AS) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == 2) :
                        LA13 = self.input.LA(3)
                        if LA13 == AS_DICT:
                            alt13 = 1
                        elif LA13 == AS_LIST:
                            alt13 = 2
                        elif LA13 == AS_VALUE:
                            alt13 = 3
                        elif LA13 == PHRASE:
                            alt13 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 13, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # SelectScript.g:287:2: ^( AS AS_DICT )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_346)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_348)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['dict'],  []]; 



                elif alt13 == 2:
                    # SelectScript.g:288:4: ^( AS AS_LIST )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_360)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_362)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['list'],  []]; 



                elif alt13 == 3:
                    # SelectScript.g:289:4: ^( AS AS_VALUE )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_374)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_376)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['value'], []]; 



                elif alt13 == 4:
                    # SelectScript.g:290:4: ^( AS v= PHRASE (p= parameter )? )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_387)

                    self.match(self.input, DOWN, None)
                    v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_391)
                    # SelectScript.g:290:18: (p= parameter )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((FCT <= LA12_0 <= NEG) or LA12_0 == STMT_SELECT or LA12_0 == AND or (XOR <= LA12_0 <= OR) or LA12_0 == NOT or (IN <= LA12_0 <= POW) or LA12_0 == IF or LA12_0 == THIS or LA12_0 == 108) :
                        alt12 = 1
                    elif (LA12_0 == 3) :
                        LA12_2 = self.input.LA(2)

                        if (self.synpred18_SelectScript()) :
                            alt12 = 1
                    if alt12 == 1:
                        # SelectScript.g:290:20: p= parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_as_397)
                        p = self.parameter()

                        self._state.following.pop()




                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ v.getText(),           p ]; 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return rep

    # $ANTLR end "as_"


    # $ANTLR start "where_"
    # SelectScript.g:293:1: where_ returns [stack] : ^( WHERE e= expr ) ;
    def where_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:293:24: ( ^( WHERE e= expr ) )
                # SelectScript.g:294:2: ^( WHERE e= expr )
                pass 
                self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_419)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_where_423)
                e = self.expr()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    stack=e 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "where_"


    # $ANTLR start "start_"
    # SelectScript.g:297:1: start_ returns [with_] : ^( START (e= expr )+ ) ;
    def start_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:298:19: ( ^( START (e= expr )+ ) )
                # SelectScript.g:299:2: ^( START (e= expr )+ )
                pass 
                self.match(self.input, START, self.FOLLOW_START_in_start_444)

                self.match(self.input, DOWN, None)
                # SelectScript.g:299:10: (e= expr )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((FCT <= LA14_0 <= NEG) or LA14_0 == STMT_SELECT or LA14_0 == AND or (XOR <= LA14_0 <= OR) or LA14_0 == NOT or (IN <= LA14_0 <= POW) or LA14_0 == IF or LA14_0 == THIS or LA14_0 == 108) :
                        alt14 = 1


                    if alt14 == 1:
                        # SelectScript.g:299:11: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_start_449)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            with_.append(e); 



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return with_

    # $ANTLR end "start_"


    # $ANTLR start "connect_"
    # SelectScript.g:302:1: connect_ returns [by] : ^( CONNECT ( CYCLE )? ( UNIQUE )? ( MEMORIZE (I1= INTEGER )? )? ( MAXIMUM I2= INTEGER )? (e= expr )+ ) ;
    def connect_(self, ):

        by = None

        I1 = None
        I2 = None
        e = None


        by = [[],[0,0,0,0]]
        try:
            try:
                # SelectScript.g:303:28: ( ^( CONNECT ( CYCLE )? ( UNIQUE )? ( MEMORIZE (I1= INTEGER )? )? ( MAXIMUM I2= INTEGER )? (e= expr )+ ) )
                # SelectScript.g:304:2: ^( CONNECT ( CYCLE )? ( UNIQUE )? ( MEMORIZE (I1= INTEGER )? )? ( MAXIMUM I2= INTEGER )? (e= expr )+ )
                pass 
                self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_473)

                self.match(self.input, DOWN, None)
                # SelectScript.g:305:8: ( CYCLE )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == CYCLE) :
                    alt15 = 1
                if alt15 == 1:
                    # SelectScript.g:305:9: CYCLE
                    pass 
                    self.match(self.input, CYCLE, self.FOLLOW_CYCLE_in_connect_483)
                    if self._state.backtracking == 0:
                        by[1][0] = 1;                       




                # SelectScript.g:306:8: ( UNIQUE )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == UNIQUE) :
                    alt16 = 1
                if alt16 == 1:
                    # SelectScript.g:306:9: UNIQUE
                    pass 
                    self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_connect_512)
                    if self._state.backtracking == 0:
                        by[1][1] = 1;                       




                # SelectScript.g:308:5: ( MEMORIZE (I1= INTEGER )? )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MEMORIZE) :
                    alt18 = 1
                if alt18 == 1:
                    # SelectScript.g:308:6: MEMORIZE (I1= INTEGER )?
                    pass 
                    self.match(self.input, MEMORIZE, self.FOLLOW_MEMORIZE_in_connect_538)
                    if self._state.backtracking == 0:
                        by[1][2] = 1; 

                    # SelectScript.g:309:9: (I1= INTEGER )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == INTEGER) :
                        alt17 = 1
                    if alt17 == 1:
                        # SelectScript.g:309:10: I1= INTEGER
                        pass 
                        I1=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_553)
                        if self._state.backtracking == 0:
                            by[1][2] = int(I1.getText()); 







                # SelectScript.g:311:5: ( MAXIMUM I2= INTEGER )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MAXIMUM) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectScript.g:311:6: MAXIMUM I2= INTEGER
                    pass 
                    self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_connect_570)
                    I2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_575)
                    if self._state.backtracking == 0:
                        by[1][3] = int(I2.getText());    




                # SelectScript.g:312:8: (e= expr )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((FCT <= LA20_0 <= NEG) or LA20_0 == STMT_SELECT or LA20_0 == AND or (XOR <= LA20_0 <= OR) or LA20_0 == NOT or (IN <= LA20_0 <= POW) or LA20_0 == IF or LA20_0 == THIS or LA20_0 == 108) :
                        alt20 = 1


                    if alt20 == 1:
                        # SelectScript.g:312:9: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_connect_595)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by[0].append(e);                    



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "connect_"


    # $ANTLR start "stop_"
    # SelectScript.g:316:1: stop_ returns [with_] : ^( STOP (e= expr ) ) ;
    def stop_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:317:19: ( ^( STOP (e= expr ) ) )
                # SelectScript.g:318:2: ^( STOP (e= expr ) )
                pass 
                self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_635)

                self.match(self.input, DOWN, None)
                # SelectScript.g:318:9: (e= expr )
                # SelectScript.g:318:10: e= expr
                pass 
                self._state.following.append(self.FOLLOW_expr_in_stop_640)
                e = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    with_ = e; 





                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return with_

    # $ANTLR end "stop_"


    # $ANTLR start "group_"
    # SelectScript.g:321:1: group_ returns [by] : ^( GROUP (type= PHRASE | f= function )+ ) ;
    def group_(self, ):

        by = None

        type = None
        f = None


        by = []
        try:
            try:
                # SelectScript.g:322:16: ( ^( GROUP (type= PHRASE | f= function )+ ) )
                # SelectScript.g:323:2: ^( GROUP (type= PHRASE | f= function )+ )
                pass 
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_664)

                self.match(self.input, DOWN, None)
                # SelectScript.g:324:3: (type= PHRASE | f= function )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 3
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == PHRASE) :
                        alt21 = 1
                    elif (LA21_0 == FCT) :
                        alt21 = 2


                    if alt21 == 1:
                        # SelectScript.g:324:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_672)
                        if self._state.backtracking == 0:
                            by.append( self._phrase ( type.getText() ) ); 



                    elif alt21 == 2:
                        # SelectScript.g:325:5: f= function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_group_683)
                        f = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( f ); 



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "group_"


    # $ANTLR start "having_"
    # SelectScript.g:330:1: having_ returns [stack] : ^( HAVING e= expr ) ;
    def having_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:330:25: ( ^( HAVING e= expr ) )
                # SelectScript.g:331:2: ^( HAVING e= expr )
                pass 
                self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_708)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_having_712)
                e = self.expr()

                self._state.following.pop()

                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    stack=e 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "having_"


    # $ANTLR start "order_"
    # SelectScript.g:334:1: order_ returns [by] : ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) ;
    def order_(self, ):

        by = None

        type = None
        f = None

        dir = None


        by = []
        try:
            try:
                # SelectScript.g:335:16: ( ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) )
                # SelectScript.g:336:2: ^( ORDER (type= PHRASE | f= function dir= direction_ )+ )
                pass 
                self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_734)

                self.match(self.input, DOWN, None)
                # SelectScript.g:337:3: (type= PHRASE | f= function dir= direction_ )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 3
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == PHRASE) :
                        alt22 = 1
                    elif (LA22_0 == FCT) :
                        alt22 = 2


                    if alt22 == 1:
                        # SelectScript.g:338:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_746)
                        if self._state.backtracking == 0:
                            by.append( [ self._phrase ( type.getText()), dir ]); 



                    elif alt22 == 2:
                        # SelectScript.g:339:5: f= function dir= direction_
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_order_758)
                        f = self.function()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_direction__in_order_762)
                        dir = self.direction_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( [f, dir] ); 



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "order_"


    # $ANTLR start "direction_"
    # SelectScript.g:344:1: direction_ returns [dir] : ( ASC | DESC )? ;
    def direction_(self, ):

        dir = None

        dir = 0
        try:
            try:
                # SelectScript.g:345:16: ( ( ASC | DESC )? )
                # SelectScript.g:346:2: ( ASC | DESC )?
                pass 
                # SelectScript.g:346:2: ( ASC | DESC )?
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == ASC) :
                    alt23 = 1
                elif (LA23_0 == DESC) :
                    alt23 = 2
                if alt23 == 1:
                    # SelectScript.g:346:4: ASC
                    pass 
                    self.match(self.input, ASC, self.FOLLOW_ASC_in_direction_792)
                    if self._state.backtracking == 0:
                        dir=0; 



                elif alt23 == 2:
                    # SelectScript.g:347:4: DESC
                    pass 
                    self.match(self.input, DESC, self.FOLLOW_DESC_in_direction_800)
                    if self._state.backtracking == 0:
                        dir=1; 








            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return dir

    # $ANTLR end "direction_"


    # $ANTLR start "expr"
    # SelectScript.g:351:1: expr returns [val] : (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | i= if_statement | a= atom );
    def expr(self, ):

        val = None

        a = None

        l = None

        c = None

        i = None


        try:
            try:
                # SelectScript.g:351:20: (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | i= if_statement | a= atom )
                alt24 = 6
                LA24 = self.input.LA(1)
                if LA24 == ASSIGN:
                    alt24 = 1
                elif LA24 == AND or LA24 == XOR or LA24 == OR or LA24 == NOT:
                    alt24 = 2
                elif LA24 == IN or LA24 == EQ or LA24 == NE or LA24 == LE or LA24 == GE or LA24 == LT or LA24 == GT:
                    alt24 = 3
                elif LA24 == ELEMENT or LA24 == POS or LA24 == NEG or LA24 == ADD or LA24 == SUB or LA24 == MUL or LA24 == DIV or LA24 == MOD or LA24 == POW:
                    alt24 = 4
                elif LA24 == IF:
                    alt24 = 5
                elif LA24 == FCT or LA24 == VAR or LA24 == VAL or LA24 == LIST or LA24 == STMT_SELECT or LA24 == THIS or LA24 == 108:
                    alt24 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # SelectScript.g:352:2: a= assign_expr
                    pass 
                    self._state.following.append(self.FOLLOW_assign_expr_in_expr824)
                    a = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt24 == 2:
                    # SelectScript.g:353:4: l= logic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_logic_expr_in_expr837)
                    l = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = l;



                elif alt24 == 3:
                    # SelectScript.g:354:4: c= compare_expr
                    pass 
                    self._state.following.append(self.FOLLOW_compare_expr_in_expr850)
                    c = self.compare_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = c;



                elif alt24 == 4:
                    # SelectScript.g:355:4: a= arithmetic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_arithmetic_expr_in_expr862)
                    a = self.arithmetic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt24 == 5:
                    # SelectScript.g:356:4: i= if_statement
                    pass 
                    self._state.following.append(self.FOLLOW_if_statement_in_expr873)
                    i = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = i;



                elif alt24 == 6:
                    # SelectScript.g:357:4: a= atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_expr887)
                    a = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return val

    # $ANTLR end "expr"


    # $ANTLR start "age"
    # SelectScript.g:360:1: age returns [a] : ^( AGE (t= expr )? ) ;
    def age(self, ):

        a = None

        t = None


        a=self._val(0); 
        try:
            try:
                # SelectScript.g:361:25: ( ^( AGE (t= expr )? ) )
                # SelectScript.g:362:2: ^( AGE (t= expr )? )
                pass 
                self.match(self.input, AGE, self.FOLLOW_AGE_in_age914)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:362:8: (t= expr )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((FCT <= LA25_0 <= NEG) or LA25_0 == STMT_SELECT or LA25_0 == AND or (XOR <= LA25_0 <= OR) or LA25_0 == NOT or (IN <= LA25_0 <= POW) or LA25_0 == IF or LA25_0 == THIS or LA25_0 == 108) :
                        alt25 = 1
                    if alt25 == 1:
                        # SelectScript.g:362:9: t= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_age919)
                        t = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            a=t; 





                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return a

    # $ANTLR end "age"


    # $ANTLR start "if_statement"
    # SelectScript.g:365:1: if_statement returns [e] : ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? ) ;
    def if_statement(self, ):

        e = None

        if_ = None

        th = None

        el = None


        if_=self._val( True ); th=self._val( True ); el=self._val( False ); 
        try:
            try:
                # SelectScript.g:366:77: ( ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? ) )
                # SelectScript.g:367:5: ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? )
                pass 
                self.match(self.input, IF, self.FOLLOW_IF_in_if_statement945)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_if_statement949)
                if_ = self.expr()

                self._state.following.pop()
                # SelectScript.g:367:19: ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == THEN) :
                    alt27 = 1
                if alt27 == 1:
                    # SelectScript.g:367:20: ^( THEN th= parameter ( ^( ELSE el= parameter ) )? )
                    pass 
                    self.match(self.input, THEN, self.FOLLOW_THEN_in_if_statement953)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_parameter_in_if_statement957)
                        th = self.parameter()

                        self._state.following.pop()
                        # SelectScript.g:367:40: ( ^( ELSE el= parameter ) )?
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ELSE) :
                            alt26 = 1
                        if alt26 == 1:
                            # SelectScript.g:367:41: ^( ELSE el= parameter )
                            pass 
                            self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_statement961)

                            if self.input.LA(1) == DOWN:
                                self.match(self.input, DOWN, None)
                                self._state.following.append(self.FOLLOW_parameter_in_if_statement965)
                                el = self.parameter()

                                self._state.following.pop()

                                self.match(self.input, UP, None)





                        self.match(self.input, UP, None)





                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    e = self._if(if_, th, el); 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return e

    # $ANTLR end "if_statement"


    # $ANTLR start "assign_expr"
    # SelectScript.g:371:1: assign_expr returns [stack] : ^( ASSIGN v= PHRASE e= expr (a= age )? ) ;
    def assign_expr(self, ):

        stack = None

        v = None
        e = None

        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:372:27: ( ^( ASSIGN v= PHRASE e= expr (a= age )? ) )
                # SelectScript.g:373:2: ^( ASSIGN v= PHRASE e= expr (a= age )? )
                pass 
                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr993)

                self.match(self.input, DOWN, None)
                v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr997)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr1001)
                e = self.expr()

                self._state.following.pop()
                # SelectScript.g:373:27: (a= age )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == AGE) :
                    alt28 = 1
                if alt28 == 1:
                    # SelectScript.g:373:28: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr1006)
                    a = self.age()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    stack = self._fct( 'assign', [ self._val(v.getText()) , e, a]); 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "assign_expr"


    # $ANTLR start "logic_expr"
    # SelectScript.g:376:1: logic_expr returns [stack] : ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) );
    def logic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:376:28: ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) )
                alt29 = 4
                LA29 = self.input.LA(1)
                if LA29 == OR:
                    alt29 = 1
                elif LA29 == XOR:
                    alt29 = 2
                elif LA29 == AND:
                    alt29 = 3
                elif LA29 == NOT:
                    alt29 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # SelectScript.g:377:2: ^( OR e1= expr e2= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_logic_expr1026)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1030)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1034)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('or',  [e1, e2]); 



                elif alt29 == 2:
                    # SelectScript.g:378:4: ^( XOR e1= expr e2= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_expr1043)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1047)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1051)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('xor', [e1, e2]); 



                elif alt29 == 3:
                    # SelectScript.g:379:4: ^( AND e1= expr e2= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_logic_expr1059)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1063)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1067)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('and', [e1, e2]); 



                elif alt29 == 4:
                    # SelectScript.g:380:4: ^( NOT e= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_expr1075)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1079)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('not', [e] ); 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "logic_expr"


    # $ANTLR start "compare_expr"
    # SelectScript.g:383:1: compare_expr returns [stack] : ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) );
    def compare_expr(self, ):

        stack = None

        e1 = None

        e2 = None


        try:
            try:
                # SelectScript.g:383:29: ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) )
                alt30 = 7
                LA30 = self.input.LA(1)
                if LA30 == IN:
                    alt30 = 1
                elif LA30 == EQ:
                    alt30 = 2
                elif LA30 == NE:
                    alt30 = 3
                elif LA30 == GE:
                    alt30 = 4
                elif LA30 == GT:
                    alt30 = 5
                elif LA30 == LE:
                    alt30 = 6
                elif LA30 == LT:
                    alt30 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # SelectScript.g:384:2: ^( IN e1= expr e2= expr )
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_compare_expr1097)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1101)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1105)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('in', [e2, e1]); 



                elif alt30 == 2:
                    # SelectScript.g:385:4: ^( EQ e1= expr e2= expr )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_expr1114)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1118)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1122)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('eq', [e1, e2]); 



                elif alt30 == 3:
                    # SelectScript.g:386:4: ^( NE e1= expr e2= expr )
                    pass 
                    self.match(self.input, NE, self.FOLLOW_NE_in_compare_expr1131)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1135)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1139)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ne', [e1, e2]); 



                elif alt30 == 4:
                    # SelectScript.g:387:4: ^( GE e1= expr e2= expr )
                    pass 
                    self.match(self.input, GE, self.FOLLOW_GE_in_compare_expr1148)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1152)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1156)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ge', [e1, e2]); 



                elif alt30 == 5:
                    # SelectScript.g:388:4: ^( GT e1= expr e2= expr )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_compare_expr1165)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1169)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1173)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('gt', [e1, e2]); 



                elif alt30 == 6:
                    # SelectScript.g:389:4: ^( LE e1= expr e2= expr )
                    pass 
                    self.match(self.input, LE, self.FOLLOW_LE_in_compare_expr1182)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1186)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1190)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('le', [e1, e2]); 



                elif alt30 == 7:
                    # SelectScript.g:390:4: ^( LT e1= expr e2= expr )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_compare_expr1199)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1203)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1207)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('lt', [e1, e2]); 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "compare_expr"


    # $ANTLR start "arithmetic_expr"
    # SelectScript.g:393:1: arithmetic_expr returns [stack] : ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) | ^( ELEMENT a= atom p= parameter ) );
    def arithmetic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None

        a = None

        p = None


        try:
            try:
                # SelectScript.g:393:32: ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) | ^( ELEMENT a= atom p= parameter ) )
                alt31 = 9
                LA31 = self.input.LA(1)
                if LA31 == MUL:
                    alt31 = 1
                elif LA31 == DIV:
                    alt31 = 2
                elif LA31 == MOD:
                    alt31 = 3
                elif LA31 == SUB:
                    alt31 = 4
                elif LA31 == ADD:
                    alt31 = 5
                elif LA31 == POW:
                    alt31 = 6
                elif LA31 == NEG:
                    alt31 = 7
                elif LA31 == POS:
                    alt31 = 8
                elif LA31 == ELEMENT:
                    alt31 = 9
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # SelectScript.g:394:2: ^( MUL e1= expr e2= expr )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_expr1224)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1228)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1232)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mul', [e1, e2]); 



                elif alt31 == 2:
                    # SelectScript.g:395:3: ^( DIV e1= expr e2= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_expr1240)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1244)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1248)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('div', [e1, e2]); 



                elif alt31 == 3:
                    # SelectScript.g:396:3: ^( MOD e1= expr e2= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_expr1256)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1260)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1264)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mod', [e1, e2]); 



                elif alt31 == 4:
                    # SelectScript.g:397:3: ^( SUB e1= expr e2= expr )
                    pass 
                    self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_expr1272)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1276)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1280)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('sub', [e1, e2]); 



                elif alt31 == 5:
                    # SelectScript.g:398:3: ^( ADD e1= expr e2= expr )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_expr1288)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1292)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1296)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('add', [e1, e2]); 



                elif alt31 == 6:
                    # SelectScript.g:399:3: ^( POW e1= expr e2= expr )
                    pass 
                    self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_expr1304)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1308)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1312)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pow', [e1, e2]); 



                elif alt31 == 7:
                    # SelectScript.g:400:3: ^( NEG e= expr )
                    pass 
                    self.match(self.input, NEG, self.FOLLOW_NEG_in_arithmetic_expr1320)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1324)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('neg', [e]); 



                elif alt31 == 8:
                    # SelectScript.g:401:3: ^( POS e= expr )
                    pass 
                    self.match(self.input, POS, self.FOLLOW_POS_in_arithmetic_expr1333)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1337)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pos', [e]); 



                elif alt31 == 9:
                    # SelectScript.g:402:3: ^( ELEMENT a= atom p= parameter )
                    pass 
                    self.match(self.input, ELEMENT, self.FOLLOW_ELEMENT_in_arithmetic_expr1346)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_expr1350)
                    a = self.atom()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_parameter_in_arithmetic_expr1354)
                    p = self.parameter()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._elem(a, p); 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "arithmetic_expr"


    # $ANTLR start "atom"
    # SelectScript.g:405:1: atom returns [stack] : (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select );
    def atom(self, ):

        stack = None

        val = None

        var = None

        fct = None

        e = None

        s = None


        try:
            try:
                # SelectScript.g:405:22: (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select )
                alt32 = 5
                LA32 = self.input.LA(1)
                if LA32 == VAL or LA32 == LIST or LA32 == THIS:
                    alt32 = 1
                elif LA32 == VAR:
                    alt32 = 2
                elif LA32 == FCT:
                    alt32 = 3
                elif LA32 == 108:
                    alt32 = 4
                elif LA32 == STMT_SELECT:
                    alt32 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # SelectScript.g:406:2: val= value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_atom1375)
                    val = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = val



                elif alt32 == 2:
                    # SelectScript.g:407:4: var= variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_atom1388)
                    var = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = var



                elif alt32 == 3:
                    # SelectScript.g:408:4: fct= function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_atom1400)
                    fct = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = fct



                elif alt32 == 4:
                    # SelectScript.g:409:4: '(' e= expr ')'
                    pass 
                    self.match(self.input, 108, self.FOLLOW_108_in_atom1408)
                    self._state.following.append(self.FOLLOW_expr_in_atom1412)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 109, self.FOLLOW_109_in_atom1414)
                    if self._state.backtracking == 0:
                        stack = e  



                elif alt32 == 5:
                    # SelectScript.g:410:4: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_atom1424)
                    s = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = s  




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "atom"


    # $ANTLR start "value"
    # SelectScript.g:413:1: value returns [val] : ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ );
    def value(self, ):

        val = None

        STRING1 = None
        INTEGER2 = None
        FLOAT3 = None
        t = None

        l = None


        try:
            try:
                # SelectScript.g:413:21: ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ )
                alt33 = 7
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # SelectScript.g:414:4: ^( VAL STRING )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1444)

                    self.match(self.input, DOWN, None)
                    STRING1=self.match(self.input, STRING, self.FOLLOW_STRING_in_value1446)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( STRING1.getText()[1:-1] ); 



                elif alt33 == 2:
                    # SelectScript.g:415:4: ^( VAL INTEGER )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1456)

                    self.match(self.input, DOWN, None)
                    INTEGER2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value1458)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( int(INTEGER2.getText()) ); 



                elif alt33 == 3:
                    # SelectScript.g:416:4: ^( VAL FLOAT )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1468)

                    self.match(self.input, DOWN, None)
                    FLOAT3=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value1470)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( float(FLOAT3.getText()) ); 



                elif alt33 == 4:
                    # SelectScript.g:417:4: ^( VAL TRUE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1480)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value1482)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( True  ); 



                elif alt33 == 5:
                    # SelectScript.g:418:4: ^( VAL FALSE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1492)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value1494)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( False ); 



                elif alt33 == 6:
                    # SelectScript.g:419:4: t= this_
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_value1505)
                    t = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val= t; 



                elif alt33 == 7:
                    # SelectScript.g:420:4: l= list_
                    pass 
                    self._state.following.append(self.FOLLOW_list__in_value1515)
                    l = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val= self._list(l ) ; 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return val

    # $ANTLR end "value"


    # $ANTLR start "this_"
    # SelectScript.g:423:1: this_ returns [p] : ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        p = None

        PHRASE4 = None

        p=self._this(); 
        try:
            try:
                # SelectScript.g:424:26: ( ^( THIS ( PHRASE )? ) )
                # SelectScript.g:425:2: ^( THIS ( PHRASE )? )
                pass 
                self.match(self.input, THIS, self.FOLLOW_THIS_in_this_1537)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:425:9: ( PHRASE )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == PHRASE) :
                        alt34 = 1
                    if alt34 == 1:
                        # SelectScript.g:425:10: PHRASE
                        pass 
                        PHRASE4=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_1540)
                        if self._state.backtracking == 0:
                            p=self._this(PHRASE4.getText()); 





                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return p

    # $ANTLR end "this_"


    # $ANTLR start "list_"
    # SelectScript.g:428:1: list_ returns [l] : ^( LIST (e= expr )* ) ;
    def list_(self, ):

        l = None

        e = None


        l = [] 
        try:
            try:
                # SelectScript.g:429:17: ( ^( LIST (e= expr )* ) )
                # SelectScript.g:430:2: ^( LIST (e= expr )* )
                pass 
                self.match(self.input, LIST, self.FOLLOW_LIST_in_list_1564)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:430:9: (e= expr )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if ((FCT <= LA35_0 <= NEG) or LA35_0 == STMT_SELECT or LA35_0 == AND or (XOR <= LA35_0 <= OR) or LA35_0 == NOT or (IN <= LA35_0 <= POW) or LA35_0 == IF or LA35_0 == THIS or LA35_0 == 108) :
                            alt35 = 1


                        if alt35 == 1:
                            # SelectScript.g:430:11: e= expr
                            pass 
                            self._state.following.append(self.FOLLOW_expr_in_list_1570)
                            e = self.expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                l.append(e); 



                        else:
                            break #loop35

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return l

    # $ANTLR end "list_"


    # $ANTLR start "variable"
    # SelectScript.g:433:1: variable returns [var] : ^( VAR PHRASE (a= age )? ) ;
    def variable(self, ):

        var = None

        PHRASE5 = None
        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:434:27: ( ^( VAR PHRASE (a= age )? ) )
                # SelectScript.g:435:2: ^( VAR PHRASE (a= age )? )
                pass 
                self.match(self.input, VAR, self.FOLLOW_VAR_in_variable1594)

                self.match(self.input, DOWN, None)
                PHRASE5=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable1596)
                # SelectScript.g:435:15: (a= age )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == AGE) :
                    alt36 = 1
                if alt36 == 1:
                    # SelectScript.g:435:16: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable1601)
                    a = self.age()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    var = self._var( PHRASE5.getText(), a ); 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return var

    # $ANTLR end "variable"


    # $ANTLR start "function"
    # SelectScript.g:438:1: function returns [stack] : ^( FCT PHRASE (params= parameter )? ) ;
    def function(self, ):

        stack = None

        PHRASE6 = None
        params = None


        try:
            try:
                # SelectScript.g:438:26: ( ^( FCT PHRASE (params= parameter )? ) )
                # SelectScript.g:439:2: ^( FCT PHRASE (params= parameter )? )
                pass 
                self.match(self.input, FCT, self.FOLLOW_FCT_in_function1621)

                self.match(self.input, DOWN, None)
                PHRASE6=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function1623)
                # SelectScript.g:439:21: (params= parameter )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if ((FCT <= LA37_0 <= NEG) or LA37_0 == STMT_SELECT or LA37_0 == AND or (XOR <= LA37_0 <= OR) or LA37_0 == NOT or (IN <= LA37_0 <= POW) or LA37_0 == IF or LA37_0 == THIS or LA37_0 == 108) :
                    alt37 = 1
                elif (LA37_0 == 3) :
                    LA37_2 = self.input.LA(2)

                    if (self.synpred71_SelectScript()) :
                        alt37 = 1
                if alt37 == 1:
                    # SelectScript.g:0:0: params= parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function1627)
                    params = self.parameter()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    stack = self._fct( PHRASE6.getText(), params) if PHRASE6.getText()!= "eval" else self._eval(params[0]) ; 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "function"


    # $ANTLR start "parameter"
    # SelectScript.g:443:1: parameter returns [stack] : (e= expr )* ;
    def parameter(self, ):

        stack = None

        e = None


        stack = []
        try:
            try:
                # SelectScript.g:444:19: ( (e= expr )* )
                # SelectScript.g:445:2: (e= expr )*
                pass 
                # SelectScript.g:445:2: (e= expr )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if ((FCT <= LA38_0 <= NEG) or LA38_0 == STMT_SELECT or LA38_0 == AND or (XOR <= LA38_0 <= OR) or LA38_0 == NOT or (IN <= LA38_0 <= POW) or LA38_0 == IF or LA38_0 == THIS or LA38_0 == 108) :
                        alt38 = 1


                    if alt38 == 1:
                        # SelectScript.g:445:3: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_parameter1653)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stack.append(e)



                    else:
                        break #loop38




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "parameter"

    # $ANTLR start "synpred2_SelectScript"
    def synpred2_SelectScript_fragment(self, ):
        # SelectScript.g:257:2: (s= statement_select )
        # SelectScript.g:257:2: s= statement_select
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectScript113)
        s = self.statement_select()

        self._state.following.pop()


    # $ANTLR end "synpred2_SelectScript"



    # $ANTLR start "synpred11_SelectScript"
    def synpred11_SelectScript_fragment(self, ):
        # SelectScript.g:273:5: (f= function )
        # SelectScript.g:273:5: f= function
        pass 
        self._state.following.append(self.FOLLOW_function_in_synpred11_SelectScript262)
        f = self.function()

        self._state.following.pop()


    # $ANTLR end "synpred11_SelectScript"



    # $ANTLR start "synpred12_SelectScript"
    def synpred12_SelectScript_fragment(self, ):
        # SelectScript.g:274:5: (t= this_ )
        # SelectScript.g:274:5: t= this_
        pass 
        self._state.following.append(self.FOLLOW_this__in_synpred12_SelectScript273)
        t = self.this_()

        self._state.following.pop()


    # $ANTLR end "synpred12_SelectScript"



    # $ANTLR start "synpred13_SelectScript"
    def synpred13_SelectScript_fragment(self, ):
        # SelectScript.g:275:5: (e= expr )
        # SelectScript.g:275:5: e= expr
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred13_SelectScript286)
        e = self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred13_SelectScript"



    # $ANTLR start "synpred18_SelectScript"
    def synpred18_SelectScript_fragment(self, ):
        # SelectScript.g:290:20: (p= parameter )
        # SelectScript.g:290:20: p= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred18_SelectScript397)
        p = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred18_SelectScript"



    # $ANTLR start "synpred71_SelectScript"
    def synpred71_SelectScript_fragment(self, ):
        # SelectScript.g:439:21: (params= parameter )
        # SelectScript.g:439:21: params= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred71_SelectScript1627)
        params = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred71_SelectScript"




    # Delegated rules

    def synpred11_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred71_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred71_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred13_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred12_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred12_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred2_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred18_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred18_SelectScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\37\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\37\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\4\1\0\35\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\154\1\0\35\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\33\uffff\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\35\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\7\2\1\uffff\1\1\11\uffff\1\2\3\uffff\2\2\1\uffff\1"
        u"\2\1\uffff\16\2\1\uffff\1\2\33\uffff\1\2\41\uffff\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    class DFA2(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA2_1 = input.LA(1)

                 
                index2_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred2_SelectScript()):
                    s = 30

                elif (True):
                    s = 2

                 
                input.seek(index2_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 2, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\42\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\42\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\3\2\uffff\2\0\35\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\154\2\uffff\2\0\35\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\1\uffff\1\5\1\1\2\uffff\1\4\32\uffff\1\2\1\3"
        )

    DFA10_special = DFA.unpack(
        u"\3\uffff\1\0\1\1\35\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\1\1\3\6\5\1\uffff\1\5\11\uffff\1\5\3\uffff\2\5\1"
        u"\uffff\1\5\1\uffff\16\5\1\uffff\1\5\33\uffff\1\4\36\uffff\1\2\2"
        u"\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA10_3 = input.LA(1)

                 
                index10_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred11_SelectScript()):
                    s = 32

                elif (self.synpred13_SelectScript()):
                    s = 5

                 
                input.seek(index10_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA10_4 = input.LA(1)

                 
                index10_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred12_SelectScript()):
                    s = 33

                elif (self.synpred13_SelectScript()):
                    s = 5

                 
                input.seek(index10_4)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 10, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\6\1\2\2\uffff\1\141\5\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\1\112\1\2\2\uffff\1\146\5\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\2\uffff\1\6\1\7\1\uffff\1\1\1\2\1\3\1\4\1\5"
        )

    DFA33_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\1\1\1\3\102\uffff\1\2"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\1\uffff\1\6\1\7\1\10\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass


 

    FOLLOW_prog_in_eval72 = frozenset([1])
    FOLLOW_statement_in_prog94 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_statement_select_in_statement113 = frozenset([1])
    FOLLOW_expr_in_statement123 = frozenset([1])
    FOLLOW_STMT_SELECT_in_statement_select150 = frozenset([2])
    FOLLOW_select__in_statement_select154 = frozenset([59])
    FOLLOW_from__in_statement_select158 = frozenset([3, 62, 63, 67, 73, 76, 77])
    FOLLOW_where__in_statement_select164 = frozenset([3, 63, 67, 73, 76, 77])
    FOLLOW_group__in_statement_select173 = frozenset([3, 63, 69, 73, 76, 77])
    FOLLOW_having__in_statement_select178 = frozenset([3, 63, 73, 76, 77])
    FOLLOW_order__in_statement_select188 = frozenset([3, 73, 76, 77])
    FOLLOW_as__in_statement_select197 = frozenset([3, 76, 77])
    FOLLOW_start__in_statement_select206 = frozenset([76, 77])
    FOLLOW_connect__in_statement_select212 = frozenset([78])
    FOLLOW_stop__in_statement_select216 = frozenset([3])
    FOLLOW_SELECT_in_select_240 = frozenset([2])
    FOLLOW_PHRASE_in_select_250 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 105, 108])
    FOLLOW_function_in_select_262 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 105, 108])
    FOLLOW_this__in_select_273 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 105, 108])
    FOLLOW_expr_in_select_286 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 105, 108])
    FOLLOW_FROM_in_from_318 = frozenset([2])
    FOLLOW_expr_in_from_323 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_AS_in_as_346 = frozenset([2])
    FOLLOW_AS_DICT_in_as_348 = frozenset([3])
    FOLLOW_AS_in_as_360 = frozenset([2])
    FOLLOW_AS_LIST_in_as_362 = frozenset([3])
    FOLLOW_AS_in_as_374 = frozenset([2])
    FOLLOW_AS_VALUE_in_as_376 = frozenset([3])
    FOLLOW_AS_in_as_387 = frozenset([2])
    FOLLOW_PHRASE_in_as_391 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_as_397 = frozenset([3])
    FOLLOW_WHERE_in_where_419 = frozenset([2])
    FOLLOW_expr_in_where_423 = frozenset([3])
    FOLLOW_START_in_start_444 = frozenset([2])
    FOLLOW_expr_in_start_449 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_CONNECT_in_connect_473 = frozenset([2])
    FOLLOW_CYCLE_in_connect_483 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 83, 86, 87, 108])
    FOLLOW_UNIQUE_in_connect_512 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 86, 87, 108])
    FOLLOW_MEMORIZE_in_connect_538 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 87, 99, 108])
    FOLLOW_INTEGER_in_connect_553 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 87, 108])
    FOLLOW_MAXIMUM_in_connect_570 = frozenset([99])
    FOLLOW_INTEGER_in_connect_575 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_connect_595 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_STOP_in_stop_635 = frozenset([2])
    FOLLOW_expr_in_stop_640 = frozenset([3])
    FOLLOW_GROUP_in_group_664 = frozenset([2])
    FOLLOW_PHRASE_in_group_672 = frozenset([3, 4, 105])
    FOLLOW_function_in_group_683 = frozenset([3, 4, 105])
    FOLLOW_HAVING_in_having_708 = frozenset([2])
    FOLLOW_expr_in_having_712 = frozenset([3])
    FOLLOW_ORDER_in_order_734 = frozenset([2])
    FOLLOW_PHRASE_in_order_746 = frozenset([3, 4, 105])
    FOLLOW_function_in_order_758 = frozenset([3, 4, 88, 89, 105])
    FOLLOW_direction__in_order_762 = frozenset([3, 4, 105])
    FOLLOW_ASC_in_direction_792 = frozenset([1])
    FOLLOW_DESC_in_direction_800 = frozenset([1])
    FOLLOW_assign_expr_in_expr824 = frozenset([1])
    FOLLOW_logic_expr_in_expr837 = frozenset([1])
    FOLLOW_compare_expr_in_expr850 = frozenset([1])
    FOLLOW_arithmetic_expr_in_expr862 = frozenset([1])
    FOLLOW_if_statement_in_expr873 = frozenset([1])
    FOLLOW_atom_in_expr887 = frozenset([1])
    FOLLOW_AGE_in_age914 = frozenset([2])
    FOLLOW_expr_in_age919 = frozenset([3])
    FOLLOW_IF_in_if_statement945 = frozenset([2])
    FOLLOW_expr_in_if_statement949 = frozenset([3, 13])
    FOLLOW_THEN_in_if_statement953 = frozenset([2])
    FOLLOW_parameter_in_if_statement957 = frozenset([3, 14])
    FOLLOW_ELSE_in_if_statement961 = frozenset([2])
    FOLLOW_parameter_in_if_statement965 = frozenset([3])
    FOLLOW_ASSIGN_in_assign_expr993 = frozenset([2])
    FOLLOW_PHRASE_in_assign_expr997 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_assign_expr1001 = frozenset([3, 11])
    FOLLOW_age_in_assign_expr1006 = frozenset([3])
    FOLLOW_OR_in_logic_expr1026 = frozenset([2])
    FOLLOW_expr_in_logic_expr1030 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1034 = frozenset([3])
    FOLLOW_XOR_in_logic_expr1043 = frozenset([2])
    FOLLOW_expr_in_logic_expr1047 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1051 = frozenset([3])
    FOLLOW_AND_in_logic_expr1059 = frozenset([2])
    FOLLOW_expr_in_logic_expr1063 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1067 = frozenset([3])
    FOLLOW_NOT_in_logic_expr1075 = frozenset([2])
    FOLLOW_expr_in_logic_expr1079 = frozenset([3])
    FOLLOW_IN_in_compare_expr1097 = frozenset([2])
    FOLLOW_expr_in_compare_expr1101 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1105 = frozenset([3])
    FOLLOW_EQ_in_compare_expr1114 = frozenset([2])
    FOLLOW_expr_in_compare_expr1118 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1122 = frozenset([3])
    FOLLOW_NE_in_compare_expr1131 = frozenset([2])
    FOLLOW_expr_in_compare_expr1135 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1139 = frozenset([3])
    FOLLOW_GE_in_compare_expr1148 = frozenset([2])
    FOLLOW_expr_in_compare_expr1152 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1156 = frozenset([3])
    FOLLOW_GT_in_compare_expr1165 = frozenset([2])
    FOLLOW_expr_in_compare_expr1169 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1173 = frozenset([3])
    FOLLOW_LE_in_compare_expr1182 = frozenset([2])
    FOLLOW_expr_in_compare_expr1186 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1190 = frozenset([3])
    FOLLOW_LT_in_compare_expr1199 = frozenset([2])
    FOLLOW_expr_in_compare_expr1203 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1207 = frozenset([3])
    FOLLOW_MUL_in_arithmetic_expr1224 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1228 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1232 = frozenset([3])
    FOLLOW_DIV_in_arithmetic_expr1240 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1244 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1248 = frozenset([3])
    FOLLOW_MOD_in_arithmetic_expr1256 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1260 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1264 = frozenset([3])
    FOLLOW_SUB_in_arithmetic_expr1272 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1276 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1280 = frozenset([3])
    FOLLOW_ADD_in_arithmetic_expr1288 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1292 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1296 = frozenset([3])
    FOLLOW_POW_in_arithmetic_expr1304 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1308 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1312 = frozenset([3])
    FOLLOW_NEG_in_arithmetic_expr1320 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1324 = frozenset([3])
    FOLLOW_POS_in_arithmetic_expr1333 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1337 = frozenset([3])
    FOLLOW_ELEMENT_in_arithmetic_expr1346 = frozenset([2])
    FOLLOW_atom_in_arithmetic_expr1350 = frozenset([4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_arithmetic_expr1354 = frozenset([3])
    FOLLOW_value_in_atom1375 = frozenset([1])
    FOLLOW_variable_in_atom1388 = frozenset([1])
    FOLLOW_function_in_atom1400 = frozenset([1])
    FOLLOW_108_in_atom1408 = frozenset([4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108, 109])
    FOLLOW_expr_in_atom1412 = frozenset([109])
    FOLLOW_109_in_atom1414 = frozenset([1])
    FOLLOW_statement_select_in_atom1424 = frozenset([1])
    FOLLOW_VAL_in_value1444 = frozenset([2])
    FOLLOW_STRING_in_value1446 = frozenset([3])
    FOLLOW_VAL_in_value1456 = frozenset([2])
    FOLLOW_INTEGER_in_value1458 = frozenset([3])
    FOLLOW_VAL_in_value1468 = frozenset([2])
    FOLLOW_FLOAT_in_value1470 = frozenset([3])
    FOLLOW_VAL_in_value1480 = frozenset([2])
    FOLLOW_TRUE_in_value1482 = frozenset([3])
    FOLLOW_VAL_in_value1492 = frozenset([2])
    FOLLOW_FALSE_in_value1494 = frozenset([3])
    FOLLOW_this__in_value1505 = frozenset([1])
    FOLLOW_list__in_value1515 = frozenset([1])
    FOLLOW_THIS_in_this_1537 = frozenset([2])
    FOLLOW_PHRASE_in_this_1540 = frozenset([3])
    FOLLOW_LIST_in_list_1564 = frozenset([2])
    FOLLOW_expr_in_list_1570 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_VAR_in_variable1594 = frozenset([2])
    FOLLOW_PHRASE_in_variable1596 = frozenset([3, 11])
    FOLLOW_age_in_variable1601 = frozenset([3])
    FOLLOW_FCT_in_function1621 = frozenset([2])
    FOLLOW_PHRASE_in_function1623 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_function1627 = frozenset([3])
    FOLLOW_expr_in_parameter1653 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_statement_select_in_synpred2_SelectScript113 = frozenset([1])
    FOLLOW_function_in_synpred11_SelectScript262 = frozenset([1])
    FOLLOW_this__in_synpred12_SelectScript273 = frozenset([1])
    FOLLOW_expr_in_synpred13_SelectScript286 = frozenset([1])
    FOLLOW_parameter_in_synpred18_SelectScript397 = frozenset([1])
    FOLLOW_parameter_in_synpred71_SelectScript1627 = frozenset([1])



       
def main(argv, otherArg=None):
	expr = ""
	simplify=True
	scene = SelectScript(None, None)
	while True:
		expr += raw_input('>>> ')
		if expr == 'quit':
			break
		elif expr == "simplify":
			simplify = not simplify
			expr = ""
		elif expr[-1] != ";":
			continue
		else:
			code = scene.compile(expr, simplify)
			print code
			scene.prettyPrint(code)
			expr = ""


if __name__ == '__main__':
    main(sys.argv)
