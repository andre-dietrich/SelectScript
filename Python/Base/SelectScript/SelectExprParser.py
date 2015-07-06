# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2015-06-24 08:19:10

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

                self._state.following.append(self.FOLLOW_prog_in_eval1511)
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
                        self._state.following.append(self.FOLLOW_statement_in_prog1521)
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

                    self._state.following.append(self.FOLLOW_statement_select_in_statement1531)
                    statement_select3 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select3.tree)
                    END4=self.match(self.input, END, self.FOLLOW_END_in_statement1533)


                elif alt2 == 2:
                    # SelectExpr.g:152:4: expr END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_statement1539)
                    expr5 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr5.tree)
                    END6=self.match(self.input, END, self.FOLLOW_END_in_statement1541)


                elif alt2 == 3:
                    # SelectExpr.g:153:4: END
                    pass 
                    root_0 = self._adaptor.nil()

                    END7=self.match(self.input, END, self.FOLLOW_END_in_statement1547)


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
                self._state.following.append(self.FOLLOW_select__in_statement_select1558)
                select_8 = self.select_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_select_.add(select_8.tree)
                self._state.following.append(self.FOLLOW_from__in_statement_select1560)
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
                    self._state.following.append(self.FOLLOW_where__in_statement_select1563)
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
                        self._state.following.append(self.FOLLOW_start__in_statement_select1569)
                        start_11 = self.start_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_start_.add(start_11.tree)



                    self._state.following.append(self.FOLLOW_connect__in_statement_select1573)
                    connect_12 = self.connect_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_connect_.add(connect_12.tree)
                    self._state.following.append(self.FOLLOW_stop__in_statement_select1575)
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
                    self._state.following.append(self.FOLLOW_group__in_statement_select1580)
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
                        self._state.following.append(self.FOLLOW_having__in_statement_select1583)
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
                    self._state.following.append(self.FOLLOW_order__in_statement_select1590)
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
                    self._state.following.append(self.FOLLOW_as__in_statement_select1595)
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
    # SelectExpr.g:160:1: select_ : SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) ;
    def select_(self, ):

        retval = self.select__return()
        retval.start = self.input.LT(1)

        root_0 = None

        SELECT18 = None
        MUL19 = None
        PHRASE20 = None
        SEP23 = None
        PHRASE24 = None
        function21 = None

        this_22 = None

        function25 = None

        this_26 = None


        SELECT18_tree = None
        MUL19_tree = None
        PHRASE20_tree = None
        SEP23_tree = None
        PHRASE24_tree = None

        try:
            try:
                # SelectExpr.g:160:9: ( SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) )
                # SelectExpr.g:160:11: SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                pass 
                root_0 = self._adaptor.nil()

                SELECT18=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_1655)
                if self._state.backtracking == 0:

                    SELECT18_tree = self._adaptor.createWithPayload(SELECT18)
                    root_0 = self._adaptor.becomeRoot(SELECT18_tree, root_0)

                # SelectExpr.g:160:19: ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == MUL) :
                    alt13 = 1
                elif (LA13_0 == THIS or LA13_0 == PHRASE) :
                    alt13 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # SelectExpr.g:160:20: MUL
                    pass 
                    MUL19=self.match(self.input, MUL, self.FOLLOW_MUL_in_select_1659)


                elif alt13 == 2:
                    # SelectExpr.g:160:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    pass 
                    # SelectExpr.g:160:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    # SelectExpr.g:160:28: ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )*
                    pass 
                    # SelectExpr.g:160:28: ( PHRASE | function | this_ )
                    alt10 = 3
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == PHRASE) :
                        LA10 = self.input.LA(2)
                        if LA10 == 108:
                            alt10 = 2
                        elif LA10 == DOT:
                            alt10 = 3
                        elif LA10 == SEP or LA10 == FROM:
                            alt10 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 10, 1, self.input)

                            raise nvae

                    elif (LA10_0 == THIS) :
                        alt10 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 10, 0, self.input)

                        raise nvae

                    if alt10 == 1:
                        # SelectExpr.g:160:29: PHRASE
                        pass 
                        PHRASE20=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1666)
                        if self._state.backtracking == 0:

                            PHRASE20_tree = self._adaptor.createWithPayload(PHRASE20)
                            self._adaptor.addChild(root_0, PHRASE20_tree)



                    elif alt10 == 2:
                        # SelectExpr.g:160:38: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_select_1670)
                        function21 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, function21.tree)


                    elif alt10 == 3:
                        # SelectExpr.g:160:49: this_
                        pass 
                        self._state.following.append(self.FOLLOW_this__in_select_1674)
                        this_22 = self.this_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, this_22.tree)



                    # SelectExpr.g:160:56: ( SEP ( PHRASE | function | this_ ) )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == SEP) :
                            alt12 = 1


                        if alt12 == 1:
                            # SelectExpr.g:160:57: SEP ( PHRASE | function | this_ )
                            pass 
                            SEP23=self.match(self.input, SEP, self.FOLLOW_SEP_in_select_1678)
                            # SelectExpr.g:160:62: ( PHRASE | function | this_ )
                            alt11 = 3
                            LA11_0 = self.input.LA(1)

                            if (LA11_0 == PHRASE) :
                                LA11 = self.input.LA(2)
                                if LA11 == 108:
                                    alt11 = 2
                                elif LA11 == DOT:
                                    alt11 = 3
                                elif LA11 == SEP or LA11 == FROM:
                                    alt11 = 1
                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    nvae = NoViableAltException("", 11, 1, self.input)

                                    raise nvae

                            elif (LA11_0 == THIS) :
                                alt11 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 11, 0, self.input)

                                raise nvae

                            if alt11 == 1:
                                # SelectExpr.g:160:63: PHRASE
                                pass 
                                PHRASE24=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1682)
                                if self._state.backtracking == 0:

                                    PHRASE24_tree = self._adaptor.createWithPayload(PHRASE24)
                                    self._adaptor.addChild(root_0, PHRASE24_tree)



                            elif alt11 == 2:
                                # SelectExpr.g:160:72: function
                                pass 
                                self._state.following.append(self.FOLLOW_function_in_select_1686)
                                function25 = self.function()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, function25.tree)


                            elif alt11 == 3:
                                # SelectExpr.g:160:83: this_
                                pass 
                                self._state.following.append(self.FOLLOW_this__in_select_1690)
                                this_26 = self.this_()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, this_26.tree)





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

        FROM27 = None
        SEP29 = None
        expr28 = None

        expr30 = None


        FROM27_tree = None
        SEP29_tree = None

        try:
            try:
                # SelectExpr.g:163:7: ( FROM expr ( SEP expr )* )
                # SelectExpr.g:163:9: FROM expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                FROM27=self.match(self.input, FROM, self.FOLLOW_FROM_in_from_1706)
                if self._state.backtracking == 0:

                    FROM27_tree = self._adaptor.createWithPayload(FROM27)
                    root_0 = self._adaptor.becomeRoot(FROM27_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_from_1709)
                expr28 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr28.tree)
                # SelectExpr.g:163:20: ( SEP expr )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == SEP) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred17_SelectExpr()) :
                            alt14 = 1




                    if alt14 == 1:
                        # SelectExpr.g:163:21: SEP expr
                        pass 
                        SEP29=self.match(self.input, SEP, self.FOLLOW_SEP_in_from_1712)
                        self._state.following.append(self.FOLLOW_expr_in_from_1715)
                        expr30 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr30.tree)


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

        WHERE31 = None
        expr32 = None


        WHERE31_tree = None

        try:
            try:
                # SelectExpr.g:166:8: ( WHERE expr )
                # SelectExpr.g:166:10: WHERE expr
                pass 
                root_0 = self._adaptor.nil()

                WHERE31=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_1726)
                if self._state.backtracking == 0:

                    WHERE31_tree = self._adaptor.createWithPayload(WHERE31)
                    root_0 = self._adaptor.becomeRoot(WHERE31_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_where_1729)
                expr32 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr32.tree)



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

        START33 = None
        WITH34 = None
        SEP36 = None
        expr35 = None

        expr37 = None


        START33_tree = None
        WITH34_tree = None
        SEP36_tree = None

        try:
            try:
                # SelectExpr.g:169:8: ( START WITH expr ( SEP expr )* )
                # SelectExpr.g:169:10: START WITH expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                START33=self.match(self.input, START, self.FOLLOW_START_in_start_1738)
                if self._state.backtracking == 0:

                    START33_tree = self._adaptor.createWithPayload(START33)
                    root_0 = self._adaptor.becomeRoot(START33_tree, root_0)

                WITH34=self.match(self.input, WITH, self.FOLLOW_WITH_in_start_1741)
                self._state.following.append(self.FOLLOW_expr_in_start_1744)
                expr35 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr35.tree)
                # SelectExpr.g:169:28: ( SEP expr )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SEP) :
                        alt15 = 1


                    if alt15 == 1:
                        # SelectExpr.g:169:29: SEP expr
                        pass 
                        SEP36=self.match(self.input, SEP, self.FOLLOW_SEP_in_start_1747)
                        self._state.following.append(self.FOLLOW_expr_in_start_1750)
                        expr37 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr37.tree)


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
    # SelectExpr.g:172:1: connect_ : CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )* ;
    def connect_(self, ):

        retval = self.connect__return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONNECT38 = None
        BY39 = None
        NO40 = None
        CYCLE41 = None
        UNIQUE42 = None
        GRAPH43 = None
        MEMORIZE44 = None
        INTEGER45 = None
        MAXIMUM46 = None
        INTEGER47 = None
        SEP49 = None
        expr48 = None

        expr50 = None


        CONNECT38_tree = None
        BY39_tree = None
        NO40_tree = None
        CYCLE41_tree = None
        UNIQUE42_tree = None
        GRAPH43_tree = None
        MEMORIZE44_tree = None
        INTEGER45_tree = None
        MAXIMUM46_tree = None
        INTEGER47_tree = None
        SEP49_tree = None

        try:
            try:
                # SelectExpr.g:172:10: ( CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )* )
                # SelectExpr.g:172:12: CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( GRAPH )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                CONNECT38=self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_1761)
                if self._state.backtracking == 0:

                    CONNECT38_tree = self._adaptor.createWithPayload(CONNECT38)
                    root_0 = self._adaptor.becomeRoot(CONNECT38_tree, root_0)

                BY39=self.match(self.input, BY, self.FOLLOW_BY_in_connect_1764)
                # SelectExpr.g:172:25: ( NO CYCLE )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == NO) :
                    alt16 = 1
                if alt16 == 1:
                    # SelectExpr.g:172:26: NO CYCLE
                    pass 
                    NO40=self.match(self.input, NO, self.FOLLOW_NO_in_connect_1768)
                    CYCLE41=self.match(self.input, CYCLE, self.FOLLOW_CYCLE_in_connect_1771)
                    if self._state.backtracking == 0:

                        CYCLE41_tree = self._adaptor.createWithPayload(CYCLE41)
                        self._adaptor.addChild(root_0, CYCLE41_tree)




                # SelectExpr.g:172:38: ( UNIQUE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == UNIQUE) :
                    alt17 = 1
                if alt17 == 1:
                    # SelectExpr.g:172:39: UNIQUE
                    pass 
                    UNIQUE42=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_connect_1776)
                    if self._state.backtracking == 0:

                        UNIQUE42_tree = self._adaptor.createWithPayload(UNIQUE42)
                        self._adaptor.addChild(root_0, UNIQUE42_tree)




                # SelectExpr.g:172:48: ( GRAPH )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == GRAPH) :
                    alt18 = 1
                if alt18 == 1:
                    # SelectExpr.g:172:49: GRAPH
                    pass 
                    GRAPH43=self.match(self.input, GRAPH, self.FOLLOW_GRAPH_in_connect_1781)
                    if self._state.backtracking == 0:

                        GRAPH43_tree = self._adaptor.createWithPayload(GRAPH43)
                        self._adaptor.addChild(root_0, GRAPH43_tree)




                # SelectExpr.g:172:57: ( MEMORIZE INTEGER )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MEMORIZE) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectExpr.g:172:58: MEMORIZE INTEGER
                    pass 
                    MEMORIZE44=self.match(self.input, MEMORIZE, self.FOLLOW_MEMORIZE_in_connect_1786)
                    if self._state.backtracking == 0:

                        MEMORIZE44_tree = self._adaptor.createWithPayload(MEMORIZE44)
                        self._adaptor.addChild(root_0, MEMORIZE44_tree)

                    INTEGER45=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1788)
                    if self._state.backtracking == 0:

                        INTEGER45_tree = self._adaptor.createWithPayload(INTEGER45)
                        self._adaptor.addChild(root_0, INTEGER45_tree)




                # SelectExpr.g:172:77: ( MAXIMUM INTEGER )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == MAXIMUM) :
                    alt20 = 1
                if alt20 == 1:
                    # SelectExpr.g:172:78: MAXIMUM INTEGER
                    pass 
                    MAXIMUM46=self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_connect_1793)
                    if self._state.backtracking == 0:

                        MAXIMUM46_tree = self._adaptor.createWithPayload(MAXIMUM46)
                        self._adaptor.addChild(root_0, MAXIMUM46_tree)

                    INTEGER47=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1795)
                    if self._state.backtracking == 0:

                        INTEGER47_tree = self._adaptor.createWithPayload(INTEGER47)
                        self._adaptor.addChild(root_0, INTEGER47_tree)




                self._state.following.append(self.FOLLOW_expr_in_connect_1799)
                expr48 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr48.tree)
                # SelectExpr.g:172:101: ( SEP expr )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == SEP) :
                        alt21 = 1


                    if alt21 == 1:
                        # SelectExpr.g:172:102: SEP expr
                        pass 
                        SEP49=self.match(self.input, SEP, self.FOLLOW_SEP_in_connect_1802)
                        self._state.following.append(self.FOLLOW_expr_in_connect_1805)
                        expr50 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr50.tree)


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

        STOP51 = None
        WITH52 = None
        expr53 = None


        STOP51_tree = None
        WITH52_tree = None

        try:
            try:
                # SelectExpr.g:175:7: ( STOP WITH expr )
                # SelectExpr.g:175:9: STOP WITH expr
                pass 
                root_0 = self._adaptor.nil()

                STOP51=self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_1818)
                if self._state.backtracking == 0:

                    STOP51_tree = self._adaptor.createWithPayload(STOP51)
                    root_0 = self._adaptor.becomeRoot(STOP51_tree, root_0)

                WITH52=self.match(self.input, WITH, self.FOLLOW_WITH_in_stop_1821)
                self._state.following.append(self.FOLLOW_expr_in_stop_1824)
                expr53 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr53.tree)



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

        GROUP54 = None
        BY55 = None
        PHRASE56 = None
        SEP58 = None
        PHRASE59 = None
        function57 = None

        function60 = None


        GROUP54_tree = None
        BY55_tree = None
        PHRASE56_tree = None
        SEP58_tree = None
        PHRASE59_tree = None

        try:
            try:
                # SelectExpr.g:178:8: ( GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* )
                # SelectExpr.g:178:10: GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )*
                pass 
                root_0 = self._adaptor.nil()

                GROUP54=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_1833)
                if self._state.backtracking == 0:

                    GROUP54_tree = self._adaptor.createWithPayload(GROUP54)
                    root_0 = self._adaptor.becomeRoot(GROUP54_tree, root_0)

                BY55=self.match(self.input, BY, self.FOLLOW_BY_in_group_1836)
                # SelectExpr.g:178:21: ( PHRASE | function )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == PHRASE) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == 108) :
                        alt22 = 2
                    elif (LA22_1 == EOF or (SEP <= LA22_1 <= END) or LA22_1 == AND or (XOR <= LA22_1 <= OR) or LA22_1 == IN or (EQ <= LA22_1 <= POW) or (LIST_BEGIN <= LA22_1 <= LIST_END) or LA22_1 == AGE_END or (WHERE <= LA22_1 <= ORDER) or LA22_1 == GROUP or LA22_1 == HAVING or LA22_1 == AS or (CONNECT <= LA22_1 <= STOP) or LA22_1 == 109) :
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
                    PHRASE56=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1841)
                    if self._state.backtracking == 0:

                        PHRASE56_tree = self._adaptor.createWithPayload(PHRASE56)
                        self._adaptor.addChild(root_0, PHRASE56_tree)



                elif alt22 == 2:
                    # SelectExpr.g:178:32: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_group_1845)
                    function57 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function57.tree)



                # SelectExpr.g:178:43: ( SEP ( PHRASE | function ) )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == SEP) :
                        LA24_2 = self.input.LA(2)

                        if (LA24_2 == PHRASE) :
                            LA24_3 = self.input.LA(3)

                            if (self.synpred27_SelectExpr()) :
                                alt24 = 1






                    if alt24 == 1:
                        # SelectExpr.g:178:44: SEP ( PHRASE | function )
                        pass 
                        SEP58=self.match(self.input, SEP, self.FOLLOW_SEP_in_group_1850)
                        # SelectExpr.g:178:49: ( PHRASE | function )
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == PHRASE) :
                            LA23_1 = self.input.LA(2)

                            if (LA23_1 == 108) :
                                alt23 = 2
                            elif (LA23_1 == EOF or (SEP <= LA23_1 <= END) or LA23_1 == AND or (XOR <= LA23_1 <= OR) or LA23_1 == IN or (EQ <= LA23_1 <= POW) or (LIST_BEGIN <= LA23_1 <= LIST_END) or LA23_1 == AGE_END or (WHERE <= LA23_1 <= ORDER) or LA23_1 == GROUP or LA23_1 == HAVING or LA23_1 == AS or (CONNECT <= LA23_1 <= STOP) or LA23_1 == 109) :
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
                            PHRASE59=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1855)
                            if self._state.backtracking == 0:

                                PHRASE59_tree = self._adaptor.createWithPayload(PHRASE59)
                                self._adaptor.addChild(root_0, PHRASE59_tree)



                        elif alt23 == 2:
                            # SelectExpr.g:178:60: function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_group_1859)
                            function60 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function60.tree)





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

        HAVING61 = None
        expr62 = None


        HAVING61_tree = None

        try:
            try:
                # SelectExpr.g:181:9: ( HAVING expr )
                # SelectExpr.g:181:11: HAVING expr
                pass 
                root_0 = self._adaptor.nil()

                HAVING61=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_1873)
                if self._state.backtracking == 0:

                    HAVING61_tree = self._adaptor.createWithPayload(HAVING61)
                    root_0 = self._adaptor.becomeRoot(HAVING61_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_having_1876)
                expr62 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr62.tree)



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

        ORDER63 = None
        BY64 = None
        PHRASE65 = None
        SEP69 = None
        PHRASE70 = None
        direction_66 = None

        function67 = None

        direction_68 = None

        direction_71 = None

        function72 = None

        direction_73 = None


        ORDER63_tree = None
        BY64_tree = None
        PHRASE65_tree = None
        SEP69_tree = None
        PHRASE70_tree = None

        try:
            try:
                # SelectExpr.g:184:8: ( ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* )
                # SelectExpr.g:184:10: ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )*
                pass 
                root_0 = self._adaptor.nil()

                ORDER63=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_1885)
                if self._state.backtracking == 0:

                    ORDER63_tree = self._adaptor.createWithPayload(ORDER63)
                    root_0 = self._adaptor.becomeRoot(ORDER63_tree, root_0)

                BY64=self.match(self.input, BY, self.FOLLOW_BY_in_order_1888)
                # SelectExpr.g:184:21: ( PHRASE direction_ | function direction_ )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == PHRASE) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == 108) :
                        alt25 = 2
                    elif (LA25_1 == EOF or (SEP <= LA25_1 <= END) or LA25_1 == AND or (XOR <= LA25_1 <= OR) or LA25_1 == IN or (EQ <= LA25_1 <= POW) or (LIST_BEGIN <= LA25_1 <= LIST_END) or LA25_1 == AGE_END or (WHERE <= LA25_1 <= ORDER) or LA25_1 == GROUP or LA25_1 == AS or (CONNECT <= LA25_1 <= STOP) or (ASC <= LA25_1 <= DESC) or LA25_1 == 109) :
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
                    PHRASE65=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1893)
                    if self._state.backtracking == 0:

                        PHRASE65_tree = self._adaptor.createWithPayload(PHRASE65)
                        self._adaptor.addChild(root_0, PHRASE65_tree)

                    self._state.following.append(self.FOLLOW_direction__in_order_1895)
                    direction_66 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_66.tree)


                elif alt25 == 2:
                    # SelectExpr.g:184:43: function direction_
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_order_1899)
                    function67 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function67.tree)
                    self._state.following.append(self.FOLLOW_direction__in_order_1901)
                    direction_68 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_68.tree)



                # SelectExpr.g:184:65: ( SEP ( PHRASE direction_ | function direction_ ) )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == SEP) :
                        LA27_2 = self.input.LA(2)

                        if (LA27_2 == PHRASE) :
                            LA27_3 = self.input.LA(3)

                            if (self.synpred30_SelectExpr()) :
                                alt27 = 1






                    if alt27 == 1:
                        # SelectExpr.g:184:66: SEP ( PHRASE direction_ | function direction_ )
                        pass 
                        SEP69=self.match(self.input, SEP, self.FOLLOW_SEP_in_order_1906)
                        # SelectExpr.g:184:71: ( PHRASE direction_ | function direction_ )
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == PHRASE) :
                            LA26_1 = self.input.LA(2)

                            if (LA26_1 == 108) :
                                alt26 = 2
                            elif (LA26_1 == EOF or (SEP <= LA26_1 <= END) or LA26_1 == AND or (XOR <= LA26_1 <= OR) or LA26_1 == IN or (EQ <= LA26_1 <= POW) or (LIST_BEGIN <= LA26_1 <= LIST_END) or LA26_1 == AGE_END or (WHERE <= LA26_1 <= ORDER) or LA26_1 == GROUP or LA26_1 == AS or (CONNECT <= LA26_1 <= STOP) or (ASC <= LA26_1 <= DESC) or LA26_1 == 109) :
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
                            PHRASE70=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1911)
                            if self._state.backtracking == 0:

                                PHRASE70_tree = self._adaptor.createWithPayload(PHRASE70)
                                self._adaptor.addChild(root_0, PHRASE70_tree)

                            self._state.following.append(self.FOLLOW_direction__in_order_1913)
                            direction_71 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_71.tree)


                        elif alt26 == 2:
                            # SelectExpr.g:184:93: function direction_
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_order_1917)
                            function72 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function72.tree)
                            self._state.following.append(self.FOLLOW_direction__in_order_1919)
                            direction_73 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_73.tree)





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

        set74 = None

        set74_tree = None

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
                    set74 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set74))
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

        AS75 = None
        AS_LIST76 = None
        AS_VALUE77 = None
        AS_DICT78 = None
        PHRASE79 = None
        char_literal80 = None
        char_literal82 = None
        parameter81 = None


        AS75_tree = None
        AS_LIST76_tree = None
        AS_VALUE77_tree = None
        AS_DICT78_tree = None
        PHRASE79_tree = None
        char_literal80_tree = None
        char_literal82_tree = None

        try:
            try:
                # SelectExpr.g:190:5: ( AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) )
                # SelectExpr.g:190:7: AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                pass 
                root_0 = self._adaptor.nil()

                AS75=self.match(self.input, AS, self.FOLLOW_AS_in_as_1950)
                if self._state.backtracking == 0:

                    AS75_tree = self._adaptor.createWithPayload(AS75)
                    root_0 = self._adaptor.becomeRoot(AS75_tree, root_0)

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
                    AS_LIST76=self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_1955)
                    if self._state.backtracking == 0:

                        AS_LIST76_tree = self._adaptor.createWithPayload(AS_LIST76)
                        self._adaptor.addChild(root_0, AS_LIST76_tree)



                elif alt31 == 2:
                    # SelectExpr.g:190:23: AS_VALUE
                    pass 
                    AS_VALUE77=self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_1959)
                    if self._state.backtracking == 0:

                        AS_VALUE77_tree = self._adaptor.createWithPayload(AS_VALUE77)
                        self._adaptor.addChild(root_0, AS_VALUE77_tree)



                elif alt31 == 3:
                    # SelectExpr.g:190:34: AS_DICT
                    pass 
                    AS_DICT78=self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_1963)
                    if self._state.backtracking == 0:

                        AS_DICT78_tree = self._adaptor.createWithPayload(AS_DICT78)
                        self._adaptor.addChild(root_0, AS_DICT78_tree)



                elif alt31 == 4:
                    # SelectExpr.g:190:44: PHRASE ( '(' ( parameter )? ')' )?
                    pass 
                    PHRASE79=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_1967)
                    if self._state.backtracking == 0:

                        PHRASE79_tree = self._adaptor.createWithPayload(PHRASE79)
                        self._adaptor.addChild(root_0, PHRASE79_tree)

                    # SelectExpr.g:190:51: ( '(' ( parameter )? ')' )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 108) :
                        alt30 = 1
                    if alt30 == 1:
                        # SelectExpr.g:190:52: '(' ( parameter )? ')'
                        pass 
                        char_literal80=self.match(self.input, 108, self.FOLLOW_108_in_as_1970)
                        # SelectExpr.g:190:57: ( parameter )?
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == NOT or (ADD <= LA29_0 <= SUB) or LA29_0 == IF or LA29_0 == LIST_BEGIN or LA29_0 == SELECT or LA29_0 == THIS or LA29_0 == STRING or (INTEGER <= LA29_0 <= FALSE) or LA29_0 == PHRASE or LA29_0 == 108) :
                            alt29 = 1
                        if alt29 == 1:
                            # SelectExpr.g:0:0: parameter
                            pass 
                            self._state.following.append(self.FOLLOW_parameter_in_as_1973)
                            parameter81 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter81.tree)



                        char_literal82=self.match(self.input, 109, self.FOLLOW_109_in_as_1976)









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

        assign_expr83 = None

        logic_expr84 = None



        try:
            try:
                # SelectExpr.g:193:6: ( assign_expr | logic_expr )
                alt32 = 2
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # SelectExpr.g:193:8: assign_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assign_expr_in_expr1990)
                    assign_expr83 = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assign_expr83.tree)


                elif alt32 == 2:
                    # SelectExpr.g:194:4: logic_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_logic_expr_in_expr1996)
                    logic_expr84 = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logic_expr84.tree)


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

        IF85 = None
        char_literal86 = None
        END88 = None
        END90 = None
        char_literal92 = None
        expr87 = None

        parameter89 = None

        parameter91 = None


        IF85_tree = None
        char_literal86_tree = None
        END88_tree = None
        END90_tree = None
        char_literal92_tree = None
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
                IF85=self.match(self.input, IF, self.FOLLOW_IF_in_if_statement2005) 
                if self._state.backtracking == 0:
                    stream_IF.add(IF85)
                char_literal86=self.match(self.input, 108, self.FOLLOW_108_in_if_statement2007) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal86)
                self._state.following.append(self.FOLLOW_expr_in_if_statement2009)
                expr87 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr87.tree)
                # SelectExpr.g:197:28: ( END parameter ( END parameter )? )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == END) :
                    alt34 = 1
                if alt34 == 1:
                    # SelectExpr.g:197:29: END parameter ( END parameter )?
                    pass 
                    END88=self.match(self.input, END, self.FOLLOW_END_in_if_statement2012) 
                    if self._state.backtracking == 0:
                        stream_END.add(END88)
                    self._state.following.append(self.FOLLOW_parameter_in_if_statement2014)
                    parameter89 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter89.tree)
                    # SelectExpr.g:197:43: ( END parameter )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == END) :
                        alt33 = 1
                    if alt33 == 1:
                        # SelectExpr.g:197:44: END parameter
                        pass 
                        END90=self.match(self.input, END, self.FOLLOW_END_in_if_statement2017) 
                        if self._state.backtracking == 0:
                            stream_END.add(END90)
                        self._state.following.append(self.FOLLOW_parameter_in_if_statement2019)
                        parameter91 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter91.tree)






                char_literal92=self.match(self.input, 109, self.FOLLOW_109_in_if_statement2025) 
                if self._state.backtracking == 0:
                    stream_109.add(char_literal92)

                # AST Rewrite
                # elements: parameter, parameter, expr, IF
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

        PHRASE93 = None
        ASSIGN95 = None
        ASSIGN98 = None
        age94 = None

        expr96 = None

        this_97 = None

        expr99 = None


        PHRASE93_tree = None
        ASSIGN95_tree = None
        ASSIGN98_tree = None
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
                    PHRASE93=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr2064) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE93)
                    # SelectExpr.g:201:22: ( age )?
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == AGE_BEGIN) :
                        alt35 = 1
                    if alt35 == 1:
                        # SelectExpr.g:201:23: age
                        pass 
                        self._state.following.append(self.FOLLOW_age_in_assign_expr2067)
                        age94 = self.age()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_age.add(age94.tree)



                    ASSIGN95=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2071) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN95)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2073)
                    expr96 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr96.tree)

                    # AST Rewrite
                    # elements: age, ASSIGN, expr, PHRASE
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
                    self._state.following.append(self.FOLLOW_this__in_assign_expr2092)
                    this_97 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_this_.add(this_97.tree)
                    ASSIGN98=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2094) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN98)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2096)
                    expr99 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr99.tree)

                    # AST Rewrite
                    # elements: this_, expr, ASSIGN
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

        logic_or100 = None



        try:
            try:
                # SelectExpr.g:203:12: ( logic_or )
                # SelectExpr.g:203:14: logic_or
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_or_in_logic_expr2115)
                logic_or100 = self.logic_or()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_or100.tree)



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

        OR102 = None
        logic_xor101 = None

        logic_xor103 = None


        OR102_tree = None

        try:
            try:
                # SelectExpr.g:204:11: ( logic_xor ( OR logic_xor )* )
                # SelectExpr.g:204:13: logic_xor ( OR logic_xor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2124)
                logic_xor101 = self.logic_xor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_xor101.tree)
                # SelectExpr.g:204:23: ( OR logic_xor )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == OR) :
                        LA37_2 = self.input.LA(2)

                        if (self.synpred43_SelectExpr()) :
                            alt37 = 1




                    if alt37 == 1:
                        # SelectExpr.g:204:24: OR logic_xor
                        pass 
                        OR102=self.match(self.input, OR, self.FOLLOW_OR_in_logic_or2127)
                        if self._state.backtracking == 0:

                            OR102_tree = self._adaptor.createWithPayload(OR102)
                            root_0 = self._adaptor.becomeRoot(OR102_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2131)
                        logic_xor103 = self.logic_xor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_xor103.tree)


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

        XOR105 = None
        logic_and104 = None

        logic_and106 = None


        XOR105_tree = None

        try:
            try:
                # SelectExpr.g:205:11: ( logic_and ( XOR logic_and )* )
                # SelectExpr.g:205:13: logic_and ( XOR logic_and )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2141)
                logic_and104 = self.logic_and()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_and104.tree)
                # SelectExpr.g:205:23: ( XOR logic_and )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == XOR) :
                        LA38_2 = self.input.LA(2)

                        if (self.synpred44_SelectExpr()) :
                            alt38 = 1




                    if alt38 == 1:
                        # SelectExpr.g:205:24: XOR logic_and
                        pass 
                        XOR105=self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_xor2144)
                        if self._state.backtracking == 0:

                            XOR105_tree = self._adaptor.createWithPayload(XOR105)
                            root_0 = self._adaptor.becomeRoot(XOR105_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2147)
                        logic_and106 = self.logic_and()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_and106.tree)


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

        AND108 = None
        logic_not107 = None

        logic_not109 = None


        AND108_tree = None

        try:
            try:
                # SelectExpr.g:206:11: ( logic_not ( AND logic_not )* )
                # SelectExpr.g:206:13: logic_not ( AND logic_not )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_not_in_logic_and2157)
                logic_not107 = self.logic_not()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_not107.tree)
                # SelectExpr.g:206:23: ( AND logic_not )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == AND) :
                        LA39_2 = self.input.LA(2)

                        if (self.synpred45_SelectExpr()) :
                            alt39 = 1




                    if alt39 == 1:
                        # SelectExpr.g:206:24: AND logic_not
                        pass 
                        AND108=self.match(self.input, AND, self.FOLLOW_AND_in_logic_and2160)
                        if self._state.backtracking == 0:

                            AND108_tree = self._adaptor.createWithPayload(AND108)
                            root_0 = self._adaptor.becomeRoot(AND108_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_not_in_logic_and2163)
                        logic_not109 = self.logic_not()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_not109.tree)


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

        NOT110 = None
        compare_expr111 = None


        NOT110_tree = None

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
                    NOT110=self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_not2174)
                    if self._state.backtracking == 0:

                        NOT110_tree = self._adaptor.createWithPayload(NOT110)
                        root_0 = self._adaptor.becomeRoot(NOT110_tree, root_0)




                self._state.following.append(self.FOLLOW_compare_expr_in_logic_not2179)
                compare_expr111 = self.compare_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_expr111.tree)



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

        compare_in112 = None



        try:
            try:
                # SelectExpr.g:209:14: ( compare_in )
                # SelectExpr.g:209:16: compare_in
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_in_in_compare_expr2188)
                compare_in112 = self.compare_in()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_in112.tree)



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

        IN114 = None
        compare_eq113 = None

        atom115 = None


        IN114_tree = None

        try:
            try:
                # SelectExpr.g:210:12: ( compare_eq ( IN atom )* )
                # SelectExpr.g:210:14: compare_eq ( IN atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_eq_in_compare_in2196)
                compare_eq113 = self.compare_eq()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_eq113.tree)
                # SelectExpr.g:210:25: ( IN atom )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == IN) :
                        LA41_2 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt41 = 1




                    if alt41 == 1:
                        # SelectExpr.g:210:26: IN atom
                        pass 
                        IN114=self.match(self.input, IN, self.FOLLOW_IN_in_compare_in2199)
                        if self._state.backtracking == 0:

                            IN114_tree = self._adaptor.createWithPayload(IN114)
                            root_0 = self._adaptor.becomeRoot(IN114_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_compare_in2202)
                        atom115 = self.atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, atom115.tree)


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

        EQ117 = None
        compare_ne116 = None

        compare_ne118 = None


        EQ117_tree = None

        try:
            try:
                # SelectExpr.g:211:12: ( compare_ne ( EQ compare_ne )* )
                # SelectExpr.g:211:14: compare_ne ( EQ compare_ne )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2212)
                compare_ne116 = self.compare_ne()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ne116.tree)
                # SelectExpr.g:211:25: ( EQ compare_ne )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == EQ) :
                        LA42_2 = self.input.LA(2)

                        if (self.synpred48_SelectExpr()) :
                            alt42 = 1




                    if alt42 == 1:
                        # SelectExpr.g:211:26: EQ compare_ne
                        pass 
                        EQ117=self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_eq2215)
                        if self._state.backtracking == 0:

                            EQ117_tree = self._adaptor.createWithPayload(EQ117)
                            root_0 = self._adaptor.becomeRoot(EQ117_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2218)
                        compare_ne118 = self.compare_ne()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ne118.tree)


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

        NE120 = None
        compare_ge119 = None

        compare_ge121 = None


        NE120_tree = None

        try:
            try:
                # SelectExpr.g:212:12: ( compare_ge ( NE compare_ge )* )
                # SelectExpr.g:212:14: compare_ge ( NE compare_ge )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2228)
                compare_ge119 = self.compare_ge()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ge119.tree)
                # SelectExpr.g:212:25: ( NE compare_ge )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == NE) :
                        LA43_2 = self.input.LA(2)

                        if (self.synpred49_SelectExpr()) :
                            alt43 = 1




                    if alt43 == 1:
                        # SelectExpr.g:212:26: NE compare_ge
                        pass 
                        NE120=self.match(self.input, NE, self.FOLLOW_NE_in_compare_ne2231)
                        if self._state.backtracking == 0:

                            NE120_tree = self._adaptor.createWithPayload(NE120)
                            root_0 = self._adaptor.becomeRoot(NE120_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2234)
                        compare_ge121 = self.compare_ge()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ge121.tree)


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

        GE123 = None
        compare_gt122 = None

        compare_gt124 = None


        GE123_tree = None

        try:
            try:
                # SelectExpr.g:213:12: ( compare_gt ( GE compare_gt )* )
                # SelectExpr.g:213:14: compare_gt ( GE compare_gt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2244)
                compare_gt122 = self.compare_gt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_gt122.tree)
                # SelectExpr.g:213:25: ( GE compare_gt )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == GE) :
                        LA44_2 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt44 = 1




                    if alt44 == 1:
                        # SelectExpr.g:213:26: GE compare_gt
                        pass 
                        GE123=self.match(self.input, GE, self.FOLLOW_GE_in_compare_ge2247)
                        if self._state.backtracking == 0:

                            GE123_tree = self._adaptor.createWithPayload(GE123)
                            root_0 = self._adaptor.becomeRoot(GE123_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2250)
                        compare_gt124 = self.compare_gt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_gt124.tree)


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

        GT126 = None
        compare_le125 = None

        compare_le127 = None


        GT126_tree = None

        try:
            try:
                # SelectExpr.g:214:12: ( compare_le ( GT compare_le )* )
                # SelectExpr.g:214:14: compare_le ( GT compare_le )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2260)
                compare_le125 = self.compare_le()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_le125.tree)
                # SelectExpr.g:214:25: ( GT compare_le )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == GT) :
                        LA45_2 = self.input.LA(2)

                        if (self.synpred51_SelectExpr()) :
                            alt45 = 1




                    if alt45 == 1:
                        # SelectExpr.g:214:26: GT compare_le
                        pass 
                        GT126=self.match(self.input, GT, self.FOLLOW_GT_in_compare_gt2263)
                        if self._state.backtracking == 0:

                            GT126_tree = self._adaptor.createWithPayload(GT126)
                            root_0 = self._adaptor.becomeRoot(GT126_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2266)
                        compare_le127 = self.compare_le()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_le127.tree)


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

        LE129 = None
        compare_lt128 = None

        compare_lt130 = None


        LE129_tree = None

        try:
            try:
                # SelectExpr.g:215:12: ( compare_lt ( LE compare_lt )* )
                # SelectExpr.g:215:14: compare_lt ( LE compare_lt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2276)
                compare_lt128 = self.compare_lt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_lt128.tree)
                # SelectExpr.g:215:25: ( LE compare_lt )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == LE) :
                        LA46_2 = self.input.LA(2)

                        if (self.synpred52_SelectExpr()) :
                            alt46 = 1




                    if alt46 == 1:
                        # SelectExpr.g:215:26: LE compare_lt
                        pass 
                        LE129=self.match(self.input, LE, self.FOLLOW_LE_in_compare_le2279)
                        if self._state.backtracking == 0:

                            LE129_tree = self._adaptor.createWithPayload(LE129)
                            root_0 = self._adaptor.becomeRoot(LE129_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2282)
                        compare_lt130 = self.compare_lt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_lt130.tree)


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

        LT132 = None
        arithmetic_expr131 = None

        arithmetic_expr133 = None


        LT132_tree = None

        try:
            try:
                # SelectExpr.g:216:12: ( arithmetic_expr ( LT arithmetic_expr )* )
                # SelectExpr.g:216:14: arithmetic_expr ( LT arithmetic_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2292)
                arithmetic_expr131 = self.arithmetic_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_expr131.tree)
                # SelectExpr.g:216:30: ( LT arithmetic_expr )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == LT) :
                        LA47_2 = self.input.LA(2)

                        if (self.synpred53_SelectExpr()) :
                            alt47 = 1




                    if alt47 == 1:
                        # SelectExpr.g:216:31: LT arithmetic_expr
                        pass 
                        LT132=self.match(self.input, LT, self.FOLLOW_LT_in_compare_lt2295)
                        if self._state.backtracking == 0:

                            LT132_tree = self._adaptor.createWithPayload(LT132)
                            root_0 = self._adaptor.becomeRoot(LT132_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2298)
                        arithmetic_expr133 = self.arithmetic_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_expr133.tree)


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

        arithmetic_sub_add134 = None



        try:
            try:
                # SelectExpr.g:218:17: ( arithmetic_sub_add )
                # SelectExpr.g:218:19: arithmetic_sub_add
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_sub_add_in_arithmetic_expr2309)
                arithmetic_sub_add134 = self.arithmetic_sub_add()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_sub_add134.tree)



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

        SUB136 = None
        ADD137 = None
        arithmetic_mul_div_mod135 = None

        arithmetic_mul_div_mod138 = None


        SUB136_tree = None
        ADD137_tree = None

        try:
            try:
                # SelectExpr.g:219:20: ( arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* )
                # SelectExpr.g:219:22: arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2317)
                arithmetic_mul_div_mod135 = self.arithmetic_mul_div_mod()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_mul_div_mod135.tree)
                # SelectExpr.g:219:45: ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == SUB) :
                        LA49_2 = self.input.LA(2)

                        if (self.synpred55_SelectExpr()) :
                            alt49 = 1


                    elif (LA49_0 == ADD) :
                        LA49_3 = self.input.LA(2)

                        if (self.synpred55_SelectExpr()) :
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
                            SUB136=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_sub_add2321)
                            if self._state.backtracking == 0:

                                SUB136_tree = self._adaptor.createWithPayload(SUB136)
                                root_0 = self._adaptor.becomeRoot(SUB136_tree, root_0)



                        elif alt48 == 2:
                            # SelectExpr.g:219:52: ADD
                            pass 
                            ADD137=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_sub_add2324)
                            if self._state.backtracking == 0:

                                ADD137_tree = self._adaptor.createWithPayload(ADD137)
                                root_0 = self._adaptor.becomeRoot(ADD137_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2328)
                        arithmetic_mul_div_mod138 = self.arithmetic_mul_div_mod()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_mul_div_mod138.tree)


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

        MUL140 = None
        DIV141 = None
        MOD142 = None
        arithmetic_pow139 = None

        arithmetic_pow143 = None


        MUL140_tree = None
        DIV141_tree = None
        MOD142_tree = None

        try:
            try:
                # SelectExpr.g:220:24: ( arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* )
                # SelectExpr.g:220:26: arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2338)
                arithmetic_pow139 = self.arithmetic_pow()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_pow139.tree)
                # SelectExpr.g:220:41: ( ( MUL | DIV | MOD ) arithmetic_pow )*
                while True: #loop51
                    alt51 = 2
                    LA51 = self.input.LA(1)
                    if LA51 == MUL:
                        LA51_2 = self.input.LA(2)

                        if (self.synpred58_SelectExpr()) :
                            alt51 = 1


                    elif LA51 == DIV:
                        LA51_3 = self.input.LA(2)

                        if (self.synpred58_SelectExpr()) :
                            alt51 = 1


                    elif LA51 == MOD:
                        LA51_4 = self.input.LA(2)

                        if (self.synpred58_SelectExpr()) :
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
                            MUL140=self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_mul_div_mod2342)
                            if self._state.backtracking == 0:

                                MUL140_tree = self._adaptor.createWithPayload(MUL140)
                                root_0 = self._adaptor.becomeRoot(MUL140_tree, root_0)



                        elif alt50 == 2:
                            # SelectExpr.g:220:50: DIV
                            pass 
                            DIV141=self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_mul_div_mod2347)
                            if self._state.backtracking == 0:

                                DIV141_tree = self._adaptor.createWithPayload(DIV141)
                                root_0 = self._adaptor.becomeRoot(DIV141_tree, root_0)



                        elif alt50 == 3:
                            # SelectExpr.g:220:57: MOD
                            pass 
                            MOD142=self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_mul_div_mod2352)
                            if self._state.backtracking == 0:

                                MOD142_tree = self._adaptor.createWithPayload(MOD142)
                                root_0 = self._adaptor.becomeRoot(MOD142_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2356)
                        arithmetic_pow143 = self.arithmetic_pow()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_pow143.tree)


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

        POW145 = None
        arithmetic_unary144 = None

        arithmetic_unary146 = None


        POW145_tree = None

        try:
            try:
                # SelectExpr.g:221:16: ( arithmetic_unary ( POW arithmetic_unary )* )
                # SelectExpr.g:221:18: arithmetic_unary ( POW arithmetic_unary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2366)
                arithmetic_unary144 = self.arithmetic_unary()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_unary144.tree)
                # SelectExpr.g:221:35: ( POW arithmetic_unary )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == POW) :
                        LA52_2 = self.input.LA(2)

                        if (self.synpred59_SelectExpr()) :
                            alt52 = 1




                    if alt52 == 1:
                        # SelectExpr.g:221:36: POW arithmetic_unary
                        pass 
                        POW145=self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_pow2369)
                        if self._state.backtracking == 0:

                            POW145_tree = self._adaptor.createWithPayload(POW145)
                            root_0 = self._adaptor.becomeRoot(POW145_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2372)
                        arithmetic_unary146 = self.arithmetic_unary()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_unary146.tree)


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

        SUB147 = None
        ADD149 = None
        LIST_BEGIN152 = None
        LIST_END154 = None
        atom148 = None

        atom150 = None

        atom151 = None

        parameter153 = None

        atom155 = None


        SUB147_tree = None
        ADD149_tree = None
        LIST_BEGIN152_tree = None
        LIST_END154_tree = None
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
                    SUB147=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_unary2383) 
                    if self._state.backtracking == 0:
                        stream_SUB.add(SUB147)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2385)
                    atom148 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom148.tree)

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
                    ADD149=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_unary2399) 
                    if self._state.backtracking == 0:
                        stream_ADD.add(ADD149)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2401)
                    atom150 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom150.tree)

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
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2415)
                    atom151 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom151.tree)
                    LIST_BEGIN152=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_arithmetic_unary2417) 
                    if self._state.backtracking == 0:
                        stream_LIST_BEGIN.add(LIST_BEGIN152)
                    self._state.following.append(self.FOLLOW_parameter_in_arithmetic_unary2419)
                    parameter153 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter153.tree)
                    LIST_END154=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_arithmetic_unary2421) 
                    if self._state.backtracking == 0:
                        stream_LIST_END.add(LIST_END154)

                    # AST Rewrite
                    # elements: atom, parameter
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

                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2437)
                    atom155 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom155.tree)


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

        char_literal160 = None
        char_literal162 = None
        value156 = None

        variable157 = None

        if_statement158 = None

        function159 = None

        expr161 = None

        statement_select163 = None


        char_literal160_tree = None
        char_literal162_tree = None

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
                    elif LA54 == EOF or LA54 == SEP or LA54 == END or LA54 == AND or LA54 == XOR or LA54 == OR or LA54 == IN or LA54 == EQ or LA54 == NE or LA54 == LE or LA54 == GE or LA54 == LT or LA54 == GT or LA54 == ADD or LA54 == SUB or LA54 == MUL or LA54 == DIV or LA54 == MOD or LA54 == POW or LA54 == LIST_BEGIN or LA54 == LIST_END or LA54 == AGE_BEGIN or LA54 == AGE_END or LA54 == WHERE or LA54 == ORDER or LA54 == GROUP or LA54 == AS or LA54 == CONNECT or LA54 == START or LA54 == STOP or LA54 == 109:
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

                    self._state.following.append(self.FOLLOW_value_in_atom2448)
                    value156 = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, value156.tree)


                elif alt54 == 2:
                    # SelectExpr.g:231:4: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_atom2453)
                    variable157 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable157.tree)


                elif alt54 == 3:
                    # SelectExpr.g:232:4: if_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_statement_in_atom2458)
                    if_statement158 = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_statement158.tree)


                elif alt54 == 4:
                    # SelectExpr.g:233:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_atom2463)
                    function159 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function159.tree)


                elif alt54 == 5:
                    # SelectExpr.g:234:4: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal160=self.match(self.input, 108, self.FOLLOW_108_in_atom2468)
                    self._state.following.append(self.FOLLOW_expr_in_atom2471)
                    expr161 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr161.tree)
                    char_literal162=self.match(self.input, 109, self.FOLLOW_109_in_atom2473)


                elif alt54 == 6:
                    # SelectExpr.g:235:4: statement_select
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_atom2479)
                    statement_select163 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select163.tree)


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

        PHRASE164 = None
        char_literal165 = None
        char_literal167 = None
        parameter166 = None


        PHRASE164_tree = None
        char_literal165_tree = None
        char_literal167_tree = None
        stream_108 = RewriteRuleTokenStream(self._adaptor, "token 108")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_109 = RewriteRuleTokenStream(self._adaptor, "token 109")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # SelectExpr.g:238:10: ( PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) )
                # SelectExpr.g:238:12: PHRASE '(' ( parameter )? ')'
                pass 
                PHRASE164=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function2488) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE164)
                char_literal165=self.match(self.input, 108, self.FOLLOW_108_in_function2490) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal165)
                # SelectExpr.g:238:23: ( parameter )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == NOT or (ADD <= LA55_0 <= SUB) or LA55_0 == IF or LA55_0 == LIST_BEGIN or LA55_0 == SELECT or LA55_0 == THIS or LA55_0 == STRING or (INTEGER <= LA55_0 <= FALSE) or LA55_0 == PHRASE or LA55_0 == 108) :
                    alt55 = 1
                if alt55 == 1:
                    # SelectExpr.g:0:0: parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function2492)
                    parameter166 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter166.tree)



                char_literal167=self.match(self.input, 109, self.FOLLOW_109_in_function2495) 
                if self._state.backtracking == 0:
                    stream_109.add(char_literal167)

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

        SEP169 = None
        expr168 = None

        expr170 = None


        SEP169_tree = None

        try:
            try:
                # SelectExpr.g:241:11: ( expr ( SEP expr )* )
                # SelectExpr.g:241:13: expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_parameter2515)
                expr168 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr168.tree)
                # SelectExpr.g:241:18: ( SEP expr )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == SEP) :
                        alt56 = 1


                    if alt56 == 1:
                        # SelectExpr.g:241:19: SEP expr
                        pass 
                        SEP169=self.match(self.input, SEP, self.FOLLOW_SEP_in_parameter2518)
                        self._state.following.append(self.FOLLOW_expr_in_parameter2521)
                        expr170 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr170.tree)


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

        PHRASE171 = None
        age172 = None


        PHRASE171_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:244:10: ( PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) )
                # SelectExpr.g:244:12: PHRASE ( age )?
                pass 
                PHRASE171=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable2532) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE171)
                # SelectExpr.g:244:19: ( age )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == AGE_BEGIN) :
                    alt57 = 1
                if alt57 == 1:
                    # SelectExpr.g:244:20: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable2535)
                    age172 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age172.tree)




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

        AGE_BEGIN173 = None
        AGE_END175 = None
        expr174 = None


        AGE_BEGIN173_tree = None
        AGE_END175_tree = None
        stream_AGE_BEGIN = RewriteRuleTokenStream(self._adaptor, "token AGE_BEGIN")
        stream_AGE_END = RewriteRuleTokenStream(self._adaptor, "token AGE_END")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:247:5: ( AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) )
                # SelectExpr.g:247:7: AGE_BEGIN ( expr )? AGE_END
                pass 
                AGE_BEGIN173=self.match(self.input, AGE_BEGIN, self.FOLLOW_AGE_BEGIN_in_age2559) 
                if self._state.backtracking == 0:
                    stream_AGE_BEGIN.add(AGE_BEGIN173)
                # SelectExpr.g:247:17: ( expr )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == NOT or (ADD <= LA58_0 <= SUB) or LA58_0 == IF or LA58_0 == LIST_BEGIN or LA58_0 == SELECT or LA58_0 == THIS or LA58_0 == STRING or (INTEGER <= LA58_0 <= FALSE) or LA58_0 == PHRASE or LA58_0 == 108) :
                    alt58 = 1
                if alt58 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_age2561)
                    expr174 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr174.tree)



                AGE_END175=self.match(self.input, AGE_END, self.FOLLOW_AGE_END_in_age2564) 
                if self._state.backtracking == 0:
                    stream_AGE_END.add(AGE_END175)

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

        STRING176 = None
        FLOAT177 = None
        INTEGER178 = None
        TRUE179 = None
        FALSE180 = None
        this_181 = None

        list_182 = None


        STRING176_tree = None
        FLOAT177_tree = None
        INTEGER178_tree = None
        TRUE179_tree = None
        FALSE180_tree = None
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
                    STRING176=self.match(self.input, STRING, self.FOLLOW_STRING_in_value2582) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING176)

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
                    FLOAT177=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value2596) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT177)

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
                    INTEGER178=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value2610) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER178)

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
                    TRUE179=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value2623) 
                    if self._state.backtracking == 0:
                        stream_TRUE.add(TRUE179)

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
                    FALSE180=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value2637) 
                    if self._state.backtracking == 0:
                        stream_FALSE.add(FALSE180)

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

                    self._state.following.append(self.FOLLOW_this__in_value2651)
                    this_181 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, this_181.tree)


                elif alt59 == 7:
                    # SelectExpr.g:256:4: list_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list__in_value2656)
                    list_182 = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_182.tree)


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

        PHRASE183 = None
        DOT184 = None
        THIS185 = None

        PHRASE183_tree = None
        DOT184_tree = None
        THIS185_tree = None
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
                    PHRASE183=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_2667) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE183)
                    DOT184=self.match(self.input, DOT, self.FOLLOW_DOT_in_this_2669) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT184)



                THIS185=self.match(self.input, THIS, self.FOLLOW_THIS_in_this_2673) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS185)

                # AST Rewrite
                # elements: PHRASE, THIS
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

        LIST_BEGIN186 = None
        SEP188 = None
        LIST_END190 = None
        expr187 = None

        expr189 = None


        LIST_BEGIN186_tree = None
        SEP188_tree = None
        LIST_END190_tree = None
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_SEP = RewriteRuleTokenStream(self._adaptor, "token SEP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:262:7: ( LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) )
                # SelectExpr.g:262:10: LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END
                pass 
                LIST_BEGIN186=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_list_2694) 
                if self._state.backtracking == 0:
                    stream_LIST_BEGIN.add(LIST_BEGIN186)
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
                    self._state.following.append(self.FOLLOW_expr_in_list_2698)
                    expr187 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr187.tree)



                # SelectExpr.g:262:29: ( SEP expr )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == SEP) :
                        alt62 = 1


                    if alt62 == 1:
                        # SelectExpr.g:262:30: SEP expr
                        pass 
                        SEP188=self.match(self.input, SEP, self.FOLLOW_SEP_in_list_2702) 
                        if self._state.backtracking == 0:
                            stream_SEP.add(SEP188)
                        self._state.following.append(self.FOLLOW_expr_in_list_2704)
                        expr189 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr189.tree)


                    else:
                        break #loop62



                LIST_END190=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_list_2710) 
                if self._state.backtracking == 0:
                    stream_LIST_END.add(LIST_END190)

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
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectExpr1531)
        self.statement_select()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred2_SelectExpr1533)


    # $ANTLR end "synpred2_SelectExpr"



    # $ANTLR start "synpred3_SelectExpr"
    def synpred3_SelectExpr_fragment(self, ):
        # SelectExpr.g:152:4: ( expr END )
        # SelectExpr.g:152:4: expr END
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred3_SelectExpr1539)
        self.expr()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred3_SelectExpr1541)


    # $ANTLR end "synpred3_SelectExpr"



    # $ANTLR start "synpred4_SelectExpr"
    def synpred4_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:17: ( where_ )
        # SelectExpr.g:157:17: where_
        pass 
        self._state.following.append(self.FOLLOW_where__in_synpred4_SelectExpr1563)
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
            self._state.following.append(self.FOLLOW_start__in_synpred6_SelectExpr1569)
            self.start_()

            self._state.following.pop()



        self._state.following.append(self.FOLLOW_connect__in_synpred6_SelectExpr1573)
        self.connect_()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_stop__in_synpred6_SelectExpr1575)
        self.stop_()

        self._state.following.pop()


    # $ANTLR end "synpred6_SelectExpr"



    # $ANTLR start "synpred8_SelectExpr"
    def synpred8_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:55: ( group_ ( having_ )? )
        # SelectExpr.g:157:55: group_ ( having_ )?
        pass 
        self._state.following.append(self.FOLLOW_group__in_synpred8_SelectExpr1580)
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
            self._state.following.append(self.FOLLOW_having__in_synpred8_SelectExpr1583)
            self.having_()

            self._state.following.pop()





    # $ANTLR end "synpred8_SelectExpr"



    # $ANTLR start "synpred9_SelectExpr"
    def synpred9_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:76: ( order_ )
        # SelectExpr.g:157:76: order_
        pass 
        self._state.following.append(self.FOLLOW_order__in_synpred9_SelectExpr1590)
        self.order_()

        self._state.following.pop()


    # $ANTLR end "synpred9_SelectExpr"



    # $ANTLR start "synpred10_SelectExpr"
    def synpred10_SelectExpr_fragment(self, ):
        # SelectExpr.g:157:86: ( as_ )
        # SelectExpr.g:157:86: as_
        pass 
        self._state.following.append(self.FOLLOW_as__in_synpred10_SelectExpr1595)
        self.as_()

        self._state.following.pop()


    # $ANTLR end "synpred10_SelectExpr"



    # $ANTLR start "synpred17_SelectExpr"
    def synpred17_SelectExpr_fragment(self, ):
        # SelectExpr.g:163:21: ( SEP expr )
        # SelectExpr.g:163:21: SEP expr
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred17_SelectExpr1712)
        self._state.following.append(self.FOLLOW_expr_in_synpred17_SelectExpr1715)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectExpr"



    # $ANTLR start "synpred27_SelectExpr"
    def synpred27_SelectExpr_fragment(self, ):
        # SelectExpr.g:178:44: ( SEP ( PHRASE | function ) )
        # SelectExpr.g:178:44: SEP ( PHRASE | function )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred27_SelectExpr1850)
        # SelectExpr.g:178:49: ( PHRASE | function )
        alt66 = 2
        LA66_0 = self.input.LA(1)

        if (LA66_0 == PHRASE) :
            LA66_1 = self.input.LA(2)

            if (LA66_1 == 108) :
                alt66 = 2
            elif (LA66_1 == EOF) :
                alt66 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 66, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 66, 0, self.input)

            raise nvae

        if alt66 == 1:
            # SelectExpr.g:178:51: PHRASE
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred27_SelectExpr1855)


        elif alt66 == 2:
            # SelectExpr.g:178:60: function
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred27_SelectExpr1859)
            self.function()

            self._state.following.pop()





    # $ANTLR end "synpred27_SelectExpr"



    # $ANTLR start "synpred30_SelectExpr"
    def synpred30_SelectExpr_fragment(self, ):
        # SelectExpr.g:184:66: ( SEP ( PHRASE direction_ | function direction_ ) )
        # SelectExpr.g:184:66: SEP ( PHRASE direction_ | function direction_ )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred30_SelectExpr1906)
        # SelectExpr.g:184:71: ( PHRASE direction_ | function direction_ )
        alt67 = 2
        LA67_0 = self.input.LA(1)

        if (LA67_0 == PHRASE) :
            LA67_1 = self.input.LA(2)

            if (LA67_1 == 108) :
                alt67 = 2
            elif (LA67_1 == EOF or (ASC <= LA67_1 <= DESC)) :
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
            # SelectExpr.g:184:73: PHRASE direction_
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred30_SelectExpr1911)
            self._state.following.append(self.FOLLOW_direction__in_synpred30_SelectExpr1913)
            self.direction_()

            self._state.following.pop()


        elif alt67 == 2:
            # SelectExpr.g:184:93: function direction_
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred30_SelectExpr1917)
            self.function()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_direction__in_synpred30_SelectExpr1919)
            self.direction_()

            self._state.following.pop()





    # $ANTLR end "synpred30_SelectExpr"



    # $ANTLR start "synpred38_SelectExpr"
    def synpred38_SelectExpr_fragment(self, ):
        # SelectExpr.g:193:8: ( assign_expr )
        # SelectExpr.g:193:8: assign_expr
        pass 
        self._state.following.append(self.FOLLOW_assign_expr_in_synpred38_SelectExpr1990)
        self.assign_expr()

        self._state.following.pop()


    # $ANTLR end "synpred38_SelectExpr"



    # $ANTLR start "synpred43_SelectExpr"
    def synpred43_SelectExpr_fragment(self, ):
        # SelectExpr.g:204:24: ( OR logic_xor )
        # SelectExpr.g:204:24: OR logic_xor
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred43_SelectExpr2127)
        self._state.following.append(self.FOLLOW_logic_xor_in_synpred43_SelectExpr2131)
        self.logic_xor()

        self._state.following.pop()


    # $ANTLR end "synpred43_SelectExpr"



    # $ANTLR start "synpred44_SelectExpr"
    def synpred44_SelectExpr_fragment(self, ):
        # SelectExpr.g:205:24: ( XOR logic_and )
        # SelectExpr.g:205:24: XOR logic_and
        pass 
        self.match(self.input, XOR, self.FOLLOW_XOR_in_synpred44_SelectExpr2144)
        self._state.following.append(self.FOLLOW_logic_and_in_synpred44_SelectExpr2147)
        self.logic_and()

        self._state.following.pop()


    # $ANTLR end "synpred44_SelectExpr"



    # $ANTLR start "synpred45_SelectExpr"
    def synpred45_SelectExpr_fragment(self, ):
        # SelectExpr.g:206:24: ( AND logic_not )
        # SelectExpr.g:206:24: AND logic_not
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred45_SelectExpr2160)
        self._state.following.append(self.FOLLOW_logic_not_in_synpred45_SelectExpr2163)
        self.logic_not()

        self._state.following.pop()


    # $ANTLR end "synpred45_SelectExpr"



    # $ANTLR start "synpred47_SelectExpr"
    def synpred47_SelectExpr_fragment(self, ):
        # SelectExpr.g:210:26: ( IN atom )
        # SelectExpr.g:210:26: IN atom
        pass 
        self.match(self.input, IN, self.FOLLOW_IN_in_synpred47_SelectExpr2199)
        self._state.following.append(self.FOLLOW_atom_in_synpred47_SelectExpr2202)
        self.atom()

        self._state.following.pop()


    # $ANTLR end "synpred47_SelectExpr"



    # $ANTLR start "synpred48_SelectExpr"
    def synpred48_SelectExpr_fragment(self, ):
        # SelectExpr.g:211:26: ( EQ compare_ne )
        # SelectExpr.g:211:26: EQ compare_ne
        pass 
        self.match(self.input, EQ, self.FOLLOW_EQ_in_synpred48_SelectExpr2215)
        self._state.following.append(self.FOLLOW_compare_ne_in_synpred48_SelectExpr2218)
        self.compare_ne()

        self._state.following.pop()


    # $ANTLR end "synpred48_SelectExpr"



    # $ANTLR start "synpred49_SelectExpr"
    def synpred49_SelectExpr_fragment(self, ):
        # SelectExpr.g:212:26: ( NE compare_ge )
        # SelectExpr.g:212:26: NE compare_ge
        pass 
        self.match(self.input, NE, self.FOLLOW_NE_in_synpred49_SelectExpr2231)
        self._state.following.append(self.FOLLOW_compare_ge_in_synpred49_SelectExpr2234)
        self.compare_ge()

        self._state.following.pop()


    # $ANTLR end "synpred49_SelectExpr"



    # $ANTLR start "synpred50_SelectExpr"
    def synpred50_SelectExpr_fragment(self, ):
        # SelectExpr.g:213:26: ( GE compare_gt )
        # SelectExpr.g:213:26: GE compare_gt
        pass 
        self.match(self.input, GE, self.FOLLOW_GE_in_synpred50_SelectExpr2247)
        self._state.following.append(self.FOLLOW_compare_gt_in_synpred50_SelectExpr2250)
        self.compare_gt()

        self._state.following.pop()


    # $ANTLR end "synpred50_SelectExpr"



    # $ANTLR start "synpred51_SelectExpr"
    def synpred51_SelectExpr_fragment(self, ):
        # SelectExpr.g:214:26: ( GT compare_le )
        # SelectExpr.g:214:26: GT compare_le
        pass 
        self.match(self.input, GT, self.FOLLOW_GT_in_synpred51_SelectExpr2263)
        self._state.following.append(self.FOLLOW_compare_le_in_synpred51_SelectExpr2266)
        self.compare_le()

        self._state.following.pop()


    # $ANTLR end "synpred51_SelectExpr"



    # $ANTLR start "synpred52_SelectExpr"
    def synpred52_SelectExpr_fragment(self, ):
        # SelectExpr.g:215:26: ( LE compare_lt )
        # SelectExpr.g:215:26: LE compare_lt
        pass 
        self.match(self.input, LE, self.FOLLOW_LE_in_synpred52_SelectExpr2279)
        self._state.following.append(self.FOLLOW_compare_lt_in_synpred52_SelectExpr2282)
        self.compare_lt()

        self._state.following.pop()


    # $ANTLR end "synpred52_SelectExpr"



    # $ANTLR start "synpred53_SelectExpr"
    def synpred53_SelectExpr_fragment(self, ):
        # SelectExpr.g:216:31: ( LT arithmetic_expr )
        # SelectExpr.g:216:31: LT arithmetic_expr
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred53_SelectExpr2295)
        self._state.following.append(self.FOLLOW_arithmetic_expr_in_synpred53_SelectExpr2298)
        self.arithmetic_expr()

        self._state.following.pop()


    # $ANTLR end "synpred53_SelectExpr"



    # $ANTLR start "synpred55_SelectExpr"
    def synpred55_SelectExpr_fragment(self, ):
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


        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_synpred55_SelectExpr2328)
        self.arithmetic_mul_div_mod()

        self._state.following.pop()


    # $ANTLR end "synpred55_SelectExpr"



    # $ANTLR start "synpred58_SelectExpr"
    def synpred58_SelectExpr_fragment(self, ):
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


        self._state.following.append(self.FOLLOW_arithmetic_pow_in_synpred58_SelectExpr2356)
        self.arithmetic_pow()

        self._state.following.pop()


    # $ANTLR end "synpred58_SelectExpr"



    # $ANTLR start "synpred59_SelectExpr"
    def synpred59_SelectExpr_fragment(self, ):
        # SelectExpr.g:221:36: ( POW arithmetic_unary )
        # SelectExpr.g:221:36: POW arithmetic_unary
        pass 
        self.match(self.input, POW, self.FOLLOW_POW_in_synpred59_SelectExpr2369)
        self._state.following.append(self.FOLLOW_arithmetic_unary_in_synpred59_SelectExpr2372)
        self.arithmetic_unary()

        self._state.following.pop()


    # $ANTLR end "synpred59_SelectExpr"



    # $ANTLR start "synpred62_SelectExpr"
    def synpred62_SelectExpr_fragment(self, ):
        # SelectExpr.g:225:5: ( atom LIST_BEGIN parameter LIST_END )
        # SelectExpr.g:225:5: atom LIST_BEGIN parameter LIST_END
        pass 
        self._state.following.append(self.FOLLOW_atom_in_synpred62_SelectExpr2415)
        self.atom()

        self._state.following.pop()
        self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_synpred62_SelectExpr2417)
        self._state.following.append(self.FOLLOW_parameter_in_synpred62_SelectExpr2419)
        self.parameter()

        self._state.following.pop()
        self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_synpred62_SelectExpr2421)


    # $ANTLR end "synpred62_SelectExpr"




    # Delegated rules

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

    def synpred30_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred30_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred44_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred44_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred48_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred48_SelectExpr_fragment()
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

    def synpred38_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred38_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred58_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred58_SelectExpr_fragment()
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

    def synpred62_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred62_SelectExpr_fragment()
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

    def synpred59_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred59_SelectExpr_fragment()
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

    def synpred43_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred43_SelectExpr_fragment()
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

    def synpred27_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred27_SelectExpr_fragment()
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
                if (self.synpred38_SelectExpr()):
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
                if (self.synpred38_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
                if (self.synpred62_SelectExpr()):
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
 

    FOLLOW_prog_in_eval1511 = frozenset([1])
    FOLLOW_statement_in_prog1521 = frozenset([1, 17, 29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_statement_select_in_statement1531 = frozenset([17])
    FOLLOW_END_in_statement1533 = frozenset([1])
    FOLLOW_expr_in_statement1539 = frozenset([17])
    FOLLOW_END_in_statement1541 = frozenset([1])
    FOLLOW_END_in_statement1547 = frozenset([1])
    FOLLOW_select__in_statement_select1558 = frozenset([59])
    FOLLOW_from__in_statement_select1560 = frozenset([1, 62, 63, 67, 73, 76, 77])
    FOLLOW_where__in_statement_select1563 = frozenset([1, 63, 67, 73, 76, 77])
    FOLLOW_start__in_statement_select1569 = frozenset([76, 77])
    FOLLOW_connect__in_statement_select1573 = frozenset([78])
    FOLLOW_stop__in_statement_select1575 = frozenset([1, 63, 67, 73])
    FOLLOW_group__in_statement_select1580 = frozenset([1, 63, 69, 73])
    FOLLOW_having__in_statement_select1583 = frozenset([1, 63, 73])
    FOLLOW_order__in_statement_select1590 = frozenset([1, 73])
    FOLLOW_as__in_statement_select1595 = frozenset([1])
    FOLLOW_SELECT_in_select_1655 = frozenset([41, 74, 105])
    FOLLOW_MUL_in_select_1659 = frozenset([1])
    FOLLOW_PHRASE_in_select_1666 = frozenset([1, 16])
    FOLLOW_function_in_select_1670 = frozenset([1, 16])
    FOLLOW_this__in_select_1674 = frozenset([1, 16])
    FOLLOW_SEP_in_select_1678 = frozenset([74, 105])
    FOLLOW_PHRASE_in_select_1682 = frozenset([1, 16])
    FOLLOW_function_in_select_1686 = frozenset([1, 16])
    FOLLOW_this__in_select_1690 = frozenset([1, 16])
    FOLLOW_FROM_in_from_1706 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_from_1709 = frozenset([1, 16])
    FOLLOW_SEP_in_from_1712 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_from_1715 = frozenset([1, 16])
    FOLLOW_WHERE_in_where_1726 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_where_1729 = frozenset([1])
    FOLLOW_START_in_start_1738 = frozenset([79])
    FOLLOW_WITH_in_start_1741 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_start_1744 = frozenset([1, 16])
    FOLLOW_SEP_in_start_1747 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_start_1750 = frozenset([1, 16])
    FOLLOW_CONNECT_in_connect_1761 = frozenset([72])
    FOLLOW_BY_in_connect_1764 = frozenset([29, 39, 40, 46, 49, 57, 74, 80, 83, 84, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_NO_in_connect_1768 = frozenset([81])
    FOLLOW_CYCLE_in_connect_1771 = frozenset([29, 39, 40, 46, 49, 57, 74, 83, 84, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_UNIQUE_in_connect_1776 = frozenset([29, 39, 40, 46, 49, 57, 74, 84, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_GRAPH_in_connect_1781 = frozenset([29, 39, 40, 46, 49, 57, 74, 86, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MEMORIZE_in_connect_1786 = frozenset([99])
    FOLLOW_INTEGER_in_connect_1788 = frozenset([29, 39, 40, 46, 49, 57, 74, 87, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MAXIMUM_in_connect_1793 = frozenset([99])
    FOLLOW_INTEGER_in_connect_1795 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_connect_1799 = frozenset([1, 16])
    FOLLOW_SEP_in_connect_1802 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_connect_1805 = frozenset([1, 16])
    FOLLOW_STOP_in_stop_1818 = frozenset([79])
    FOLLOW_WITH_in_stop_1821 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_stop_1824 = frozenset([1])
    FOLLOW_GROUP_in_group_1833 = frozenset([72])
    FOLLOW_BY_in_group_1836 = frozenset([105])
    FOLLOW_PHRASE_in_group_1841 = frozenset([1, 16])
    FOLLOW_function_in_group_1845 = frozenset([1, 16])
    FOLLOW_SEP_in_group_1850 = frozenset([105])
    FOLLOW_PHRASE_in_group_1855 = frozenset([1, 16])
    FOLLOW_function_in_group_1859 = frozenset([1, 16])
    FOLLOW_HAVING_in_having_1873 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_having_1876 = frozenset([1])
    FOLLOW_ORDER_in_order_1885 = frozenset([72])
    FOLLOW_BY_in_order_1888 = frozenset([105])
    FOLLOW_PHRASE_in_order_1893 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1895 = frozenset([1, 16])
    FOLLOW_function_in_order_1899 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1901 = frozenset([1, 16])
    FOLLOW_SEP_in_order_1906 = frozenset([105])
    FOLLOW_PHRASE_in_order_1911 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1913 = frozenset([1, 16])
    FOLLOW_function_in_order_1917 = frozenset([16, 88, 89])
    FOLLOW_direction__in_order_1919 = frozenset([1, 16])
    FOLLOW_set_in_direction_1934 = frozenset([1])
    FOLLOW_AS_in_as_1950 = frozenset([90, 91, 92, 105])
    FOLLOW_AS_LIST_in_as_1955 = frozenset([1])
    FOLLOW_AS_VALUE_in_as_1959 = frozenset([1])
    FOLLOW_AS_DICT_in_as_1963 = frozenset([1])
    FOLLOW_PHRASE_in_as_1967 = frozenset([1, 108])
    FOLLOW_108_in_as_1970 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108, 109])
    FOLLOW_parameter_in_as_1973 = frozenset([109])
    FOLLOW_109_in_as_1976 = frozenset([1])
    FOLLOW_assign_expr_in_expr1990 = frozenset([1])
    FOLLOW_logic_expr_in_expr1996 = frozenset([1])
    FOLLOW_IF_in_if_statement2005 = frozenset([108])
    FOLLOW_108_in_if_statement2007 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_if_statement2009 = frozenset([17, 109])
    FOLLOW_END_in_if_statement2012 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_if_statement2014 = frozenset([17, 109])
    FOLLOW_END_in_if_statement2017 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_if_statement2019 = frozenset([109])
    FOLLOW_109_in_if_statement2025 = frozenset([1])
    FOLLOW_PHRASE_in_assign_expr2064 = frozenset([32, 51])
    FOLLOW_age_in_assign_expr2067 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2071 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_assign_expr2073 = frozenset([1])
    FOLLOW_this__in_assign_expr2092 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2094 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_assign_expr2096 = frozenset([1])
    FOLLOW_logic_or_in_logic_expr2115 = frozenset([1])
    FOLLOW_logic_xor_in_logic_or2124 = frozenset([1, 27])
    FOLLOW_OR_in_logic_or2127 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_xor_in_logic_or2131 = frozenset([1, 27])
    FOLLOW_logic_and_in_logic_xor2141 = frozenset([1, 26])
    FOLLOW_XOR_in_logic_xor2144 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_and_in_logic_xor2147 = frozenset([1, 26])
    FOLLOW_logic_not_in_logic_and2157 = frozenset([1, 22])
    FOLLOW_AND_in_logic_and2160 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_not_in_logic_and2163 = frozenset([1, 22])
    FOLLOW_NOT_in_logic_not2174 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_expr_in_logic_not2179 = frozenset([1])
    FOLLOW_compare_in_in_compare_expr2188 = frozenset([1])
    FOLLOW_compare_eq_in_compare_in2196 = frozenset([1, 31])
    FOLLOW_IN_in_compare_in2199 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_compare_in2202 = frozenset([1, 31])
    FOLLOW_compare_ne_in_compare_eq2212 = frozenset([1, 33])
    FOLLOW_EQ_in_compare_eq2215 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ne_in_compare_eq2218 = frozenset([1, 33])
    FOLLOW_compare_ge_in_compare_ne2228 = frozenset([1, 34])
    FOLLOW_NE_in_compare_ne2231 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ge_in_compare_ne2234 = frozenset([1, 34])
    FOLLOW_compare_gt_in_compare_ge2244 = frozenset([1, 36])
    FOLLOW_GE_in_compare_ge2247 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_gt_in_compare_ge2250 = frozenset([1, 36])
    FOLLOW_compare_le_in_compare_gt2260 = frozenset([1, 38])
    FOLLOW_GT_in_compare_gt2263 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_le_in_compare_gt2266 = frozenset([1, 38])
    FOLLOW_compare_lt_in_compare_le2276 = frozenset([1, 35])
    FOLLOW_LE_in_compare_le2279 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_lt_in_compare_le2282 = frozenset([1, 35])
    FOLLOW_arithmetic_expr_in_compare_lt2292 = frozenset([1, 37])
    FOLLOW_LT_in_compare_lt2295 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_expr_in_compare_lt2298 = frozenset([1, 37])
    FOLLOW_arithmetic_sub_add_in_arithmetic_expr2309 = frozenset([1])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2317 = frozenset([1, 39, 40])
    FOLLOW_SUB_in_arithmetic_sub_add2321 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_ADD_in_arithmetic_sub_add2324 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2328 = frozenset([1, 39, 40])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2338 = frozenset([1, 41, 42, 43])
    FOLLOW_MUL_in_arithmetic_mul_div_mod2342 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_DIV_in_arithmetic_mul_div_mod2347 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_MOD_in_arithmetic_mul_div_mod2352 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2356 = frozenset([1, 41, 42, 43])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2366 = frozenset([1, 44])
    FOLLOW_POW_in_arithmetic_pow2369 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2372 = frozenset([1, 44])
    FOLLOW_SUB_in_arithmetic_unary2383 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_arithmetic_unary2385 = frozenset([1])
    FOLLOW_ADD_in_arithmetic_unary2399 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_arithmetic_unary2401 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2415 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_arithmetic_unary2417 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_arithmetic_unary2419 = frozenset([50])
    FOLLOW_LIST_END_in_arithmetic_unary2421 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2437 = frozenset([1])
    FOLLOW_value_in_atom2448 = frozenset([1])
    FOLLOW_variable_in_atom2453 = frozenset([1])
    FOLLOW_if_statement_in_atom2458 = frozenset([1])
    FOLLOW_function_in_atom2463 = frozenset([1])
    FOLLOW_108_in_atom2468 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_atom2471 = frozenset([109])
    FOLLOW_109_in_atom2473 = frozenset([1])
    FOLLOW_statement_select_in_atom2479 = frozenset([1])
    FOLLOW_PHRASE_in_function2488 = frozenset([108])
    FOLLOW_108_in_function2490 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108, 109])
    FOLLOW_parameter_in_function2492 = frozenset([109])
    FOLLOW_109_in_function2495 = frozenset([1])
    FOLLOW_expr_in_parameter2515 = frozenset([1, 16])
    FOLLOW_SEP_in_parameter2518 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_parameter2521 = frozenset([1, 16])
    FOLLOW_PHRASE_in_variable2532 = frozenset([1, 51])
    FOLLOW_age_in_variable2535 = frozenset([1])
    FOLLOW_AGE_BEGIN_in_age2559 = frozenset([29, 39, 40, 46, 49, 52, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_age2561 = frozenset([52])
    FOLLOW_AGE_END_in_age2564 = frozenset([1])
    FOLLOW_STRING_in_value2582 = frozenset([1])
    FOLLOW_FLOAT_in_value2596 = frozenset([1])
    FOLLOW_INTEGER_in_value2610 = frozenset([1])
    FOLLOW_TRUE_in_value2623 = frozenset([1])
    FOLLOW_FALSE_in_value2637 = frozenset([1])
    FOLLOW_this__in_value2651 = frozenset([1])
    FOLLOW_list__in_value2656 = frozenset([1])
    FOLLOW_PHRASE_in_this_2667 = frozenset([15])
    FOLLOW_DOT_in_this_2669 = frozenset([74])
    FOLLOW_THIS_in_this_2673 = frozenset([1])
    FOLLOW_LIST_BEGIN_in_list_2694 = frozenset([16, 29, 39, 40, 46, 49, 50, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_list_2698 = frozenset([16, 50])
    FOLLOW_SEP_in_list_2702 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_list_2704 = frozenset([16, 50])
    FOLLOW_LIST_END_in_list_2710 = frozenset([1])
    FOLLOW_statement_select_in_synpred2_SelectExpr1531 = frozenset([17])
    FOLLOW_END_in_synpred2_SelectExpr1533 = frozenset([1])
    FOLLOW_expr_in_synpred3_SelectExpr1539 = frozenset([17])
    FOLLOW_END_in_synpred3_SelectExpr1541 = frozenset([1])
    FOLLOW_where__in_synpred4_SelectExpr1563 = frozenset([1])
    FOLLOW_start__in_synpred6_SelectExpr1569 = frozenset([76, 77])
    FOLLOW_connect__in_synpred6_SelectExpr1573 = frozenset([78])
    FOLLOW_stop__in_synpred6_SelectExpr1575 = frozenset([1])
    FOLLOW_group__in_synpred8_SelectExpr1580 = frozenset([1, 69])
    FOLLOW_having__in_synpred8_SelectExpr1583 = frozenset([1])
    FOLLOW_order__in_synpred9_SelectExpr1590 = frozenset([1])
    FOLLOW_as__in_synpred10_SelectExpr1595 = frozenset([1])
    FOLLOW_SEP_in_synpred17_SelectExpr1712 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_expr_in_synpred17_SelectExpr1715 = frozenset([1])
    FOLLOW_SEP_in_synpred27_SelectExpr1850 = frozenset([105])
    FOLLOW_PHRASE_in_synpred27_SelectExpr1855 = frozenset([1])
    FOLLOW_function_in_synpred27_SelectExpr1859 = frozenset([1])
    FOLLOW_SEP_in_synpred30_SelectExpr1906 = frozenset([105])
    FOLLOW_PHRASE_in_synpred30_SelectExpr1911 = frozenset([88, 89])
    FOLLOW_direction__in_synpred30_SelectExpr1913 = frozenset([1])
    FOLLOW_function_in_synpred30_SelectExpr1917 = frozenset([88, 89])
    FOLLOW_direction__in_synpred30_SelectExpr1919 = frozenset([1])
    FOLLOW_assign_expr_in_synpred38_SelectExpr1990 = frozenset([1])
    FOLLOW_OR_in_synpred43_SelectExpr2127 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_xor_in_synpred43_SelectExpr2131 = frozenset([1])
    FOLLOW_XOR_in_synpred44_SelectExpr2144 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_and_in_synpred44_SelectExpr2147 = frozenset([1])
    FOLLOW_AND_in_synpred45_SelectExpr2160 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_logic_not_in_synpred45_SelectExpr2163 = frozenset([1])
    FOLLOW_IN_in_synpred47_SelectExpr2199 = frozenset([46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_atom_in_synpred47_SelectExpr2202 = frozenset([1])
    FOLLOW_EQ_in_synpred48_SelectExpr2215 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ne_in_synpred48_SelectExpr2218 = frozenset([1])
    FOLLOW_NE_in_synpred49_SelectExpr2231 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_ge_in_synpred49_SelectExpr2234 = frozenset([1])
    FOLLOW_GE_in_synpred50_SelectExpr2247 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_gt_in_synpred50_SelectExpr2250 = frozenset([1])
    FOLLOW_GT_in_synpred51_SelectExpr2263 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_le_in_synpred51_SelectExpr2266 = frozenset([1])
    FOLLOW_LE_in_synpred52_SelectExpr2279 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_compare_lt_in_synpred52_SelectExpr2282 = frozenset([1])
    FOLLOW_LT_in_synpred53_SelectExpr2295 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_expr_in_synpred53_SelectExpr2298 = frozenset([1])
    FOLLOW_set_in_synpred55_SelectExpr2320 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_mul_div_mod_in_synpred55_SelectExpr2328 = frozenset([1])
    FOLLOW_set_in_synpred58_SelectExpr2341 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_pow_in_synpred58_SelectExpr2356 = frozenset([1])
    FOLLOW_POW_in_synpred59_SelectExpr2369 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_arithmetic_unary_in_synpred59_SelectExpr2372 = frozenset([1])
    FOLLOW_atom_in_synpred62_SelectExpr2415 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_synpred62_SelectExpr2417 = frozenset([29, 39, 40, 46, 49, 57, 74, 97, 99, 100, 101, 102, 105, 108])
    FOLLOW_parameter_in_synpred62_SelectExpr2419 = frozenset([50])
    FOLLOW_LIST_END_in_synpred62_SelectExpr2421 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SelectExprLexer", SelectExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
