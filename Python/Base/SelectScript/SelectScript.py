# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectScript.g 2014-11-19 16:00:43

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
LIST_BEGIN=44
PHRASE=93
SUB=37
IN=28
STOP=74
DOT=12
WHERE=58
AS=69
LINE_COMMENT=84
POS=8
FCT=4
POW=41
XOR=23
SEP=13
A=16
B=66
C=51
D=18
E=49
F=53
G=60
H=57
I=27
CONNECT=72
J=95
K=96
ASSIGN=29
L=50
M=54
N=17
COMMENT=83
O=21
P=62
ORDER=59
GROUP=63
ASC=76
Q=94
R=22
S=48
T=25
U=61
V=64
W=56
BY=68
X=20
Y=67
CHARACTER=91
Z=97
SQ=42
SELECT=52
DIV=39
NEG=9
LIST_END=45
LE=32
STRING=85
ADD=36
LT=34
FROM=55
DQ=43
SPECIAL=92
DESC=77
T__99=99
T__98=98
INTEGER=87
MUL=38
NEWLINE=81
TRUE=89
EQ=30
NOT=26
AND=19
NE=31
THIS=70
END=14
HAVING=65
LIST=7
FLOAT=88
AS_VALUE=79
AGE_END=47
AS_DICT=80
WS=82
EOF=-1
GE=33
AGE=10
OR=24
MOD=40
AGE_BEGIN=46
STMT_SELECT=11
COLON=15
TIME=71
GT=35
DIGIT=86
WITH=75
START=73
FALSE=90
AS_LIST=78

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FCT", "VAR", "VAL", "LIST", "POS", "NEG", "AGE", "STMT_SELECT", "DOT", 
    "SEP", "END", "COLON", "A", "N", "D", "AND", "X", "O", "R", "XOR", "OR", 
    "T", "NOT", "I", "IN", "ASSIGN", "EQ", "NE", "LE", "GE", "LT", "GT", 
    "ADD", "SUB", "MUL", "DIV", "MOD", "POW", "SQ", "DQ", "LIST_BEGIN", 
    "LIST_END", "AGE_BEGIN", "AGE_END", "S", "E", "L", "C", "SELECT", "F", 
    "M", "FROM", "W", "H", "WHERE", "ORDER", "G", "U", "P", "GROUP", "V", 
    "HAVING", "B", "Y", "BY", "AS", "THIS", "TIME", "CONNECT", "START", 
    "STOP", "WITH", "ASC", "DESC", "AS_LIST", "AS_VALUE", "AS_DICT", "NEWLINE", 
    "WS", "COMMENT", "LINE_COMMENT", "STRING", "DIGIT", "INTEGER", "FLOAT", 
    "TRUE", "FALSE", "CHARACTER", "SPECIAL", "PHRASE", "Q", "J", "K", "Z", 
    "'('", "')'"
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

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
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

    types = {'fct' :0, 'var' :1,
             'list':2, 'val' :3,
             'sel' :4, 'this':5,
             'phrase':6, 'eval': 7 }
             
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
    # SelectScript.g:238:1: eval returns [stmt_list] : p= prog ;
    def eval(self, ):

        stmt_list = None

        p = None


        try:
            try:
                # SelectScript.g:238:25: (p= prog )
                # SelectScript.g:239:5: p= prog
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
    # SelectScript.g:242:1: prog returns [stmt_list] : (stmt= statement )+ ;
    def prog(self, ):

        stmt_list = None

        stmt = None


        stmt_list = []
        try:
            try:
                # SelectScript.g:243:22: ( (stmt= statement )+ )
                # SelectScript.g:244:2: (stmt= statement )+
                pass 
                # SelectScript.g:244:2: (stmt= statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((FCT <= LA1_0 <= NEG) or LA1_0 == STMT_SELECT or LA1_0 == AND or (XOR <= LA1_0 <= OR) or LA1_0 == NOT or (IN <= LA1_0 <= POW) or LA1_0 == THIS or LA1_0 == 98) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectScript.g:244:3: stmt= statement
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
    # SelectScript.g:247:1: statement returns [stmt] : (s= statement_select | e= expr );
    def statement(self, ):

        stmt = None

        s = None

        e = None


        try:
            try:
                # SelectScript.g:247:25: (s= statement_select | e= expr )
                alt2 = 2
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectScript.g:248:2: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_statement117)
                    s = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stmt = s



                elif alt2 == 2:
                    # SelectScript.g:249:4: e= expr
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
    # SelectScript.g:252:1: statement_select returns [selection] : ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? ) ;
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


        s=[]; f=[]; w=[]; g=[]; h=[]; o=[]; a=[self.asTypes['dict'],[]]; rec_start=[]; rec_connect=[]; rec_stop=[]; 
        try:
            try:
                # SelectScript.g:255:1: ( ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? ) )
                # SelectScript.g:256:2: ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )? )
                pass 
                self.match(self.input, STMT_SELECT, self.FOLLOW_STMT_SELECT_in_statement_select156)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_select__in_statement_select160)
                s = self.select_()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_from__in_statement_select164)
                f = self.from_()

                self._state.following.pop()
                # SelectScript.g:256:34: (w= where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    alt3 = 1
                if alt3 == 1:
                    # SelectScript.g:256:36: w= where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select170)
                    w = self.where_()

                    self._state.following.pop()



                # SelectScript.g:256:48: (g= group_ (h= having_ )? )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == GROUP) :
                    alt5 = 1
                if alt5 == 1:
                    # SelectScript.g:256:50: g= group_ (h= having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select179)
                    g = self.group_()

                    self._state.following.pop()
                    # SelectScript.g:256:59: (h= having_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == HAVING) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectScript.g:256:60: h= having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select184)
                        h = self.having_()

                        self._state.following.pop()






                # SelectScript.g:256:74: (o= order_ )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ORDER) :
                    alt6 = 1
                if alt6 == 1:
                    # SelectScript.g:256:76: o= order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select194)
                    o = self.order_()

                    self._state.following.pop()



                # SelectScript.g:256:88: (a= as_ )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == AS) :
                    alt7 = 1
                if alt7 == 1:
                    # SelectScript.g:256:90: a= as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select203)
                    a = self.as_()

                    self._state.following.pop()



                # SelectScript.g:256:99: ( (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_ )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((CONNECT <= LA9_0 <= START)) :
                    alt9 = 1
                if alt9 == 1:
                    # SelectScript.g:256:100: (rec_start= start_ )? rec_connect= connect_ rec_stop= stop_
                    pass 
                    # SelectScript.g:256:100: (rec_start= start_ )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == START) :
                        alt8 = 1
                    if alt8 == 1:
                        # SelectScript.g:256:101: rec_start= start_
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
                    selection = self._sel(s, f, w, g, h, o, a, [rec_start, rec_connect, rec_stop]); 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return selection

    # $ANTLR end "statement_select"


    # $ANTLR start "select_"
    # SelectScript.g:259:1: select_ returns [types] : ^( SELECT (type= PHRASE | f= function | t= this_ )* ) ;
    def select_(self, ):

        types = None

        type = None
        f = None

        t = None


        types = []
        try:
            try:
                # SelectScript.g:260:19: ( ^( SELECT (type= PHRASE | f= function | t= this_ )* ) )
                # SelectScript.g:261:2: ^( SELECT (type= PHRASE | f= function | t= this_ )* )
                pass 
                self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_246)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:262:3: (type= PHRASE | f= function | t= this_ )*
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
                            # SelectScript.g:263:3: type= PHRASE
                            pass 
                            type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_257)
                            if self._state.backtracking == 0:
                                types.append( self._phrase (type.getText()) ); 



                        elif alt10 == 2:
                            # SelectScript.g:264:5: f= function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_select_269)
                            f = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( f ); 



                        elif alt10 == 3:
                            # SelectScript.g:265:5: t= this_
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
    # SelectScript.g:270:1: from_ returns [env] : ^( FROM (e= expr )+ ) ;
    def from_(self, ):

        env = None

        e = None


        env=[]; 
        try:
            try:
                # SelectScript.g:271:17: ( ^( FROM (e= expr )+ ) )
                # SelectScript.g:272:2: ^( FROM (e= expr )+ )
                pass 
                self.match(self.input, FROM, self.FOLLOW_FROM_in_from_310)

                self.match(self.input, DOWN, None)
                # SelectScript.g:272:9: (e= expr )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((FCT <= LA11_0 <= NEG) or LA11_0 == STMT_SELECT or LA11_0 == AND or (XOR <= LA11_0 <= OR) or LA11_0 == NOT or (IN <= LA11_0 <= POW) or LA11_0 == THIS or LA11_0 == 98) :
                        alt11 = 1


                    if alt11 == 1:
                        # SelectScript.g:272:10: e= expr
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
    # SelectScript.g:275:1: as_ returns [rep] : ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) );
    def as_(self, ):

        rep = None

        v = None
        p = None


        p=[]; 
        try:
            try:
                # SelectScript.g:276:15: ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) )
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
                    # SelectScript.g:277:2: ^( AS AS_DICT )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_339)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_341)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['dict'],  []]; 



                elif alt13 == 2:
                    # SelectScript.g:278:4: ^( AS AS_LIST )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_353)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_355)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['list'],  []]; 



                elif alt13 == 3:
                    # SelectScript.g:279:4: ^( AS AS_VALUE )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_367)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_369)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['value'], []]; 



                elif alt13 == 4:
                    # SelectScript.g:280:4: ^( AS v= PHRASE (p= parameter )? )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_381)

                    self.match(self.input, DOWN, None)
                    v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_385)
                    # SelectScript.g:280:18: (p= parameter )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((FCT <= LA12_0 <= NEG) or LA12_0 == STMT_SELECT or LA12_0 == AND or (XOR <= LA12_0 <= OR) or LA12_0 == NOT or (IN <= LA12_0 <= POW) or LA12_0 == THIS or LA12_0 == 98) :
                        alt12 = 1
                    elif (LA12_0 == 3) :
                        LA12_2 = self.input.LA(2)

                        if (self.synpred17_SelectScript()) :
                            alt12 = 1
                    if alt12 == 1:
                        # SelectScript.g:280:20: p= parameter
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
    # SelectScript.g:283:1: where_ returns [stack] : ^( WHERE e= expr ) ;
    def where_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:283:24: ( ^( WHERE e= expr ) )
                # SelectScript.g:284:2: ^( WHERE e= expr )
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
    # SelectScript.g:287:1: start_ returns [with_] : ^( START (e= expr )+ ) ;
    def start_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:288:19: ( ^( START (e= expr )+ ) )
                # SelectScript.g:289:2: ^( START (e= expr )+ )
                pass 
                self.match(self.input, START, self.FOLLOW_START_in_start_440)

                self.match(self.input, DOWN, None)
                # SelectScript.g:289:10: (e= expr )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((FCT <= LA14_0 <= NEG) or LA14_0 == STMT_SELECT or LA14_0 == AND or (XOR <= LA14_0 <= OR) or LA14_0 == NOT or (IN <= LA14_0 <= POW) or LA14_0 == THIS or LA14_0 == 98) :
                        alt14 = 1


                    if alt14 == 1:
                        # SelectScript.g:289:11: e= expr
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
    # SelectScript.g:292:1: connect_ returns [by] : ^( CONNECT (e= expr )+ ) ;
    def connect_(self, ):

        by = None

        e = None


        by = []
        try:
            try:
                # SelectScript.g:293:16: ( ^( CONNECT (e= expr )+ ) )
                # SelectScript.g:294:2: ^( CONNECT (e= expr )+ )
                pass 
                self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_469)

                self.match(self.input, DOWN, None)
                # SelectScript.g:294:12: (e= expr )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((FCT <= LA15_0 <= NEG) or LA15_0 == STMT_SELECT or LA15_0 == AND or (XOR <= LA15_0 <= OR) or LA15_0 == NOT or (IN <= LA15_0 <= POW) or LA15_0 == THIS or LA15_0 == 98) :
                        alt15 = 1


                    if alt15 == 1:
                        # SelectScript.g:294:13: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_connect_474)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append(e); 



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "connect_"


    # $ANTLR start "stop_"
    # SelectScript.g:297:1: stop_ returns [with_] : ^( STOP (e= expr ) ) ;
    def stop_(self, ):

        with_ = None

        e = None


        with_ = []
        try:
            try:
                # SelectScript.g:298:19: ( ^( STOP (e= expr ) ) )
                # SelectScript.g:299:2: ^( STOP (e= expr ) )
                pass 
                self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_498)

                self.match(self.input, DOWN, None)
                # SelectScript.g:299:9: (e= expr )
                # SelectScript.g:299:10: e= expr
                pass 
                self._state.following.append(self.FOLLOW_expr_in_stop_503)
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
    # SelectScript.g:302:1: group_ returns [by] : ^( GROUP (type= PHRASE | f= function )+ ) ;
    def group_(self, ):

        by = None

        type = None
        f = None


        by = []
        try:
            try:
                # SelectScript.g:303:16: ( ^( GROUP (type= PHRASE | f= function )+ ) )
                # SelectScript.g:304:2: ^( GROUP (type= PHRASE | f= function )+ )
                pass 
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_527)

                self.match(self.input, DOWN, None)
                # SelectScript.g:305:3: (type= PHRASE | f= function )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 3
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == PHRASE) :
                        alt16 = 1
                    elif (LA16_0 == FCT) :
                        alt16 = 2


                    if alt16 == 1:
                        # SelectScript.g:305:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_536)
                        if self._state.backtracking == 0:
                            by.append( self._phrase ( type.getText() ) ); 



                    elif alt16 == 2:
                        # SelectScript.g:306:5: f= function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_group_547)
                        f = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( f ); 



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "group_"


    # $ANTLR start "having_"
    # SelectScript.g:311:1: having_ returns [stack] : ^( HAVING e= expr ) ;
    def having_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:311:25: ( ^( HAVING e= expr ) )
                # SelectScript.g:312:2: ^( HAVING e= expr )
                pass 
                self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_572)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_having_576)
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
    # SelectScript.g:315:1: order_ returns [by] : ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) ;
    def order_(self, ):

        by = None

        type = None
        f = None

        dir = None


        by = []
        try:
            try:
                # SelectScript.g:316:16: ( ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) )
                # SelectScript.g:317:2: ^( ORDER (type= PHRASE | f= function dir= direction_ )+ )
                pass 
                self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_599)

                self.match(self.input, DOWN, None)
                # SelectScript.g:318:3: (type= PHRASE | f= function dir= direction_ )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 3
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == PHRASE) :
                        alt17 = 1
                    elif (LA17_0 == FCT) :
                        alt17 = 2


                    if alt17 == 1:
                        # SelectScript.g:319:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_613)
                        if self._state.backtracking == 0:
                            by.append( [ self._phrase ( type.getText()), dir ]); 



                    elif alt17 == 2:
                        # SelectScript.g:320:5: f= function dir= direction_
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_order_625)
                        f = self.function()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_direction__in_order_629)
                        dir = self.direction_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( [f, dir] ); 



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "order_"


    # $ANTLR start "direction_"
    # SelectScript.g:325:1: direction_ returns [dir] : ( ASC | DESC )? ;
    def direction_(self, ):

        dir = None

        dir = 0
        try:
            try:
                # SelectScript.g:326:16: ( ( ASC | DESC )? )
                # SelectScript.g:327:2: ( ASC | DESC )?
                pass 
                # SelectScript.g:327:2: ( ASC | DESC )?
                alt18 = 3
                LA18_0 = self.input.LA(1)

                if (LA18_0 == ASC) :
                    alt18 = 1
                elif (LA18_0 == DESC) :
                    alt18 = 2
                if alt18 == 1:
                    # SelectScript.g:327:4: ASC
                    pass 
                    self.match(self.input, ASC, self.FOLLOW_ASC_in_direction_659)
                    if self._state.backtracking == 0:
                        dir=0; 



                elif alt18 == 2:
                    # SelectScript.g:328:4: DESC
                    pass 
                    self.match(self.input, DESC, self.FOLLOW_DESC_in_direction_667)
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
    # SelectScript.g:332:1: expr returns [val] : (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | a= atom );
    def expr(self, ):

        val = None

        a = None

        l = None

        c = None


        try:
            try:
                # SelectScript.g:332:20: (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | a= atom )
                alt19 = 5
                LA19 = self.input.LA(1)
                if LA19 == ASSIGN:
                    alt19 = 1
                elif LA19 == AND or LA19 == XOR or LA19 == OR or LA19 == NOT:
                    alt19 = 2
                elif LA19 == IN or LA19 == EQ or LA19 == NE or LA19 == LE or LA19 == GE or LA19 == LT or LA19 == GT:
                    alt19 = 3
                elif LA19 == POS or LA19 == NEG or LA19 == ADD or LA19 == SUB or LA19 == MUL or LA19 == DIV or LA19 == MOD or LA19 == POW:
                    alt19 = 4
                elif LA19 == FCT or LA19 == VAR or LA19 == VAL or LA19 == LIST or LA19 == STMT_SELECT or LA19 == THIS or LA19 == 98:
                    alt19 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # SelectScript.g:333:2: a= assign_expr
                    pass 
                    self._state.following.append(self.FOLLOW_assign_expr_in_expr691)
                    a = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt19 == 2:
                    # SelectScript.g:334:4: l= logic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_logic_expr_in_expr703)
                    l = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = l;



                elif alt19 == 3:
                    # SelectScript.g:335:4: c= compare_expr
                    pass 
                    self._state.following.append(self.FOLLOW_compare_expr_in_expr714)
                    c = self.compare_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = c;



                elif alt19 == 4:
                    # SelectScript.g:336:4: a= arithmetic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_arithmetic_expr_in_expr724)
                    a = self.arithmetic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt19 == 5:
                    # SelectScript.g:337:4: a= atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_expr734)
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
    # SelectScript.g:340:1: age returns [a] : ^( AGE (t= expr )? ) ;
    def age(self, ):

        a = None

        t = None


        a=self._val(0); 
        try:
            try:
                # SelectScript.g:341:25: ( ^( AGE (t= expr )? ) )
                # SelectScript.g:342:2: ^( AGE (t= expr )? )
                pass 
                self.match(self.input, AGE, self.FOLLOW_AGE_in_age756)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:342:8: (t= expr )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((FCT <= LA20_0 <= NEG) or LA20_0 == STMT_SELECT or LA20_0 == AND or (XOR <= LA20_0 <= OR) or LA20_0 == NOT or (IN <= LA20_0 <= POW) or LA20_0 == THIS or LA20_0 == 98) :
                        alt20 = 1
                    if alt20 == 1:
                        # SelectScript.g:342:9: t= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_age761)
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


    # $ANTLR start "assign_expr"
    # SelectScript.g:345:1: assign_expr returns [stack] : ^( ASSIGN v= PHRASE e= expr (a= age )? ) ;
    def assign_expr(self, ):

        stack = None

        v = None
        e = None

        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:346:27: ( ^( ASSIGN v= PHRASE e= expr (a= age )? ) )
                # SelectScript.g:347:2: ^( ASSIGN v= PHRASE e= expr (a= age )? )
                pass 
                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr785)

                self.match(self.input, DOWN, None)
                v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr789)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr793)
                e = self.expr()

                self._state.following.pop()
                # SelectScript.g:347:27: (a= age )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == AGE) :
                    alt21 = 1
                if alt21 == 1:
                    # SelectScript.g:347:28: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr798)
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
    # SelectScript.g:350:1: logic_expr returns [stack] : ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) );
    def logic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:350:28: ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) )
                alt22 = 4
                LA22 = self.input.LA(1)
                if LA22 == OR:
                    alt22 = 1
                elif LA22 == XOR:
                    alt22 = 2
                elif LA22 == AND:
                    alt22 = 3
                elif LA22 == NOT:
                    alt22 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # SelectScript.g:351:2: ^( OR e1= expr e2= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_logic_expr819)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr823)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr827)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('or',  [e1, e2]); 



                elif alt22 == 2:
                    # SelectScript.g:352:4: ^( XOR e1= expr e2= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_expr836)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr840)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr844)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('xor', [e1, e2]); 



                elif alt22 == 3:
                    # SelectScript.g:353:4: ^( AND e1= expr e2= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_logic_expr853)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr857)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr861)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('and', [e1, e2]); 



                elif alt22 == 4:
                    # SelectScript.g:354:4: ^( NOT e= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_expr869)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr873)
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
    # SelectScript.g:357:1: compare_expr returns [stack] : ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) );
    def compare_expr(self, ):

        stack = None

        e1 = None

        e2 = None


        try:
            try:
                # SelectScript.g:357:29: ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) )
                alt23 = 7
                LA23 = self.input.LA(1)
                if LA23 == IN:
                    alt23 = 1
                elif LA23 == EQ:
                    alt23 = 2
                elif LA23 == NE:
                    alt23 = 3
                elif LA23 == GE:
                    alt23 = 4
                elif LA23 == GT:
                    alt23 = 5
                elif LA23 == LE:
                    alt23 = 6
                elif LA23 == LT:
                    alt23 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # SelectScript.g:358:2: ^( IN e1= expr e2= expr )
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_compare_expr892)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr896)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr900)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('in', [e2, e1]); 



                elif alt23 == 2:
                    # SelectScript.g:359:4: ^( EQ e1= expr e2= expr )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_expr909)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr913)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr917)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('eq', [e1, e2]); 



                elif alt23 == 3:
                    # SelectScript.g:360:4: ^( NE e1= expr e2= expr )
                    pass 
                    self.match(self.input, NE, self.FOLLOW_NE_in_compare_expr926)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr930)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr934)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ne', [e1, e2]); 



                elif alt23 == 4:
                    # SelectScript.g:361:4: ^( GE e1= expr e2= expr )
                    pass 
                    self.match(self.input, GE, self.FOLLOW_GE_in_compare_expr943)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr947)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr951)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ge', [e1, e2]); 



                elif alt23 == 5:
                    # SelectScript.g:362:4: ^( GT e1= expr e2= expr )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_compare_expr960)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr964)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr968)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('gt', [e1, e2]); 



                elif alt23 == 6:
                    # SelectScript.g:363:4: ^( LE e1= expr e2= expr )
                    pass 
                    self.match(self.input, LE, self.FOLLOW_LE_in_compare_expr977)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr981)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr985)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('le', [e1, e2]); 



                elif alt23 == 7:
                    # SelectScript.g:364:4: ^( LT e1= expr e2= expr )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_compare_expr994)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr998)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr1002)
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
    # SelectScript.g:367:1: arithmetic_expr returns [stack] : ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) );
    def arithmetic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:367:32: ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) )
                alt24 = 8
                LA24 = self.input.LA(1)
                if LA24 == MUL:
                    alt24 = 1
                elif LA24 == DIV:
                    alt24 = 2
                elif LA24 == MOD:
                    alt24 = 3
                elif LA24 == SUB:
                    alt24 = 4
                elif LA24 == ADD:
                    alt24 = 5
                elif LA24 == POW:
                    alt24 = 6
                elif LA24 == NEG:
                    alt24 = 7
                elif LA24 == POS:
                    alt24 = 8
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # SelectScript.g:368:2: ^( MUL e1= expr e2= expr )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_expr1020)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1024)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1028)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mul', [e1, e2]); 



                elif alt24 == 2:
                    # SelectScript.g:369:3: ^( DIV e1= expr e2= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_expr1036)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1040)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1044)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('div', [e1, e2]); 



                elif alt24 == 3:
                    # SelectScript.g:370:3: ^( MOD e1= expr e2= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_expr1052)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1056)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1060)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mod', [e1, e2]); 



                elif alt24 == 4:
                    # SelectScript.g:371:3: ^( SUB e1= expr e2= expr )
                    pass 
                    self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_expr1068)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1072)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1076)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('sub', [e1, e2]); 



                elif alt24 == 5:
                    # SelectScript.g:372:3: ^( ADD e1= expr e2= expr )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_expr1084)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1088)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1092)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('add', [e1, e2]); 



                elif alt24 == 6:
                    # SelectScript.g:373:3: ^( POW e1= expr e2= expr )
                    pass 
                    self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_expr1100)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1104)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1108)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pow', [e1, e2]); 



                elif alt24 == 7:
                    # SelectScript.g:374:3: ^( NEG e= expr )
                    pass 
                    self.match(self.input, NEG, self.FOLLOW_NEG_in_arithmetic_expr1116)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1120)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('neg', [e]); 



                elif alt24 == 8:
                    # SelectScript.g:375:3: ^( POS e= expr )
                    pass 
                    self.match(self.input, POS, self.FOLLOW_POS_in_arithmetic_expr1129)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1133)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pos', [e]); 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "arithmetic_expr"


    # $ANTLR start "atom"
    # SelectScript.g:378:1: atom returns [stack] : (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select );
    def atom(self, ):

        stack = None

        val = None

        var = None

        fct = None

        e = None

        s = None


        try:
            try:
                # SelectScript.g:378:22: (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select )
                alt25 = 5
                LA25 = self.input.LA(1)
                if LA25 == VAL or LA25 == LIST or LA25 == THIS:
                    alt25 = 1
                elif LA25 == VAR:
                    alt25 = 2
                elif LA25 == FCT:
                    alt25 = 3
                elif LA25 == 98:
                    alt25 = 4
                elif LA25 == STMT_SELECT:
                    alt25 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # SelectScript.g:379:2: val= value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_atom1155)
                    val = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = val



                elif alt25 == 2:
                    # SelectScript.g:380:4: var= variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_atom1168)
                    var = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = var



                elif alt25 == 3:
                    # SelectScript.g:381:4: fct= function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_atom1180)
                    fct = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = fct



                elif alt25 == 4:
                    # SelectScript.g:382:4: '(' e= expr ')'
                    pass 
                    self.match(self.input, 98, self.FOLLOW_98_in_atom1188)
                    self._state.following.append(self.FOLLOW_expr_in_atom1192)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 99, self.FOLLOW_99_in_atom1194)
                    if self._state.backtracking == 0:
                        stack = e  



                elif alt25 == 5:
                    # SelectScript.g:383:4: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_atom1204)
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
    # SelectScript.g:386:1: value returns [val] : ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ );
    def value(self, ):

        val = None

        STRING1 = None
        INTEGER2 = None
        FLOAT3 = None
        t = None

        l = None


        try:
            try:
                # SelectScript.g:386:21: ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ )
                alt26 = 7
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # SelectScript.g:387:4: ^( VAL STRING )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1224)

                    self.match(self.input, DOWN, None)
                    STRING1=self.match(self.input, STRING, self.FOLLOW_STRING_in_value1226)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( STRING1.getText()[1:-1] ); 



                elif alt26 == 2:
                    # SelectScript.g:388:4: ^( VAL INTEGER )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1236)

                    self.match(self.input, DOWN, None)
                    INTEGER2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value1238)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( int(INTEGER2.getText()) ); 



                elif alt26 == 3:
                    # SelectScript.g:389:4: ^( VAL FLOAT )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1248)

                    self.match(self.input, DOWN, None)
                    FLOAT3=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value1250)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( float(FLOAT3.getText()) ); 



                elif alt26 == 4:
                    # SelectScript.g:390:4: ^( VAL TRUE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1260)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value1262)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( True  ); 



                elif alt26 == 5:
                    # SelectScript.g:391:4: ^( VAL FALSE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1272)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value1274)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( False ); 



                elif alt26 == 6:
                    # SelectScript.g:392:4: t= this_
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_value1285)
                    t = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val=t; 



                elif alt26 == 7:
                    # SelectScript.g:393:4: l= list_
                    pass 
                    self._state.following.append(self.FOLLOW_list__in_value1295)
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
    # SelectScript.g:396:1: this_ returns [p] : ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        p = None

        PHRASE4 = None

        p=self._this(); 
        try:
            try:
                # SelectScript.g:397:26: ( ^( THIS ( PHRASE )? ) )
                # SelectScript.g:398:2: ^( THIS ( PHRASE )? )
                pass 
                self.match(self.input, THIS, self.FOLLOW_THIS_in_this_1317)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:398:9: ( PHRASE )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == PHRASE) :
                        alt27 = 1
                    if alt27 == 1:
                        # SelectScript.g:398:10: PHRASE
                        pass 
                        PHRASE4=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_1320)
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
    # SelectScript.g:401:1: list_ returns [l] : ^( LIST (e= expr )* ) ;
    def list_(self, ):

        l = None

        e = None


        l = [] 
        try:
            try:
                # SelectScript.g:402:17: ( ^( LIST (e= expr )* ) )
                # SelectScript.g:403:2: ^( LIST (e= expr )* )
                pass 
                self.match(self.input, LIST, self.FOLLOW_LIST_in_list_1344)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:403:9: (e= expr )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if ((FCT <= LA28_0 <= NEG) or LA28_0 == STMT_SELECT or LA28_0 == AND or (XOR <= LA28_0 <= OR) or LA28_0 == NOT or (IN <= LA28_0 <= POW) or LA28_0 == THIS or LA28_0 == 98) :
                            alt28 = 1


                        if alt28 == 1:
                            # SelectScript.g:403:11: e= expr
                            pass 
                            self._state.following.append(self.FOLLOW_expr_in_list_1350)
                            e = self.expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                l.append(e); 



                        else:
                            break #loop28

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return l

    # $ANTLR end "list_"


    # $ANTLR start "variable"
    # SelectScript.g:406:1: variable returns [var] : ^( VAR PHRASE (a= age )? ) ;
    def variable(self, ):

        var = None

        PHRASE5 = None
        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:407:27: ( ^( VAR PHRASE (a= age )? ) )
                # SelectScript.g:408:2: ^( VAR PHRASE (a= age )? )
                pass 
                self.match(self.input, VAR, self.FOLLOW_VAR_in_variable1374)

                self.match(self.input, DOWN, None)
                PHRASE5=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable1376)
                # SelectScript.g:408:15: (a= age )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == AGE) :
                    alt29 = 1
                if alt29 == 1:
                    # SelectScript.g:408:16: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable1381)
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
    # SelectScript.g:411:1: function returns [stack] : ^( FCT PHRASE (params= parameter )? ) ;
    def function(self, ):

        stack = None

        PHRASE6 = None
        params = None


        try:
            try:
                # SelectScript.g:411:26: ( ^( FCT PHRASE (params= parameter )? ) )
                # SelectScript.g:412:2: ^( FCT PHRASE (params= parameter )? )
                pass 
                self.match(self.input, FCT, self.FOLLOW_FCT_in_function1401)

                self.match(self.input, DOWN, None)
                PHRASE6=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function1403)
                # SelectScript.g:412:21: (params= parameter )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if ((FCT <= LA30_0 <= NEG) or LA30_0 == STMT_SELECT or LA30_0 == AND or (XOR <= LA30_0 <= OR) or LA30_0 == NOT or (IN <= LA30_0 <= POW) or LA30_0 == THIS or LA30_0 == 98) :
                    alt30 = 1
                elif (LA30_0 == 3) :
                    LA30_2 = self.input.LA(2)

                    if (self.synpred61_SelectScript()) :
                        alt30 = 1
                if alt30 == 1:
                    # SelectScript.g:0:0: params= parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function1407)
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
    # SelectScript.g:416:1: parameter returns [stack] : (e= expr )* ;
    def parameter(self, ):

        stack = None

        e = None


        stack = []
        try:
            try:
                # SelectScript.g:417:19: ( (e= expr )* )
                # SelectScript.g:418:2: (e= expr )*
                pass 
                # SelectScript.g:418:2: (e= expr )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if ((FCT <= LA31_0 <= NEG) or LA31_0 == STMT_SELECT or LA31_0 == AND or (XOR <= LA31_0 <= OR) or LA31_0 == NOT or (IN <= LA31_0 <= POW) or LA31_0 == THIS or LA31_0 == 98) :
                        alt31 = 1


                    if alt31 == 1:
                        # SelectScript.g:418:3: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_parameter1433)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stack.append(e)



                    else:
                        break #loop31




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "parameter"

    # $ANTLR start "synpred2_SelectScript"
    def synpred2_SelectScript_fragment(self, ):
        # SelectScript.g:248:2: (s= statement_select )
        # SelectScript.g:248:2: s= statement_select
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectScript117)
        s = self.statement_select()

        self._state.following.pop()


    # $ANTLR end "synpred2_SelectScript"



    # $ANTLR start "synpred17_SelectScript"
    def synpred17_SelectScript_fragment(self, ):
        # SelectScript.g:280:20: (p= parameter )
        # SelectScript.g:280:20: p= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred17_SelectScript391)
        p = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectScript"



    # $ANTLR start "synpred61_SelectScript"
    def synpred61_SelectScript_fragment(self, ):
        # SelectScript.g:412:21: (params= parameter )
        # SelectScript.g:412:21: params= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred61_SelectScript1407)
        params = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred61_SelectScript"




    # Delegated rules

    def synpred61_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred61_SelectScript_fragment()
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
        u"\35\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\35\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\4\1\0\33\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\142\1\0\33\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\31\uffff\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\33\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\6\2\1\uffff\1\1\7\uffff\1\2\3\uffff\2\2\1\uffff\1\2"
        u"\1\uffff\16\2\34\uffff\1\2\33\uffff\1\2"),
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
                    s = 28

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
    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\6\1\2\2\uffff\1\125\5\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\106\1\2\2\uffff\1\132\5\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\2\uffff\1\6\1\7\1\uffff\1\1\1\2\1\3\1\4\1\5"
        )

    DFA26_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\1\3\76\uffff\1\2"),
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

    # class definition for DFA #26

    class DFA26(DFA):
        pass


 

    FOLLOW_prog_in_eval74 = frozenset([1])
    FOLLOW_statement_in_prog96 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_statement_select_in_statement117 = frozenset([1])
    FOLLOW_expr_in_statement127 = frozenset([1])
    FOLLOW_STMT_SELECT_in_statement_select156 = frozenset([2])
    FOLLOW_select__in_statement_select160 = frozenset([55])
    FOLLOW_from__in_statement_select164 = frozenset([3, 58, 59, 63, 69, 72, 73])
    FOLLOW_where__in_statement_select170 = frozenset([3, 59, 63, 69, 72, 73])
    FOLLOW_group__in_statement_select179 = frozenset([3, 59, 65, 69, 72, 73])
    FOLLOW_having__in_statement_select184 = frozenset([3, 59, 69, 72, 73])
    FOLLOW_order__in_statement_select194 = frozenset([3, 69, 72, 73])
    FOLLOW_as__in_statement_select203 = frozenset([3, 72, 73])
    FOLLOW_start__in_statement_select212 = frozenset([72, 73])
    FOLLOW_connect__in_statement_select218 = frozenset([74])
    FOLLOW_stop__in_statement_select222 = frozenset([3])
    FOLLOW_SELECT_in_select_246 = frozenset([2])
    FOLLOW_PHRASE_in_select_257 = frozenset([3, 4, 70, 93])
    FOLLOW_function_in_select_269 = frozenset([3, 4, 70, 93])
    FOLLOW_this__in_select_281 = frozenset([3, 4, 70, 93])
    FOLLOW_FROM_in_from_310 = frozenset([2])
    FOLLOW_expr_in_from_315 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_AS_in_as_339 = frozenset([2])
    FOLLOW_AS_DICT_in_as_341 = frozenset([3])
    FOLLOW_AS_in_as_353 = frozenset([2])
    FOLLOW_AS_LIST_in_as_355 = frozenset([3])
    FOLLOW_AS_in_as_367 = frozenset([2])
    FOLLOW_AS_VALUE_in_as_369 = frozenset([3])
    FOLLOW_AS_in_as_381 = frozenset([2])
    FOLLOW_PHRASE_in_as_385 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_parameter_in_as_391 = frozenset([3])
    FOLLOW_WHERE_in_where_414 = frozenset([2])
    FOLLOW_expr_in_where_418 = frozenset([3])
    FOLLOW_START_in_start_440 = frozenset([2])
    FOLLOW_expr_in_start_445 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_CONNECT_in_connect_469 = frozenset([2])
    FOLLOW_expr_in_connect_474 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_STOP_in_stop_498 = frozenset([2])
    FOLLOW_expr_in_stop_503 = frozenset([3])
    FOLLOW_GROUP_in_group_527 = frozenset([2])
    FOLLOW_PHRASE_in_group_536 = frozenset([3, 4, 93])
    FOLLOW_function_in_group_547 = frozenset([3, 4, 93])
    FOLLOW_HAVING_in_having_572 = frozenset([2])
    FOLLOW_expr_in_having_576 = frozenset([3])
    FOLLOW_ORDER_in_order_599 = frozenset([2])
    FOLLOW_PHRASE_in_order_613 = frozenset([3, 4, 93])
    FOLLOW_function_in_order_625 = frozenset([3, 4, 76, 77, 93])
    FOLLOW_direction__in_order_629 = frozenset([3, 4, 93])
    FOLLOW_ASC_in_direction_659 = frozenset([1])
    FOLLOW_DESC_in_direction_667 = frozenset([1])
    FOLLOW_assign_expr_in_expr691 = frozenset([1])
    FOLLOW_logic_expr_in_expr703 = frozenset([1])
    FOLLOW_compare_expr_in_expr714 = frozenset([1])
    FOLLOW_arithmetic_expr_in_expr724 = frozenset([1])
    FOLLOW_atom_in_expr734 = frozenset([1])
    FOLLOW_AGE_in_age756 = frozenset([2])
    FOLLOW_expr_in_age761 = frozenset([3])
    FOLLOW_ASSIGN_in_assign_expr785 = frozenset([2])
    FOLLOW_PHRASE_in_assign_expr789 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_assign_expr793 = frozenset([3, 10])
    FOLLOW_age_in_assign_expr798 = frozenset([3])
    FOLLOW_OR_in_logic_expr819 = frozenset([2])
    FOLLOW_expr_in_logic_expr823 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_logic_expr827 = frozenset([3])
    FOLLOW_XOR_in_logic_expr836 = frozenset([2])
    FOLLOW_expr_in_logic_expr840 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_logic_expr844 = frozenset([3])
    FOLLOW_AND_in_logic_expr853 = frozenset([2])
    FOLLOW_expr_in_logic_expr857 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_logic_expr861 = frozenset([3])
    FOLLOW_NOT_in_logic_expr869 = frozenset([2])
    FOLLOW_expr_in_logic_expr873 = frozenset([3])
    FOLLOW_IN_in_compare_expr892 = frozenset([2])
    FOLLOW_expr_in_compare_expr896 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr900 = frozenset([3])
    FOLLOW_EQ_in_compare_expr909 = frozenset([2])
    FOLLOW_expr_in_compare_expr913 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr917 = frozenset([3])
    FOLLOW_NE_in_compare_expr926 = frozenset([2])
    FOLLOW_expr_in_compare_expr930 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr934 = frozenset([3])
    FOLLOW_GE_in_compare_expr943 = frozenset([2])
    FOLLOW_expr_in_compare_expr947 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr951 = frozenset([3])
    FOLLOW_GT_in_compare_expr960 = frozenset([2])
    FOLLOW_expr_in_compare_expr964 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr968 = frozenset([3])
    FOLLOW_LE_in_compare_expr977 = frozenset([2])
    FOLLOW_expr_in_compare_expr981 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr985 = frozenset([3])
    FOLLOW_LT_in_compare_expr994 = frozenset([2])
    FOLLOW_expr_in_compare_expr998 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_compare_expr1002 = frozenset([3])
    FOLLOW_MUL_in_arithmetic_expr1020 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1024 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1028 = frozenset([3])
    FOLLOW_DIV_in_arithmetic_expr1036 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1040 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1044 = frozenset([3])
    FOLLOW_MOD_in_arithmetic_expr1052 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1056 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1060 = frozenset([3])
    FOLLOW_SUB_in_arithmetic_expr1068 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1072 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1076 = frozenset([3])
    FOLLOW_ADD_in_arithmetic_expr1084 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1088 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1092 = frozenset([3])
    FOLLOW_POW_in_arithmetic_expr1100 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1104 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_expr_in_arithmetic_expr1108 = frozenset([3])
    FOLLOW_NEG_in_arithmetic_expr1116 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1120 = frozenset([3])
    FOLLOW_POS_in_arithmetic_expr1129 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1133 = frozenset([3])
    FOLLOW_value_in_atom1155 = frozenset([1])
    FOLLOW_variable_in_atom1168 = frozenset([1])
    FOLLOW_function_in_atom1180 = frozenset([1])
    FOLLOW_98_in_atom1188 = frozenset([4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98, 99])
    FOLLOW_expr_in_atom1192 = frozenset([99])
    FOLLOW_99_in_atom1194 = frozenset([1])
    FOLLOW_statement_select_in_atom1204 = frozenset([1])
    FOLLOW_VAL_in_value1224 = frozenset([2])
    FOLLOW_STRING_in_value1226 = frozenset([3])
    FOLLOW_VAL_in_value1236 = frozenset([2])
    FOLLOW_INTEGER_in_value1238 = frozenset([3])
    FOLLOW_VAL_in_value1248 = frozenset([2])
    FOLLOW_FLOAT_in_value1250 = frozenset([3])
    FOLLOW_VAL_in_value1260 = frozenset([2])
    FOLLOW_TRUE_in_value1262 = frozenset([3])
    FOLLOW_VAL_in_value1272 = frozenset([2])
    FOLLOW_FALSE_in_value1274 = frozenset([3])
    FOLLOW_this__in_value1285 = frozenset([1])
    FOLLOW_list__in_value1295 = frozenset([1])
    FOLLOW_THIS_in_this_1317 = frozenset([2])
    FOLLOW_PHRASE_in_this_1320 = frozenset([3])
    FOLLOW_LIST_in_list_1344 = frozenset([2])
    FOLLOW_expr_in_list_1350 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_VAR_in_variable1374 = frozenset([2])
    FOLLOW_PHRASE_in_variable1376 = frozenset([3, 10])
    FOLLOW_age_in_variable1381 = frozenset([3])
    FOLLOW_FCT_in_function1401 = frozenset([2])
    FOLLOW_PHRASE_in_function1403 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_parameter_in_function1407 = frozenset([3])
    FOLLOW_expr_in_parameter1433 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 98])
    FOLLOW_statement_select_in_synpred2_SelectScript117 = frozenset([1])
    FOLLOW_parameter_in_synpred17_SelectScript391 = frozenset([1])
    FOLLOW_parameter_in_synpred61_SelectScript1407 = frozenset([1])



       
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
