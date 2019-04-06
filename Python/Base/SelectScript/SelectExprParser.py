# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2015-08-10 19:05:45

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

        
import antlr3
import antlr3.tree
from SelectExprLexer import SelectExprLexer



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




class SelectExprParser(Parser):
    grammarFileName = "SelectExpr.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SelectExprParser, self).__init__(input, state, *args, **kwargs)

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

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class eval_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.eval_return, self).__init__()

            self.tree = None




    # $ANTLR start "eval"
    # SelectExpr.g:145:1: eval : prog ;
    def eval(self, ):

        retval = self.eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prog1 = None



        try:
            try:
                # SelectExpr.g:145:6: ( prog )
                # SelectExpr.g:145:8: prog
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_prog_in_eval1501)
                prog1 = self.prog()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, prog1.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "eval"

    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.prog_return, self).__init__()

            self.tree = None




    # $ANTLR start "prog"
    # SelectExpr.g:148:1: prog : ( statement )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None



        try:
            try:
                # SelectExpr.g:148:6: ( ( statement )+ )
                # SelectExpr.g:148:8: ( statement )+
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:148:8: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == END or LA1_0 == NOT or (ADD <= LA1_0 <= SUB) or LA1_0 == IF or LA1_0 == LIST_BEGIN or LA1_0 == SELECT or LA1_0 == THIS or LA1_0 == STRING or (INTEGER <= LA1_0 <= FALSE) or LA1_0 == PHRASE or LA1_0 == 108) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectExpr.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_prog1511)
                        statement2 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement2.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prog"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # SelectExpr.g:151:1: statement : ( statement_select END | expr END | END );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        END4 = None
        END6 = None
        END7 = None
        statement_select3 = None

        expr5 = None


        END4_tree = None
        END6_tree = None
        END7_tree = None

        try:
            try:
                # SelectExpr.g:151:11: ( statement_select END | expr END | END )
                alt2 = 3
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectExpr.g:151:13: statement_select END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_statement1521)
                    statement_select3 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select3.tree)
                    END4=self.match(self.input, END, self.FOLLOW_END_in_statement1523)


                elif alt2 == 2:
                    # SelectExpr.g:152:4: expr END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_statement1529)
                    expr5 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr5.tree)
                    END6=self.match(self.input, END, self.FOLLOW_END_in_statement1531)


                elif alt2 == 3:
                    # SelectExpr.g:153:4: END
                    pass 
                    root_0 = self._adaptor.nil()

                    END7=self.match(self.input, END, self.FOLLOW_END_in_statement1537)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "statement"

    class statement_select_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.statement_select_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement_select"
    # SelectExpr.g:156:1: statement_select : select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) ;
    def statement_select(self, ):

        retval = self.statement_select_return()
        retval.start = self.input.LT(1)

        root_0 = None

        select_8 = None

        from_9 = None

        where_10 = None

        start_11 = None

        connect_12 = None

        stop_13 = None

        group_14 = None

        having_15 = None

        order_16 = None

        as_17 = None


        stream_start_ = RewriteRuleSubtreeStream(self._adaptor, "rule start_")
        stream_where_ = RewriteRuleSubtreeStream(self._adaptor, "rule where_")
        stream_select_ = RewriteRuleSubtreeStream(self._adaptor, "rule select_")
        stream_having_ = RewriteRuleSubtreeStream(self._adaptor, "rule having_")
        stream_from_ = RewriteRuleSubtreeStream(self._adaptor, "rule from_")
        stream_stop_ = RewriteRuleSubtreeStream(self._adaptor, "rule stop_")
        stream_as_ = RewriteRuleSubtreeStream(self._adaptor, "rule as_")
        stream_group_ = RewriteRuleSubtreeStream(self._adaptor, "rule group_")
        stream_order_ = RewriteRuleSubtreeStream(self._adaptor, "rule order_")
        stream_connect_ = RewriteRuleSubtreeStream(self._adaptor, "rule connect_")
        try:
            try:
                # SelectExpr.g:156:18: ( select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) )
                # SelectExpr.g:157:2: select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )?
                pass 
                self._state.following.append(self.FOLLOW_select__in_statement_select1548)
                select_8 = self.select_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_select_.add(select_8.tree)
                self._state.following.append(self.FOLLOW_from__in_statement_select1550)
                from_9 = self.from_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_from_.add(from_9.tree)
                # SelectExpr.g:157:16: ( where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    LA3_1 = self.input.LA(2)

                    if (self.synpred4_SelectExpr()) :
                        alt3 = 1
                if alt3 == 1:
                    # SelectExpr.g:157:17: where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select1553)
                    where_10 = self.where_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where_.add(where_10.tree)



                # SelectExpr.g:157:26: ( ( start_ )? connect_ stop_ )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == START) :
                    LA5_1 = self.input.LA(2)

                    if (self.synpred6_SelectExpr()) :
                        alt5 = 1
                elif (LA5_0 == CONNECT) :
                    LA5_2 = self.input.LA(2)

                    if (self.synpred6_SelectExpr()) :
                        alt5 = 1
                if alt5 == 1:
                    # SelectExpr.g:157:27: ( start_ )? connect_ stop_
                    pass 
                    # SelectExpr.g:157:27: ( start_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == START) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectExpr.g:157:28: start_
                        pass 
                        self._state.following.append(self.FOLLOW_start__in_statement_select1559)
                        start_11 = self.start_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_start_.add(start_11.tree)



                    self._state.following.append(self.FOLLOW_connect__in_statement_select1563)
                    connect_12 = self.connect_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_connect_.add(connect_12.tree)
                    self._state.following.append(self.FOLLOW_stop__in_statement_select1565)
                    stop_13 = self.stop_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_stop_.add(stop_13.tree)



                # SelectExpr.g:157:54: ( group_ ( having_ )? )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == GROUP) :
                    LA7_1 = self.input.LA(2)

                    if (self.synpred8_SelectExpr()) :
                        alt7 = 1
                if alt7 == 1:
                    # SelectExpr.g:157:55: group_ ( having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select1570)
                    group_14 = self.group_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_group_.add(group_14.tree)
                    # SelectExpr.g:157:62: ( having_ )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == HAVING) :
                        alt6 = 1
                    if alt6 == 1:
                        # SelectExpr.g:157:63: having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select1573)
                        having_15 = self.having_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_having_.add(having_15.tree)






                # SelectExpr.g:157:75: ( order_ )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ORDER) :
                    LA8_1 = self.input.LA(2)

                    if (self.synpred9_SelectExpr()) :
                        alt8 = 1
                if alt8 == 1:
                    # SelectExpr.g:157:76: order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select1580)
                    order_16 = self.order_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_order_.add(order_16.tree)



                # SelectExpr.g:157:85: ( as_ )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == AS) :
                    LA9_1 = self.input.LA(2)

                    if (self.synpred10_SelectExpr()) :
                        alt9 = 1
                if alt9 == 1:
                    # SelectExpr.g:157:86: as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select1585)
                    as_17 = self.as_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_as_.add(as_17.tree)




                # AST Rewrite
                # elements: as_, having_, connect_, stop_, where_, start_, group_, select_, order_, from_
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 157:92: -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    # SelectExpr.g:157:96: ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STMT_SELECT, "STMT_SELECT"), root_1)

                    self._adaptor.addChild(root_1, stream_select_.nextTree())
                    self._adaptor.addChild(root_1, stream_from_.nextTree())
                    # SelectExpr.g:157:124: ( where_ )?
                    if stream_where_.hasNext():
                        self._adaptor.addChild(root_1, stream_where_.nextTree())


                    stream_where_.reset();
                    # SelectExpr.g:157:134: ( group_ ( having_ )? )?
                    if stream_having_.hasNext() or stream_group_.hasNext():
                        self._adaptor.addChild(root_1, stream_group_.nextTree())
                        # SelectExpr.g:157:142: ( having_ )?
                        if stream_having_.hasNext():
                            self._adaptor.addChild(root_1, stream_having_.nextTree())


                        stream_having_.reset();


                    stream_having_.reset();
                    stream_group_.reset();
                    # SelectExpr.g:157:155: ( order_ )?
                    if stream_order_.hasNext():
                        self._adaptor.addChild(root_1, stream_order_.nextTree())


                    stream_order_.reset();
                    # SelectExpr.g:157:165: ( as_ )?
                    if stream_as_.hasNext():
                        self._adaptor.addChild(root_1, stream_as_.nextTree())


                    stream_as_.reset();
                    # SelectExpr.g:157:172: ( ( start_ )? connect_ stop_ )?
                    if stream_connect_.hasNext() or stream_stop_.hasNext() or stream_start_.hasNext():
                        # SelectExpr.g:157:173: ( start_ )?
                        if stream_start_.hasNext():
                            self._adaptor.addChild(root_1, stream_start_.nextTree())


                        stream_start_.reset();
                        self._adaptor.addChild(root_1, stream_connect_.nextTree())
                        self._adaptor.addChild(root_1, stream_stop_.nextTree())


                    stream_connect_.reset();
                    stream_stop_.reset();
                    stream_start_.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "statement_select"

    class select__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.select__return, self).__init__()

            self.tree = None




    # $ANTLR start "select_"
    # SelectExpr.g:160:1: select_ : SELECT ( MUL | ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* ) ) ;
    def select_(self, ):

        retval = self.select__return()
        retval.start = self.input.LT(1)

        root_0 = None

        SELECT18 = None
        MUL19 = None
        PHRASE20 = None
        SEP24 = None
        PHRASE25 = None
        function21 = None

        this_22 = None

        expr23 = None

        function26 = None

        this_27 = None

        expr28 = None


        SELECT18_tree = None
        MUL19_tree = None
        PHRASE20_tree = None
        SEP24_tree = None
        PHRASE25_tree = None

        try:
            try:
                # SelectExpr.g:160:9: ( SELECT ( MUL | ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* ) ) )
                # SelectExpr.g:160:11: SELECT ( MUL | ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* ) )
                pass 
                root_0 = self._adaptor.nil()

                SELECT18=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_1644)
                if self._state.backtracking == 0:

                    SELECT18_tree = self._adaptor.createWithPayload(SELECT18)
                    root_0 = self._adaptor.becomeRoot(SELECT18_tree, root_0)

                # SelectExpr.g:160:19: ( MUL | ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == MUL) :
                    alt13 = 1
                elif (LA13_0 == NOT or (ADD <= LA13_0 <= SUB) or LA13_0 == IF or LA13_0 == LIST_BEGIN or LA13_0 == SELECT or LA13_0 == THIS or LA13_0 == STRING or (INTEGER <= LA13_0 <= FALSE) or LA13_0 == PHRASE or LA13_0 == 108) :
                    alt13 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # SelectExpr.g:160:20: MUL
                    pass 
                    MUL19=self.match(self.input, MUL, self.FOLLOW_MUL_in_select_1648)


                elif alt13 == 2:
                    # SelectExpr.g:160:27: ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* )
                    pass 
                    # SelectExpr.g:160:27: ( ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )* )
                    # SelectExpr.g:160:28: ( PHRASE | function | this_ | expr ) ( SEP ( PHRASE | function | this_ | expr ) )*
                    pass 
                    # SelectExpr.g:160:28: ( PHRASE | function | this_ | expr )
                    alt10 = 4
                    LA10 = self.input.LA(1)
                    if LA10 == PHRASE:
                        LA10_1 = self.input.LA(2)

                        if (LA10_1 == 108) :
                            alt10 = 2
                        elif (LA10_1 == DOT) :
                            alt10 = 3
                        elif (self.synpred12_SelectExpr()) :
                            alt10 = 1
                        elif (True) :
                            alt10 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 10, 1, self.input)

                            raise nvae

                    elif LA10 == THIS:
                        LA10_2 = self.input.LA(2)

                        if (self.synpred14_SelectExpr()) :
                            alt10 = 3
                        elif (True) :
                            alt10 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 10, 2, self.input)

                            raise nvae

                    elif LA10 == NOT or LA10 == ADD or LA10 == SUB or LA10 == IF or LA10 == LIST_BEGIN or LA10 == SELECT or LA10 == STRING or LA10 == INTEGER or LA10 == FLOAT or LA10 == TRUE or LA10 == FALSE or LA10 == 108:
                        alt10 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 10, 0, self.input)

                        raise nvae

                    if alt10 == 1:
                        # SelectExpr.g:160:29: PHRASE
                        pass 
                        PHRASE20=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1655)
                        if self._state.backtracking == 0:

                            PHRASE20_tree = self._adaptor.createWithPayload(PHRASE20)
                            self._adaptor.addChild(root_0, PHRASE20_tree)



                    elif alt10 == 2:
                        # SelectExpr.g:160:38: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_select_1659)
                        function21 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, function21.tree)


                    elif alt10 == 3:
                        # SelectExpr.g:160:49: this_
                        pass 
                        self._state.following.append(self.FOLLOW_this__in_select_1663)
                        this_22 = self.this_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, this_22.tree)


                    elif alt10 == 4:
                        # SelectExpr.g:160:57: expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_select_1667)
                        expr23 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr23.tree)



                    # SelectExpr.g:160:63: ( SEP ( PHRASE | function | this_ | expr ) )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == SEP) :
                            alt12 = 1


                        if alt12 == 1:
                            # SelectExpr.g:160:64: SEP ( PHRASE | function | this_ | expr )
                            pass 
                            SEP24=self.match(self.input, SEP, self.FOLLOW_SEP_in_select_1671)
                            # SelectExpr.g:160:69: ( PHRASE | function | this_ | expr )
                            alt11 = 4
                            LA11 = self.input.LA(1)
                            if LA11 == PHRASE:
                                LA11_1 = self.input.LA(2)

                                if (LA11_1 == 108) :
                                    alt11 = 2
                                elif (LA11_1 == DOT) :
                                    alt11 = 3
                                elif (self.synpred15_SelectExpr()) :
                                    alt11 = 1
                                elif (True) :
                                    alt11 = 4
                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    nvae = NoViableAltException("", 11, 1, self.input)

                                    raise nvae

                            elif LA11 == THIS:
                                LA11_2 = self.input.LA(2)

                                if (self.synpred17_SelectExpr()) :
                                    alt11 = 3
                                elif (True) :
                                    alt11 = 4
                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    nvae = NoViableAltException("", 11, 2, self.input)

                                    raise nvae

                            elif LA11 == NOT or LA11 == ADD or LA11 == SUB or LA11 == IF or LA11 == LIST_BEGIN or LA11 == SELECT or LA11 == STRING or LA11 == INTEGER or LA11 == FLOAT or LA11 == TRUE or LA11 == FALSE or LA11 == 108:
                                alt11 = 4
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 11, 0, self.input)

                                raise nvae

                            if alt11 == 1:
                                # SelectExpr.g:160:70: PHRASE
                                pass 
                                PHRASE25=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1675)
                                if self._state.backtracking == 0:

                                    PHRASE25_tree = self._adaptor.createWithPayload(PHRASE25)
                                    self._adaptor.addChild(root_0, PHRASE25_tree)



                            elif alt11 == 2:
                                # SelectExpr.g:160:79: function
                                pass 
                                self._state.following.append(self.FOLLOW_function_in_select_1679)
                                function26 = self.function()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, function26.tree)


                            elif alt11 == 3:
                                # SelectExpr.g:160:90: this_
                                pass 
                                self._state.following.append(self.FOLLOW_this__in_select_1683)
                                this_27 = self.this_()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, this_27.tree)


                            elif alt11 == 4:
                                # SelectExpr.g:160:98: expr
                                pass 
                                self._state.following.append(self.FOLLOW_expr_in_select_1687)
                                expr28 = self.expr()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, expr28.tree)





                        else:
                            break #loop12









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "select_"

    class from__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.from__return, self).__init__()

            self.tree = None




    # $ANTLR start "from_"
    # SelectExpr.g:163:1: from_ : FROM expr ( SEP expr )* ;
    def from_(self, ):

        retval = self.from__return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROM29 = None
        SEP31 = None
        expr30 = None

        expr32 = None


        FROM29_tree = None
        SEP31_tree = None

        try:
            try:
                # SelectExpr.g:163:7: ( FROM expr ( SEP expr )* )
                # SelectExpr.g:163:9: FROM expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                FROM29=self.match(self.input, FROM, self.FOLLOW_FROM_in_from_1703)
                if self._state.backtracking == 0:

                    FROM29_tree = self._adaptor.createWithPayload(FROM29)
                    root_0 = self._adaptor.becomeRoot(FROM29_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_from_1706)
                expr30 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr30.tree)
                # SelectExpr.g:163:20: ( SEP expr )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == SEP) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred19_SelectExpr()) :
                            alt14 = 1




                    if alt14 == 1:
                        # SelectExpr.g:163:21: SEP expr
                        pass 
                        SEP31=self.match(self.input, SEP, self.FOLLOW_SEP_in_from_1709)
                        self._state.following.append(self.FOLLOW_expr_in_from_1712)
                        expr32 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr32.tree)


                    else:
                        break #loop14



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "from_"

    class where__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.where__return, self).__init__()

            self.tree = None




    # $ANTLR start "where_"
    # SelectExpr.g:166:1: where_ : WHERE expr ;
    def where_(self, ):

        retval = self.where__return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHERE33 = None
        expr34 = None


        WHERE33_tree = None

        try:
            try:
                # SelectExpr.g:166:8: ( WHERE expr )
                # SelectExpr.g:166:10: WHERE expr
                pass 
                root_0 = self._adaptor.nil()

                WHERE33=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_1723)
                if self._state.backtracking == 0:

                    WHERE33_tree = self._adaptor.createWithPayload(WHERE33)
                    root_0 = self._adaptor.becomeRoot(WHERE33_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_where_1726)
                expr34 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr34.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "where_"

    class start__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.start__return, self).__init__()

            self.tree = None




    # $ANTLR start "start_"
    # SelectExpr.g:169:1: start_ : START WITH expr ( SEP expr )* ;
    def start_(self, ):

        retval = self.start__return()
        retval.start = self.input.LT(1)

        root_0 = None

        START35 = None
        WITH36 = None
        SEP38 = None
        expr37 = None

        expr39 = None


        START35_tree = None
        WITH36_tree = None
        SEP38_tree = None

        try:
            try:
                # SelectExpr.g:169:8: ( START WITH expr ( SEP expr )* )
                # SelectExpr.g:169:10: START WITH expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                START35=self.match(self.input, START, self.FOLLOW_START_in_start_1735)
                if self._state.backtracking == 0:

                    START35_tree = self._adaptor.createWithPayload(START35)
                    root_0 = self._adaptor.becomeRoot(START35_tree, root_0)

                WITH36=self.match(self.input, WITH, self.FOLLOW_WITH_in_start_1738)
                self._state.following.append(self.FOLLOW_expr_in_start_1741)
                expr37 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr37.tree)
                # SelectExpr.g:169:28: ( SEP expr )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SEP) :
                        alt15 = 1


                    if alt15 == 1:
                        # SelectExpr.g:169:29: SEP expr
                        pass 
                        SEP38=self.match(self.input, SEP, self.FOLLOW_SEP_in_start_1744)
                        self._state.following.append(self.FOLLOW_expr_in_start_1747)
                        expr39 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr39.tree)


                    else:
                        break #loop15



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "start_"

    class connect__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.connect__return, self).__init__()

            self.tree = None




    # $ANTLR start "connect_"
    # SelectExpr.g:172:1: connect_ : CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE ( INTEGER )? )? ( MAXIMUM INTEGER )? expr ( SEP expr )* ;
    def connect_(self, ):

        retval = self.connect__return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONNECT40 = None
        BY41 = None
        NO42 = None
        CYCLE43 = None
        UNIQUE44 = None
        MEMORIZE45 = None
        INTEGER46 = None
        MAXIMUM47 = None
        INTEGER48 = None
        SEP50 = None
        expr49 = None

        expr51 = None


        CONNECT40_tree = None
        BY41_tree = None
        NO42_tree = None
        CYCLE43_tree = None
        UNIQUE44_tree = None
        MEMORIZE45_tree = None
        INTEGER46_tree = None
        MAXIMUM47_tree = None
        INTEGER48_tree = None
        SEP50_tree = None

        try:
            try:
                # SelectExpr.g:172:10: ( CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE ( INTEGER )? )? ( MAXIMUM INTEGER )? expr ( SEP expr )* )
                # SelectExpr.g:172:12: CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE ( INTEGER )? )? ( MAXIMUM INTEGER )? expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                CONNECT40=self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_1758)
                if self._state.backtracking == 0:

                    CONNECT40_tree = self._adaptor.createWithPayload(CONNECT40)
                    root_0 = self._adaptor.becomeRoot(CONNECT40_tree, root_0)

                BY41=self.match(self.input, BY, self.FOLLOW_BY_in_connect_1761)
                # SelectExpr.g:172:25: ( NO CYCLE )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == NO) :
                    alt16 = 1
                if alt16 == 1:
                    # SelectExpr.g:172:26: NO CYCLE
                    pass 
                    NO42=self.match(self.input, NO, self.FOLLOW_NO_in_connect_1765)
                    CYCLE43=self.match(self.input, CYCLE, self.FOLLOW_CYCLE_in_connect_1768)
                    if self._state.backtracking == 0:

                        CYCLE43_tree = self._adaptor.createWithPayload(CYCLE43)
                        self._adaptor.addChild(root_0, CYCLE43_tree)




                # SelectExpr.g:172:38: ( UNIQUE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == UNIQUE) :
                    alt17 = 1
                if alt17 == 1:
                    # SelectExpr.g:172:39: UNIQUE
                    pass 
                    UNIQUE44=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_connect_1773)
                    if self._state.backtracking == 0:

                        UNIQUE44_tree = self._adaptor.createWithPayload(UNIQUE44)
                        self._adaptor.addChild(root_0, UNIQUE44_tree)




                # SelectExpr.g:172:48: ( MEMORIZE ( INTEGER )? )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MEMORIZE) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectExpr.g:172:49: MEMORIZE ( INTEGER )?
                    pass 
                    MEMORIZE45=self.match(self.input, MEMORIZE, self.FOLLOW_MEMORIZE_in_connect_1778)
                    if self._state.backtracking == 0:

                        MEMORIZE45_tree = self._adaptor.createWithPayload(MEMORIZE45)
                        self._adaptor.addChild(root_0, MEMORIZE45_tree)

                    # SelectExpr.g:172:58: ( INTEGER )?
                    alt18 = 2
                    alt18 = self.dfa18.predict(self.input)
                    if alt18 == 1:
                        # SelectExpr.g:172:59: INTEGER
                        pass 
                        INTEGER46=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1781)
                        if self._state.backtracking == 0:

                            INTEGER46_tree = self._adaptor.createWithPayload(INTEGER46)
                            self._adaptor.addChild(root_0, INTEGER46_tree)







                # SelectExpr.g:172:71: ( MAXIMUM INTEGER )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == MAXIMUM) :
                    alt20 = 1
                if alt20 == 1:
                    # SelectExpr.g:172:72: MAXIMUM INTEGER
                    pass 
                    MAXIMUM47=self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_connect_1788)
                    if self._state.backtracking == 0:

                        MAXIMUM47_tree = self._adaptor.createWithPayload(MAXIMUM47)
                        self._adaptor.addChild(root_0, MAXIMUM47_tree)

                    INTEGER48=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1790)
                    if self._state.backtracking == 0:

                        INTEGER48_tree = self._adaptor.createWithPayload(INTEGER48)
                        self._adaptor.addChild(root_0, INTEGER48_tree)




                self._state.following.append(self.FOLLOW_expr_in_connect_1794)
                expr49 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr49.tree)
                # SelectExpr.g:172:95: ( SEP expr )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == SEP) :
                        alt21 = 1


                    if alt21 == 1:
                        # SelectExpr.g:172:96: SEP expr
                        pass 
                        SEP50=self.match(self.input, SEP, self.FOLLOW_SEP_in_connect_1797)
                        self._state.following.append(self.FOLLOW_expr_in_connect_1800)
                        expr51 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr51.tree)


                    else:
                        break #loop21



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "connect_"

    class stop__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.stop__return, self).__init__()

            self.tree = None




    # $ANTLR start "stop_"
    # SelectExpr.g:175:1: stop_ : STOP WITH expr ;
    def stop_(self, ):

        retval = self.stop__return()
        retval.start = self.input.LT(1)

        root_0 = None

        STOP52 = None
        WITH53 = None
        expr54 = None


        STOP52_tree = None
        WITH53_tree = None

        try:
            try:
                # SelectExpr.g:175:7: ( STOP WITH expr )
                # SelectExpr.g:175:9: STOP WITH expr
                pass 
                root_0 = self._adaptor.nil()

                STOP52=self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_1811)
                if self._state.backtracking == 0:

                    STOP52_tree = self._adaptor.createWithPayload(STOP52)
                    root_0 = self._adaptor.becomeRoot(STOP52_tree, root_0)

                WITH53=self.match(self.input, WITH, self.FOLLOW_WITH_in_stop_1814)
                self._state.following.append(self.FOLLOW_expr_in_stop_1817)
                expr54 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr54.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "stop_"

    class group__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.group__return, self).__init__()

            self.tree = None




    # $ANTLR start "group_"
    # SelectExpr.g:178:1: group_ : GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* ;
    def group_(self, ):

        retval = self.group__return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP55 = None
        BY56 = None
        PHRASE57 = None
        SEP59 = None
        PHRASE60 = None
        function58 = None

        function61 = None


        GROUP55_tree = None
        BY56_tree = None
        PHRASE57_tree = None
        SEP59_tree = None
        PHRASE60_tree = None

        try:
            try:
                # SelectExpr.g:178:8: ( GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* )
                # SelectExpr.g:178:10: GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )*
                pass 
                root_0 = self._adaptor.nil()

                GROUP55=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_1826)
                if self._state.backtracking == 0:

                    GROUP55_tree = self._adaptor.createWithPayload(GROUP55)
                    root_0 = self._adaptor.becomeRoot(GROUP55_tree, root_0)

                BY56=self.match(self.input, BY, self.FOLLOW_BY_in_group_1829)
                # SelectExpr.g:178:21: ( PHRASE | function )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == PHRASE) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == 108) :
                        alt22 = 2
                    elif (LA22_1 == EOF or (SEP <= LA22_1 <= END) or LA22_1 == AND or (XOR <= LA22_1 <= OR) or LA22_1 == IN or (EQ <= LA22_1 <= POW) or (LIST_BEGIN <= LA22_1 <= LIST_END) or LA22_1 == AGE_END or LA22_1 == FROM or (WHERE <= LA22_1 <= ORDER) or LA22_1 == GROUP or LA22_1 == HAVING or LA22_1 == AS or (CONNECT <= LA22_1 <= STOP) or LA22_1 == 109) :
                        alt22 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # SelectExpr.g:178:23: PHRASE
                    pass 
                    PHRASE57=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1834)
                    if self._state.backtracking == 0:

                        PHRASE57_tree = self._adaptor.createWithPayload(PHRASE57)
                        self._adaptor.addChild(root_0, PHRASE57_tree)



                elif alt22 == 2:
                    # SelectExpr.g:178:32: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_group_1838)
                    function58 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function58.tree)



                # SelectExpr.g:178:43: ( SEP ( PHRASE | function ) )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == SEP) :
                        LA24_2 = self.input.LA(2)

                        if (LA24_2 == PHRASE) :
                            LA24_3 = self.input.LA(3)

                            if (self.synpred29_SelectExpr()) :
                                alt24 = 1






                    if alt24 == 1:
                        # SelectExpr.g:178:44: SEP ( PHRASE | function )
                        pass 
                        SEP59=self.match(self.input, SEP, self.FOLLOW_SEP_in_group_1843)
                        # SelectExpr.g:178:49: ( PHRASE | function )
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == PHRASE) :
                            LA23_1 = self.input.LA(2)

                            if (LA23_1 == 108) :
                                alt23 = 2
                            elif (LA23_1 == EOF or (SEP <= LA23_1 <= END) or LA23_1 == AND or (XOR <= LA23_1 <= OR) or LA23_1 == IN or (EQ <= LA23_1 <= POW) or (LIST_BEGIN <= LA23_1 <= LIST_END) or LA23_1 == AGE_END or LA23_1 == FROM or (WHERE <= LA23_1 <= ORDER) or LA23_1 == GROUP or LA23_1 == HAVING or LA23_1 == AS or (CONNECT <= LA23_1 <= STOP) or LA23_1 == 109) :
                                alt23 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 23, 1, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 23, 0, self.input)

                            raise nvae

                        if alt23 == 1:
                            # SelectExpr.g:178:51: PHRASE
                            pass 
                            PHRASE60=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1848)
                            if self._state.backtracking == 0:

                                PHRASE60_tree = self._adaptor.createWithPayload(PHRASE60)
                                self._adaptor.addChild(root_0, PHRASE60_tree)



                        elif alt23 == 2:
                            # SelectExpr.g:178:60: function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_group_1852)
                            function61 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function61.tree)





                    else:
                        break #loop24



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "group_"

    class having__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.having__return, self).__init__()

            self.tree = None




    # $ANTLR start "having_"
    # SelectExpr.g:181:1: having_ : HAVING expr ;
    def having_(self, ):

        retval = self.having__return()
        retval.start = self.input.LT(1)

        root_0 = None

        HAVING62 = None
        expr63 = None


        HAVING62_tree = None

        try:
            try:
                # SelectExpr.g:181:9: ( HAVING expr )
                # SelectExpr.g:181:11: HAVING expr
                pass 
                root_0 = self._adaptor.nil()

                HAVING62=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_1866)
                if self._state.backtracking == 0:

                    HAVING62_tree = self._adaptor.createWithPayload(HAVING62)
                    root_0 = self._adaptor.becomeRoot(HAVING62_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_having_1869)
                expr63 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr63.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "having_"

    class order__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.order__return, self).__init__()

            self.tree = None




    # $ANTLR start "order_"
    # SelectExpr.g:184:1: order_ : ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* ;
    def order_(self, ):

        retval = self.order__return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER64 = None
        BY65 = None
        PHRASE66 = None
        SEP70 = None
        PHRASE71 = None
        direction_67 = None

        function68 = None

        direction_69 = None

        direction_72 = None

        function73 = None

        direction_74 = None


        ORDER64_tree = None
        BY65_tree = None
        PHRASE66_tree = None
        SEP70_tree = None
        PHRASE71_tree = None

        try:
            try:
                # SelectExpr.g:184:8: ( ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* )
                # SelectExpr.g:184:10: ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )*
                pass 
                root_0 = self._adaptor.nil()

                ORDER64=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_1878)
                if self._state.backtracking == 0:

                    ORDER64_tree = self._adaptor.createWithPayload(ORDER64)
                    root_0 = self._adaptor.becomeRoot(ORDER64_tree, root_0)

                BY65=self.match(self.input, BY, self.FOLLOW_BY_in_order_1881)
                # SelectExpr.g:184:21: ( PHRASE direction_ | function direction_ )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == PHRASE) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == 108) :
                        alt25 = 2
                    elif (LA25_1 == EOF or (SEP <= LA25_1 <= END) or LA25_1 == AND or (XOR <= LA25_1 <= OR) or LA25_1 == IN or (EQ <= LA25_1 <= POW) or (LIST_BEGIN <= LA25_1 <= LIST_END) or LA25_1 == AGE_END or LA25_1 == FROM or (WHERE <= LA25_1 <= ORDER) or LA25_1 == GROUP or LA25_1 == AS or (CONNECT <= LA25_1 <= STOP) or (ASC <= LA25_1 <= DESC) or LA25_1 == 109) :
                        alt25 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # SelectExpr.g:184:23: PHRASE direction_
                    pass 
                    PHRASE66=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1886)
                    if self._state.backtracking == 0:

                        PHRASE66_tree = self._adaptor.createWithPayload(PHRASE66)
                        self._adaptor.addChild(root_0, PHRASE66_tree)

                    self._state.following.append(self.FOLLOW_direction__in_order_1888)
                    direction_67 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_67.tree)


                elif alt25 == 2:
                    # SelectExpr.g:184:43: function direction_
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_order_1892)
                    function68 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function68.tree)
                    self._state.following.append(self.FOLLOW_direction__in_order_1894)
                    direction_69 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_69.tree)



                # SelectExpr.g:184:65: ( SEP ( PHRASE direction_ | function direction_ ) )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == SEP) :
                        LA27_2 = self.input.LA(2)

                        if (LA27_2 == PHRASE) :
                            LA27_3 = self.input.LA(3)

                            if (self.synpred32_SelectExpr()) :
                                alt27 = 1






                    if alt27 == 1:
                        # SelectExpr.g:184:66: SEP ( PHRASE direction_ | function direction_ )
                        pass 
                        SEP70=self.match(self.input, SEP, self.FOLLOW_SEP_in_order_1899)
                        # SelectExpr.g:184:71: ( PHRASE direction_ | function direction_ )
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == PHRASE) :
                            LA26_1 = self.input.LA(2)

                            if (LA26_1 == 108) :
                                alt26 = 2
                            elif (LA26_1 == EOF or (SEP <= LA26_1 <= END) or LA26_1 == AND or (XOR <= LA26_1 <= OR) or LA26_1 == IN or (EQ <= LA26_1 <= POW) or (LIST_BEGIN <= LA26_1 <= LIST_END) or LA26_1 == AGE_END or LA26_1 == FROM or (WHERE <= LA26_1 <= ORDER) or LA26_1 == GROUP or LA26_1 == AS or (CONNECT <= LA26_1 <= STOP) or (ASC <= LA26_1 <= DESC) or LA26_1 == 109) :
                                alt26 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 26, 1, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 26, 0, self.input)

                            raise nvae

                        if alt26 == 1:
                            # SelectExpr.g:184:73: PHRASE direction_
                            pass 
                            PHRASE71=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1904)
                            if self._state.backtracking == 0:

                                PHRASE71_tree = self._adaptor.createWithPayload(PHRASE71)
                                self._adaptor.addChild(root_0, PHRASE71_tree)

                            self._state.following.append(self.FOLLOW_direction__in_order_1906)
                            direction_72 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_72.tree)


                        elif alt26 == 2:
                            # SelectExpr.g:184:93: function direction_
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_order_1910)
                            function73 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function73.tree)
                            self._state.following.append(self.FOLLOW_direction__in_order_1912)
                            direction_74 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_74.tree)





                    else:
                        break #loop27



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "order_"

    class direction__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.direction__return, self).__init__()

            self.tree = None




    # $ANTLR start "direction_"
    # SelectExpr.g:187:1: direction_ : ( ASC | DESC )? ;
    def direction_(self, ):

        retval = self.direction__return()
        retval.start = self.input.LT(1)

        root_0 = None

        set75 = None

        set75_tree = None

        try:
            try:
                # SelectExpr.g:187:12: ( ( ASC | DESC )? )
                # SelectExpr.g:187:14: ( ASC | DESC )?
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:187:14: ( ASC | DESC )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if ((ASC <= LA28_0 <= DESC)) :
                    alt28 = 1
                if alt28 == 1:
                    # SelectExpr.g:
                    pass 
                    set75 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set75))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse








                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "direction_"

    class as__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.as__return, self).__init__()

            self.tree = None




    # $ANTLR start "as_"
    # SelectExpr.g:190:1: as_ : AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) ;
    def as_(self, ):

        retval = self.as__return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS76 = None
        AS_LIST77 = None
        AS_VALUE78 = None
        AS_DICT79 = None
        PHRASE80 = None
        char_literal81 = None
        char_literal83 = None
        parameter82 = None


        AS76_tree = None
        AS_LIST77_tree = None
        AS_VALUE78_tree = None
        AS_DICT79_tree = None
        PHRASE80_tree = None
        char_literal81_tree = None
        char_literal83_tree = None

        try:
            try:
                # SelectExpr.g:190:5: ( AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) )
                # SelectExpr.g:190:7: AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                pass 
                root_0 = self._adaptor.nil()

                AS76=self.match(self.input, AS, self.FOLLOW_AS_in_as_1942)
                if self._state.backtracking == 0:

                    AS76_tree = self._adaptor.createWithPayload(AS76)
                    root_0 = self._adaptor.becomeRoot(AS76_tree, root_0)

                # SelectExpr.g:190:11: ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                alt31 = 4
                LA31 = self.input.LA(1)
                if LA31 == AS_LIST:
                    alt31 = 1
                elif LA31 == AS_VALUE:
                    alt31 = 2
                elif LA31 == AS_DICT:
                    alt31 = 3
                elif LA31 == PHRASE:
                    alt31 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # SelectExpr.g:190:13: AS_LIST
                    pass 
                    AS_LIST77=self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_1947)
                    if self._state.backtracking == 0:

                        AS_LIST77_tree = self._adaptor.createWithPayload(AS_LIST77)
                        self._adaptor.addChild(root_0, AS_LIST77_tree)



                elif alt31 == 2:
                    # SelectExpr.g:190:23: AS_VALUE
                    pass 
                    AS_VALUE78=self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_1951)
                    if self._state.backtracking == 0:

                        AS_VALUE78_tree = self._adaptor.createWithPayload(AS_VALUE78)
                        self._adaptor.addChild(root_0, AS_VALUE78_tree)



                elif alt31 == 3:
                    # SelectExpr.g:190:34: AS_DICT
                    pass 
                    AS_DICT79=self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_1955)
                    if self._state.backtracking == 0:

                        AS_DICT79_tree = self._adaptor.createWithPayload(AS_DICT79)
                        self._adaptor.addChild(root_0, AS_DICT79_tree)



                elif alt31 == 4:
                    # SelectExpr.g:190:44: PHRASE ( '(' ( parameter )? ')' )?
                    pass 
                    PHRASE80=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_1959)
                    if self._state.backtracking == 0:

                        PHRASE80_tree = self._adaptor.createWithPayload(PHRASE80)
                        self._adaptor.addChild(root_0, PHRASE80_tree)

                    # SelectExpr.g:190:51: ( '(' ( parameter )? ')' )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 108) :
                        alt30 = 1
                    if alt30 == 1:
                        # SelectExpr.g:190:52: '(' ( parameter )? ')'
                        pass 
                        char_literal81=self.match(self.input, 108, self.FOLLOW_108_in_as_1962)
                        # SelectExpr.g:190:57: ( parameter )?
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == NOT or (ADD <= LA29_0 <= SUB) or LA29_0 == IF or LA29_0 == LIST_BEGIN or LA29_0 == SELECT or LA29_0 == THIS or LA29_0 == STRING or (INTEGER <= LA29_0 <= FALSE) or LA29_0 == PHRASE or LA29_0 == 108) :
                            alt29 = 1
                        if alt29 == 1:
                            # SelectExpr.g:0:0: parameter
                            pass 
                            self._state.following.append(self.FOLLOW_parameter_in_as_1965)
                            parameter82 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter82.tree)



                        char_literal83=self.match(self.input, 109, self.FOLLOW_109_in_as_1968)









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "as_"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # SelectExpr.g:193:1: expr : ( assign_expr | logic_expr );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_expr84 = None

        logic_expr85 = None



        try:
            try:
                # SelectExpr.g:193:6: ( assign_expr | logic_expr )
                alt32 = 2
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # SelectExpr.g:193:8: assign_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assign_expr_in_expr1982)
                    assign_expr84 = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assign_expr84.tree)


                elif alt32 == 2:
                    # SelectExpr.g:194:4: logic_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_logic_expr_in_expr1987)
                    logic_expr85 = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logic_expr85.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class if_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.if_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "if_statement"
    # SelectExpr.g:197:1: if_statement : IF '(' expr ( END parameter ( END parameter )? )? ')' -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? ) ;
    def if_statement(self, ):

        retval = self.if_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IF86 = None
        char_literal87 = None
        END89 = None
        END91 = None
        char_literal93 = None
        expr88 = None

        parameter90 = None

        parameter92 = None


        IF86_tree = None
        char_literal87_tree = None
        END89_tree = None
        END91_tree = None
        char_literal93_tree = None
        stream_108 = RewriteRuleTokenStream(self._adaptor, "token 108")
        stream_109 = RewriteRuleTokenStream(self._adaptor, "token 109")
        stream_END = RewriteRuleTokenStream(self._adaptor, "token END")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:197:14: ( IF '(' expr ( END parameter ( END parameter )? )? ')' -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? ) )
                # SelectExpr.g:197:16: IF '(' expr ( END parameter ( END parameter )? )? ')'
                pass 
                IF86=self.match(self.input, IF, self.FOLLOW_IF_in_if_statement1996) 
                if self._state.backtracking == 0:
                    stream_IF.add(IF86)
                char_literal87=self.match(self.input, 108, self.FOLLOW_108_in_if_statement1998) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal87)
                self._state.following.append(self.FOLLOW_expr_in_if_statement2000)
                expr88 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr88.tree)
                # SelectExpr.g:197:28: ( END parameter ( END parameter )? )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == END) :
                    alt34 = 1
                if alt34 == 1:
                    # SelectExpr.g:197:29: END parameter ( END parameter )?
                    pass 
                    END89=self.match(self.input, END, self.FOLLOW_END_in_if_statement2003) 
                    if self._state.backtracking == 0:
                        stream_END.add(END89)
                    self._state.following.append(self.FOLLOW_parameter_in_if_statement2005)
                    parameter90 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter90.tree)
                    # SelectExpr.g:197:43: ( END parameter )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == END) :
                        alt33 = 1
                    if alt33 == 1:
                        # SelectExpr.g:197:44: END parameter
                        pass 
                        END91=self.match(self.input, END, self.FOLLOW_END_in_if_statement2008) 
                        if self._state.backtracking == 0:
                            stream_END.add(END91)
                        self._state.following.append(self.FOLLOW_parameter_in_if_statement2010)
                        parameter92 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter92.tree)






                char_literal93=self.match(self.input, 109, self.FOLLOW_109_in_if_statement2016) 
                if self._state.backtracking == 0:
                    stream_109.add(char_literal93)

                # AST Rewrite
                # elements: expr, parameter, IF, parameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 197:66: -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? )
                    # SelectExpr.g:197:69: ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IF.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # SelectExpr.g:197:79: ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )?
                    if stream_parameter.hasNext() or stream_parameter.hasNext():
                        # SelectExpr.g:197:81: ^( THEN parameter ( ^( ELSE parameter ) )? )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(THEN, "THEN"), root_2)

                        self._adaptor.addChild(root_2, stream_parameter.nextTree())
                        # SelectExpr.g:197:98: ( ^( ELSE parameter ) )?
                        if stream_parameter.hasNext():
                            # SelectExpr.g:197:99: ^( ELSE parameter )
                            root_3 = self._adaptor.nil()
                            root_3 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELSE, "ELSE"), root_3)

                            self._adaptor.addChild(root_3, stream_parameter.nextTree())

                            self._adaptor.addChild(root_2, root_3)


                        stream_parameter.reset();

                        self._adaptor.addChild(root_1, root_2)


                    stream_parameter.reset();
                    stream_parameter.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "if_statement"

    class assign_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.assign_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "assign_expr"
    # SelectExpr.g:201:1: assign_expr : ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) | this_ ASSIGN expr -> ^( ASSIGN this_ expr ) );
    def assign_expr(self, ):

        retval = self.assign_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE94 = None
        ASSIGN96 = None
        ASSIGN99 = None
        age95 = None

        expr97 = None

        this_98 = None

        expr100 = None


        PHRASE94_tree = None
        ASSIGN96_tree = None
        ASSIGN99_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_this_ = RewriteRuleSubtreeStream(self._adaptor, "rule this_")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:201:13: ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) | this_ ASSIGN expr -> ^( ASSIGN this_ expr ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == PHRASE) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == DOT) :
                        alt36 = 2
                    elif (LA36_1 == ASSIGN or LA36_1 == AGE_BEGIN) :
                        alt36 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae

                elif (LA36_0 == THIS) :
                    alt36 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # SelectExpr.g:201:15: PHRASE ( age )? ASSIGN expr
                    pass 
                    PHRASE94=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr2055) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE94)
                    # SelectExpr.g:201:22: ( age )?
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == AGE_BEGIN) :
                        alt35 = 1
                    if alt35 == 1:
                        # SelectExpr.g:201:23: age
                        pass 
                        self._state.following.append(self.FOLLOW_age_in_assign_expr2058)
                        age95 = self.age()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_age.add(age95.tree)



                    ASSIGN96=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2062) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN96)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2064)
                    expr97 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr97.tree)

                    # AST Rewrite
                    # elements: expr, PHRASE, ASSIGN, age
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 201:41: -> ^( ASSIGN PHRASE expr ( age )? )
                        # SelectExpr.g:201:44: ^( ASSIGN PHRASE expr ( age )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # SelectExpr.g:201:65: ( age )?
                        if stream_age.hasNext():
                            self._adaptor.addChild(root_1, stream_age.nextTree())


                        stream_age.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # SelectExpr.g:201:75: this_ ASSIGN expr
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_assign_expr2083)
                    this_98 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_this_.add(this_98.tree)
                    ASSIGN99=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2085) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN99)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2087)
                    expr100 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr100.tree)

                    # AST Rewrite
                    # elements: expr, ASSIGN, this_
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 201:93: -> ^( ASSIGN this_ expr )
                        # SelectExpr.g:201:96: ^( ASSIGN this_ expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_this_.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assign_expr"

    class logic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_expr"
    # SelectExpr.g:203:1: logic_expr : logic_or ;
    def logic_expr(self, ):

        retval = self.logic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        logic_or101 = None



        try:
            try:
                # SelectExpr.g:203:12: ( logic_or )
                # SelectExpr.g:203:14: logic_or
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_or_in_logic_expr2106)
                logic_or101 = self.logic_or()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_or101.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "logic_expr"

    class logic_or_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_or_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_or"
    # SelectExpr.g:204:1: logic_or : logic_xor ( OR logic_xor )* ;
    def logic_or(self, ):

        retval = self.logic_or_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR103 = None
        logic_xor102 = None

        logic_xor104 = None


        OR103_tree = None

        try:
            try:
                # SelectExpr.g:204:11: ( logic_xor ( OR logic_xor )* )
                # SelectExpr.g:204:13: logic_xor ( OR logic_xor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2115)
                logic_xor102 = self.logic_xor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_xor102.tree)
                # SelectExpr.g:204:23: ( OR logic_xor )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == OR) :
                        LA37_2 = self.input.LA(2)

                        if (self.synpred45_SelectExpr()) :
                            alt37 = 1




                    if alt37 == 1:
                        # SelectExpr.g:204:24: OR logic_xor
                        pass 
                        OR103=self.match(self.input, OR, self.FOLLOW_OR_in_logic_or2118)
                        if self._state.backtracking == 0:

                            OR103_tree = self._adaptor.createWithPayload(OR103)
                            root_0 = self._adaptor.becomeRoot(OR103_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2122)
                        logic_xor104 = self.logic_xor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_xor104.tree)


                    else:
                        break #loop37



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "logic_or"

    class logic_xor_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_xor_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_xor"
    # SelectExpr.g:205:1: logic_xor : logic_and ( XOR logic_and )* ;
    def logic_xor(self, ):

        retval = self.logic_xor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        XOR106 = None
        logic_and105 = None

        logic_and107 = None


        XOR106_tree = None

        try:
            try:
                # SelectExpr.g:205:11: ( logic_and ( XOR logic_and )* )
                # SelectExpr.g:205:13: logic_and ( XOR logic_and )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2132)
                logic_and105 = self.logic_and()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_and105.tree)
                # SelectExpr.g:205:23: ( XOR logic_and )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == XOR) :
                        LA38_2 = self.input.LA(2)

                        if (self.synpred46_SelectExpr()) :
                            alt38 = 1




                    if alt38 == 1:
                        # SelectExpr.g:205:24: XOR logic_and
                        pass 
                        XOR106=self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_xor2135)
                        if self._state.backtracking == 0:

                            XOR106_tree = self._adaptor.createWithPayload(XOR106)
                            root_0 = self._adaptor.becomeRoot(XOR106_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2138)
                        logic_and107 = self.logic_and()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_and107.tree)


                    else:
                        break #loop38



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "logic_xor"

    class logic_and_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_and_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_and"
    # SelectExpr.g:206:1: logic_and : logic_not ( AND logic_not )* ;
    def logic_and(self, ):

        retval = self.logic_and_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND109 = None
        logic_not108 = None

        logic_not110 = None


        AND109_tree = None

        try:
            try:
                # SelectExpr.g:206:11: ( logic_not ( AND logic_not )* )
                # SelectExpr.g:206:13: logic_not ( AND logic_not )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_not_in_logic_and2148)
                logic_not108 = self.logic_not()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_not108.tree)
                # SelectExpr.g:206:23: ( AND logic_not )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == AND) :
                        LA39_2 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt39 = 1




                    if alt39 == 1:
                        # SelectExpr.g:206:24: AND logic_not
                        pass 
                        AND109=self.match(self.input, AND, self.FOLLOW_AND_in_logic_and2151)
                        if self._state.backtracking == 0:

                            AND109_tree = self._adaptor.createWithPayload(AND109)
                            root_0 = self._adaptor.becomeRoot(AND109_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_not_in_logic_and2154)
                        logic_not110 = self.logic_not()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_not110.tree)


                    else:
                        break #loop39



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "logic_and"

    class logic_not_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_not_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_not"
    # SelectExpr.g:207:1: logic_not : ( NOT )? compare_expr ;
    def logic_not(self, ):

        retval = self.logic_not_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT111 = None
        compare_expr112 = None


        NOT111_tree = None

        try:
            try:
                # SelectExpr.g:207:11: ( ( NOT )? compare_expr )
                # SelectExpr.g:207:13: ( NOT )? compare_expr
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:207:13: ( NOT )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == NOT) :
                    alt40 = 1
                if alt40 == 1:
                    # SelectExpr.g:207:14: NOT
                    pass 
                    NOT111=self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_not2165)
                    if self._state.backtracking == 0:

                        NOT111_tree = self._adaptor.createWithPayload(NOT111)
                        root_0 = self._adaptor.becomeRoot(NOT111_tree, root_0)




                self._state.following.append(self.FOLLOW_compare_expr_in_logic_not2170)
                compare_expr112 = self.compare_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_expr112.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "logic_not"

    class compare_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_expr"
    # SelectExpr.g:209:1: compare_expr : compare_in ;
    def compare_expr(self, ):

        retval = self.compare_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        compare_in113 = None



        try:
            try:
                # SelectExpr.g:209:14: ( compare_in )
                # SelectExpr.g:209:16: compare_in
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_in_in_compare_expr2179)
                compare_in113 = self.compare_in()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_in113.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_expr"

    class compare_in_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_in_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_in"
    # SelectExpr.g:210:1: compare_in : compare_eq ( IN atom )* ;
    def compare_in(self, ):

        retval = self.compare_in_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IN115 = None
        compare_eq114 = None

        atom116 = None


        IN115_tree = None

        try:
            try:
                # SelectExpr.g:210:12: ( compare_eq ( IN atom )* )
                # SelectExpr.g:210:14: compare_eq ( IN atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_eq_in_compare_in2187)
                compare_eq114 = self.compare_eq()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_eq114.tree)
                # SelectExpr.g:210:25: ( IN atom )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == IN) :
                        LA41_2 = self.input.LA(2)

                        if (self.synpred49_SelectExpr()) :
                            alt41 = 1




                    if alt41 == 1:
                        # SelectExpr.g:210:26: IN atom
                        pass 
                        IN115=self.match(self.input, IN, self.FOLLOW_IN_in_compare_in2190)
                        if self._state.backtracking == 0:

                            IN115_tree = self._adaptor.createWithPayload(IN115)
                            root_0 = self._adaptor.becomeRoot(IN115_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_compare_in2193)
                        atom116 = self.atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, atom116.tree)


                    else:
                        break #loop41



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_in"

    class compare_eq_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_eq_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_eq"
    # SelectExpr.g:211:1: compare_eq : compare_ne ( EQ compare_ne )* ;
    def compare_eq(self, ):

        retval = self.compare_eq_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQ118 = None
        compare_ne117 = None

        compare_ne119 = None


        EQ118_tree = None

        try:
            try:
                # SelectExpr.g:211:12: ( compare_ne ( EQ compare_ne )* )
                # SelectExpr.g:211:14: compare_ne ( EQ compare_ne )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2203)
                compare_ne117 = self.compare_ne()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ne117.tree)
                # SelectExpr.g:211:25: ( EQ compare_ne )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == EQ) :
                        LA42_2 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt42 = 1




                    if alt42 == 1:
                        # SelectExpr.g:211:26: EQ compare_ne
                        pass 
                        EQ118=self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_eq2206)
                        if self._state.backtracking == 0:

                            EQ118_tree = self._adaptor.createWithPayload(EQ118)
                            root_0 = self._adaptor.becomeRoot(EQ118_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2209)
                        compare_ne119 = self.compare_ne()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ne119.tree)


                    else:
                        break #loop42



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_eq"

    class compare_ne_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ne_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ne"
    # SelectExpr.g:212:1: compare_ne : compare_ge ( NE compare_ge )* ;
    def compare_ne(self, ):

        retval = self.compare_ne_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NE121 = None
        compare_ge120 = None

        compare_ge122 = None


        NE121_tree = None

        try:
            try:
                # SelectExpr.g:212:12: ( compare_ge ( NE compare_ge )* )
                # SelectExpr.g:212:14: compare_ge ( NE compare_ge )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2219)
                compare_ge120 = self.compare_ge()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ge120.tree)
                # SelectExpr.g:212:25: ( NE compare_ge )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == NE) :
                        LA43_2 = self.input.LA(2)

                        if (self.synpred51_SelectExpr()) :
                            alt43 = 1




                    if alt43 == 1:
                        # SelectExpr.g:212:26: NE compare_ge
                        pass 
                        NE121=self.match(self.input, NE, self.FOLLOW_NE_in_compare_ne2222)
                        if self._state.backtracking == 0:

                            NE121_tree = self._adaptor.createWithPayload(NE121)
                            root_0 = self._adaptor.becomeRoot(NE121_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2225)
                        compare_ge122 = self.compare_ge()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ge122.tree)


                    else:
                        break #loop43



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_ne"

    class compare_ge_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ge_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ge"
    # SelectExpr.g:213:1: compare_ge : compare_gt ( GE compare_gt )* ;
    def compare_ge(self, ):

        retval = self.compare_ge_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GE124 = None
        compare_gt123 = None

        compare_gt125 = None


        GE124_tree = None

        try:
            try:
                # SelectExpr.g:213:12: ( compare_gt ( GE compare_gt )* )
                # SelectExpr.g:213:14: compare_gt ( GE compare_gt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2235)
                compare_gt123 = self.compare_gt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_gt123.tree)
                # SelectExpr.g:213:25: ( GE compare_gt )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == GE) :
                        LA44_2 = self.input.LA(2)

                        if (self.synpred52_SelectExpr()) :
                            alt44 = 1




                    if alt44 == 1:
                        # SelectExpr.g:213:26: GE compare_gt
                        pass 
                        GE124=self.match(self.input, GE, self.FOLLOW_GE_in_compare_ge2238)
                        if self._state.backtracking == 0:

                            GE124_tree = self._adaptor.createWithPayload(GE124)
                            root_0 = self._adaptor.becomeRoot(GE124_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2241)
                        compare_gt125 = self.compare_gt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_gt125.tree)


                    else:
                        break #loop44



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_ge"

    class compare_gt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_gt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_gt"
    # SelectExpr.g:214:1: compare_gt : compare_le ( GT compare_le )* ;
    def compare_gt(self, ):

        retval = self.compare_gt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GT127 = None
        compare_le126 = None

        compare_le128 = None


        GT127_tree = None

        try:
            try:
                # SelectExpr.g:214:12: ( compare_le ( GT compare_le )* )
                # SelectExpr.g:214:14: compare_le ( GT compare_le )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2251)
                compare_le126 = self.compare_le()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_le126.tree)
                # SelectExpr.g:214:25: ( GT compare_le )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == GT) :
                        LA45_2 = self.input.LA(2)

                        if (self.synpred53_SelectExpr()) :
                            alt45 = 1




                    if alt45 == 1:
                        # SelectExpr.g:214:26: GT compare_le
                        pass 
                        GT127=self.match(self.input, GT, self.FOLLOW_GT_in_compare_gt2254)
                        if self._state.backtracking == 0:

                            GT127_tree = self._adaptor.createWithPayload(GT127)
                            root_0 = self._adaptor.becomeRoot(GT127_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2257)
                        compare_le128 = self.compare_le()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_le128.tree)


                    else:
                        break #loop45



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_gt"

    class compare_le_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_le_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_le"
    # SelectExpr.g:215:1: compare_le : compare_lt ( LE compare_lt )* ;
    def compare_le(self, ):

        retval = self.compare_le_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LE130 = None
        compare_lt129 = None

        compare_lt131 = None


        LE130_tree = None

        try:
            try:
                # SelectExpr.g:215:12: ( compare_lt ( LE compare_lt )* )
                # SelectExpr.g:215:14: compare_lt ( LE compare_lt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2267)
                compare_lt129 = self.compare_lt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_lt129.tree)
                # SelectExpr.g:215:25: ( LE compare_lt )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == LE) :
                        LA46_2 = self.input.LA(2)

                        if (self.synpred54_SelectExpr()) :
                            alt46 = 1




                    if alt46 == 1:
                        # SelectExpr.g:215:26: LE compare_lt
                        pass 
                        LE130=self.match(self.input, LE, self.FOLLOW_LE_in_compare_le2270)
                        if self._state.backtracking == 0:

                            LE130_tree = self._adaptor.createWithPayload(LE130)
                            root_0 = self._adaptor.becomeRoot(LE130_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2273)
                        compare_lt131 = self.compare_lt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_lt131.tree)


                    else:
                        break #loop46



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_le"

    class compare_lt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_lt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_lt"
    # SelectExpr.g:216:1: compare_lt : arithmetic_expr ( LT arithmetic_expr )* ;
    def compare_lt(self, ):

        retval = self.compare_lt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LT133 = None
        arithmetic_expr132 = None

        arithmetic_expr134 = None


        LT133_tree = None

        try:
            try:
                # SelectExpr.g:216:12: ( arithmetic_expr ( LT arithmetic_expr )* )
                # SelectExpr.g:216:14: arithmetic_expr ( LT arithmetic_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2283)
                arithmetic_expr132 = self.arithmetic_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_expr132.tree)
                # SelectExpr.g:216:30: ( LT arithmetic_expr )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == LT) :
                        LA47_2 = self.input.LA(2)

                        if (self.synpred55_SelectExpr()) :
                            alt47 = 1




                    if alt47 == 1:
                        # SelectExpr.g:216:31: LT arithmetic_expr
                        pass 
                        LT133=self.match(self.input, LT, self.FOLLOW_LT_in_compare_lt2286)
                        if self._state.backtracking == 0:

                            LT133_tree = self._adaptor.createWithPayload(LT133)
                            root_0 = self._adaptor.becomeRoot(LT133_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2289)
                        arithmetic_expr134 = self.arithmetic_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_expr134.tree)


                    else:
                        break #loop47



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "compare_lt"

    class arithmetic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_expr"
    # SelectExpr.g:218:1: arithmetic_expr : arithmetic_sub_add ;
    def arithmetic_expr(self, ):

        retval = self.arithmetic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        arithmetic_sub_add135 = None



        try:
            try:
                # SelectExpr.g:218:17: ( arithmetic_sub_add )
                # SelectExpr.g:218:19: arithmetic_sub_add
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_sub_add_in_arithmetic_expr2300)
                arithmetic_sub_add135 = self.arithmetic_sub_add()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_sub_add135.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arithmetic_expr"

    class arithmetic_sub_add_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_sub_add_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_sub_add"
    # SelectExpr.g:219:1: arithmetic_sub_add : arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* ;
    def arithmetic_sub_add(self, ):

        retval = self.arithmetic_sub_add_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB137 = None
        ADD138 = None
        arithmetic_mul_div_mod136 = None

        arithmetic_mul_div_mod139 = None


        SUB137_tree = None
        ADD138_tree = None

        try:
            try:
                # SelectExpr.g:219:20: ( arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* )
                # SelectExpr.g:219:22: arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2308)
                arithmetic_mul_div_mod136 = self.arithmetic_mul_div_mod()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_mul_div_mod136.tree)
                # SelectExpr.g:219:45: ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == SUB) :
                        LA49_2 = self.input.LA(2)

                        if (self.synpred57_SelectExpr()) :
                            alt49 = 1


                    elif (LA49_0 == ADD) :
                        LA49_3 = self.input.LA(2)

                        if (self.synpred57_SelectExpr()) :
                            alt49 = 1




                    if alt49 == 1:
                        # SelectExpr.g:219:46: ( SUB | ADD ) arithmetic_mul_div_mod
                        pass 
                        # SelectExpr.g:219:46: ( SUB | ADD )
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == SUB) :
                            alt48 = 1
                        elif (LA48_0 == ADD) :
                            alt48 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 48, 0, self.input)

                            raise nvae

                        if alt48 == 1:
                            # SelectExpr.g:219:47: SUB
                            pass 
                            SUB137=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_sub_add2312)
                            if self._state.backtracking == 0:

                                SUB137_tree = self._adaptor.createWithPayload(SUB137)
                                root_0 = self._adaptor.becomeRoot(SUB137_tree, root_0)



                        elif alt48 == 2:
                            # SelectExpr.g:219:52: ADD
                            pass 
                            ADD138=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_sub_add2315)
                            if self._state.backtracking == 0:

                                ADD138_tree = self._adaptor.createWithPayload(ADD138)
                                root_0 = self._adaptor.becomeRoot(ADD138_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2319)
                        arithmetic_mul_div_mod139 = self.arithmetic_mul_div_mod()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_mul_div_mod139.tree)


                    else:
                        break #loop49



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arithmetic_sub_add"

    class arithmetic_mul_div_mod_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_mul_div_mod_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_mul_div_mod"
    # SelectExpr.g:220:1: arithmetic_mul_div_mod : arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* ;
    def arithmetic_mul_div_mod(self, ):

        retval = self.arithmetic_mul_div_mod_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MUL141 = None
        DIV142 = None
        MOD143 = None
        arithmetic_pow140 = None

        arithmetic_pow144 = None


        MUL141_tree = None
        DIV142_tree = None
        MOD143_tree = None

        try:
            try:
                # SelectExpr.g:220:24: ( arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* )
                # SelectExpr.g:220:26: arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2329)
                arithmetic_pow140 = self.arithmetic_pow()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_pow140.tree)
                # SelectExpr.g:220:41: ( ( MUL | DIV | MOD ) arithmetic_pow )*
                while True: #loop51
                    alt51 = 2
                    LA51 = self.input.LA(1)
                    if LA51 == MUL:
                        LA51_2 = self.input.LA(2)

                        if (self.synpred60_SelectExpr()) :
                            alt51 = 1


                    elif LA51 == DIV:
                        LA51_3 = self.input.LA(2)

                        if (self.synpred60_SelectExpr()) :
                            alt51 = 1


                    elif LA51 == MOD:
                        LA51_4 = self.input.LA(2)

                        if (self.synpred60_SelectExpr()) :
                            alt51 = 1



                    if alt51 == 1:
                        # SelectExpr.g:220:42: ( MUL | DIV | MOD ) arithmetic_pow
                        pass 
                        # SelectExpr.g:220:42: ( MUL | DIV | MOD )
                        alt50 = 3
                        LA50 = self.input.LA(1)
                        if LA50 == MUL:
                            alt50 = 1
                        elif LA50 == DIV:
                            alt50 = 2
                        elif LA50 == MOD:
                            alt50 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 50, 0, self.input)

                            raise nvae

                        if alt50 == 1:
                            # SelectExpr.g:220:43: MUL
                            pass 
                            MUL141=self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_mul_div_mod2333)
                            if self._state.backtracking == 0:

                                MUL141_tree = self._adaptor.createWithPayload(MUL141)
                                root_0 = self._adaptor.becomeRoot(MUL141_tree, root_0)



                        elif alt50 == 2:
                            # SelectExpr.g:220:50: DIV
                            pass 
                            DIV142=self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_mul_div_mod2338)
                            if self._state.backtracking == 0:

                                DIV142_tree = self._adaptor.createWithPayload(DIV142)
                                root_0 = self._adaptor.becomeRoot(DIV142_tree, root_0)



                        elif alt50 == 3:
                            # SelectExpr.g:220:57: MOD
                            pass 
                            MOD143=self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_mul_div_mod2343)
                            if self._state.backtracking == 0:

                                MOD143_tree = self._adaptor.createWithPayload(MOD143)
                                root_0 = self._adaptor.becomeRoot(MOD143_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2347)
                        arithmetic_pow144 = self.arithmetic_pow()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_pow144.tree)


                    else:
                        break #loop51



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arithmetic_mul_div_mod"

    class arithmetic_pow_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_pow_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_pow"
    # SelectExpr.g:221:1: arithmetic_pow : arithmetic_unary ( POW arithmetic_unary )* ;
    def arithmetic_pow(self, ):

        retval = self.arithmetic_pow_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POW146 = None
        arithmetic_unary145 = None

        arithmetic_unary147 = None


        POW146_tree = None

        try:
            try:
                # SelectExpr.g:221:16: ( arithmetic_unary ( POW arithmetic_unary )* )
                # SelectExpr.g:221:18: arithmetic_unary ( POW arithmetic_unary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2357)
                arithmetic_unary145 = self.arithmetic_unary()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_unary145.tree)
                # SelectExpr.g:221:35: ( POW arithmetic_unary )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == POW) :
                        LA52_2 = self.input.LA(2)

                        if (self.synpred61_SelectExpr()) :
                            alt52 = 1




                    if alt52 == 1:
                        # SelectExpr.g:221:36: POW arithmetic_unary
                        pass 
                        POW146=self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_pow2360)
                        if self._state.backtracking == 0:

                            POW146_tree = self._adaptor.createWithPayload(POW146)
                            root_0 = self._adaptor.becomeRoot(POW146_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2363)
                        arithmetic_unary147 = self.arithmetic_unary()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_unary147.tree)


                    else:
                        break #loop52



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arithmetic_pow"

    class arithmetic_unary_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_unary_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_unary"
    # SelectExpr.g:222:1: arithmetic_unary : ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom LIST_BEGIN parameter LIST_END -> ^( ELEMENT atom parameter ) | atom );
    def arithmetic_unary(self, ):

        retval = self.arithmetic_unary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB148 = None
        ADD150 = None
        LIST_BEGIN153 = None
        LIST_END155 = None
        atom149 = None

        atom151 = None

        atom152 = None

        parameter154 = None

        atom156 = None


        SUB148_tree = None
        ADD150_tree = None
        LIST_BEGIN153_tree = None
        LIST_END155_tree = None
        stream_SUB = RewriteRuleTokenStream(self._adaptor, "token SUB")
        stream_ADD = RewriteRuleTokenStream(self._adaptor, "token ADD")
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # SelectExpr.g:222:18: ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom LIST_BEGIN parameter LIST_END -> ^( ELEMENT atom parameter ) | atom )
                alt53 = 4
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # SelectExpr.g:223:2: SUB atom
                    pass 
                    SUB148=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_unary2374) 
                    if self._state.backtracking == 0:
                        stream_SUB.add(SUB148)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2376)
                    atom149 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom149.tree)

                    # AST Rewrite
                    # elements: atom
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 223:11: -> ^( NEG atom )
                        # SelectExpr.g:223:14: ^( NEG atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEG, "NEG"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 2:
                    # SelectExpr.g:224:5: ADD atom
                    pass 
                    ADD150=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_unary2390) 
                    if self._state.backtracking == 0:
                        stream_ADD.add(ADD150)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2392)
                    atom151 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom151.tree)

                    # AST Rewrite
                    # elements: atom
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 224:14: -> ^( POS atom )
                        # SelectExpr.g:224:17: ^( POS atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(POS, "POS"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 3:
                    # SelectExpr.g:225:5: atom LIST_BEGIN parameter LIST_END
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2406)
                    atom152 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom152.tree)
                    LIST_BEGIN153=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_arithmetic_unary2408) 
                    if self._state.backtracking == 0:
                        stream_LIST_BEGIN.add(LIST_BEGIN153)
                    self._state.following.append(self.FOLLOW_parameter_in_arithmetic_unary2410)
                    parameter154 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter154.tree)
                    LIST_END155=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_arithmetic_unary2412) 
                    if self._state.backtracking == 0:
                        stream_LIST_END.add(LIST_END155)

                    # AST Rewrite
                    # elements: parameter, atom
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 225:40: -> ^( ELEMENT atom parameter )
                        # SelectExpr.g:225:43: ^( ELEMENT atom parameter )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEMENT, "ELEMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 4:
                    # SelectExpr.g:226:5: atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2428)
                    atom156 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom156.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arithmetic_unary"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "atom"
    # SelectExpr.g:229:1: atom : ( value | variable | if_statement | function | '(' expr ')' | statement_select );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal161 = None
        char_literal163 = None
        value157 = None

        variable158 = None

        if_statement159 = None

        function160 = None

        expr162 = None

        statement_select164 = None


        char_literal161_tree = None
        char_literal163_tree = None

        try:
            try:
                # SelectExpr.g:230:2: ( value | variable | if_statement | function | '(' expr ')' | statement_select )
                alt54 = 6
                LA54 = self.input.LA(1)
                if LA54 == LIST_BEGIN or LA54 == THIS or LA54 == STRING or LA54 == INTEGER or LA54 == FLOAT or LA54 == TRUE or LA54 == FALSE:
                    alt54 = 1
                elif LA54 == PHRASE:
                    LA54 = self.input.LA(2)
                    if LA54 == DOT:
                        alt54 = 1
                    elif LA54 == 108:
                        alt54 = 4
                    elif LA54 == EOF or LA54 == SEP or LA54 == END or LA54 == AND or LA54 == XOR or LA54 == OR or LA54 == IN or LA54 == EQ or LA54 == NE or LA54 == LE or LA54 == GE or LA54 == LT or LA54 == GT or LA54 == ADD or LA54 == SUB or LA54 == MUL or LA54 == DIV or LA54 == MOD or LA54 == POW or LA54 == LIST_BEGIN or LA54 == LIST_END or LA54 == AGE_BEGIN or LA54 == AGE_END or LA54 == FROM or LA54 == WHERE or LA54 == ORDER or LA54 == GROUP or LA54 == AS or LA54 == CONNECT or LA54 == START or LA54 == STOP or LA54 == 109:
                        alt54 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 54, 2, self.input)

                        raise nvae

                elif LA54 == IF:
                    alt54 = 3
                elif LA54 == 108:
                    alt54 = 5
                elif LA54 == SELECT:
                    alt54 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # SelectExpr.g:230:4: value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_value_in_atom2438)
                    value157 = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, value157.tree)


                elif alt54 == 2:
                    # SelectExpr.g:231:4: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_atom2443)
                    variable158 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable158.tree)


                elif alt54 == 3:
                    # SelectExpr.g:232:4: if_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_statement_in_atom2448)
                    if_statement159 = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_statement159.tree)


                elif alt54 == 4:
                    # SelectExpr.g:233:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_atom2453)
                    function160 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function160.tree)


                elif alt54 == 5:
                    # SelectExpr.g:234:4: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal161=self.match(self.input, 108, self.FOLLOW_108_in_atom2458)
                    self._state.following.append(self.FOLLOW_expr_in_atom2461)
                    expr162 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr162.tree)
                    char_literal163=self.match(self.input, 109, self.FOLLOW_109_in_atom2463)


                elif alt54 == 6:
                    # SelectExpr.g:235:4: statement_select
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_atom2469)
                    statement_select164 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select164.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atom"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.function_return, self).__init__()

            self.tree = None




    # $ANTLR start "function"
    # SelectExpr.g:238:1: function : PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE165 = None
        char_literal166 = None
        char_literal168 = None
        parameter167 = None


        PHRASE165_tree = None
        char_literal166_tree = None
        char_literal168_tree = None
        stream_108 = RewriteRuleTokenStream(self._adaptor, "token 108")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_109 = RewriteRuleTokenStream(self._adaptor, "token 109")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # SelectExpr.g:238:10: ( PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) )
                # SelectExpr.g:238:12: PHRASE '(' ( parameter )? ')'
                pass 
                PHRASE165=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function2478) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE165)
                char_literal166=self.match(self.input, 108, self.FOLLOW_108_in_function2480) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal166)
                # SelectExpr.g:238:23: ( parameter )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == NOT or (ADD <= LA55_0 <= SUB) or LA55_0 == IF or LA55_0 == LIST_BEGIN or LA55_0 == SELECT or LA55_0 == THIS or LA55_0 == STRING or (INTEGER <= LA55_0 <= FALSE) or LA55_0 == PHRASE or LA55_0 == 108) :
                    alt55 = 1
                if alt55 == 1:
                    # SelectExpr.g:0:0: parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function2482)
                    parameter167 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter167.tree)



                char_literal168=self.match(self.input, 109, self.FOLLOW_109_in_function2485) 
                if self._state.backtracking == 0:
                    stream_109.add(char_literal168)

                # AST Rewrite
                # elements: PHRASE, parameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 238:38: -> ^( FCT PHRASE ( parameter )? )
                    # SelectExpr.g:238:41: ^( FCT PHRASE ( parameter )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FCT, "FCT"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:238:54: ( parameter )?
                    if stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "function"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # SelectExpr.g:241:1: parameter : expr ( SEP expr )* ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEP170 = None
        expr169 = None

        expr171 = None


        SEP170_tree = None

        try:
            try:
                # SelectExpr.g:241:11: ( expr ( SEP expr )* )
                # SelectExpr.g:241:13: expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_parameter2505)
                expr169 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr169.tree)
                # SelectExpr.g:241:18: ( SEP expr )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == SEP) :
                        alt56 = 1


                    if alt56 == 1:
                        # SelectExpr.g:241:19: SEP expr
                        pass 
                        SEP170=self.match(self.input, SEP, self.FOLLOW_SEP_in_parameter2508)
                        self._state.following.append(self.FOLLOW_expr_in_parameter2511)
                        expr171 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr171.tree)


                    else:
                        break #loop56



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameter"

    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.variable_return, self).__init__()

            self.tree = None




    # $ANTLR start "variable"
    # SelectExpr.g:244:1: variable : PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) ;
    def variable(self, ):

        retval = self.variable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE172 = None
        age173 = None


        PHRASE172_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:244:10: ( PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) )
                # SelectExpr.g:244:12: PHRASE ( age )?
                pass 
                PHRASE172=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable2522) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE172)
                # SelectExpr.g:244:19: ( age )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == AGE_BEGIN) :
                    alt57 = 1
                if alt57 == 1:
                    # SelectExpr.g:244:20: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable2525)
                    age173 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age173.tree)




                # AST Rewrite
                # elements: PHRASE, age
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 244:26: -> ^( VAR PHRASE ( age )? )
                    # SelectExpr.g:244:29: ^( VAR PHRASE ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:244:42: ( age )?
                    if stream_age.hasNext():
                        self._adaptor.addChild(root_1, stream_age.nextTree())


                    stream_age.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "variable"

    class age_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.age_return, self).__init__()

            self.tree = None




    # $ANTLR start "age"
    # SelectExpr.g:247:1: age : AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) ;
    def age(self, ):

        retval = self.age_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AGE_BEGIN174 = None
        AGE_END176 = None
        expr175 = None


        AGE_BEGIN174_tree = None
        AGE_END176_tree = None
        stream_AGE_BEGIN = RewriteRuleTokenStream(self._adaptor, "token AGE_BEGIN")
        stream_AGE_END = RewriteRuleTokenStream(self._adaptor, "token AGE_END")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:247:5: ( AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) )
                # SelectExpr.g:247:7: AGE_BEGIN ( expr )? AGE_END
                pass 
                AGE_BEGIN174=self.match(self.input, AGE_BEGIN, self.FOLLOW_AGE_BEGIN_in_age2549) 
                if self._state.backtracking == 0:
                    stream_AGE_BEGIN.add(AGE_BEGIN174)
                # SelectExpr.g:247:17: ( expr )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == NOT or (ADD <= LA58_0 <= SUB) or LA58_0 == IF or LA58_0 == LIST_BEGIN or LA58_0 == SELECT or LA58_0 == THIS or LA58_0 == STRING or (INTEGER <= LA58_0 <= FALSE) or LA58_0 == PHRASE or LA58_0 == 108) :
                    alt58 = 1
                if alt58 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_age2551)
                    expr175 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr175.tree)



                AGE_END176=self.match(self.input, AGE_END, self.FOLLOW_AGE_END_in_age2554) 
                if self._state.backtracking == 0:
                    stream_AGE_END.add(AGE_END176)

                # AST Rewrite
                # elements: expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 247:31: -> ^( AGE ( expr )? )
                    # SelectExpr.g:247:34: ^( AGE ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AGE, "AGE"), root_1)

                    # SelectExpr.g:247:40: ( expr )?
                    if stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "age"

    class value_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.value_return, self).__init__()

            self.tree = None




    # $ANTLR start "value"
    # SelectExpr.g:250:1: value : ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRING177 = None
        FLOAT178 = None
        INTEGER179 = None
        TRUE180 = None
        FALSE181 = None
        this_182 = None

        list_183 = None


        STRING177_tree = None
        FLOAT178_tree = None
        INTEGER179_tree = None
        TRUE180_tree = None
        FALSE181_tree = None
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_TRUE = RewriteRuleTokenStream(self._adaptor, "token TRUE")
        stream_FALSE = RewriteRuleTokenStream(self._adaptor, "token FALSE")
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")

        try:
            try:
                # SelectExpr.g:250:7: ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ )
                alt59 = 7
                LA59 = self.input.LA(1)
                if LA59 == STRING:
                    alt59 = 1
                elif LA59 == FLOAT:
                    alt59 = 2
                elif LA59 == INTEGER:
                    alt59 = 3
                elif LA59 == TRUE:
                    alt59 = 4
                elif LA59 == FALSE:
                    alt59 = 5
                elif LA59 == THIS or LA59 == PHRASE:
                    alt59 = 6
                elif LA59 == LIST_BEGIN:
                    alt59 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # SelectExpr.g:250:9: STRING
                    pass 
                    STRING177=self.match(self.input, STRING, self.FOLLOW_STRING_in_value2572) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING177)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 250:17: -> ^( VAL STRING )
                        # SelectExpr.g:250:20: ^( VAL STRING )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_STRING.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt59 == 2:
                    # SelectExpr.g:251:4: FLOAT
                    pass 
                    FLOAT178=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value2586) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT178)

                    # AST Rewrite
                    # elements: FLOAT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 251:11: -> ^( VAL FLOAT )
                        # SelectExpr.g:251:14: ^( VAL FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt59 == 3:
                    # SelectExpr.g:252:4: INTEGER
                    pass 
                    INTEGER179=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value2600) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER179)

                    # AST Rewrite
                    # elements: INTEGER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 252:12: -> ^( VAL INTEGER )
                        # SelectExpr.g:252:15: ^( VAL INTEGER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt59 == 4:
                    # SelectExpr.g:253:4: TRUE
                    pass 
                    TRUE180=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value2613) 
                    if self._state.backtracking == 0:
                        stream_TRUE.add(TRUE180)

                    # AST Rewrite
                    # elements: TRUE
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 253:10: -> ^( VAL TRUE )
                        # SelectExpr.g:253:13: ^( VAL TRUE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_TRUE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt59 == 5:
                    # SelectExpr.g:254:4: FALSE
                    pass 
                    FALSE181=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value2627) 
                    if self._state.backtracking == 0:
                        stream_FALSE.add(FALSE181)

                    # AST Rewrite
                    # elements: FALSE
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 254:11: -> ^( VAL FALSE )
                        # SelectExpr.g:254:14: ^( VAL FALSE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FALSE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt59 == 6:
                    # SelectExpr.g:255:4: this_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_this__in_value2641)
                    this_182 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, this_182.tree)


                elif alt59 == 7:
                    # SelectExpr.g:256:4: list_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list__in_value2646)
                    list_183 = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_183.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value"

    class this__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.this__return, self).__init__()

            self.tree = None




    # $ANTLR start "this_"
    # SelectExpr.g:259:1: this_ : ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        retval = self.this__return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE184 = None
        DOT185 = None
        THIS186 = None

        PHRASE184_tree = None
        DOT185_tree = None
        THIS186_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")

        try:
            try:
                # SelectExpr.g:259:7: ( ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) )
                # SelectExpr.g:259:9: ( PHRASE DOT )? THIS
                pass 
                # SelectExpr.g:259:9: ( PHRASE DOT )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == PHRASE) :
                    alt60 = 1
                if alt60 == 1:
                    # SelectExpr.g:259:10: PHRASE DOT
                    pass 
                    PHRASE184=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_2656) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE184)
                    DOT185=self.match(self.input, DOT, self.FOLLOW_DOT_in_this_2658) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT185)



                THIS186=self.match(self.input, THIS, self.FOLLOW_THIS_in_this_2662) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS186)

                # AST Rewrite
                # elements: THIS, PHRASE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 259:29: -> ^( THIS ( PHRASE )? )
                    # SelectExpr.g:259:32: ^( THIS ( PHRASE )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_THIS.nextNode(), root_1)

                    # SelectExpr.g:259:39: ( PHRASE )?
                    if stream_PHRASE.hasNext():
                        self._adaptor.addChild(root_1, stream_PHRASE.nextNode())


                    stream_PHRASE.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "this_"

    class list__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.list__return, self).__init__()

            self.tree = None




    # $ANTLR start "list_"
    # SelectExpr.g:262:1: list_ : LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) ;
    def list_(self, ):

        retval = self.list__return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIST_BEGIN187 = None
        SEP189 = None
        LIST_END191 = None
        expr188 = None

        expr190 = None


        LIST_BEGIN187_tree = None
        SEP189_tree = None
        LIST_END191_tree = None
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_SEP = RewriteRuleTokenStream(self._adaptor, "token SEP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:262:7: ( LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) )
                # SelectExpr.g:262:10: LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END
                pass 
                LIST_BEGIN187=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_list_2682) 
                if self._state.backtracking == 0:
                    stream_LIST_BEGIN.add(LIST_BEGIN187)
                # SelectExpr.g:262:21: ( ( expr )? ( SEP expr )* )
                # SelectExpr.g:262:23: ( expr )? ( SEP expr )*
                pass 
                # SelectExpr.g:262:23: ( expr )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == NOT or (ADD <= LA61_0 <= SUB) or LA61_0 == IF or LA61_0 == LIST_BEGIN or LA61_0 == SELECT or LA61_0 == THIS or LA61_0 == STRING or (INTEGER <= LA61_0 <= FALSE) or LA61_0 == PHRASE or LA61_0 == 108) :
                    alt61 = 1
                if alt61 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_list_2686)
                    expr188 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr188.tree)



                # SelectExpr.g:262:29: ( SEP expr )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == SEP) :
                        alt62 = 1


                    if alt62 == 1:
                        # SelectExpr.g:262:30: SEP expr
                        pass 
                        SEP189=self.match(self.input, SEP, self.FOLLOW_SEP_in_list_2690) 
                        if self._state.backtracking == 0:
                            stream_SEP.add(SEP189)
                        self._state.following.append(self.FOLLOW_expr_in_list_2692)
                        expr190 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr190.tree)


                    else:
                        break #loop62



                LIST_END191=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_list_2698) 
                if self._state.backtracking == 0:
                    stream_LIST_END.add(LIST_END191)

                # AST Rewrite
                # elements: expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 262:52: -> ^( LIST ( expr )* )
                    # SelectExpr.g:262:55: ^( LIST ( expr )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # SelectExpr.g:262:62: ( expr )*
                    while stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "list_"

    # $ANTLR start "synpred2_SelectExpr"
    def synpred2_SelectExpr_fragment(self, ):
        # SelectExpr.g:151:13: ( statement_select END )
        # SelectExpr.g:151:13: statement_select END
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectExpr1521)
        self.statement_select()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred2_SelectExpr1523)


    # $ANTLR end "synpred2_SelectExpr"



    # $ANTLR start "synpred3_SelectExpr"
    def synpred3_SelectExpr_fragment(self, ):
        # SelectExpr.g:152:4: ( expr END )
        # SelectExpr.g:152:4: expr END
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred3_SelectExpr1529)
        self.expr()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred3_SelectExpr1531)


    # $ANTLR end "synpred3_SelectExpr"



    # $ANTLR start "synpred4_SelectExpr"
    def synpred4_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:17: ( where_ )
        # SelectExpr.g:157:17: where_
        pass 
        self._state.following.append(self.FOLLOW_where__in_synpred4_SelectExpr1553)
        self.where_()

        self._state.following.pop()


    # $ANTLR end "synpred4_SelectExpr"



    # $ANTLR start "synpred6_SelectExpr"
    def synpred6_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:27: ( ( start_ )? connect_ stop_ )
        # SelectExpr.g:157:27: ( start_ )? connect_ stop_
        pass 
        # SelectExpr.g:157:27: ( start_ )?
        alt63 = 2
        LA63_0 = self.input.LA(1)

        if (LA63_0 == START) :
            alt63 = 1
        if alt63 == 1:
            # SelectExpr.g:157:28: start_
            pass 
            self._state.following.append(self.FOLLOW_start__in_synpred6_SelectExpr1559)
            self.start_()

            self._state.following.pop()



        self._state.following.append(self.FOLLOW_connect__in_synpred6_SelectExpr1563)
        self.connect_()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_stop__in_synpred6_SelectExpr1565)
        self.stop_()

        self._state.following.pop()


    # $ANTLR end "synpred6_SelectExpr"



    # $ANTLR start "synpred8_SelectExpr"
    def synpred8_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:55: ( group_ ( having_ )? )
        # SelectExpr.g:157:55: group_ ( having_ )?
        pass 
        self._state.following.append(self.FOLLOW_group__in_synpred8_SelectExpr1570)
        self.group_()

        self._state.following.pop()
        # SelectExpr.g:157:62: ( having_ )?
        alt64 = 2
        LA64_0 = self.input.LA(1)

        if (LA64_0 == HAVING) :
            alt64 = 1
        if alt64 == 1:
            # SelectExpr.g:157:63: having_
            pass 
            self._state.following.append(self.FOLLOW_having__in_synpred8_SelectExpr1573)
            self.having_()

            self._state.following.pop()





    # $ANTLR end "synpred8_SelectExpr"



    # $ANTLR start "synpred9_SelectExpr"
    def synpred9_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:76: ( order_ )
        # SelectExpr.g:157:76: order_
        pass 
        self._state.following.append(self.FOLLOW_order__in_synpred9_SelectExpr1580)
        self.order_()

        self._state.following.pop()


    # $ANTLR end "synpred9_SelectExpr"



    # $ANTLR start "synpred10_SelectExpr"
    def synpred10_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:86: ( as_ )
        # SelectExpr.g:157:86: as_
        pass 
        self._state.following.append(self.FOLLOW_as__in_synpred10_SelectExpr1585)
        self.as_()

        self._state.following.pop()


    # $ANTLR end "synpred10_SelectExpr"



    # $ANTLR start "synpred12_SelectExpr"
    def synpred12_SelectExpr_fragment(self, ):
        # SelectExpr.g:160:29: ( PHRASE )
        # SelectExpr.g:160:29: PHRASE
        pass 
        self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred12_SelectExpr1655)


    # $ANTLR end "synpred12_SelectExpr"



    # $ANTLR start "synpred14_SelectExpr"
    def synpred14_SelectExpr_fragment(self, ):
        # SelectExpr.g:160:49: ( this_ )
        # SelectExpr.g:160:49: this_
        pass 
        self._state.following.append(self.FOLLOW_this__in_synpred14_SelectExpr1663)
        self.this_()

        self._state.following.pop()


    # $ANTLR end "synpred14_SelectExpr"



    # $ANTLR start "synpred15_SelectExpr"
    def synpred15_SelectExpr_fragment(self, ):
        # SelectExpr.g:160:70: ( PHRASE )
        # SelectExpr.g:160:70: PHRASE
        pass 
        self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred15_SelectExpr1675)


    # $ANTLR end "synpred15_SelectExpr"



    # $ANTLR start "synpred17_SelectExpr"
    def synpred17_SelectExpr_fragment(self, ):
        # SelectExpr.g:160:90: ( this_ )
        # SelectExpr.g:160:90: this_
        pass 
        self._state.following.append(self.FOLLOW_this__in_synpred17_SelectExpr1683)
        self.this_()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectExpr"



    # $ANTLR start "synpred19_SelectExpr"
    def synpred19_SelectExpr_fragment(self, ):
        # SelectExpr.g:163:21: ( SEP expr )
        # SelectExpr.g:163:21: SEP expr
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred19_SelectExpr1709)
        self._state.following.append(self.FOLLOW_expr_in_synpred19_SelectExpr1712)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred19_SelectExpr"



    # $ANTLR start "synpred23_SelectExpr"
    def synpred23_SelectExpr_fragment(self, ):
        # SelectExpr.g:172:59: ( INTEGER )
        # SelectExpr.g:172:59: INTEGER
        pass 
        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_synpred23_SelectExpr1781)


    # $ANTLR end "synpred23_SelectExpr"



    # $ANTLR start "synpred29_SelectExpr"
    def synpred29_SelectExpr_fragment(self, ):
        # SelectExpr.g:178:44: ( SEP ( PHRASE | function ) )
        # SelectExpr.g:178:44: SEP ( PHRASE | function )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred29_SelectExpr1843)
        # SelectExpr.g:178:49: ( PHRASE | function )
        alt67 = 2
        LA67_0 = self.input.LA(1)

        if (LA67_0 == PHRASE) :
            LA67_1 = self.input.LA(2)

            if (LA67_1 == 108) :
                alt67 = 2
            elif (LA67_1 == EOF) :
                alt67 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 67, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 67, 0, self.input)

            raise nvae

        if alt67 == 1:
            # SelectExpr.g:178:51: PHRASE
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred29_SelectExpr1848)


        elif alt67 == 2:
            # SelectExpr.g:178:60: function
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred29_SelectExpr1852)
            self.function()

            self._state.following.pop()





    # $ANTLR end "synpred29_SelectExpr"



    # $ANTLR start "synpred32_SelectExpr"
    def synpred32_SelectExpr_fragment(self, ):
        # SelectExpr.g:184:66: ( SEP ( PHRASE direction_ | function direction_ ) )
        # SelectExpr.g:184:66: SEP ( PHRASE direction_ | function direction_ )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred32_SelectExpr1899)
        # SelectExpr.g:184:71: ( PHRASE direction_ | function direction_ )
        alt68 = 2
        LA68_0 = self.input.LA(1)

        if (LA68_0 == PHRASE) :
            LA68_1 = self.input.LA(2)

            if (LA68_1 == 108) :
                alt68 = 2
            elif (LA68_1 == EOF or (ASC <= LA68_1 <= DESC)) :
                alt68 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 68, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 68, 0, self.input)

            raise nvae

        if alt68 == 1:
            # SelectExpr.g:184:73: PHRASE direction_
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred32_SelectExpr1904)
            self._state.following.append(self.FOLLOW_direction__in_synpred32_SelectExpr1906)
            self.direction_()

            self._state.following.pop()


        elif alt68 == 2:
            # SelectExpr.g:184:93: function direction_
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred32_SelectExpr1910)
            self.function()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_direction__in_synpred32_SelectExpr1912)
            self.direction_()

            self._state.following.pop()





    # $ANTLR end "synpred32_SelectExpr"



    # $ANTLR start "synpred40_SelectExpr"
    def synpred40_SelectExpr_fragment(self, ):
        # SelectExpr.g:193:8: ( assign_expr )
        # SelectExpr.g:193:8: assign_expr
        pass 
        self._state.following.append(self.FOLLOW_assign_expr_in_synpred40_SelectExpr1982)
        self.assign_expr()

        self._state.following.pop()


    # $ANTLR end "synpred40_SelectExpr"



    # $ANTLR start "synpred45_SelectExpr"
    def synpred45_SelectExpr_fragment(self, ):
        # SelectExpr.g:204:24: ( OR logic_xor )
        # SelectExpr.g:204:24: OR logic_xor
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred45_SelectExpr2118)
        self._state.following.append(self.FOLLOW_logic_xor_in_synpred45_SelectExpr2122)
        self.logic_xor()

        self._state.following.pop()


    # $ANTLR end "synpred45_SelectExpr"



    # $ANTLR start "synpred46_SelectExpr"
    def synpred46_SelectExpr_fragment(self, ):
        # SelectExpr.g:205:24: ( XOR logic_and )
        # SelectExpr.g:205:24: XOR logic_and
        pass 
        self.match(self.input, XOR, self.FOLLOW_XOR_in_synpred46_SelectExpr2135)
        self._state.following.append(self.FOLLOW_logic_and_in_synpred46_SelectExpr2138)
        self.logic_and()

        self._state.following.pop()


    # $ANTLR end "synpred46_SelectExpr"



    # $ANTLR start "synpred47_SelectExpr"
    def synpred47_SelectExpr_fragment(self, ):
        # SelectExpr.g:206:24: ( AND logic_not )
        # SelectExpr.g:206:24: AND logic_not
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred47_SelectExpr2151)
        self._state.following.append(self.FOLLOW_logic_not_in_synpred47_SelectExpr2154)
        self.logic_not()

        self._state.following.pop()


    # $ANTLR end "synpred47_SelectExpr"



    # $ANTLR start "synpred49_SelectExpr"
    def synpred49_SelectExpr_fragment(self, ):
        # SelectExpr.g:210:26: ( IN atom )
        # SelectExpr.g:210:26: IN atom
        pass 
        self.match(self.input, IN, self.FOLLOW_IN_in_synpred49_SelectExpr2190)
        self._state.following.append(self.FOLLOW_atom_in_synpred49_SelectExpr2193)
        self.atom()

        self._state.following.pop()


    # $ANTLR end "synpred49_SelectExpr"



    # $ANTLR start "synpred50_SelectExpr"
    def synpred50_SelectExpr_fragment(self, ):
        # SelectExpr.g:211:26: ( EQ compare_ne )
        # SelectExpr.g:211:26: EQ compare_ne
        pass 
        self.match(self.input, EQ, self.FOLLOW_EQ_in_synpred50_SelectExpr2206)
        self._state.following.append(self.FOLLOW_compare_ne_in_synpred50_SelectExpr2209)
        self.compare_ne()

        self._state.following.pop()


    # $ANTLR end "synpred50_SelectExpr"



    # $ANTLR start "synpred51_SelectExpr"
    def synpred51_SelectExpr_fragment(self, ):
        # SelectExpr.g:212:26: ( NE compare_ge )
        # SelectExpr.g:212:26: NE compare_ge
        pass 
        self.match(self.input, NE, self.FOLLOW_NE_in_synpred51_SelectExpr2222)
        self._state.following.append(self.FOLLOW_compare_ge_in_synpred51_SelectExpr2225)
        self.compare_ge()

        self._state.following.pop()


    # $ANTLR end "synpred51_SelectExpr"



    # $ANTLR start "synpred52_SelectExpr"
    def synpred52_SelectExpr_fragment(self, ):
        # SelectExpr.g:213:26: ( GE compare_gt )
        # SelectExpr.g:213:26: GE compare_gt
        pass 
        self.match(self.input, GE, self.FOLLOW_GE_in_synpred52_SelectExpr2238)
        self._state.following.append(self.FOLLOW_compare_gt_in_synpred52_SelectExpr2241)
        self.compare_gt()

        self._state.following.pop()


    # $ANTLR end "synpred52_SelectExpr"



    # $ANTLR start "synpred53_SelectExpr"
    def synpred53_SelectExpr_fragment(self, ):
        # SelectExpr.g:214:26: ( GT compare_le )
        # SelectExpr.g:214:26: GT compare_le
        pass 
        self.match(self.input, GT, self.FOLLOW_GT_in_synpred53_SelectExpr2254)
        self._state.following.append(self.FOLLOW_compare_le_in_synpred53_SelectExpr2257)
        self.compare_le()

        self._state.following.pop()


    # $ANTLR end "synpred53_SelectExpr"



    # $ANTLR start "synpred54_SelectExpr"
    def synpred54_SelectExpr_fragment(self, ):
        # SelectExpr.g:215:26: ( LE compare_lt )
        # SelectExpr.g:215:26: LE compare_lt
        pass 
        self.match(self.input, LE, self.FOLLOW_LE_in_synpred54_SelectExpr2270)
        self._state.following.append(self.FOLLOW_compare_lt_in_synpred54_SelectExpr2273)
        self.compare_lt()

        self._state.following.pop()


    # $ANTLR end "synpred54_SelectExpr"



    # $ANTLR start "synpred55_SelectExpr"
    def synpred55_SelectExpr_fragment(self, ):
        # SelectExpr.g:216:31: ( LT arithmetic_expr )
        # SelectExpr.g:216:31: LT arithmetic_expr
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred55_SelectExpr2286)
        self._state.following.append(self.FOLLOW_arithmetic_expr_in_synpred55_SelectExpr2289)
        self.arithmetic_expr()

        self._state.following.pop()


    # $ANTLR end "synpred55_SelectExpr"



    # $ANTLR start "synpred57_SelectExpr"
    def synpred57_SelectExpr_fragment(self, ):
        # SelectExpr.g:219:46: ( ( SUB | ADD ) arithmetic_mul_div_mod )
        # SelectExpr.g:219:46: ( SUB | ADD ) arithmetic_mul_div_mod
        pass 
        if (ADD <= self.input.LA(1) <= SUB):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_synpred57_SelectExpr2319)
        self.arithmetic_mul_div_mod()

        self._state.following.pop()


    # $ANTLR end "synpred57_SelectExpr"



    # $ANTLR start "synpred60_SelectExpr"
    def synpred60_SelectExpr_fragment(self, ):
        # SelectExpr.g:220:42: ( ( MUL | DIV | MOD ) arithmetic_pow )
        # SelectExpr.g:220:42: ( MUL | DIV | MOD ) arithmetic_pow
        pass 
        if (MUL <= self.input.LA(1) <= MOD):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_pow_in_synpred60_SelectExpr2347)
        self.arithmetic_pow()

        self._state.following.pop()


    # $ANTLR end "synpred60_SelectExpr"



    # $ANTLR start "synpred61_SelectExpr"
    def synpred61_SelectExpr_fragment(self, ):
        # SelectExpr.g:221:36: ( POW arithmetic_unary )
        # SelectExpr.g:221:36: POW arithmetic_unary
        pass 
        self.match(self.input, POW, self.FOLLOW_POW_in_synpred61_SelectExpr2360)
        self._state.following.append(self.FOLLOW_arithmetic_unary_in_synpred61_SelectExpr2363)
        self.arithmetic_unary()

        self._state.following.pop()


    # $ANTLR end "synpred61_SelectExpr"



    # $ANTLR start "synpred64_SelectExpr"
    def synpred64_SelectExpr_fragment(self, ):
        # SelectExpr.g:225:5: ( atom LIST_BEGIN parameter LIST_END )
        # SelectExpr.g:225:5: atom LIST_BEGIN parameter LIST_END
        pass 
        self._state.following.append(self.FOLLOW_atom_in_synpred64_SelectExpr2406)
        self.atom()

        self._state.following.pop()
        self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_synpred64_SelectExpr2408)
        self._state.following.append(self.FOLLOW_parameter_in_synpred64_SelectExpr2410)
        self.parameter()

        self._state.following.pop()
        self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_synpred64_SelectExpr2412)


    # $ANTLR end "synpred64_SelectExpr"




    # Delegated rules

    def synpred57_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred57_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred60_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred60_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred8_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred47_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred47_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred50_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred50_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred14_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred54_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred54_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred40_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred40_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred51_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred51_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred61_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred61_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred9_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred45_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred45_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred64_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred64_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred6_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred6_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred2_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred29_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred29_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred19_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred19_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred12_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred12_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred52_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred52_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred55_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred55_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred49_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred49_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred3_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred32_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred32_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred23_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred23_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred10_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred10_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred46_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred46_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred53_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred53_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\21\1\0\17\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\154\1\0\17\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\14\uffff\1\3\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\17\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\17\13\uffff\1\2\11\uffff\2\2\5\uffff\1\2\2\uffff"
        u"\1\2\7\uffff\1\1\20\uffff\1\2\26\uffff\1\2\1\uffff\4\2\2\uffff"
        u"\1\2\2\uffff\1\2"),
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
                if (self.synpred2_SelectExpr()):
                    s = 16

                elif (self.synpred3_SelectExpr()):
                    s = 2

                 
                input.seek(index2_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 2, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\35\1\0\17\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\1\154\1\0\17\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\2\uffff\1\2\15\uffff\1\1"
        )

    DFA18_special = DFA.unpack(
        u"\1\uffff\1\0\17\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\2\11\uffff\2\2\5\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\20\uffff\1\2\14\uffff\1\2\11\uffff\1\2\1\uffff\1\1\3\2\2\uffff"
        u"\1\2\2\uffff\1\2"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA18_1 = input.LA(1)

                 
                index18_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred23_SelectExpr()):
                    s = 16

                elif (True):
                    s = 2

                 
                input.seek(index18_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 18, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\35\2\0\15\uffff"
        )

    DFA32_max = DFA.unpack(
        u"\1\154\2\0\15\uffff"
        )

    DFA32_accept = DFA.unpack(
        u"\3\uffff\1\2\13\uffff\1\1"
        )

    DFA32_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\15\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\1\3\11\uffff\2\3\5\uffff\1\3\2\uffff\1\3\7\uffff\1"
        u"\3\20\uffff\1\2\26\uffff\1\3\1\uffff\4\3\2\uffff\1\1\2\uffff\1"
        u"\3"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA32_1 = input.LA(1)

                 
                index32_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred40_SelectExpr()):
                    s = 15

                elif (True):
                    s = 3

                 
                input.seek(index32_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA32_2 = input.LA(1)

                 
                index32_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred40_SelectExpr()):
                    s = 15

                elif (True):
                    s = 3

                 
                input.seek(index32_2)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 32, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\1\47\2\uffff\13\0\2\uffff"
        )

    DFA53_max = DFA.unpack(
        u"\1\154\2\uffff\13\0\2\uffff"
        )

    DFA53_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\13\uffff\1\3\1\4"
        )

    DFA53_special = DFA.unpack(
        u"\3\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\2\uffff"
        )

            
    DFA53_transition = [
        DFA.unpack(u"\1\2\1\1\5\uffff\1\13\2\uffff\1\12\7\uffff\1\15\20\uffff"
        u"\1\11\26\uffff\1\3\1\uffff\1\5\1\4\1\6\1\7\2\uffff\1\10\2\uffff"
        u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA53_3 = input.LA(1)

                 
                index53_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA53_4 = input.LA(1)

                 
                index53_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_4)
                if s >= 0:
                    return s
            elif s == 2: 
                LA53_5 = input.LA(1)

                 
                index53_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_5)
                if s >= 0:
                    return s
            elif s == 3: 
                LA53_6 = input.LA(1)

                 
                index53_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_6)
                if s >= 0:
                    return s
            elif s == 4: 
                LA53_7 = input.LA(1)

                 
                index53_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_7)
                if s >= 0:
                    return s
            elif s == 5: 
                LA53_8 = input.LA(1)

                 
                index53_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_8)
                if s >= 0:
                    return s
            elif s == 6: 
                LA53_9 = input.LA(1)

                 
                index53_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_9)
                if s >= 0:
                    return s
            elif s == 7: 
                LA53_10 = input.LA(1)

                 
                index53_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_10)
                if s >= 0:
                    return s
            elif s == 8: 
                LA53_11 = input.LA(1)

                 
                index53_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_11)
                if s >= 0:
                    return s
            elif s == 9: 
                LA53_12 = input.LA(1)

                 
                index53_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_12)
                if s >= 0:
                    return s
            elif s == 10: 
                LA53_13 = input.LA(1)

                 
                index53_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred64_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index53_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 53, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_prog_in_eval1501 = frozenset([1])
    FOLLOW_statement_in_prog1511 = frozenset([1, 17, 29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_statement_select_in_statement1521 = frozenset([17])
    FOLLOW_END_in_statement1523 = frozenset([1])
    FOLLOW_expr_in_statement1529 = frozenset([17])
    FOLLOW_END_in_statement1531 = frozenset([1])
    FOLLOW_END_in_statement1537 = frozenset([1])
    FOLLOW_select__in_statement_select1548 = frozenset([59])
    FOLLOW_from__in_statement_select1550 = frozenset([1, 62, 63, 67, 73, 76, 77])
    FOLLOW_where__in_statement_select1553 = frozenset([1, 63, 67, 73, 76, 77])
    FOLLOW_start__in_statement_select1559 = frozenset([76, 77])
    FOLLOW_connect__in_statement_select1563 = frozenset([78])
    FOLLOW_stop__in_statement_select1565 = frozenset([1, 63, 67, 73])
    FOLLOW_group__in_statement_select1570 = frozenset([1, 63, 69, 73])
    FOLLOW_having__in_statement_select1573 = frozenset([1, 63, 73])
    FOLLOW_order__in_statement_select1580 = frozenset([1, 73])
    FOLLOW_as__in_statement_select1585 = frozenset([1])
    FOLLOW_SELECT_in_select_1644 = frozenset([29, 39, 40, 41, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MUL_in_select_1648 = frozenset([1])
    FOLLOW_PHRASE_in_select_1655 = frozenset([1, 16])
    FOLLOW_function_in_select_1659 = frozenset([1, 16])
    FOLLOW_this__in_select_1663 = frozenset([1, 16])
    FOLLOW_expr_in_select_1667 = frozenset([1, 16])
    FOLLOW_SEP_in_select_1671 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_PHRASE_in_select_1675 = frozenset([1, 16])
    FOLLOW_function_in_select_1679 = frozenset([1, 16])
    FOLLOW_this__in_select_1683 = frozenset([1, 16])
    FOLLOW_expr_in_select_1687 = frozenset([1, 16])
    FOLLOW_FROM_in_from_1703 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_from_1706 = frozenset([1, 16])
    FOLLOW_SEP_in_from_1709 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_from_1712 = frozenset([1, 16])
    FOLLOW_WHERE_in_where_1723 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_where_1726 = frozenset([1])
    FOLLOW_START_in_start_1735 = frozenset([79])
    FOLLOW_WITH_in_start_1738 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_start_1741 = frozenset([1, 16])
    FOLLOW_SEP_in_start_1744 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_start_1747 = frozenset([1, 16])
    FOLLOW_CONNECT_in_connect_1758 = frozenset([72])
    FOLLOW_BY_in_connect_1761 = frozenset([29, 39, 40, 46, 49, 57, 74, 80, 83, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_NO_in_connect_1765 = frozenset([81])
    FOLLOW_CYCLE_in_connect_1768 = frozenset([29, 39, 40, 46, 49, 57, 74, 83, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_UNIQUE_in_connect_1773 = frozenset([29, 39, 40, 46, 49, 57, 74, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MEMORIZE_in_connect_1778 = frozenset([29, 39, 40, 46, 49, 57, 74, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_INTEGER_in_connect_1781 = frozenset([29, 39, 40, 46, 49, 57, 74, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MAXIMUM_in_connect_1788 = frozenset([99])
    FOLLOW_INTEGER_in_connect_1790 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_connect_1794 = frozenset([1, 16])
    FOLLOW_SEP_in_connect_1797 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_connect_1800 = frozenset([1, 16])
    FOLLOW_STOP_in_stop_1811 = frozenset([79])
    FOLLOW_WITH_in_stop_1814 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_stop_1817 = frozenset([1])
    FOLLOW_GROUP_in_group_1826 = frozenset([72])
    FOLLOW_BY_in_group_1829 = frozenset([105])
    FOLLOW_PHRASE_in_group_1834 = frozenset([1, 16])
    FOLLOW_function_in_group_1838 = frozenset([1, 16])
    FOLLOW_SEP_in_group_1843 = frozenset([105])
    FOLLOW_PHRASE_in_group_1848 = frozenset([1, 16])
    FOLLOW_function_in_group_1852 = frozenset([1, 16])
    FOLLOW_HAVING_in_having_1866 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_having_1869 = frozenset([1])
    FOLLOW_ORDER_in_order_1878 = frozenset([72])
    FOLLOW_BY_in_order_1881 = frozenset([105])
    FOLLOW_PHRASE_in_order_1886 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1888 = frozenset([1, 16])
    FOLLOW_function_in_order_1892 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1894 = frozenset([1, 16])
    FOLLOW_SEP_in_order_1899 = frozenset([105])
    FOLLOW_PHRASE_in_order_1904 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1906 = frozenset([1, 16])
    FOLLOW_function_in_order_1910 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1912 = frozenset([1, 16])
    FOLLOW_set_in_direction_1926 = frozenset([1])
    FOLLOW_AS_in_as_1942 = frozenset([90, 91, 92, 105])
    FOLLOW_AS_LIST_in_as_1947 = frozenset([1])
    FOLLOW_AS_VALUE_in_as_1951 = frozenset([1])
    FOLLOW_AS_DICT_in_as_1955 = frozenset([1])
    FOLLOW_PHRASE_in_as_1959 = frozenset([1, 108])
    FOLLOW_108_in_as_1962 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108, 109])
    FOLLOW_parameter_in_as_1965 = frozenset([109])
    FOLLOW_109_in_as_1968 = frozenset([1])
    FOLLOW_assign_expr_in_expr1982 = frozenset([1])
    FOLLOW_logic_expr_in_expr1987 = frozenset([1])
    FOLLOW_IF_in_if_statement1996 = frozenset([108])
    FOLLOW_108_in_if_statement1998 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_if_statement2000 = frozenset([17, 109])
    FOLLOW_END_in_if_statement2003 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_if_statement2005 = frozenset([17, 109])
    FOLLOW_END_in_if_statement2008 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_if_statement2010 = frozenset([109])
    FOLLOW_109_in_if_statement2016 = frozenset([1])
    FOLLOW_PHRASE_in_assign_expr2055 = frozenset([32, 51])
    FOLLOW_age_in_assign_expr2058 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2062 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_assign_expr2064 = frozenset([1])
    FOLLOW_this__in_assign_expr2083 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2085 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_assign_expr2087 = frozenset([1])
    FOLLOW_logic_or_in_logic_expr2106 = frozenset([1])
    FOLLOW_logic_xor_in_logic_or2115 = frozenset([1, 27])
    FOLLOW_OR_in_logic_or2118 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_xor_in_logic_or2122 = frozenset([1, 27])
    FOLLOW_logic_and_in_logic_xor2132 = frozenset([1, 26])
    FOLLOW_XOR_in_logic_xor2135 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_and_in_logic_xor2138 = frozenset([1, 26])
    FOLLOW_logic_not_in_logic_and2148 = frozenset([1, 22])
    FOLLOW_AND_in_logic_and2151 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_not_in_logic_and2154 = frozenset([1, 22])
    FOLLOW_NOT_in_logic_not2165 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_expr_in_logic_not2170 = frozenset([1])
    FOLLOW_compare_in_in_compare_expr2179 = frozenset([1])
    FOLLOW_compare_eq_in_compare_in2187 = frozenset([1, 31])
    FOLLOW_IN_in_compare_in2190 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_compare_in2193 = frozenset([1, 31])
    FOLLOW_compare_ne_in_compare_eq2203 = frozenset([1, 33])
    FOLLOW_EQ_in_compare_eq2206 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ne_in_compare_eq2209 = frozenset([1, 33])
    FOLLOW_compare_ge_in_compare_ne2219 = frozenset([1, 34])
    FOLLOW_NE_in_compare_ne2222 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ge_in_compare_ne2225 = frozenset([1, 34])
    FOLLOW_compare_gt_in_compare_ge2235 = frozenset([1, 36])
    FOLLOW_GE_in_compare_ge2238 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_gt_in_compare_ge2241 = frozenset([1, 36])
    FOLLOW_compare_le_in_compare_gt2251 = frozenset([1, 38])
    FOLLOW_GT_in_compare_gt2254 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_le_in_compare_gt2257 = frozenset([1, 38])
    FOLLOW_compare_lt_in_compare_le2267 = frozenset([1, 35])
    FOLLOW_LE_in_compare_le2270 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_lt_in_compare_le2273 = frozenset([1, 35])
    FOLLOW_arithmetic_expr_in_compare_lt2283 = frozenset([1, 37])
    FOLLOW_LT_in_compare_lt2286 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_expr_in_compare_lt2289 = frozenset([1, 37])
    FOLLOW_arithmetic_sub_add_in_arithmetic_expr2300 = frozenset([1])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2308 = frozenset([1, 39, 40])
    FOLLOW_SUB_in_arithmetic_sub_add2312 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_ADD_in_arithmetic_sub_add2315 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2319 = frozenset([1, 39, 40])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2329 = frozenset([1, 41, 42, 43])
    FOLLOW_MUL_in_arithmetic_mul_div_mod2333 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_DIV_in_arithmetic_mul_div_mod2338 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MOD_in_arithmetic_mul_div_mod2343 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2347 = frozenset([1, 41, 42, 43])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2357 = frozenset([1, 44])
    FOLLOW_POW_in_arithmetic_pow2360 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2363 = frozenset([1, 44])
    FOLLOW_SUB_in_arithmetic_unary2374 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_arithmetic_unary2376 = frozenset([1])
    FOLLOW_ADD_in_arithmetic_unary2390 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_arithmetic_unary2392 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2406 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_arithmetic_unary2408 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_arithmetic_unary2410 = frozenset([50])
    FOLLOW_LIST_END_in_arithmetic_unary2412 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2428 = frozenset([1])
    FOLLOW_value_in_atom2438 = frozenset([1])
    FOLLOW_variable_in_atom2443 = frozenset([1])
    FOLLOW_if_statement_in_atom2448 = frozenset([1])
    FOLLOW_function_in_atom2453 = frozenset([1])
    FOLLOW_108_in_atom2458 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_atom2461 = frozenset([109])
    FOLLOW_109_in_atom2463 = frozenset([1])
    FOLLOW_statement_select_in_atom2469 = frozenset([1])
    FOLLOW_PHRASE_in_function2478 = frozenset([108])
    FOLLOW_108_in_function2480 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108, 109])
    FOLLOW_parameter_in_function2482 = frozenset([109])
    FOLLOW_109_in_function2485 = frozenset([1])
    FOLLOW_expr_in_parameter2505 = frozenset([1, 16])
    FOLLOW_SEP_in_parameter2508 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_parameter2511 = frozenset([1, 16])
    FOLLOW_PHRASE_in_variable2522 = frozenset([1, 51])
    FOLLOW_age_in_variable2525 = frozenset([1])
    FOLLOW_AGE_BEGIN_in_age2549 = frozenset([29, 39, 40, 46, 49, 52, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_age2551 = frozenset([52])
    FOLLOW_AGE_END_in_age2554 = frozenset([1])
    FOLLOW_STRING_in_value2572 = frozenset([1])
    FOLLOW_FLOAT_in_value2586 = frozenset([1])
    FOLLOW_INTEGER_in_value2600 = frozenset([1])
    FOLLOW_TRUE_in_value2613 = frozenset([1])
    FOLLOW_FALSE_in_value2627 = frozenset([1])
    FOLLOW_this__in_value2641 = frozenset([1])
    FOLLOW_list__in_value2646 = frozenset([1])
    FOLLOW_PHRASE_in_this_2656 = frozenset([15])
    FOLLOW_DOT_in_this_2658 = frozenset([74])
    FOLLOW_THIS_in_this_2662 = frozenset([1])
    FOLLOW_LIST_BEGIN_in_list_2682 = frozenset([16, 29, 39, 40, 46, 49, 50, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_list_2686 = frozenset([16, 50])
    FOLLOW_SEP_in_list_2690 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_list_2692 = frozenset([16, 50])
    FOLLOW_LIST_END_in_list_2698 = frozenset([1])
    FOLLOW_statement_select_in_synpred2_SelectExpr1521 = frozenset([17])
    FOLLOW_END_in_synpred2_SelectExpr1523 = frozenset([1])
    FOLLOW_expr_in_synpred3_SelectExpr1529 = frozenset([17])
    FOLLOW_END_in_synpred3_SelectExpr1531 = frozenset([1])
    FOLLOW_where__in_synpred4_SelectExpr1553 = frozenset([1])
    FOLLOW_start__in_synpred6_SelectExpr1559 = frozenset([76, 77])
    FOLLOW_connect__in_synpred6_SelectExpr1563 = frozenset([78])
    FOLLOW_stop__in_synpred6_SelectExpr1565 = frozenset([1])
    FOLLOW_group__in_synpred8_SelectExpr1570 = frozenset([1, 69])
    FOLLOW_having__in_synpred8_SelectExpr1573 = frozenset([1])
    FOLLOW_order__in_synpred9_SelectExpr1580 = frozenset([1])
    FOLLOW_as__in_synpred10_SelectExpr1585 = frozenset([1])
    FOLLOW_PHRASE_in_synpred12_SelectExpr1655 = frozenset([1])
    FOLLOW_this__in_synpred14_SelectExpr1663 = frozenset([1])
    FOLLOW_PHRASE_in_synpred15_SelectExpr1675 = frozenset([1])
    FOLLOW_this__in_synpred17_SelectExpr1683 = frozenset([1])
    FOLLOW_SEP_in_synpred19_SelectExpr1709 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_synpred19_SelectExpr1712 = frozenset([1])
    FOLLOW_INTEGER_in_synpred23_SelectExpr1781 = frozenset([1])
    FOLLOW_SEP_in_synpred29_SelectExpr1843 = frozenset([105])
    FOLLOW_PHRASE_in_synpred29_SelectExpr1848 = frozenset([1])
    FOLLOW_function_in_synpred29_SelectExpr1852 = frozenset([1])
    FOLLOW_SEP_in_synpred32_SelectExpr1899 = frozenset([105])
    FOLLOW_PHRASE_in_synpred32_SelectExpr1904 = frozenset([88, 89])
    FOLLOW_direction__in_synpred32_SelectExpr1906 = frozenset([1])
    FOLLOW_function_in_synpred32_SelectExpr1910 = frozenset([88, 89])
    FOLLOW_direction__in_synpred32_SelectExpr1912 = frozenset([1])
    FOLLOW_assign_expr_in_synpred40_SelectExpr1982 = frozenset([1])
    FOLLOW_OR_in_synpred45_SelectExpr2118 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_xor_in_synpred45_SelectExpr2122 = frozenset([1])
    FOLLOW_XOR_in_synpred46_SelectExpr2135 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_and_in_synpred46_SelectExpr2138 = frozenset([1])
    FOLLOW_AND_in_synpred47_SelectExpr2151 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_not_in_synpred47_SelectExpr2154 = frozenset([1])
    FOLLOW_IN_in_synpred49_SelectExpr2190 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_synpred49_SelectExpr2193 = frozenset([1])
    FOLLOW_EQ_in_synpred50_SelectExpr2206 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ne_in_synpred50_SelectExpr2209 = frozenset([1])
    FOLLOW_NE_in_synpred51_SelectExpr2222 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ge_in_synpred51_SelectExpr2225 = frozenset([1])
    FOLLOW_GE_in_synpred52_SelectExpr2238 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_gt_in_synpred52_SelectExpr2241 = frozenset([1])
    FOLLOW_GT_in_synpred53_SelectExpr2254 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_le_in_synpred53_SelectExpr2257 = frozenset([1])
    FOLLOW_LE_in_synpred54_SelectExpr2270 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_lt_in_synpred54_SelectExpr2273 = frozenset([1])
    FOLLOW_LT_in_synpred55_SelectExpr2286 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_expr_in_synpred55_SelectExpr2289 = frozenset([1])
    FOLLOW_set_in_synpred57_SelectExpr2311 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_mul_div_mod_in_synpred57_SelectExpr2319 = frozenset([1])
    FOLLOW_set_in_synpred60_SelectExpr2332 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_pow_in_synpred60_SelectExpr2347 = frozenset([1])
    FOLLOW_POW_in_synpred61_SelectExpr2360 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_unary_in_synpred61_SelectExpr2363 = frozenset([1])
    FOLLOW_atom_in_synpred64_SelectExpr2406 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_synpred64_SelectExpr2408 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_synpred64_SelectExpr2410 = frozenset([50])
    FOLLOW_LIST_END_in_synpred64_SelectExpr2412 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SelectExprLexer", SelectExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
