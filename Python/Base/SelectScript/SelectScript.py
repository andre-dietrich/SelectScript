# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectScript.g 2014-11-06 17:12:30

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
PHRASE=89
SUB=37
IN=28
DOT=12
WHERE=58
AS=69
LINE_COMMENT=80
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
J=91
K=92
ASSIGN=29
L=50
M=54
N=17
COMMENT=79
O=21
P=62
ORDER=59
GROUP=63
ASC=72
Q=90
R=22
S=48
T=25
U=61
V=64
W=56
BY=68
X=20
Y=67
CHARACTER=87
Z=93
SQ=42
SELECT=52
DIV=39
NEG=9
LIST_END=45
LE=32
STRING=81
ADD=36
T__94=94
LT=34
FROM=55
DQ=43
SPECIAL=88
DESC=73
T__95=95
INTEGER=83
MUL=38
NEWLINE=77
TRUE=85
EQ=30
NOT=26
AND=19
NE=31
THIS=70
END=14
HAVING=65
LIST=7
FLOAT=84
AS_VALUE=75
AGE_END=47
AS_DICT=76
WS=78
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
DIGIT=82
FALSE=86
AS_LIST=74

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FCT", "VAR", "VAL", "LIST", "POS", "NEG", "AGE", "STMT_SELECT", "DOT", 
    "SEP", "END", "COLON", "A", "N", "D", "AND", "X", "O", "R", "XOR", "OR", 
    "T", "NOT", "I", "IN", "ASSIGN", "EQ", "NE", "LE", "GE", "LT", "GT", 
    "ADD", "SUB", "MUL", "DIV", "MOD", "POW", "SQ", "DQ", "LIST_BEGIN", 
    "LIST_END", "AGE_BEGIN", "AGE_END", "S", "E", "L", "C", "SELECT", "F", 
    "M", "FROM", "W", "H", "WHERE", "ORDER", "G", "U", "P", "GROUP", "V", 
    "HAVING", "B", "Y", "BY", "AS", "THIS", "TIME", "ASC", "DESC", "AS_LIST", 
    "AS_VALUE", "AS_DICT", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT", "STRING", 
    "DIGIT", "INTEGER", "FLOAT", "TRUE", "FALSE", "CHARACTER", "SPECIAL", 
    "PHRASE", "Q", "J", "K", "Z", "'('", "')'"
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

        self.dfa22 = self.DFA22(
            self, 22,
            eot = self.DFA22_eot,
            eof = self.DFA22_eof,
            min = self.DFA22_min,
            max = self.DFA22_max,
            accept = self.DFA22_accept,
            special = self.DFA22_special,
            transition = self.DFA22_transition
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
             'phrase':6 }
             
    asTypes = {'dict' :'d', 'list' :'l', 'value':'v'}
    			
    def _fct(self, name, params):
    	return [self.types['fct'], name, params]

    def _var(self, var_name, age=0) :
    	return [self.types['var'], var_name, age]

    def _val(self, value) :
    	return [self.types['val'], value]
    	
    def _list(self, l) :
    	return [self.types['list'], l]
    	
    def _sel(self, s, f, w, g, h, o, a) :
    	return [self.types['sel'], s, f, w, g, h, o, a]
    	
    def _this(self, name='') :
    	return [self.types['this'], name]
    	
    def _phrase(self, name) :
    	return [self.types['phrase'], name]
    	
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
    		S, F, W, G, H, O, A = prog[1:]
    		
    		S = [self.Simplify(expr) for expr in S]
    		F = [self.Simplify(expr) for expr in F]
    		W =  self.Simplify(W)
    		G = [self.Simplify(expr) for expr in G]
    		H = [self.Simplify(expr) for expr in H]
    		if O != []:
    			O = [[self.Simplify(expr[0]), expr[1]] for expr in O]
    		A[1] = [self.Simplify(expr) for expr in A[1]]
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
    	else:
    		print ""



    # $ANTLR start "eval"
    # SelectScript.g:221:1: eval returns [stmt_list] : p= prog ;
    def eval(self, ):

        stmt_list = None

        p = None


        try:
            try:
                # SelectScript.g:221:25: (p= prog )
                # SelectScript.g:222:5: p= prog
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
    # SelectScript.g:225:1: prog returns [stmt_list] : (stmt= statement )+ ;
    def prog(self, ):

        stmt_list = None

        stmt = None


        stmt_list = []
        try:
            try:
                # SelectScript.g:226:22: ( (stmt= statement )+ )
                # SelectScript.g:227:2: (stmt= statement )+
                pass 
                # SelectScript.g:227:2: (stmt= statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((FCT <= LA1_0 <= NEG) or LA1_0 == STMT_SELECT or LA1_0 == AND or (XOR <= LA1_0 <= OR) or LA1_0 == NOT or (IN <= LA1_0 <= POW) or LA1_0 == THIS or LA1_0 == 94) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectScript.g:227:3: stmt= statement
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
    # SelectScript.g:230:1: statement returns [stmt] : (s= statement_select | e= expr );
    def statement(self, ):

        stmt = None

        s = None

        e = None


        try:
            try:
                # SelectScript.g:230:25: (s= statement_select | e= expr )
                alt2 = 2
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectScript.g:231:2: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_statement117)
                    s = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stmt = s



                elif alt2 == 2:
                    # SelectScript.g:232:4: e= expr
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
    # SelectScript.g:235:1: statement_select returns [selection] : ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ) ;
    def statement_select(self, ):

        selection = None

        s = None

        f = None

        w = None

        g = None

        h = None

        o = None

        a = None


        s=[]; f=[]; w=[]; g=[]; h=[]; o=[]; a=[self.asTypes['dict'], []]; 
        try:
            try:
                # SelectScript.g:238:1: ( ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? ) )
                # SelectScript.g:239:2: ^( STMT_SELECT s= select_ f= from_ (w= where_ )? (g= group_ (h= having_ )? )? (o= order_ )? (a= as_ )? )
                pass 
                self.match(self.input, STMT_SELECT, self.FOLLOW_STMT_SELECT_in_statement_select156)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_select__in_statement_select160)
                s = self.select_()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_from__in_statement_select164)
                f = self.from_()

                self._state.following.pop()
                # SelectScript.g:239:34: (w= where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    alt3 = 1
                if alt3 == 1:
                    # SelectScript.g:239:36: w= where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select170)
                    w = self.where_()

                    self._state.following.pop()



                # SelectScript.g:239:48: (g= group_ (h= having_ )? )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == GROUP) :
                    alt5 = 1
                if alt5 == 1:
                    # SelectScript.g:239:50: g= group_ (h= having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select179)
                    g = self.group_()

                    self._state.following.pop()
                    # SelectScript.g:239:59: (h= having_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == HAVING) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectScript.g:239:60: h= having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select184)
                        h = self.having_()

                        self._state.following.pop()






                # SelectScript.g:239:74: (o= order_ )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ORDER) :
                    alt6 = 1
                if alt6 == 1:
                    # SelectScript.g:239:76: o= order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select194)
                    o = self.order_()

                    self._state.following.pop()



                # SelectScript.g:239:88: (a= as_ )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == AS) :
                    alt7 = 1
                if alt7 == 1:
                    # SelectScript.g:239:90: a= as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select203)
                    a = self.as_()

                    self._state.following.pop()




                self.match(self.input, UP, None)



                if self._state.backtracking == 0:
                    selection = self._sel(s, f, w, g, h, o, a); 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return selection

    # $ANTLR end "statement_select"


    # $ANTLR start "select_"
    # SelectScript.g:242:1: select_ returns [types] : ^( SELECT (type= PHRASE | f= function | t= this_ )* ) ;
    def select_(self, ):

        types = None

        type = None
        f = None

        t = None


        types = []
        try:
            try:
                # SelectScript.g:243:19: ( ^( SELECT (type= PHRASE | f= function | t= this_ )* ) )
                # SelectScript.g:244:2: ^( SELECT (type= PHRASE | f= function | t= this_ )* )
                pass 
                self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_227)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:245:3: (type= PHRASE | f= function | t= this_ )*
                    while True: #loop8
                        alt8 = 4
                        LA8 = self.input.LA(1)
                        if LA8 == PHRASE:
                            alt8 = 1
                        elif LA8 == FCT:
                            alt8 = 2
                        elif LA8 == THIS:
                            alt8 = 3

                        if alt8 == 1:
                            # SelectScript.g:246:3: type= PHRASE
                            pass 
                            type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_238)
                            if self._state.backtracking == 0:
                                types.append( self._phrase (type.getText()) ); 



                        elif alt8 == 2:
                            # SelectScript.g:247:5: f= function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_select_250)
                            f = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( f ); 



                        elif alt8 == 3:
                            # SelectScript.g:248:5: t= this_
                            pass 
                            self._state.following.append(self.FOLLOW_this__in_select_262)
                            t = self.this_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                types.append( t ); 



                        else:
                            break #loop8

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return types

    # $ANTLR end "select_"


    # $ANTLR start "from_"
    # SelectScript.g:253:1: from_ returns [env] : ^( FROM (e= expr )+ ) ;
    def from_(self, ):

        env = None

        e = None


        env=[]; 
        try:
            try:
                # SelectScript.g:254:17: ( ^( FROM (e= expr )+ ) )
                # SelectScript.g:255:2: ^( FROM (e= expr )+ )
                pass 
                self.match(self.input, FROM, self.FOLLOW_FROM_in_from_291)

                self.match(self.input, DOWN, None)
                # SelectScript.g:255:9: (e= expr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((FCT <= LA9_0 <= NEG) or LA9_0 == STMT_SELECT or LA9_0 == AND or (XOR <= LA9_0 <= OR) or LA9_0 == NOT or (IN <= LA9_0 <= POW) or LA9_0 == THIS or LA9_0 == 94) :
                        alt9 = 1


                    if alt9 == 1:
                        # SelectScript.g:255:10: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_from_296)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            env.append(e); 



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return env

    # $ANTLR end "from_"


    # $ANTLR start "as_"
    # SelectScript.g:258:1: as_ returns [rep] : ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) );
    def as_(self, ):

        rep = None

        v = None
        p = None


        p=[]; 
        try:
            try:
                # SelectScript.g:259:15: ( ^( AS AS_DICT ) | ^( AS AS_LIST ) | ^( AS AS_VALUE ) | ^( AS v= PHRASE (p= parameter )? ) )
                alt11 = 4
                LA11_0 = self.input.LA(1)

                if (LA11_0 == AS) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == 2) :
                        LA11 = self.input.LA(3)
                        if LA11 == AS_DICT:
                            alt11 = 1
                        elif LA11 == AS_LIST:
                            alt11 = 2
                        elif LA11 == AS_VALUE:
                            alt11 = 3
                        elif LA11 == PHRASE:
                            alt11 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 11, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 11, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # SelectScript.g:260:2: ^( AS AS_DICT )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_320)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_322)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['dict'],  []]; 



                elif alt11 == 2:
                    # SelectScript.g:261:4: ^( AS AS_LIST )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_334)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_336)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['list'],  []]; 



                elif alt11 == 3:
                    # SelectScript.g:262:4: ^( AS AS_VALUE )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_348)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_350)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        rep= [ self.asTypes['value'], []]; 



                elif alt11 == 4:
                    # SelectScript.g:263:4: ^( AS v= PHRASE (p= parameter )? )
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_as_362)

                    self.match(self.input, DOWN, None)
                    v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_366)
                    # SelectScript.g:263:18: (p= parameter )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((FCT <= LA10_0 <= NEG) or LA10_0 == STMT_SELECT or LA10_0 == AND or (XOR <= LA10_0 <= OR) or LA10_0 == NOT or (IN <= LA10_0 <= POW) or LA10_0 == THIS or LA10_0 == 94) :
                        alt10 = 1
                    elif (LA10_0 == 3) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred15_SelectScript()) :
                            alt10 = 1
                    if alt10 == 1:
                        # SelectScript.g:263:20: p= parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_as_372)
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
    # SelectScript.g:266:1: where_ returns [stack] : ^( WHERE e= expr ) ;
    def where_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:266:24: ( ^( WHERE e= expr ) )
                # SelectScript.g:267:2: ^( WHERE e= expr )
                pass 
                self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_395)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_where_399)
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


    # $ANTLR start "group_"
    # SelectScript.g:270:1: group_ returns [by] : ^( GROUP (type= PHRASE | f= function )+ ) ;
    def group_(self, ):

        by = None

        type = None
        f = None


        by = []
        try:
            try:
                # SelectScript.g:271:16: ( ^( GROUP (type= PHRASE | f= function )+ ) )
                # SelectScript.g:272:2: ^( GROUP (type= PHRASE | f= function )+ )
                pass 
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_422)

                self.match(self.input, DOWN, None)
                # SelectScript.g:273:3: (type= PHRASE | f= function )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 3
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == PHRASE) :
                        alt12 = 1
                    elif (LA12_0 == FCT) :
                        alt12 = 2


                    if alt12 == 1:
                        # SelectScript.g:273:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_431)
                        if self._state.backtracking == 0:
                            by.append( self._phrase ( type.getText() ) ); 



                    elif alt12 == 2:
                        # SelectScript.g:274:5: f= function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_group_442)
                        f = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( f ); 



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "group_"


    # $ANTLR start "having_"
    # SelectScript.g:279:1: having_ returns [stack] : ^( HAVING e= expr ) ;
    def having_(self, ):

        stack = None

        e = None


        try:
            try:
                # SelectScript.g:279:25: ( ^( HAVING e= expr ) )
                # SelectScript.g:280:2: ^( HAVING e= expr )
                pass 
                self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_467)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_having_471)
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
    # SelectScript.g:283:1: order_ returns [by] : ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) ;
    def order_(self, ):

        by = None

        type = None
        f = None

        dir = None


        by = []
        try:
            try:
                # SelectScript.g:284:16: ( ^( ORDER (type= PHRASE | f= function dir= direction_ )+ ) )
                # SelectScript.g:285:2: ^( ORDER (type= PHRASE | f= function dir= direction_ )+ )
                pass 
                self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_494)

                self.match(self.input, DOWN, None)
                # SelectScript.g:286:3: (type= PHRASE | f= function dir= direction_ )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 3
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == PHRASE) :
                        alt13 = 1
                    elif (LA13_0 == FCT) :
                        alt13 = 2


                    if alt13 == 1:
                        # SelectScript.g:287:5: type= PHRASE
                        pass 
                        type=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_508)
                        if self._state.backtracking == 0:
                            by.append( [ self._phrase ( type.getText()), dir ]); 



                    elif alt13 == 2:
                        # SelectScript.g:288:5: f= function dir= direction_
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_order_520)
                        f = self.function()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_direction__in_order_524)
                        dir = self.direction_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            by.append( [f, dir] ); 



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return by

    # $ANTLR end "order_"


    # $ANTLR start "direction_"
    # SelectScript.g:293:1: direction_ returns [dir] : ( ASC | DESC )? ;
    def direction_(self, ):

        dir = None

        dir = 0
        try:
            try:
                # SelectScript.g:294:16: ( ( ASC | DESC )? )
                # SelectScript.g:295:2: ( ASC | DESC )?
                pass 
                # SelectScript.g:295:2: ( ASC | DESC )?
                alt14 = 3
                LA14_0 = self.input.LA(1)

                if (LA14_0 == ASC) :
                    alt14 = 1
                elif (LA14_0 == DESC) :
                    alt14 = 2
                if alt14 == 1:
                    # SelectScript.g:295:4: ASC
                    pass 
                    self.match(self.input, ASC, self.FOLLOW_ASC_in_direction_554)
                    if self._state.backtracking == 0:
                        dir=0; 



                elif alt14 == 2:
                    # SelectScript.g:296:4: DESC
                    pass 
                    self.match(self.input, DESC, self.FOLLOW_DESC_in_direction_562)
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
    # SelectScript.g:300:1: expr returns [val] : (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | a= atom );
    def expr(self, ):

        val = None

        a = None

        l = None

        c = None


        try:
            try:
                # SelectScript.g:300:20: (a= assign_expr | l= logic_expr | c= compare_expr | a= arithmetic_expr | a= atom )
                alt15 = 5
                LA15 = self.input.LA(1)
                if LA15 == ASSIGN:
                    alt15 = 1
                elif LA15 == AND or LA15 == XOR or LA15 == OR or LA15 == NOT:
                    alt15 = 2
                elif LA15 == IN or LA15 == EQ or LA15 == NE or LA15 == LE or LA15 == GE or LA15 == LT or LA15 == GT:
                    alt15 = 3
                elif LA15 == POS or LA15 == NEG or LA15 == ADD or LA15 == SUB or LA15 == MUL or LA15 == DIV or LA15 == MOD or LA15 == POW:
                    alt15 = 4
                elif LA15 == FCT or LA15 == VAR or LA15 == VAL or LA15 == LIST or LA15 == STMT_SELECT or LA15 == THIS or LA15 == 94:
                    alt15 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # SelectScript.g:301:2: a= assign_expr
                    pass 
                    self._state.following.append(self.FOLLOW_assign_expr_in_expr586)
                    a = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt15 == 2:
                    # SelectScript.g:302:4: l= logic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_logic_expr_in_expr598)
                    l = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = l;



                elif alt15 == 3:
                    # SelectScript.g:303:4: c= compare_expr
                    pass 
                    self._state.following.append(self.FOLLOW_compare_expr_in_expr609)
                    c = self.compare_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = c;



                elif alt15 == 4:
                    # SelectScript.g:304:4: a= arithmetic_expr
                    pass 
                    self._state.following.append(self.FOLLOW_arithmetic_expr_in_expr619)
                    a = self.arithmetic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val = a;



                elif alt15 == 5:
                    # SelectScript.g:305:4: a= atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_expr629)
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
    # SelectScript.g:308:1: age returns [a] : ^( AGE (t= expr )? ) ;
    def age(self, ):

        a = None

        t = None


        a=self._val(0); 
        try:
            try:
                # SelectScript.g:309:25: ( ^( AGE (t= expr )? ) )
                # SelectScript.g:310:2: ^( AGE (t= expr )? )
                pass 
                self.match(self.input, AGE, self.FOLLOW_AGE_in_age651)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:310:8: (t= expr )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((FCT <= LA16_0 <= NEG) or LA16_0 == STMT_SELECT or LA16_0 == AND or (XOR <= LA16_0 <= OR) or LA16_0 == NOT or (IN <= LA16_0 <= POW) or LA16_0 == THIS or LA16_0 == 94) :
                        alt16 = 1
                    if alt16 == 1:
                        # SelectScript.g:310:9: t= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_age656)
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
    # SelectScript.g:313:1: assign_expr returns [stack] : ^( ASSIGN v= PHRASE e= expr (a= age )? ) ;
    def assign_expr(self, ):

        stack = None

        v = None
        e = None

        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:314:27: ( ^( ASSIGN v= PHRASE e= expr (a= age )? ) )
                # SelectScript.g:315:2: ^( ASSIGN v= PHRASE e= expr (a= age )? )
                pass 
                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr680)

                self.match(self.input, DOWN, None)
                v=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr684)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr688)
                e = self.expr()

                self._state.following.pop()
                # SelectScript.g:315:27: (a= age )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == AGE) :
                    alt17 = 1
                if alt17 == 1:
                    # SelectScript.g:315:28: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr693)
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
    # SelectScript.g:318:1: logic_expr returns [stack] : ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) );
    def logic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:318:28: ( ^( OR e1= expr e2= expr ) | ^( XOR e1= expr e2= expr ) | ^( AND e1= expr e2= expr ) | ^( NOT e= expr ) )
                alt18 = 4
                LA18 = self.input.LA(1)
                if LA18 == OR:
                    alt18 = 1
                elif LA18 == XOR:
                    alt18 = 2
                elif LA18 == AND:
                    alt18 = 3
                elif LA18 == NOT:
                    alt18 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # SelectScript.g:319:2: ^( OR e1= expr e2= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_logic_expr714)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr718)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr722)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('or',  [e1, e2]); 



                elif alt18 == 2:
                    # SelectScript.g:320:4: ^( XOR e1= expr e2= expr )
                    pass 
                    self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_expr731)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr735)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr739)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('xor', [e1, e2]); 



                elif alt18 == 3:
                    # SelectScript.g:321:4: ^( AND e1= expr e2= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_logic_expr748)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr752)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr756)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('and', [e1, e2]); 



                elif alt18 == 4:
                    # SelectScript.g:322:4: ^( NOT e= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_expr764)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_logic_expr768)
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
    # SelectScript.g:325:1: compare_expr returns [stack] : ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) );
    def compare_expr(self, ):

        stack = None

        e1 = None

        e2 = None


        try:
            try:
                # SelectScript.g:325:29: ( ^( IN e1= expr e2= expr ) | ^( EQ e1= expr e2= expr ) | ^( NE e1= expr e2= expr ) | ^( GE e1= expr e2= expr ) | ^( GT e1= expr e2= expr ) | ^( LE e1= expr e2= expr ) | ^( LT e1= expr e2= expr ) )
                alt19 = 7
                LA19 = self.input.LA(1)
                if LA19 == IN:
                    alt19 = 1
                elif LA19 == EQ:
                    alt19 = 2
                elif LA19 == NE:
                    alt19 = 3
                elif LA19 == GE:
                    alt19 = 4
                elif LA19 == GT:
                    alt19 = 5
                elif LA19 == LE:
                    alt19 = 6
                elif LA19 == LT:
                    alt19 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # SelectScript.g:326:2: ^( IN e1= expr e2= expr )
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_compare_expr787)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr791)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr795)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('in', [e2, e1]); 



                elif alt19 == 2:
                    # SelectScript.g:327:4: ^( EQ e1= expr e2= expr )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_expr804)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr808)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr812)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('eq', [e1, e2]); 



                elif alt19 == 3:
                    # SelectScript.g:328:4: ^( NE e1= expr e2= expr )
                    pass 
                    self.match(self.input, NE, self.FOLLOW_NE_in_compare_expr821)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr825)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr829)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ne', [e1, e2]); 



                elif alt19 == 4:
                    # SelectScript.g:329:4: ^( GE e1= expr e2= expr )
                    pass 
                    self.match(self.input, GE, self.FOLLOW_GE_in_compare_expr838)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr842)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr846)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('ge', [e1, e2]); 



                elif alt19 == 5:
                    # SelectScript.g:330:4: ^( GT e1= expr e2= expr )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_compare_expr855)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr859)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr863)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('gt', [e1, e2]); 



                elif alt19 == 6:
                    # SelectScript.g:331:4: ^( LE e1= expr e2= expr )
                    pass 
                    self.match(self.input, LE, self.FOLLOW_LE_in_compare_expr872)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr876)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr880)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('le', [e1, e2]); 



                elif alt19 == 7:
                    # SelectScript.g:332:4: ^( LT e1= expr e2= expr )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_compare_expr889)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr893)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_compare_expr897)
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
    # SelectScript.g:335:1: arithmetic_expr returns [stack] : ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) );
    def arithmetic_expr(self, ):

        stack = None

        e1 = None

        e2 = None

        e = None


        try:
            try:
                # SelectScript.g:335:32: ( ^( MUL e1= expr e2= expr ) | ^( DIV e1= expr e2= expr ) | ^( MOD e1= expr e2= expr ) | ^( SUB e1= expr e2= expr ) | ^( ADD e1= expr e2= expr ) | ^( POW e1= expr e2= expr ) | ^( NEG e= expr ) | ^( POS e= expr ) )
                alt20 = 8
                LA20 = self.input.LA(1)
                if LA20 == MUL:
                    alt20 = 1
                elif LA20 == DIV:
                    alt20 = 2
                elif LA20 == MOD:
                    alt20 = 3
                elif LA20 == SUB:
                    alt20 = 4
                elif LA20 == ADD:
                    alt20 = 5
                elif LA20 == POW:
                    alt20 = 6
                elif LA20 == NEG:
                    alt20 = 7
                elif LA20 == POS:
                    alt20 = 8
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # SelectScript.g:336:2: ^( MUL e1= expr e2= expr )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_expr915)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr919)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr923)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mul', [e1, e2]); 



                elif alt20 == 2:
                    # SelectScript.g:337:3: ^( DIV e1= expr e2= expr )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_expr931)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr935)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr939)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('div', [e1, e2]); 



                elif alt20 == 3:
                    # SelectScript.g:338:3: ^( MOD e1= expr e2= expr )
                    pass 
                    self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_expr947)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr951)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr955)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('mod', [e1, e2]); 



                elif alt20 == 4:
                    # SelectScript.g:339:3: ^( SUB e1= expr e2= expr )
                    pass 
                    self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_expr963)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr967)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr971)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('sub', [e1, e2]); 



                elif alt20 == 5:
                    # SelectScript.g:340:3: ^( ADD e1= expr e2= expr )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_expr979)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr983)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr987)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('add', [e1, e2]); 



                elif alt20 == 6:
                    # SelectScript.g:341:3: ^( POW e1= expr e2= expr )
                    pass 
                    self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_expr995)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr999)
                    e1 = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1003)
                    e2 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('pow', [e1, e2]); 



                elif alt20 == 7:
                    # SelectScript.g:342:3: ^( NEG e= expr )
                    pass 
                    self.match(self.input, NEG, self.FOLLOW_NEG_in_arithmetic_expr1011)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1015)
                    e = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        stack = self._fct('neg', [e]); 



                elif alt20 == 8:
                    # SelectScript.g:343:3: ^( POS e= expr )
                    pass 
                    self.match(self.input, POS, self.FOLLOW_POS_in_arithmetic_expr1024)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_arithmetic_expr1028)
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
    # SelectScript.g:346:1: atom returns [stack] : (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select );
    def atom(self, ):

        stack = None

        val = None

        var = None

        fct = None

        e = None

        s = None


        try:
            try:
                # SelectScript.g:346:22: (val= value | var= variable | fct= function | '(' e= expr ')' | s= statement_select )
                alt21 = 5
                LA21 = self.input.LA(1)
                if LA21 == VAL or LA21 == LIST or LA21 == THIS:
                    alt21 = 1
                elif LA21 == VAR:
                    alt21 = 2
                elif LA21 == FCT:
                    alt21 = 3
                elif LA21 == 94:
                    alt21 = 4
                elif LA21 == STMT_SELECT:
                    alt21 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # SelectScript.g:347:2: val= value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_atom1050)
                    val = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = val



                elif alt21 == 2:
                    # SelectScript.g:348:4: var= variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_atom1063)
                    var = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = var



                elif alt21 == 3:
                    # SelectScript.g:349:4: fct= function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_atom1075)
                    fct = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stack = fct



                elif alt21 == 4:
                    # SelectScript.g:350:4: '(' e= expr ')'
                    pass 
                    self.match(self.input, 94, self.FOLLOW_94_in_atom1083)
                    self._state.following.append(self.FOLLOW_expr_in_atom1087)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 95, self.FOLLOW_95_in_atom1089)
                    if self._state.backtracking == 0:
                        stack = e  



                elif alt21 == 5:
                    # SelectScript.g:351:4: s= statement_select
                    pass 
                    self._state.following.append(self.FOLLOW_statement_select_in_atom1099)
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
    # SelectScript.g:354:1: value returns [val] : ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ );
    def value(self, ):

        val = None

        STRING1 = None
        INTEGER2 = None
        FLOAT3 = None
        t = None

        l = None


        try:
            try:
                # SelectScript.g:354:21: ( ^( VAL STRING ) | ^( VAL INTEGER ) | ^( VAL FLOAT ) | ^( VAL TRUE ) | ^( VAL FALSE ) | t= this_ | l= list_ )
                alt22 = 7
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # SelectScript.g:355:4: ^( VAL STRING )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1119)

                    self.match(self.input, DOWN, None)
                    STRING1=self.match(self.input, STRING, self.FOLLOW_STRING_in_value1121)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( STRING1.getText()[1:-1] ); 



                elif alt22 == 2:
                    # SelectScript.g:356:4: ^( VAL INTEGER )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1131)

                    self.match(self.input, DOWN, None)
                    INTEGER2=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value1133)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( int(INTEGER2.getText()) ); 



                elif alt22 == 3:
                    # SelectScript.g:357:4: ^( VAL FLOAT )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1143)

                    self.match(self.input, DOWN, None)
                    FLOAT3=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value1145)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( float(FLOAT3.getText()) ); 



                elif alt22 == 4:
                    # SelectScript.g:358:4: ^( VAL TRUE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1155)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value1157)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( True  ); 



                elif alt22 == 5:
                    # SelectScript.g:359:4: ^( VAL FALSE )
                    pass 
                    self.match(self.input, VAL, self.FOLLOW_VAL_in_value1167)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value1169)

                    self.match(self.input, UP, None)
                    if self._state.backtracking == 0:
                        val= self._val( False ); 



                elif alt22 == 6:
                    # SelectScript.g:360:4: t= this_
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_value1180)
                    t = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        val=t; 



                elif alt22 == 7:
                    # SelectScript.g:361:4: l= list_
                    pass 
                    self._state.following.append(self.FOLLOW_list__in_value1190)
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
    # SelectScript.g:364:1: this_ returns [p] : ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        p = None

        PHRASE4 = None

        p=self._this(); 
        try:
            try:
                # SelectScript.g:365:26: ( ^( THIS ( PHRASE )? ) )
                # SelectScript.g:366:2: ^( THIS ( PHRASE )? )
                pass 
                self.match(self.input, THIS, self.FOLLOW_THIS_in_this_1212)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:366:9: ( PHRASE )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == PHRASE) :
                        alt23 = 1
                    if alt23 == 1:
                        # SelectScript.g:366:10: PHRASE
                        pass 
                        PHRASE4=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_1215)
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
    # SelectScript.g:369:1: list_ returns [l] : ^( LIST (e= expr )* ) ;
    def list_(self, ):

        l = None

        e = None


        l = [] 
        try:
            try:
                # SelectScript.g:370:17: ( ^( LIST (e= expr )* ) )
                # SelectScript.g:371:2: ^( LIST (e= expr )* )
                pass 
                self.match(self.input, LIST, self.FOLLOW_LIST_in_list_1239)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # SelectScript.g:371:9: (e= expr )*
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((FCT <= LA24_0 <= NEG) or LA24_0 == STMT_SELECT or LA24_0 == AND or (XOR <= LA24_0 <= OR) or LA24_0 == NOT or (IN <= LA24_0 <= POW) or LA24_0 == THIS or LA24_0 == 94) :
                            alt24 = 1


                        if alt24 == 1:
                            # SelectScript.g:371:11: e= expr
                            pass 
                            self._state.following.append(self.FOLLOW_expr_in_list_1245)
                            e = self.expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                l.append(e); 



                        else:
                            break #loop24

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return l

    # $ANTLR end "list_"


    # $ANTLR start "variable"
    # SelectScript.g:374:1: variable returns [var] : ^( VAR PHRASE (a= age )? ) ;
    def variable(self, ):

        var = None

        PHRASE5 = None
        a = None


        a = self._val(0); 
        try:
            try:
                # SelectScript.g:375:27: ( ^( VAR PHRASE (a= age )? ) )
                # SelectScript.g:376:2: ^( VAR PHRASE (a= age )? )
                pass 
                self.match(self.input, VAR, self.FOLLOW_VAR_in_variable1269)

                self.match(self.input, DOWN, None)
                PHRASE5=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable1271)
                # SelectScript.g:376:15: (a= age )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == AGE) :
                    alt25 = 1
                if alt25 == 1:
                    # SelectScript.g:376:16: a= age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable1276)
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
    # SelectScript.g:379:1: function returns [stack] : ^( FCT PHRASE (params= parameter )? ) ;
    def function(self, ):

        stack = None

        PHRASE6 = None
        params = None


        try:
            try:
                # SelectScript.g:379:26: ( ^( FCT PHRASE (params= parameter )? ) )
                # SelectScript.g:380:2: ^( FCT PHRASE (params= parameter )? )
                pass 
                self.match(self.input, FCT, self.FOLLOW_FCT_in_function1296)

                self.match(self.input, DOWN, None)
                PHRASE6=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function1298)
                # SelectScript.g:380:21: (params= parameter )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if ((FCT <= LA26_0 <= NEG) or LA26_0 == STMT_SELECT or LA26_0 == AND or (XOR <= LA26_0 <= OR) or LA26_0 == NOT or (IN <= LA26_0 <= POW) or LA26_0 == THIS or LA26_0 == 94) :
                    alt26 = 1
                elif (LA26_0 == 3) :
                    LA26_2 = self.input.LA(2)

                    if (self.synpred57_SelectScript()) :
                        alt26 = 1
                if alt26 == 1:
                    # SelectScript.g:0:0: params= parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function1302)
                    params = self.parameter()

                    self._state.following.pop()




                self.match(self.input, UP, None)
                if self._state.backtracking == 0:
                    stack = self._fct( PHRASE6.getText(), params); 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "function"


    # $ANTLR start "parameter"
    # SelectScript.g:384:1: parameter returns [stack] : (e= expr )* ;
    def parameter(self, ):

        stack = None

        e = None


        stack = []
        try:
            try:
                # SelectScript.g:385:19: ( (e= expr )* )
                # SelectScript.g:386:2: (e= expr )*
                pass 
                # SelectScript.g:386:2: (e= expr )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if ((FCT <= LA27_0 <= NEG) or LA27_0 == STMT_SELECT or LA27_0 == AND or (XOR <= LA27_0 <= OR) or LA27_0 == NOT or (IN <= LA27_0 <= POW) or LA27_0 == THIS or LA27_0 == 94) :
                        alt27 = 1


                    if alt27 == 1:
                        # SelectScript.g:386:3: e= expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_parameter1328)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stack.append(e)



                    else:
                        break #loop27




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return stack

    # $ANTLR end "parameter"

    # $ANTLR start "synpred2_SelectScript"
    def synpred2_SelectScript_fragment(self, ):
        # SelectScript.g:231:2: (s= statement_select )
        # SelectScript.g:231:2: s= statement_select
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectScript117)
        s = self.statement_select()

        self._state.following.pop()


    # $ANTLR end "synpred2_SelectScript"



    # $ANTLR start "synpred15_SelectScript"
    def synpred15_SelectScript_fragment(self, ):
        # SelectScript.g:263:20: (p= parameter )
        # SelectScript.g:263:20: p= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred15_SelectScript372)
        p = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred15_SelectScript"



    # $ANTLR start "synpred57_SelectScript"
    def synpred57_SelectScript_fragment(self, ):
        # SelectScript.g:380:21: (params= parameter )
        # SelectScript.g:380:21: params= parameter
        pass 
        self._state.following.append(self.FOLLOW_parameter_in_synpred57_SelectScript1302)
        params = self.parameter()

        self._state.following.pop()


    # $ANTLR end "synpred57_SelectScript"




    # Delegated rules

    def synpred57_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred57_SelectScript_fragment()
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

    def synpred15_SelectScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_SelectScript_fragment()
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
        u"\1\136\1\0\33\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\31\uffff\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\33\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\6\2\1\uffff\1\1\7\uffff\1\2\3\uffff\2\2\1\uffff\1\2"
        u"\1\uffff\16\2\34\uffff\1\2\27\uffff\1\2"),
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
    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\6\1\2\2\uffff\1\121\5\uffff"
        )

    DFA22_max = DFA.unpack(
        u"\1\106\1\2\2\uffff\1\126\5\uffff"
        )

    DFA22_accept = DFA.unpack(
        u"\2\uffff\1\6\1\7\1\uffff\1\1\1\2\1\3\1\4\1\5"
        )

    DFA22_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA22_transition = [
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

    # class definition for DFA #22

    class DFA22(DFA):
        pass


 

    FOLLOW_prog_in_eval74 = frozenset([1])
    FOLLOW_statement_in_prog96 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_statement_select_in_statement117 = frozenset([1])
    FOLLOW_expr_in_statement127 = frozenset([1])
    FOLLOW_STMT_SELECT_in_statement_select156 = frozenset([2])
    FOLLOW_select__in_statement_select160 = frozenset([55])
    FOLLOW_from__in_statement_select164 = frozenset([3, 58, 59, 63, 69])
    FOLLOW_where__in_statement_select170 = frozenset([3, 59, 63, 69])
    FOLLOW_group__in_statement_select179 = frozenset([3, 59, 65, 69])
    FOLLOW_having__in_statement_select184 = frozenset([3, 59, 69])
    FOLLOW_order__in_statement_select194 = frozenset([3, 69])
    FOLLOW_as__in_statement_select203 = frozenset([3])
    FOLLOW_SELECT_in_select_227 = frozenset([2])
    FOLLOW_PHRASE_in_select_238 = frozenset([3, 4, 70, 89])
    FOLLOW_function_in_select_250 = frozenset([3, 4, 70, 89])
    FOLLOW_this__in_select_262 = frozenset([3, 4, 70, 89])
    FOLLOW_FROM_in_from_291 = frozenset([2])
    FOLLOW_expr_in_from_296 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_AS_in_as_320 = frozenset([2])
    FOLLOW_AS_DICT_in_as_322 = frozenset([3])
    FOLLOW_AS_in_as_334 = frozenset([2])
    FOLLOW_AS_LIST_in_as_336 = frozenset([3])
    FOLLOW_AS_in_as_348 = frozenset([2])
    FOLLOW_AS_VALUE_in_as_350 = frozenset([3])
    FOLLOW_AS_in_as_362 = frozenset([2])
    FOLLOW_PHRASE_in_as_366 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_parameter_in_as_372 = frozenset([3])
    FOLLOW_WHERE_in_where_395 = frozenset([2])
    FOLLOW_expr_in_where_399 = frozenset([3])
    FOLLOW_GROUP_in_group_422 = frozenset([2])
    FOLLOW_PHRASE_in_group_431 = frozenset([3, 4, 89])
    FOLLOW_function_in_group_442 = frozenset([3, 4, 89])
    FOLLOW_HAVING_in_having_467 = frozenset([2])
    FOLLOW_expr_in_having_471 = frozenset([3])
    FOLLOW_ORDER_in_order_494 = frozenset([2])
    FOLLOW_PHRASE_in_order_508 = frozenset([3, 4, 89])
    FOLLOW_function_in_order_520 = frozenset([3, 4, 72, 73, 89])
    FOLLOW_direction__in_order_524 = frozenset([3, 4, 89])
    FOLLOW_ASC_in_direction_554 = frozenset([1])
    FOLLOW_DESC_in_direction_562 = frozenset([1])
    FOLLOW_assign_expr_in_expr586 = frozenset([1])
    FOLLOW_logic_expr_in_expr598 = frozenset([1])
    FOLLOW_compare_expr_in_expr609 = frozenset([1])
    FOLLOW_arithmetic_expr_in_expr619 = frozenset([1])
    FOLLOW_atom_in_expr629 = frozenset([1])
    FOLLOW_AGE_in_age651 = frozenset([2])
    FOLLOW_expr_in_age656 = frozenset([3])
    FOLLOW_ASSIGN_in_assign_expr680 = frozenset([2])
    FOLLOW_PHRASE_in_assign_expr684 = frozenset([3, 4, 5, 6, 7, 8, 9, 10, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_assign_expr688 = frozenset([3, 10])
    FOLLOW_age_in_assign_expr693 = frozenset([3])
    FOLLOW_OR_in_logic_expr714 = frozenset([2])
    FOLLOW_expr_in_logic_expr718 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_logic_expr722 = frozenset([3])
    FOLLOW_XOR_in_logic_expr731 = frozenset([2])
    FOLLOW_expr_in_logic_expr735 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_logic_expr739 = frozenset([3])
    FOLLOW_AND_in_logic_expr748 = frozenset([2])
    FOLLOW_expr_in_logic_expr752 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_logic_expr756 = frozenset([3])
    FOLLOW_NOT_in_logic_expr764 = frozenset([2])
    FOLLOW_expr_in_logic_expr768 = frozenset([3])
    FOLLOW_IN_in_compare_expr787 = frozenset([2])
    FOLLOW_expr_in_compare_expr791 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr795 = frozenset([3])
    FOLLOW_EQ_in_compare_expr804 = frozenset([2])
    FOLLOW_expr_in_compare_expr808 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr812 = frozenset([3])
    FOLLOW_NE_in_compare_expr821 = frozenset([2])
    FOLLOW_expr_in_compare_expr825 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr829 = frozenset([3])
    FOLLOW_GE_in_compare_expr838 = frozenset([2])
    FOLLOW_expr_in_compare_expr842 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr846 = frozenset([3])
    FOLLOW_GT_in_compare_expr855 = frozenset([2])
    FOLLOW_expr_in_compare_expr859 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr863 = frozenset([3])
    FOLLOW_LE_in_compare_expr872 = frozenset([2])
    FOLLOW_expr_in_compare_expr876 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr880 = frozenset([3])
    FOLLOW_LT_in_compare_expr889 = frozenset([2])
    FOLLOW_expr_in_compare_expr893 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_compare_expr897 = frozenset([3])
    FOLLOW_MUL_in_arithmetic_expr915 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr919 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr923 = frozenset([3])
    FOLLOW_DIV_in_arithmetic_expr931 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr935 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr939 = frozenset([3])
    FOLLOW_MOD_in_arithmetic_expr947 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr951 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr955 = frozenset([3])
    FOLLOW_SUB_in_arithmetic_expr963 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr967 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr971 = frozenset([3])
    FOLLOW_ADD_in_arithmetic_expr979 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr983 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr987 = frozenset([3])
    FOLLOW_POW_in_arithmetic_expr995 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr999 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_expr_in_arithmetic_expr1003 = frozenset([3])
    FOLLOW_NEG_in_arithmetic_expr1011 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1015 = frozenset([3])
    FOLLOW_POS_in_arithmetic_expr1024 = frozenset([2])
    FOLLOW_expr_in_arithmetic_expr1028 = frozenset([3])
    FOLLOW_value_in_atom1050 = frozenset([1])
    FOLLOW_variable_in_atom1063 = frozenset([1])
    FOLLOW_function_in_atom1075 = frozenset([1])
    FOLLOW_94_in_atom1083 = frozenset([4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94, 95])
    FOLLOW_expr_in_atom1087 = frozenset([95])
    FOLLOW_95_in_atom1089 = frozenset([1])
    FOLLOW_statement_select_in_atom1099 = frozenset([1])
    FOLLOW_VAL_in_value1119 = frozenset([2])
    FOLLOW_STRING_in_value1121 = frozenset([3])
    FOLLOW_VAL_in_value1131 = frozenset([2])
    FOLLOW_INTEGER_in_value1133 = frozenset([3])
    FOLLOW_VAL_in_value1143 = frozenset([2])
    FOLLOW_FLOAT_in_value1145 = frozenset([3])
    FOLLOW_VAL_in_value1155 = frozenset([2])
    FOLLOW_TRUE_in_value1157 = frozenset([3])
    FOLLOW_VAL_in_value1167 = frozenset([2])
    FOLLOW_FALSE_in_value1169 = frozenset([3])
    FOLLOW_this__in_value1180 = frozenset([1])
    FOLLOW_list__in_value1190 = frozenset([1])
    FOLLOW_THIS_in_this_1212 = frozenset([2])
    FOLLOW_PHRASE_in_this_1215 = frozenset([3])
    FOLLOW_LIST_in_list_1239 = frozenset([2])
    FOLLOW_expr_in_list_1245 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_VAR_in_variable1269 = frozenset([2])
    FOLLOW_PHRASE_in_variable1271 = frozenset([3, 10])
    FOLLOW_age_in_variable1276 = frozenset([3])
    FOLLOW_FCT_in_function1296 = frozenset([2])
    FOLLOW_PHRASE_in_function1298 = frozenset([3, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_parameter_in_function1302 = frozenset([3])
    FOLLOW_expr_in_parameter1328 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 70, 94])
    FOLLOW_statement_select_in_synpred2_SelectScript117 = frozenset([1])
    FOLLOW_parameter_in_synpred15_SelectScript372 = frozenset([1])
    FOLLOW_parameter_in_synpred57_SelectScript1302 = frozenset([1])



       
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
			scene.prettyPrint(code)
			expr = ""


if __name__ == '__main__':
    main(sys.argv)
