# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectScript.g 2015-06-10 17:47:30

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
                self._state.following.append(self.FOLLOW_prog_in_eval74)
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
                        self._state.following.append(self.FOLLOW_statement_in_prog96)
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
                    self._state.following.append(self.FOLLOW_statement_select_in_statement117)
                    s = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stmt = s



                elif alt2 == 2:
                    # SelectScript.g:258:4: e= expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_statement127)
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
                self.match(self.input, STMT_SELECT, self.FOLLOW_STMT_SELECT_in_statement_select156)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_select__in_statement_select160)
                s = self.select_()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_from__in_statement_select164)
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
                    self._state.following.append(self.FOLLOW_where__in_statement_select170)
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
                    self._state.following.append(self.FOLLOW_group__in_statement_select179)
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
                        self._state.following.append(self.FOLLOW_having__in_statement_select184)
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
                    self._state.following.append(self.FOLLOW_order__in_statement_select194)
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
                    self._state.following.append(self.FOLLOW_as__in_statement_select203)
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
                        self._state.following.append(self.FOLLOW_start__in_statement_select212)
                        rec_start = self.start_()

                        self._state.following.pop()



                    self._state.following.append(self.FOLLOW_connect__in_statement_select218)
                    rec_connect = self.connect_()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_stop__in_statement_select222)
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
    # SelectScript.g:268:1: select_ returns [types] : ^( SELECT (type= PHRASE | f= function | t= this_ )* ) ;
    def select_(self, ):

        types = None

        type = None
        f = None

        t = None


        types = []
        try:
            try:
                # SelectScript.g:269:19: ( ^( SELECT (type= PHRASE | f= function | t= this_ )* ) )
                # SelectScript.g:270:2: ^( SELECT (type= PHRASE | f= function | t= this_ )* )
                pass 
                self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_246)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:271:3: (type= PHRASE | f= function | t= this_ )*
                    while True: #loop10
                        alt10 = 4
                        LA10 = self.input.LA(1)
                        if LA10 == PHRASE:
                            alt10 = 1
                        elif LA10 == FCT:
                            alt10 = 2
                        elif LA10 == THIS:
                            alt10 = 3

                        if alt10 == 1:
                            # SelectScript.g:272:3: type= PHRASE
                            pass 
                            type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_257)
                            if self._state.backtracking == 0:
                                types.append( self._phrase (type.getText()) ); 



                        elif alt10 == 2:
                            # SelectScript.g:273:5: f= function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_select_269)
                            f = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( f ); 



                        elif alt10 == 3:
                            # SelectScript.g:274:5: t= this_
                            pass 
                            self._state.following.append(self.FOLLOW_this__in_select_281)
                            t = self.this_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( t ); 



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
    # SelectScript.g:279:1: from_ returns [env] : ^( FROM (e= expr )+ ) ;
    def from_(self, ):

        env = None

        e = None


        env=[]; 
        try:
            try:
                # SelectScript.g:280:17: ( ^( FROM (e= expr )+ ) )
                # SelectScript.g:281:2: ^( FROM (e= expr )+ )
                pass 
                self.match(self.input, FROM, self.FOLLOW_FROM_in_from_310)

                self.match(self.input, DOWN, None)
                # SelectScript.g:281:9: (e= expr )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((FCT <= LA11_0 <= NEG) or LA11_0 == STMT_SELECT or LA11_0 == AND or (XOR <= LA11_0 <= OR) or LA11_0 == NOT or (IN <= LA11_0 <= POW) or LA11_0 == IF or LA11_0 == THIS or LA11_0 == 108) :
                        alt11 = 1


                    if alt11 == 1:
                        # SelectScript.g:281:10: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_from_315)
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
    # SelectScript.g:284:1: as_ returns [rep] : ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) );
    def as_(self, ):

        rep = None

        v = None
        p = None


        p=[]; 
        try:
            try:
                # SelectScript.g:285:15: ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) )
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
                    # SelectScript.g:286:2: ^( AS AS_DICT )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_339)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_341)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['dict'],  []]; 



                elif alt13 == 2:
                    # SelectScript.g:287:4: ^( AS AS_LIST )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_353)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_355)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['list'],  []]; 



                elif alt13 == 3:
                    # SelectScript.g:288:4: ^( AS AS_VALUE )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_367)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_369)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['value'], []]; 



                elif alt13 == 4:
                    # SelectScript.g:289:4: ^( AS v= PHRASE (p= parameter )? )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_381)

                    self.match(self.input, DOWN, None)
                    v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_385)
                    # SelectScript.g:289:18: (p= parameter )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((FCT <= LA12_0 <= NEG) or LA12_0 == STMT_SELECT or LA12_0 == AND or (XOR <= LA12_0 <= OR) or LA12_0 == NOT or (IN <= LA12_0 <= POW) or LA12_0 == IF or LA12_0 == THIS or LA12_0 == 108) :
                        alt12 = 1
                    elif (LA12_0 == 3) :
                        LA12_2 = self.input.LA(2)

                        if (self.synpred17_SelectScript()) :
                            alt12 = 1
                    if alt12 == 1:
                        # SelectScript.g:289:20: p= parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_as_391)
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
    # SelectScript.g:292:1: where_ returns [stack] : ^( WHERE e= expr ) ;
    def where_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:292:24: ( ^( WHERE e= expr ) )
                # SelectScript.g:293:2: ^( WHERE e= expr )
                pass 
                self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_414)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_where_418)
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
    # SelectScript.g:296:1: start_ returns [with_] : ^( START (e= expr )+ ) ;
    def start_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:297:19: ( ^( START (e= expr )+ ) )
                # SelectScript.g:298:2: ^( START (e= expr )+ )
                pass 
                self.match(self.input, START, self.FOLLOW_START_in_start_440)

                self.match(self.input, DOWN, None)
                # SelectScript.g:298:10: (e= expr )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((FCT <= LA14_0 <= NEG) or LA14_0 == STMT_SELECT or LA14_0 == AND or (XOR <= LA14_0 <= OR) or LA14_0 == NOT or (IN <= LA14_0 <= POW) or LA14_0 == IF or LA14_0 == THIS or LA14_0 == 108) :
                        alt14 = 1


                    if alt14 == 1:
                        # SelectScript.g:298:11: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_start_445)
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
    # SelectScript.g:301:1: connect_ returns [by] : ^( CONNECT ( CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE I1= INTEGER )? ( MAXIMUM I2= INTEGER )? (e= expr )+ ) ;
    def connect_(self, ):

        by = None

        I1 = None
        I2 = None
        e = None


        by = [[],[0,0,0,0,0]]
        try:
            try:
                # SelectScript.g:302:30: ( ^( CONNECT ( CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE I1= INTEGER )? ( MAXIMUM I2= INTEGER )? (e= expr )+ ) )
                # SelectScript.g:303:2: ^( CONNECT ( CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE I1= INTEGER )? ( MAXIMUM I2= INTEGER )? (e= expr )+ )
                pass 
                self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_469)

                self.match(self.input, DOWN, None)
                # SelectScript.g:304:8: ( CYCLE )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == CYCLE) :
                    alt15 = 1
                if alt15 == 1:
                    # SelectScript.g:304:9: CYCLE
                    pass 
                    self.match(self.input, CYCLE, self.FOLLOW_CYCLE_in_connect_479)
                    if self._state.backtracking == 0:
                        by[1][0] = 1;                       




                # SelectScript.g:305:8: ( UNIQUE )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == UNIQUE) :
                    alt16 = 1
                if alt16 == 1:
                    # SelectScript.g:305:9: UNIQUE
                    pass 
                    self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_connect_508)
                    if self._state.backtracking == 0:
                        by[1][1] = 1;                       




                # SelectScript.g:306:8: ( GRAPH )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == GRAPH) :
                    alt17 = 1
                if alt17 == 1:
                    # SelectScript.g:306:9: GRAPH
                    pass 
                    self.match(self.input, GRAPH, self.FOLLOW_GRAPH_in_connect_536)
                    if self._state.backtracking == 0:
                        by[1][4] = 1;                       




                # SelectScript.g:307:8: ( MEMORIZE I1= INTEGER )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MEMORIZE) :
                    alt18 = 1
                if alt18 == 1:
                    # SelectScript.g:307:9: MEMORIZE I1= INTEGER
                    pass 
                    self.match(self.input, MEMORIZE, self.FOLLOW_MEMORIZE_in_connect_565)
                    I1=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_569)
                    if self._state.backtracking == 0:
                        by[1][2] = int(I1.getText()); 




                # SelectScript.g:308:8: ( MAXIMUM I2= INTEGER )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MAXIMUM) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectScript.g:308:9: MAXIMUM I2= INTEGER
                    pass 
                    self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_connect_591)
                    I2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_596)
                    if self._state.backtracking == 0:
                        by[1][3] = int(I2.getText()); 




                # SelectScript.g:309:8: (e= expr )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((FCT <= LA20_0 <= NEG) or LA20_0 == STMT_SELECT or LA20_0 == AND or (XOR <= LA20_0 <= OR) or LA20_0 == NOT or (IN <= LA20_0 <= POW) or LA20_0 == IF or LA20_0 == THIS or LA20_0 == 108) :
                        alt20 = 1


                    if alt20 == 1:
                        # SelectScript.g:309:9: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_connect_619)
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
    # SelectScript.g:313:1: stop_ returns [with_] : ^( STOP (e= expr ) ) ;
    def stop_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:314:19: ( ^( STOP (e= expr ) ) )
                # SelectScript.g:315:2: ^( STOP (e= expr ) )
                pass 
                self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_659)

                self.match(self.input, DOWN, None)
                # SelectScript.g:315:9: (e= expr )
                # SelectScript.g:315:10: e= expr
                pass 
                self._state.following.append(self.FOLLOW_expr_in_stop_664)
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
    # SelectScript.g:318:1: group_ returns [by] : ^( GROUP (type= PHRASE | f= function )+ ) ;
    def group_(self, ):

        by = None

        type = None
        f = None


        by = []
        try:
            try:
                # SelectScript.g:319:16: ( ^( GROUP (type= PHRASE | f= function )+ ) )
                # SelectScript.g:320:2: ^( GROUP (type= PHRASE | f= function )+ )
                pass 
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_688)

                self.match(self.input, DOWN, None)
                # SelectScript.g:321:3: (type= PHRASE | f= function )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 3
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == PHRASE) :
                        alt21 = 1
                    elif (LA21_0 == FCT) :
                        alt21 = 2


                    if alt21 == 1:
                        # SelectScript.g:321:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_697)
                        if self._state.backtracking == 0:
                            by.append( self._phrase ( type.getText() ) ); 



                    elif alt21 == 2:
                        # SelectScript.g:322:5: f= function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_group_708)
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
    # SelectScript.g:327:1: having_ returns [stack] : ^( HAVING e= expr ) ;
    def having_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:327:25: ( ^( HAVING e= expr ) )
                # SelectScript.g:328:2: ^( HAVING e= expr )
                pass 
                self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_733)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_having_737)
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
    # SelectScript.g:331:1: order_ returns [by] : ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) ;
    def order_(self, ):

        by = None

        type = None
        f = None

        dir = None


        by = []
        try:
            try:
                # SelectScript.g:332:16: ( ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) )
                # SelectScript.g:333:2: ^( ORDER (type= PHRASE | f= function dir= direction_ )+ )
                pass 
                self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_760)

                self.match(self.input, DOWN, None)
                # SelectScript.g:334:3: (type= PHRASE | f= function dir= direction_ )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 3
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == PHRASE) :
                        alt22 = 1
                    elif (LA22_0 == FCT) :
                        alt22 = 2


                    if alt22 == 1:
                        # SelectScript.g:335:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_774)
                        if self._state.backtracking == 0:
                            by.append( [ self._phrase ( type.getText()), dir ]); 



                    elif alt22 == 2:
                        # SelectScript.g:336:5: f= function dir= direction_
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_order_786)
                        f = self.function()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_direction__in_order_790)
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
    # SelectScript.g:341:1: direction_ returns [dir] : ( ASC | DESC )? ;
    def direction_(self, ):

        dir = None

        dir = 0
        try:
            try:
                # SelectScript.g:342:16: ( ( ASC | DESC )? )
                # SelectScript.g:343:2: ( ASC | DESC )?
                pass 
                # SelectScript.g:343:2: ( ASC | DESC )?
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == ASC) :
                    alt23 = 1
                elif (LA23_0 == DESC) :
                    alt23 = 2
                if alt23 == 1:
                    # SelectScript.g:343:4: ASC
                    pass 
                    self.match(self.input, ASC, self.FOLLOW_ASC_in_direction_820)
                    if self._state.backtracking == 0:
                        dir=0; 



                elif alt23 == 2:
                    # SelectScript.g:344:4: DESC
                    pass 
                    self.match(self.input, DESC, self.FOLLOW_DESC_in_direction_828)
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
    # SelectScript.g:348:1: expr returns [val] : (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | i= if_statement | a= atom );
    def expr(self, ):

        val = None

        a = None

        l = None

        c = None

        i = None


        try:
            try:
                # SelectScript.g:348:20: (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | i= if_statement | a= atom )
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
                    # SelectScript.g:349:2: a= assign_expr
                    pass 
                    self._state.following.append(self.FOLLOW_assign_expr_in_expr852)
                    a = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt24 == 2:
                    # SelectScript.g:350:4: l= logic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_logic_expr_in_expr866)
                    l = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = l;



                elif alt24 == 3:
                    # SelectScript.g:351:4: c= compare_expr
                    pass 
                    self._state.following.append(self.FOLLOW_compare_expr_in_expr879)
                    c = self.compare_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = c;



                elif alt24 == 4:
                    # SelectScript.g:352:4: a= arithmetic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_arithmetic_expr_in_expr891)
                    a = self.arithmetic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt24 == 5:
                    # SelectScript.g:353:4: i= if_statement
                    pass 
                    self._state.following.append(self.FOLLOW_if_statement_in_expr902)
                    i = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = i;



                elif alt24 == 6:
                    # SelectScript.g:354:4: a= atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_expr916)
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
    # SelectScript.g:357:1: age returns [a] : ^( AGE (t= expr )? ) ;
    def age(self, ):

        a = None

        t = None


        a=self._val(0); 
        try:
            try:
                # SelectScript.g:358:25: ( ^( AGE (t= expr )? ) )
                # SelectScript.g:359:2: ^( AGE (t= expr )? )
                pass 
                self.match(self.input, AGE, self.FOLLOW_AGE_in_age944)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:359:8: (t= expr )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((FCT <= LA25_0 <= NEG) or LA25_0 == STMT_SELECT or LA25_0 == AND or (XOR <= LA25_0 <= OR) or LA25_0 == NOT or (IN <= LA25_0 <= POW) or LA25_0 == IF or LA25_0 == THIS or LA25_0 == 108) :
                        alt25 = 1
                    if alt25 == 1:
                        # SelectScript.g:359:9: t= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_age949)
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
    # SelectScript.g:362:1: if_statement returns [e] : ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? ) ;
    def if_statement(self, ):

        e = None

        if_ = None

        th = None

        el = None


        if_=self._val( True ); th=self._val( True ); el=self._val( False ); 
        try:
            try:
                # SelectScript.g:363:77: ( ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? ) )
                # SelectScript.g:364:5: ^( IF if_= expr ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )? )
                pass 
                self.match(self.input, IF, self.FOLLOW_IF_in_if_statement976)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_if_statement980)
                if_ = self.expr()

                self._state.following.pop()
                # SelectScript.g:364:19: ( ^( THEN th= parameter ( ^( ELSE el= parameter ) )? ) )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == THEN) :
                    alt27 = 1
                if alt27 == 1:
                    # SelectScript.g:364:20: ^( THEN th= parameter ( ^( ELSE el= parameter ) )? )
                    pass 
                    self.match(self.input, THEN, self.FOLLOW_THEN_in_if_statement984)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_parameter_in_if_statement988)
                        th = self.parameter()

                        self._state.following.pop()
                        # SelectScript.g:364:40: ( ^( ELSE el= parameter ) )?
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ELSE) :
                            alt26 = 1
                        if alt26 == 1:
                            # SelectScript.g:364:41: ^( ELSE el= parameter )
                            pass 
                            self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_statement992)

                            if self.input.LA(1) == DOWN:
                                self.match(self.input, DOWN, None)
                                self._state.following.append(self.FOLLOW_parameter_in_if_statement996)
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
    # SelectScript.g:368:1: assign_expr returns [stack] : ^( ASSIGN v= PHRASE e= expr (a= age )? ) ;
    def assign_expr(self, ):

        stack = None

        v = None
        e = None

        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:369:27: ( ^( ASSIGN v= PHRASE e= expr (a= age )? ) )
                # SelectScript.g:370:2: ^( ASSIGN v= PHRASE e= expr (a= age )? )
                pass 
                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr1025)

                self.match(self.input, DOWN, None)
                v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr1029)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr1033)
                e = self.expr()

                self._state.following.pop()
                # SelectScript.g:370:27: (a= age )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == AGE) :
                    alt28 = 1
                if alt28 == 1:
                    # SelectScript.g:370:28: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr1038)
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
    # SelectScript.g:373:1: logic_expr returns [stack] : ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) );
    def logic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:373:28: ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) )
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
                    # SelectScript.g:374:2: ^( OR e1= expr e2= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_logic_expr1059)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1063)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1067)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('or',  [e1, e2]); 



                elif alt29 == 2:
                    # SelectScript.g:375:4: ^( XOR e1= expr e2= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_expr1076)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1080)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1084)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('xor', [e1, e2]); 



                elif alt29 == 3:
                    # SelectScript.g:376:4: ^( AND e1= expr e2= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_logic_expr1093)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1097)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1101)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('and', [e1, e2]); 



                elif alt29 == 4:
                    # SelectScript.g:377:4: ^( NOT e= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_expr1109)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr1113)
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
    # SelectScript.g:380:1: compare_expr returns [stack] : ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) );
    def compare_expr(self, ):

        stack = None

        e1 = None

        e2 = None


        try:
            try:
                # SelectScript.g:380:29: ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) )
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
                    # SelectScript.g:381:2: ^( IN e1= expr e2= expr )
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_compare_expr1132)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1136)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1140)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('in', [e2, e1]); 



                elif alt30 == 2:
                    # SelectScript.g:382:4: ^( EQ e1= expr e2= expr )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_expr1149)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1153)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1157)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('eq', [e1, e2]); 



                elif alt30 == 3:
                    # SelectScript.g:383:4: ^( NE e1= expr e2= expr )
                    pass 
                    self.match(self.input, NE, self.FOLLOW_NE_in_compare_expr1166)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1170)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1174)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ne', [e1, e2]); 



                elif alt30 == 4:
                    # SelectScript.g:384:4: ^( GE e1= expr e2= expr )
                    pass 
                    self.match(self.input, GE, self.FOLLOW_GE_in_compare_expr1183)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1187)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1191)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ge', [e1, e2]); 



                elif alt30 == 5:
                    # SelectScript.g:385:4: ^( GT e1= expr e2= expr )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_compare_expr1200)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1204)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1208)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('gt', [e1, e2]); 



                elif alt30 == 6:
                    # SelectScript.g:386:4: ^( LE e1= expr e2= expr )
                    pass 
                    self.match(self.input, LE, self.FOLLOW_LE_in_compare_expr1217)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1221)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1225)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('le', [e1, e2]); 



                elif alt30 == 7:
                    # SelectScript.g:387:4: ^( LT e1= expr e2= expr )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_compare_expr1234)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1238)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1242)
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
    # SelectScript.g:390:1: arithmetic_expr returns [stack] : ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) | ^( ELEMENT a= atom p= parameter ) );
    def arithmetic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None

        a = None

        p = None


        try:
            try:
                # SelectScript.g:390:32: ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) | ^( ELEMENT a= atom p= parameter ) )
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
                    # SelectScript.g:391:2: ^( MUL e1= expr e2= expr )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_expr1260)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1264)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1268)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mul', [e1, e2]); 



                elif alt31 == 2:
                    # SelectScript.g:392:3: ^( DIV e1= expr e2= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_expr1276)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1280)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1284)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('div', [e1, e2]); 



                elif alt31 == 3:
                    # SelectScript.g:393:3: ^( MOD e1= expr e2= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_expr1292)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1296)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1300)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mod', [e1, e2]); 



                elif alt31 == 4:
                    # SelectScript.g:394:3: ^( SUB e1= expr e2= expr )
                    pass 
                    self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_expr1308)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1312)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1316)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('sub', [e1, e2]); 



                elif alt31 == 5:
                    # SelectScript.g:395:3: ^( ADD e1= expr e2= expr )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_expr1324)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1328)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1332)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('add', [e1, e2]); 



                elif alt31 == 6:
                    # SelectScript.g:396:3: ^( POW e1= expr e2= expr )
                    pass 
                    self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_expr1340)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1344)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1348)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pow', [e1, e2]); 



                elif alt31 == 7:
                    # SelectScript.g:397:3: ^( NEG e= expr )
                    pass 
                    self.match(self.input, NEG, self.FOLLOW_NEG_in_arithmetic_expr1356)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1360)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('neg', [e]); 



                elif alt31 == 8:
                    # SelectScript.g:398:3: ^( POS e= expr )
                    pass 
                    self.match(self.input, POS, self.FOLLOW_POS_in_arithmetic_expr1369)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1373)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pos', [e]); 



                elif alt31 == 9:
                    # SelectScript.g:399:3: ^( ELEMENT a= atom p= parameter )
                    pass 
                    self.match(self.input, ELEMENT, self.FOLLOW_ELEMENT_in_arithmetic_expr1382)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_expr1386)
                    a = self.atom()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_parameter_in_arithmetic_expr1390)
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
    # SelectScript.g:402:1: atom returns [stack] : (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select );
    def atom(self, ):

        stack = None

        val = None

        var = None

        fct = None

        e = None

        s = None


        try:
            try:
                # SelectScript.g:402:22: (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select )
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
                    # SelectScript.g:403:2: val= value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_atom1411)
                    val = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = val



                elif alt32 == 2:
                    # SelectScript.g:404:4: var= variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_atom1424)
                    var = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = var



                elif alt32 == 3:
                    # SelectScript.g:405:4: fct= function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_atom1436)
                    fct = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = fct



                elif alt32 == 4:
                    # SelectScript.g:406:4: '(' e= expr ')'
                    pass 
                    self.match(self.input, 108, self.FOLLOW_108_in_atom1444)
                    self._state.following.append(self.FOLLOW_expr_in_atom1448)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 109, self.FOLLOW_109_in_atom1450)
                    if self._state.backtracking == 0:
                        stack = e  



                elif alt32 == 5:
                    # SelectScript.g:407:4: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_atom1460)
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
    # SelectScript.g:410:1: value returns [val] : ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ );
    def value(self, ):

        val = None

        STRING1 = None
        INTEGER2 = None
        FLOAT3 = None
        t = None

        l = None


        try:
            try:
                # SelectScript.g:410:21: ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ )
                alt33 = 7
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # SelectScript.g:411:4: ^( VAL STRING )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1480)

                    self.match(self.input, DOWN, None)
                    STRING1=self.match(self.input, STRING, self.FOLLOW_STRING_in_value1482)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( STRING1.getText()[1:-1] ); 



                elif alt33 == 2:
                    # SelectScript.g:412:4: ^( VAL INTEGER )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1492)

                    self.match(self.input, DOWN, None)
                    INTEGER2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value1494)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( int(INTEGER2.getText()) ); 



                elif alt33 == 3:
                    # SelectScript.g:413:4: ^( VAL FLOAT )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1504)

                    self.match(self.input, DOWN, None)
                    FLOAT3=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value1506)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( float(FLOAT3.getText()) ); 



                elif alt33 == 4:
                    # SelectScript.g:414:4: ^( VAL TRUE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1516)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value1518)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( True  ); 



                elif alt33 == 5:
                    # SelectScript.g:415:4: ^( VAL FALSE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1528)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value1530)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( False ); 



                elif alt33 == 6:
                    # SelectScript.g:416:4: t= this_
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_value1541)
                    t = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val= t; 



                elif alt33 == 7:
                    # SelectScript.g:417:4: l= list_
                    pass 
                    self._state.following.append(self.FOLLOW_list__in_value1551)
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
    # SelectScript.g:420:1: this_ returns [p] : ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        p = None

        PHRASE4 = None

        p=self._this(); 
        try:
            try:
                # SelectScript.g:421:26: ( ^( THIS ( PHRASE )? ) )
                # SelectScript.g:422:2: ^( THIS ( PHRASE )? )
                pass 
                self.match(self.input, THIS, self.FOLLOW_THIS_in_this_1573)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:422:9: ( PHRASE )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == PHRASE) :
                        alt34 = 1
                    if alt34 == 1:
                        # SelectScript.g:422:10: PHRASE
                        pass 
                        PHRASE4=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_1576)
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
    # SelectScript.g:425:1: list_ returns [l] : ^( LIST (e= expr )* ) ;
    def list_(self, ):

        l = None

        e = None


        l = [] 
        try:
            try:
                # SelectScript.g:426:17: ( ^( LIST (e= expr )* ) )
                # SelectScript.g:427:2: ^( LIST (e= expr )* )
                pass 
                self.match(self.input, LIST, self.FOLLOW_LIST_in_list_1600)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:427:9: (e= expr )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if ((FCT <= LA35_0 <= NEG) or LA35_0 == STMT_SELECT or LA35_0 == AND or (XOR <= LA35_0 <= OR) or LA35_0 == NOT or (IN <= LA35_0 <= POW) or LA35_0 == IF or LA35_0 == THIS or LA35_0 == 108) :
                            alt35 = 1


                        if alt35 == 1:
                            # SelectScript.g:427:11: e= expr
                            pass 
                            self._state.following.append(self.FOLLOW_expr_in_list_1606)
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
    # SelectScript.g:430:1: variable returns [var] : ^( VAR PHRASE (a= age )? ) ;
    def variable(self, ):

        var = None

        PHRASE5 = None
        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:431:27: ( ^( VAR PHRASE (a= age )? ) )
                # SelectScript.g:432:2: ^( VAR PHRASE (a= age )? )
                pass 
                self.match(self.input, VAR, self.FOLLOW_VAR_in_variable1630)

                self.match(self.input, DOWN, None)
                PHRASE5=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable1632)
                # SelectScript.g:432:15: (a= age )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == AGE) :
                    alt36 = 1
                if alt36 == 1:
                    # SelectScript.g:432:16: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable1637)
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
    # SelectScript.g:435:1: function returns [stack] : ^( FCT PHRASE (params= parameter )? ) ;
    def function(self, ):

        stack = None

        PHRASE6 = None
        params = None


        try:
            try:
                # SelectScript.g:435:26: ( ^( FCT PHRASE (params= parameter )? ) )
                # SelectScript.g:436:2: ^( FCT PHRASE (params= parameter )? )
                pass 
                self.match(self.input, FCT, self.FOLLOW_FCT_in_function1657)

                self.match(self.input, DOWN, None)
                PHRASE6=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function1659)
                # SelectScript.g:436:21: (params= parameter )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if ((FCT <= LA37_0 <= NEG) or LA37_0 == STMT_SELECT or LA37_0 == AND or (XOR <= LA37_0 <= OR) or LA37_0 == NOT or (IN <= LA37_0 <= POW) or LA37_0 == IF or LA37_0 == THIS or LA37_0 == 108) :
                    alt37 = 1
                elif (LA37_0 == 3) :
                    LA37_2 = self.input.LA(2)

                    if (self.synpred70_SelectScript()) :
                        alt37 = 1
                if alt37 == 1:
                    # SelectScript.g:0:0: params= parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function1663)
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
    # SelectScript.g:440:1: parameter returns [stack] : (e= expr )* ;
    def parameter(self, ):

        stack = None

        e = None


        stack = []
        try:
            try:
                # SelectScript.g:441:19: ( (e= expr )* )
                # SelectScript.g:442:2: (e= expr )*
                pass 
                # SelectScript.g:442:2: (e= expr )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if ((FCT <= LA38_0 <= NEG) or LA38_0 == STMT_SELECT or LA38_0 == AND or (XOR <= LA38_0 <= OR) or LA38_0 == NOT or (IN <= LA38_0 <= POW) or LA38_0 == IF or LA38_0 == THIS or LA38_0 == 108) :
                        alt38 = 1


                    if alt38 == 1:
                        # SelectScript.g:442:3: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_parameter1689)
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
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectScript117)
        s = self.statement_select()

        self._state.following.pop()


    # $ANTLR end "synpred2_SelectScript"



    # $ANTLR start "synpred17_SelectScript"
    def synpred17_SelectScript_fragment(self, ):
        # SelectScript.g:289:20: (p= parameter )
        # SelectScript.g:289:20: p= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred17_SelectScript391)
        p = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectScript"



    # $ANTLR start "synpred70_SelectScript"
    def synpred70_SelectScript_fragment(self, ):
        # SelectScript.g:436:21: (params= parameter )
        # SelectScript.g:436:21: params= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred70_SelectScript1663)
        params = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred70_SelectScript"




    # Delegated rules

    def synpred70_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred70_SelectScript_fragment()
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

    def synpred17_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_SelectScript_fragment()
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


 

    FOLLOW_prog_in_eval74 = frozenset([1])
    FOLLOW_statement_in_prog96 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_statement_select_in_statement117 = frozenset([1])
    FOLLOW_expr_in_statement127 = frozenset([1])
    FOLLOW_STMT_SELECT_in_statement_select156 = frozenset([2])
    FOLLOW_select__in_statement_select160 = frozenset([59])
    FOLLOW_from__in_statement_select164 = frozenset([3, 62, 63, 67, 73, 76, 77])
    FOLLOW_where__in_statement_select170 = frozenset([3, 63, 67, 73, 76, 77])
    FOLLOW_group__in_statement_select179 = frozenset([3, 63, 69, 73, 76, 77])
    FOLLOW_having__in_statement_select184 = frozenset([3, 63, 73, 76, 77])
    FOLLOW_order__in_statement_select194 = frozenset([3, 73, 76, 77])
    FOLLOW_as__in_statement_select203 = frozenset([3, 76, 77])
    FOLLOW_start__in_statement_select212 = frozenset([76, 77])
    FOLLOW_connect__in_statement_select218 = frozenset([78])
    FOLLOW_stop__in_statement_select222 = frozenset([3])
    FOLLOW_SELECT_in_select_246 = frozenset([2])
    FOLLOW_PHRASE_in_select_257 = frozenset([3, 4, 74, 105])
    FOLLOW_function_in_select_269 = frozenset([3, 4, 74, 105])
    FOLLOW_this__in_select_281 = frozenset([3, 4, 74, 105])
    FOLLOW_FROM_in_from_310 = frozenset([2])
    FOLLOW_expr_in_from_315 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_AS_in_as_339 = frozenset([2])
    FOLLOW_AS_DICT_in_as_341 = frozenset([3])
    FOLLOW_AS_in_as_353 = frozenset([2])
    FOLLOW_AS_LIST_in_as_355 = frozenset([3])
    FOLLOW_AS_in_as_367 = frozenset([2])
    FOLLOW_AS_VALUE_in_as_369 = frozenset([3])
    FOLLOW_AS_in_as_381 = frozenset([2])
    FOLLOW_PHRASE_in_as_385 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_as_391 = frozenset([3])
    FOLLOW_WHERE_in_where_414 = frozenset([2])
    FOLLOW_expr_in_where_418 = frozenset([3])
    FOLLOW_START_in_start_440 = frozenset([2])
    FOLLOW_expr_in_start_445 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_CONNECT_in_connect_469 = frozenset([2])
    FOLLOW_CYCLE_in_connect_479 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 83, 84, 86, 87, 108])
    FOLLOW_UNIQUE_in_connect_508 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 84, 86, 87, 108])
    FOLLOW_GRAPH_in_connect_536 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 86, 87, 108])
    FOLLOW_MEMORIZE_in_connect_565 = frozenset([99])
    FOLLOW_INTEGER_in_connect_569 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 87, 108])
    FOLLOW_MAXIMUM_in_connect_591 = frozenset([99])
    FOLLOW_INTEGER_in_connect_596 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_connect_619 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_STOP_in_stop_659 = frozenset([2])
    FOLLOW_expr_in_stop_664 = frozenset([3])
    FOLLOW_GROUP_in_group_688 = frozenset([2])
    FOLLOW_PHRASE_in_group_697 = frozenset([3, 4, 105])
    FOLLOW_function_in_group_708 = frozenset([3, 4, 105])
    FOLLOW_HAVING_in_having_733 = frozenset([2])
    FOLLOW_expr_in_having_737 = frozenset([3])
    FOLLOW_ORDER_in_order_760 = frozenset([2])
    FOLLOW_PHRASE_in_order_774 = frozenset([3, 4, 105])
    FOLLOW_function_in_order_786 = frozenset([3, 4, 88, 89, 105])
    FOLLOW_direction__in_order_790 = frozenset([3, 4, 105])
    FOLLOW_ASC_in_direction_820 = frozenset([1])
    FOLLOW_DESC_in_direction_828 = frozenset([1])
    FOLLOW_assign_expr_in_expr852 = frozenset([1])
    FOLLOW_logic_expr_in_expr866 = frozenset([1])
    FOLLOW_compare_expr_in_expr879 = frozenset([1])
    FOLLOW_arithmetic_expr_in_expr891 = frozenset([1])
    FOLLOW_if_statement_in_expr902 = frozenset([1])
    FOLLOW_atom_in_expr916 = frozenset([1])
    FOLLOW_AGE_in_age944 = frozenset([2])
    FOLLOW_expr_in_age949 = frozenset([3])
    FOLLOW_IF_in_if_statement976 = frozenset([2])
    FOLLOW_expr_in_if_statement980 = frozenset([3, 13])
    FOLLOW_THEN_in_if_statement984 = frozenset([2])
    FOLLOW_parameter_in_if_statement988 = frozenset([3, 14])
    FOLLOW_ELSE_in_if_statement992 = frozenset([2])
    FOLLOW_parameter_in_if_statement996 = frozenset([3])
    FOLLOW_ASSIGN_in_assign_expr1025 = frozenset([2])
    FOLLOW_PHRASE_in_assign_expr1029 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_assign_expr1033 = frozenset([3, 11])
    FOLLOW_age_in_assign_expr1038 = frozenset([3])
    FOLLOW_OR_in_logic_expr1059 = frozenset([2])
    FOLLOW_expr_in_logic_expr1063 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1067 = frozenset([3])
    FOLLOW_XOR_in_logic_expr1076 = frozenset([2])
    FOLLOW_expr_in_logic_expr1080 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1084 = frozenset([3])
    FOLLOW_AND_in_logic_expr1093 = frozenset([2])
    FOLLOW_expr_in_logic_expr1097 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_logic_expr1101 = frozenset([3])
    FOLLOW_NOT_in_logic_expr1109 = frozenset([2])
    FOLLOW_expr_in_logic_expr1113 = frozenset([3])
    FOLLOW_IN_in_compare_expr1132 = frozenset([2])
    FOLLOW_expr_in_compare_expr1136 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1140 = frozenset([3])
    FOLLOW_EQ_in_compare_expr1149 = frozenset([2])
    FOLLOW_expr_in_compare_expr1153 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1157 = frozenset([3])
    FOLLOW_NE_in_compare_expr1166 = frozenset([2])
    FOLLOW_expr_in_compare_expr1170 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1174 = frozenset([3])
    FOLLOW_GE_in_compare_expr1183 = frozenset([2])
    FOLLOW_expr_in_compare_expr1187 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1191 = frozenset([3])
    FOLLOW_GT_in_compare_expr1200 = frozenset([2])
    FOLLOW_expr_in_compare_expr1204 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1208 = frozenset([3])
    FOLLOW_LE_in_compare_expr1217 = frozenset([2])
    FOLLOW_expr_in_compare_expr1221 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1225 = frozenset([3])
    FOLLOW_LT_in_compare_expr1234 = frozenset([2])
    FOLLOW_expr_in_compare_expr1238 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_compare_expr1242 = frozenset([3])
    FOLLOW_MUL_in_arithmetic_expr1260 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1264 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1268 = frozenset([3])
    FOLLOW_DIV_in_arithmetic_expr1276 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1280 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1284 = frozenset([3])
    FOLLOW_MOD_in_arithmetic_expr1292 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1296 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1300 = frozenset([3])
    FOLLOW_SUB_in_arithmetic_expr1308 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1312 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1316 = frozenset([3])
    FOLLOW_ADD_in_arithmetic_expr1324 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1328 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1332 = frozenset([3])
    FOLLOW_POW_in_arithmetic_expr1340 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1344 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_expr_in_arithmetic_expr1348 = frozenset([3])
    FOLLOW_NEG_in_arithmetic_expr1356 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1360 = frozenset([3])
    FOLLOW_POS_in_arithmetic_expr1369 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1373 = frozenset([3])
    FOLLOW_ELEMENT_in_arithmetic_expr1382 = frozenset([2])
    FOLLOW_atom_in_arithmetic_expr1386 = frozenset([4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_arithmetic_expr1390 = frozenset([3])
    FOLLOW_value_in_atom1411 = frozenset([1])
    FOLLOW_variable_in_atom1424 = frozenset([1])
    FOLLOW_function_in_atom1436 = frozenset([1])
    FOLLOW_108_in_atom1444 = frozenset([4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108, 109])
    FOLLOW_expr_in_atom1448 = frozenset([109])
    FOLLOW_109_in_atom1450 = frozenset([1])
    FOLLOW_statement_select_in_atom1460 = frozenset([1])
    FOLLOW_VAL_in_value1480 = frozenset([2])
    FOLLOW_STRING_in_value1482 = frozenset([3])
    FOLLOW_VAL_in_value1492 = frozenset([2])
    FOLLOW_INTEGER_in_value1494 = frozenset([3])
    FOLLOW_VAL_in_value1504 = frozenset([2])
    FOLLOW_FLOAT_in_value1506 = frozenset([3])
    FOLLOW_VAL_in_value1516 = frozenset([2])
    FOLLOW_TRUE_in_value1518 = frozenset([3])
    FOLLOW_VAL_in_value1528 = frozenset([2])
    FOLLOW_FALSE_in_value1530 = frozenset([3])
    FOLLOW_this__in_value1541 = frozenset([1])
    FOLLOW_list__in_value1551 = frozenset([1])
    FOLLOW_THIS_in_this_1573 = frozenset([2])
    FOLLOW_PHRASE_in_this_1576 = frozenset([3])
    FOLLOW_LIST_in_list_1600 = frozenset([2])
    FOLLOW_expr_in_list_1606 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_VAR_in_variable1630 = frozenset([2])
    FOLLOW_PHRASE_in_variable1632 = frozenset([3, 11])
    FOLLOW_age_in_variable1637 = frozenset([3])
    FOLLOW_FCT_in_function1657 = frozenset([2])
    FOLLOW_PHRASE_in_function1659 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_parameter_in_function1663 = frozenset([3])
    FOLLOW_expr_in_parameter1689 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 12, 22, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 74, 108])
    FOLLOW_statement_select_in_synpred2_SelectScript117 = frozenset([1])
    FOLLOW_parameter_in_synpred17_SelectScript391 = frozenset([1])
    FOLLOW_parameter_in_synpred70_SelectScript1663 = frozenset([1])



       
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
