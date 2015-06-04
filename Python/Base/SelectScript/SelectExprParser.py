# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2015-06-04 17:55:52

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
PHRASE=104
IF=46
CYCLE=81
SUB=40
IN=31
STOP=78
MAXIMUM=86
DOT=15
WHERE=62
AS=73
LINE_COMMENT=95
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
J=105
K=106
ASSIGN=32
L=55
M=58
N=20
COMMENT=94
O=24
P=66
ORDER=63
GROUP=67
Q=82
ASC=87
R=25
S=53
T=28
U=65
V=68
W=60
BY=72
X=23
Y=71
Z=84
CHARACTER=102
SQ=47
SELECT=57
DIV=42
NEG=10
MEMORIZE=85
ELEMENT=8
LIST_END=50
LE=35
STRING=96
ADD=39
LT=37
FROM=59
DQ=48
SPECIAL=103
DESC=88
INTEGER=98
MUL=41
NEWLINE=92
UNIQUE=83
TRUE=100
EQ=33
NOT=29
AND=22
NE=34
THIS=74
END=17
HAVING=69
LIST=7
NO=80
FLOAT=99
AS_VALUE=90
AGE_END=52
AS_DICT=91
WS=93
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
DIGIT=97
WITH=79
T__108=108
T__107=107
START=77
FALSE=101
AS_LIST=89

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
    "Z", "MEMORIZE", "MAXIMUM", "ASC", "DESC", "AS_LIST", "AS_VALUE", "AS_DICT", 
    "NEWLINE", "WS", "COMMENT", "LINE_COMMENT", "STRING", "DIGIT", "INTEGER", 
    "FLOAT", "TRUE", "FALSE", "CHARACTER", "SPECIAL", "PHRASE", "J", "K", 
    "'('", "')'"
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

        self.dfa31 = self.DFA31(
            self, 31,
            eot = self.DFA31_eot,
            eof = self.DFA31_eof,
            min = self.DFA31_min,
            max = self.DFA31_max,
            accept = self.DFA31_accept,
            special = self.DFA31_special,
            transition = self.DFA31_transition
            )

        self.dfa52 = self.DFA52(
            self, 52,
            eot = self.DFA52_eot,
            eof = self.DFA52_eof,
            min = self.DFA52_min,
            max = self.DFA52_max,
            accept = self.DFA52_accept,
            special = self.DFA52_special,
            transition = self.DFA52_transition
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
    # SelectExpr.g:144:1: eval : prog ;
    def eval(self, ):

        retval = self.eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prog1 = None



        try:
            try:
                # SelectExpr.g:144:6: ( prog )
                # SelectExpr.g:144:8: prog
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_prog_in_eval1493)
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
    # SelectExpr.g:147:1: prog : ( statement )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None



        try:
            try:
                # SelectExpr.g:147:6: ( ( statement )+ )
                # SelectExpr.g:147:8: ( statement )+
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:147:8: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == END or LA1_0 == NOT or (ADD <= LA1_0 <= SUB) or LA1_0 == IF or LA1_0 == LIST_BEGIN or LA1_0 == SELECT or LA1_0 == THIS or LA1_0 == STRING or (INTEGER <= LA1_0 <= FALSE) or LA1_0 == PHRASE or LA1_0 == 107) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectExpr.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_prog1503)
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
    # SelectExpr.g:150:1: statement : ( statement_select END | expr END | END );
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
                # SelectExpr.g:150:11: ( statement_select END | expr END | END )
                alt2 = 3
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectExpr.g:150:13: statement_select END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_statement1513)
                    statement_select3 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select3.tree)
                    END4=self.match(self.input, END, self.FOLLOW_END_in_statement1515)


                elif alt2 == 2:
                    # SelectExpr.g:151:4: expr END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_statement1521)
                    expr5 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr5.tree)
                    END6=self.match(self.input, END, self.FOLLOW_END_in_statement1523)


                elif alt2 == 3:
                    # SelectExpr.g:152:4: END
                    pass 
                    root_0 = self._adaptor.nil()

                    END7=self.match(self.input, END, self.FOLLOW_END_in_statement1529)


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
    # SelectExpr.g:155:1: statement_select : select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) ;
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
                # SelectExpr.g:155:18: ( select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) )
                # SelectExpr.g:156:2: select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )?
                pass 
                self._state.following.append(self.FOLLOW_select__in_statement_select1540)
                select_8 = self.select_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_select_.add(select_8.tree)
                self._state.following.append(self.FOLLOW_from__in_statement_select1542)
                from_9 = self.from_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_from_.add(from_9.tree)
                # SelectExpr.g:156:16: ( where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    LA3_1 = self.input.LA(2)

                    if (self.synpred4_SelectExpr()) :
                        alt3 = 1
                if alt3 == 1:
                    # SelectExpr.g:156:17: where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select1545)
                    where_10 = self.where_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where_.add(where_10.tree)



                # SelectExpr.g:156:26: ( ( start_ )? connect_ stop_ )?
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
                    # SelectExpr.g:156:27: ( start_ )? connect_ stop_
                    pass 
                    # SelectExpr.g:156:27: ( start_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == START) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectExpr.g:156:28: start_
                        pass 
                        self._state.following.append(self.FOLLOW_start__in_statement_select1551)
                        start_11 = self.start_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_start_.add(start_11.tree)



                    self._state.following.append(self.FOLLOW_connect__in_statement_select1555)
                    connect_12 = self.connect_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_connect_.add(connect_12.tree)
                    self._state.following.append(self.FOLLOW_stop__in_statement_select1557)
                    stop_13 = self.stop_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_stop_.add(stop_13.tree)



                # SelectExpr.g:156:54: ( group_ ( having_ )? )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == GROUP) :
                    LA7_1 = self.input.LA(2)

                    if (self.synpred8_SelectExpr()) :
                        alt7 = 1
                if alt7 == 1:
                    # SelectExpr.g:156:55: group_ ( having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select1562)
                    group_14 = self.group_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_group_.add(group_14.tree)
                    # SelectExpr.g:156:62: ( having_ )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == HAVING) :
                        alt6 = 1
                    if alt6 == 1:
                        # SelectExpr.g:156:63: having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select1565)
                        having_15 = self.having_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_having_.add(having_15.tree)






                # SelectExpr.g:156:75: ( order_ )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ORDER) :
                    LA8_1 = self.input.LA(2)

                    if (self.synpred9_SelectExpr()) :
                        alt8 = 1
                if alt8 == 1:
                    # SelectExpr.g:156:76: order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select1572)
                    order_16 = self.order_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_order_.add(order_16.tree)



                # SelectExpr.g:156:85: ( as_ )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == AS) :
                    LA9_1 = self.input.LA(2)

                    if (self.synpred10_SelectExpr()) :
                        alt9 = 1
                if alt9 == 1:
                    # SelectExpr.g:156:86: as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select1577)
                    as_17 = self.as_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_as_.add(as_17.tree)




                # AST Rewrite
                # elements: select_, start_, order_, stop_, group_, connect_, having_, from_, as_, where_
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
                    # 156:92: -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    # SelectExpr.g:156:96: ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STMT_SELECT, "STMT_SELECT"), root_1)

                    self._adaptor.addChild(root_1, stream_select_.nextTree())
                    self._adaptor.addChild(root_1, stream_from_.nextTree())
                    # SelectExpr.g:156:124: ( where_ )?
                    if stream_where_.hasNext():
                        self._adaptor.addChild(root_1, stream_where_.nextTree())


                    stream_where_.reset();
                    # SelectExpr.g:156:134: ( group_ ( having_ )? )?
                    if stream_group_.hasNext() or stream_having_.hasNext():
                        self._adaptor.addChild(root_1, stream_group_.nextTree())
                        # SelectExpr.g:156:142: ( having_ )?
                        if stream_having_.hasNext():
                            self._adaptor.addChild(root_1, stream_having_.nextTree())


                        stream_having_.reset();


                    stream_group_.reset();
                    stream_having_.reset();
                    # SelectExpr.g:156:155: ( order_ )?
                    if stream_order_.hasNext():
                        self._adaptor.addChild(root_1, stream_order_.nextTree())


                    stream_order_.reset();
                    # SelectExpr.g:156:165: ( as_ )?
                    if stream_as_.hasNext():
                        self._adaptor.addChild(root_1, stream_as_.nextTree())


                    stream_as_.reset();
                    # SelectExpr.g:156:172: ( ( start_ )? connect_ stop_ )?
                    if stream_start_.hasNext() or stream_stop_.hasNext() or stream_connect_.hasNext():
                        # SelectExpr.g:156:173: ( start_ )?
                        if stream_start_.hasNext():
                            self._adaptor.addChild(root_1, stream_start_.nextTree())


                        stream_start_.reset();
                        self._adaptor.addChild(root_1, stream_connect_.nextTree())
                        self._adaptor.addChild(root_1, stream_stop_.nextTree())


                    stream_start_.reset();
                    stream_stop_.reset();
                    stream_connect_.reset();

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
    # SelectExpr.g:159:1: select_ : SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) ;
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
                # SelectExpr.g:159:9: ( SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) )
                # SelectExpr.g:159:11: SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                pass 
                root_0 = self._adaptor.nil()

                SELECT18=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_1637)
                if self._state.backtracking == 0:

                    SELECT18_tree = self._adaptor.createWithPayload(SELECT18)
                    root_0 = self._adaptor.becomeRoot(SELECT18_tree, root_0)

                # SelectExpr.g:159:19: ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
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
                    # SelectExpr.g:159:20: MUL
                    pass 
                    MUL19=self.match(self.input, MUL, self.FOLLOW_MUL_in_select_1641)


                elif alt13 == 2:
                    # SelectExpr.g:159:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    pass 
                    # SelectExpr.g:159:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    # SelectExpr.g:159:28: ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )*
                    pass 
                    # SelectExpr.g:159:28: ( PHRASE | function | this_ )
                    alt10 = 3
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == PHRASE) :
                        LA10 = self.input.LA(2)
                        if LA10 == 107:
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
                        # SelectExpr.g:159:29: PHRASE
                        pass 
                        PHRASE20=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1648)
                        if self._state.backtracking == 0:

                            PHRASE20_tree = self._adaptor.createWithPayload(PHRASE20)
                            self._adaptor.addChild(root_0, PHRASE20_tree)



                    elif alt10 == 2:
                        # SelectExpr.g:159:38: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_select_1652)
                        function21 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, function21.tree)


                    elif alt10 == 3:
                        # SelectExpr.g:159:49: this_
                        pass 
                        self._state.following.append(self.FOLLOW_this__in_select_1656)
                        this_22 = self.this_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, this_22.tree)



                    # SelectExpr.g:159:56: ( SEP ( PHRASE | function | this_ ) )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == SEP) :
                            alt12 = 1


                        if alt12 == 1:
                            # SelectExpr.g:159:57: SEP ( PHRASE | function | this_ )
                            pass 
                            SEP23=self.match(self.input, SEP, self.FOLLOW_SEP_in_select_1660)
                            # SelectExpr.g:159:62: ( PHRASE | function | this_ )
                            alt11 = 3
                            LA11_0 = self.input.LA(1)

                            if (LA11_0 == PHRASE) :
                                LA11 = self.input.LA(2)
                                if LA11 == 107:
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
                                # SelectExpr.g:159:63: PHRASE
                                pass 
                                PHRASE24=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1664)
                                if self._state.backtracking == 0:

                                    PHRASE24_tree = self._adaptor.createWithPayload(PHRASE24)
                                    self._adaptor.addChild(root_0, PHRASE24_tree)



                            elif alt11 == 2:
                                # SelectExpr.g:159:72: function
                                pass 
                                self._state.following.append(self.FOLLOW_function_in_select_1668)
                                function25 = self.function()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, function25.tree)


                            elif alt11 == 3:
                                # SelectExpr.g:159:83: this_
                                pass 
                                self._state.following.append(self.FOLLOW_this__in_select_1672)
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
    # SelectExpr.g:162:1: from_ : FROM expr ( SEP expr )* ;
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
                # SelectExpr.g:162:7: ( FROM expr ( SEP expr )* )
                # SelectExpr.g:162:9: FROM expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                FROM27=self.match(self.input, FROM, self.FOLLOW_FROM_in_from_1688)
                if self._state.backtracking == 0:

                    FROM27_tree = self._adaptor.createWithPayload(FROM27)
                    root_0 = self._adaptor.becomeRoot(FROM27_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_from_1691)
                expr28 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr28.tree)
                # SelectExpr.g:162:20: ( SEP expr )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == SEP) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred17_SelectExpr()) :
                            alt14 = 1




                    if alt14 == 1:
                        # SelectExpr.g:162:21: SEP expr
                        pass 
                        SEP29=self.match(self.input, SEP, self.FOLLOW_SEP_in_from_1694)
                        self._state.following.append(self.FOLLOW_expr_in_from_1697)
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
    # SelectExpr.g:165:1: where_ : WHERE expr ;
    def where_(self, ):

        retval = self.where__return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHERE31 = None
        expr32 = None


        WHERE31_tree = None

        try:
            try:
                # SelectExpr.g:165:8: ( WHERE expr )
                # SelectExpr.g:165:10: WHERE expr
                pass 
                root_0 = self._adaptor.nil()

                WHERE31=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_1708)
                if self._state.backtracking == 0:

                    WHERE31_tree = self._adaptor.createWithPayload(WHERE31)
                    root_0 = self._adaptor.becomeRoot(WHERE31_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_where_1711)
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
    # SelectExpr.g:168:1: start_ : START WITH expr ( SEP expr )* ;
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
                # SelectExpr.g:168:8: ( START WITH expr ( SEP expr )* )
                # SelectExpr.g:168:10: START WITH expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                START33=self.match(self.input, START, self.FOLLOW_START_in_start_1720)
                if self._state.backtracking == 0:

                    START33_tree = self._adaptor.createWithPayload(START33)
                    root_0 = self._adaptor.becomeRoot(START33_tree, root_0)

                WITH34=self.match(self.input, WITH, self.FOLLOW_WITH_in_start_1723)
                self._state.following.append(self.FOLLOW_expr_in_start_1726)
                expr35 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr35.tree)
                # SelectExpr.g:168:28: ( SEP expr )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SEP) :
                        alt15 = 1


                    if alt15 == 1:
                        # SelectExpr.g:168:29: SEP expr
                        pass 
                        SEP36=self.match(self.input, SEP, self.FOLLOW_SEP_in_start_1729)
                        self._state.following.append(self.FOLLOW_expr_in_start_1732)
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
    # SelectExpr.g:171:1: connect_ : CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )* ;
    def connect_(self, ):

        retval = self.connect__return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONNECT38 = None
        BY39 = None
        NO40 = None
        CYCLE41 = None
        UNIQUE42 = None
        MEMORIZE43 = None
        INTEGER44 = None
        MAXIMUM45 = None
        INTEGER46 = None
        SEP48 = None
        expr47 = None

        expr49 = None


        CONNECT38_tree = None
        BY39_tree = None
        NO40_tree = None
        CYCLE41_tree = None
        UNIQUE42_tree = None
        MEMORIZE43_tree = None
        INTEGER44_tree = None
        MAXIMUM45_tree = None
        INTEGER46_tree = None
        SEP48_tree = None

        try:
            try:
                # SelectExpr.g:171:10: ( CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )* )
                # SelectExpr.g:171:12: CONNECT BY ( NO CYCLE )? ( UNIQUE )? ( MEMORIZE INTEGER )? ( MAXIMUM INTEGER )? expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                CONNECT38=self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_1743)
                if self._state.backtracking == 0:

                    CONNECT38_tree = self._adaptor.createWithPayload(CONNECT38)
                    root_0 = self._adaptor.becomeRoot(CONNECT38_tree, root_0)

                BY39=self.match(self.input, BY, self.FOLLOW_BY_in_connect_1746)
                # SelectExpr.g:171:25: ( NO CYCLE )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == NO) :
                    alt16 = 1
                if alt16 == 1:
                    # SelectExpr.g:171:26: NO CYCLE
                    pass 
                    NO40=self.match(self.input, NO, self.FOLLOW_NO_in_connect_1750)
                    CYCLE41=self.match(self.input, CYCLE, self.FOLLOW_CYCLE_in_connect_1753)
                    if self._state.backtracking == 0:

                        CYCLE41_tree = self._adaptor.createWithPayload(CYCLE41)
                        self._adaptor.addChild(root_0, CYCLE41_tree)




                # SelectExpr.g:171:38: ( UNIQUE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == UNIQUE) :
                    alt17 = 1
                if alt17 == 1:
                    # SelectExpr.g:171:39: UNIQUE
                    pass 
                    UNIQUE42=self.match(self.input, UNIQUE, self.FOLLOW_UNIQUE_in_connect_1758)
                    if self._state.backtracking == 0:

                        UNIQUE42_tree = self._adaptor.createWithPayload(UNIQUE42)
                        self._adaptor.addChild(root_0, UNIQUE42_tree)




                # SelectExpr.g:171:48: ( MEMORIZE INTEGER )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MEMORIZE) :
                    alt18 = 1
                if alt18 == 1:
                    # SelectExpr.g:171:49: MEMORIZE INTEGER
                    pass 
                    MEMORIZE43=self.match(self.input, MEMORIZE, self.FOLLOW_MEMORIZE_in_connect_1763)
                    if self._state.backtracking == 0:

                        MEMORIZE43_tree = self._adaptor.createWithPayload(MEMORIZE43)
                        self._adaptor.addChild(root_0, MEMORIZE43_tree)

                    INTEGER44=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1765)
                    if self._state.backtracking == 0:

                        INTEGER44_tree = self._adaptor.createWithPayload(INTEGER44)
                        self._adaptor.addChild(root_0, INTEGER44_tree)




                # SelectExpr.g:171:68: ( MAXIMUM INTEGER )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MAXIMUM) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectExpr.g:171:69: MAXIMUM INTEGER
                    pass 
                    MAXIMUM45=self.match(self.input, MAXIMUM, self.FOLLOW_MAXIMUM_in_connect_1770)
                    if self._state.backtracking == 0:

                        MAXIMUM45_tree = self._adaptor.createWithPayload(MAXIMUM45)
                        self._adaptor.addChild(root_0, MAXIMUM45_tree)

                    INTEGER46=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_connect_1772)
                    if self._state.backtracking == 0:

                        INTEGER46_tree = self._adaptor.createWithPayload(INTEGER46)
                        self._adaptor.addChild(root_0, INTEGER46_tree)




                self._state.following.append(self.FOLLOW_expr_in_connect_1776)
                expr47 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr47.tree)
                # SelectExpr.g:171:92: ( SEP expr )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == SEP) :
                        alt20 = 1


                    if alt20 == 1:
                        # SelectExpr.g:171:93: SEP expr
                        pass 
                        SEP48=self.match(self.input, SEP, self.FOLLOW_SEP_in_connect_1779)
                        self._state.following.append(self.FOLLOW_expr_in_connect_1782)
                        expr49 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr49.tree)


                    else:
                        break #loop20



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
    # SelectExpr.g:174:1: stop_ : STOP WITH expr ;
    def stop_(self, ):

        retval = self.stop__return()
        retval.start = self.input.LT(1)

        root_0 = None

        STOP50 = None
        WITH51 = None
        expr52 = None


        STOP50_tree = None
        WITH51_tree = None

        try:
            try:
                # SelectExpr.g:174:7: ( STOP WITH expr )
                # SelectExpr.g:174:9: STOP WITH expr
                pass 
                root_0 = self._adaptor.nil()

                STOP50=self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_1795)
                if self._state.backtracking == 0:

                    STOP50_tree = self._adaptor.createWithPayload(STOP50)
                    root_0 = self._adaptor.becomeRoot(STOP50_tree, root_0)

                WITH51=self.match(self.input, WITH, self.FOLLOW_WITH_in_stop_1798)
                self._state.following.append(self.FOLLOW_expr_in_stop_1801)
                expr52 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr52.tree)



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
    # SelectExpr.g:177:1: group_ : GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* ;
    def group_(self, ):

        retval = self.group__return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP53 = None
        BY54 = None
        PHRASE55 = None
        SEP57 = None
        PHRASE58 = None
        function56 = None

        function59 = None


        GROUP53_tree = None
        BY54_tree = None
        PHRASE55_tree = None
        SEP57_tree = None
        PHRASE58_tree = None

        try:
            try:
                # SelectExpr.g:177:8: ( GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* )
                # SelectExpr.g:177:10: GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )*
                pass 
                root_0 = self._adaptor.nil()

                GROUP53=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_1810)
                if self._state.backtracking == 0:

                    GROUP53_tree = self._adaptor.createWithPayload(GROUP53)
                    root_0 = self._adaptor.becomeRoot(GROUP53_tree, root_0)

                BY54=self.match(self.input, BY, self.FOLLOW_BY_in_group_1813)
                # SelectExpr.g:177:21: ( PHRASE | function )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == PHRASE) :
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == 107) :
                        alt21 = 2
                    elif (LA21_1 == EOF or (SEP <= LA21_1 <= END) or LA21_1 == AND or (XOR <= LA21_1 <= OR) or LA21_1 == IN or (EQ <= LA21_1 <= POW) or (LIST_BEGIN <= LA21_1 <= LIST_END) or LA21_1 == AGE_END or (WHERE <= LA21_1 <= ORDER) or LA21_1 == GROUP or LA21_1 == HAVING or LA21_1 == AS or (CONNECT <= LA21_1 <= STOP) or LA21_1 == 108) :
                        alt21 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # SelectExpr.g:177:23: PHRASE
                    pass 
                    PHRASE55=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1818)
                    if self._state.backtracking == 0:

                        PHRASE55_tree = self._adaptor.createWithPayload(PHRASE55)
                        self._adaptor.addChild(root_0, PHRASE55_tree)



                elif alt21 == 2:
                    # SelectExpr.g:177:32: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_group_1822)
                    function56 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function56.tree)



                # SelectExpr.g:177:43: ( SEP ( PHRASE | function ) )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == SEP) :
                        LA23_2 = self.input.LA(2)

                        if (LA23_2 == PHRASE) :
                            LA23_3 = self.input.LA(3)

                            if (self.synpred26_SelectExpr()) :
                                alt23 = 1






                    if alt23 == 1:
                        # SelectExpr.g:177:44: SEP ( PHRASE | function )
                        pass 
                        SEP57=self.match(self.input, SEP, self.FOLLOW_SEP_in_group_1827)
                        # SelectExpr.g:177:49: ( PHRASE | function )
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == PHRASE) :
                            LA22_1 = self.input.LA(2)

                            if (LA22_1 == 107) :
                                alt22 = 2
                            elif (LA22_1 == EOF or (SEP <= LA22_1 <= END) or LA22_1 == AND or (XOR <= LA22_1 <= OR) or LA22_1 == IN or (EQ <= LA22_1 <= POW) or (LIST_BEGIN <= LA22_1 <= LIST_END) or LA22_1 == AGE_END or (WHERE <= LA22_1 <= ORDER) or LA22_1 == GROUP or LA22_1 == HAVING or LA22_1 == AS or (CONNECT <= LA22_1 <= STOP) or LA22_1 == 108) :
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
                            # SelectExpr.g:177:51: PHRASE
                            pass 
                            PHRASE58=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1832)
                            if self._state.backtracking == 0:

                                PHRASE58_tree = self._adaptor.createWithPayload(PHRASE58)
                                self._adaptor.addChild(root_0, PHRASE58_tree)



                        elif alt22 == 2:
                            # SelectExpr.g:177:60: function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_group_1836)
                            function59 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function59.tree)





                    else:
                        break #loop23



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
    # SelectExpr.g:180:1: having_ : HAVING expr ;
    def having_(self, ):

        retval = self.having__return()
        retval.start = self.input.LT(1)

        root_0 = None

        HAVING60 = None
        expr61 = None


        HAVING60_tree = None

        try:
            try:
                # SelectExpr.g:180:9: ( HAVING expr )
                # SelectExpr.g:180:11: HAVING expr
                pass 
                root_0 = self._adaptor.nil()

                HAVING60=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_1850)
                if self._state.backtracking == 0:

                    HAVING60_tree = self._adaptor.createWithPayload(HAVING60)
                    root_0 = self._adaptor.becomeRoot(HAVING60_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_having_1853)
                expr61 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr61.tree)



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
    # SelectExpr.g:183:1: order_ : ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* ;
    def order_(self, ):

        retval = self.order__return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER62 = None
        BY63 = None
        PHRASE64 = None
        SEP68 = None
        PHRASE69 = None
        direction_65 = None

        function66 = None

        direction_67 = None

        direction_70 = None

        function71 = None

        direction_72 = None


        ORDER62_tree = None
        BY63_tree = None
        PHRASE64_tree = None
        SEP68_tree = None
        PHRASE69_tree = None

        try:
            try:
                # SelectExpr.g:183:8: ( ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* )
                # SelectExpr.g:183:10: ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )*
                pass 
                root_0 = self._adaptor.nil()

                ORDER62=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_1862)
                if self._state.backtracking == 0:

                    ORDER62_tree = self._adaptor.createWithPayload(ORDER62)
                    root_0 = self._adaptor.becomeRoot(ORDER62_tree, root_0)

                BY63=self.match(self.input, BY, self.FOLLOW_BY_in_order_1865)
                # SelectExpr.g:183:21: ( PHRASE direction_ | function direction_ )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == PHRASE) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == 107) :
                        alt24 = 2
                    elif (LA24_1 == EOF or (SEP <= LA24_1 <= END) or LA24_1 == AND or (XOR <= LA24_1 <= OR) or LA24_1 == IN or (EQ <= LA24_1 <= POW) or (LIST_BEGIN <= LA24_1 <= LIST_END) or LA24_1 == AGE_END or (WHERE <= LA24_1 <= ORDER) or LA24_1 == GROUP or LA24_1 == AS or (CONNECT <= LA24_1 <= STOP) or (ASC <= LA24_1 <= DESC) or LA24_1 == 108) :
                        alt24 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # SelectExpr.g:183:23: PHRASE direction_
                    pass 
                    PHRASE64=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1870)
                    if self._state.backtracking == 0:

                        PHRASE64_tree = self._adaptor.createWithPayload(PHRASE64)
                        self._adaptor.addChild(root_0, PHRASE64_tree)

                    self._state.following.append(self.FOLLOW_direction__in_order_1872)
                    direction_65 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_65.tree)


                elif alt24 == 2:
                    # SelectExpr.g:183:43: function direction_
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_order_1876)
                    function66 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function66.tree)
                    self._state.following.append(self.FOLLOW_direction__in_order_1878)
                    direction_67 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_67.tree)



                # SelectExpr.g:183:65: ( SEP ( PHRASE direction_ | function direction_ ) )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEP) :
                        LA26_2 = self.input.LA(2)

                        if (LA26_2 == PHRASE) :
                            LA26_3 = self.input.LA(3)

                            if (self.synpred29_SelectExpr()) :
                                alt26 = 1






                    if alt26 == 1:
                        # SelectExpr.g:183:66: SEP ( PHRASE direction_ | function direction_ )
                        pass 
                        SEP68=self.match(self.input, SEP, self.FOLLOW_SEP_in_order_1883)
                        # SelectExpr.g:183:71: ( PHRASE direction_ | function direction_ )
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == PHRASE) :
                            LA25_1 = self.input.LA(2)

                            if (LA25_1 == 107) :
                                alt25 = 2
                            elif (LA25_1 == EOF or (SEP <= LA25_1 <= END) or LA25_1 == AND or (XOR <= LA25_1 <= OR) or LA25_1 == IN or (EQ <= LA25_1 <= POW) or (LIST_BEGIN <= LA25_1 <= LIST_END) or LA25_1 == AGE_END or (WHERE <= LA25_1 <= ORDER) or LA25_1 == GROUP or LA25_1 == AS or (CONNECT <= LA25_1 <= STOP) or (ASC <= LA25_1 <= DESC) or LA25_1 == 108) :
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
                            # SelectExpr.g:183:73: PHRASE direction_
                            pass 
                            PHRASE69=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1888)
                            if self._state.backtracking == 0:

                                PHRASE69_tree = self._adaptor.createWithPayload(PHRASE69)
                                self._adaptor.addChild(root_0, PHRASE69_tree)

                            self._state.following.append(self.FOLLOW_direction__in_order_1890)
                            direction_70 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_70.tree)


                        elif alt25 == 2:
                            # SelectExpr.g:183:93: function direction_
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_order_1894)
                            function71 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function71.tree)
                            self._state.following.append(self.FOLLOW_direction__in_order_1896)
                            direction_72 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_72.tree)





                    else:
                        break #loop26



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
    # SelectExpr.g:186:1: direction_ : ( ASC | DESC )? ;
    def direction_(self, ):

        retval = self.direction__return()
        retval.start = self.input.LT(1)

        root_0 = None

        set73 = None

        set73_tree = None

        try:
            try:
                # SelectExpr.g:186:12: ( ( ASC | DESC )? )
                # SelectExpr.g:186:14: ( ASC | DESC )?
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:186:14: ( ASC | DESC )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if ((ASC <= LA27_0 <= DESC)) :
                    alt27 = 1
                if alt27 == 1:
                    # SelectExpr.g:
                    pass 
                    set73 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set73))
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
    # SelectExpr.g:189:1: as_ : AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) ;
    def as_(self, ):

        retval = self.as__return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS74 = None
        AS_LIST75 = None
        AS_VALUE76 = None
        AS_DICT77 = None
        PHRASE78 = None
        char_literal79 = None
        char_literal81 = None
        parameter80 = None


        AS74_tree = None
        AS_LIST75_tree = None
        AS_VALUE76_tree = None
        AS_DICT77_tree = None
        PHRASE78_tree = None
        char_literal79_tree = None
        char_literal81_tree = None

        try:
            try:
                # SelectExpr.g:189:5: ( AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) )
                # SelectExpr.g:189:7: AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                pass 
                root_0 = self._adaptor.nil()

                AS74=self.match(self.input, AS, self.FOLLOW_AS_in_as_1927)
                if self._state.backtracking == 0:

                    AS74_tree = self._adaptor.createWithPayload(AS74)
                    root_0 = self._adaptor.becomeRoot(AS74_tree, root_0)

                # SelectExpr.g:189:11: ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                alt30 = 4
                LA30 = self.input.LA(1)
                if LA30 == AS_LIST:
                    alt30 = 1
                elif LA30 == AS_VALUE:
                    alt30 = 2
                elif LA30 == AS_DICT:
                    alt30 = 3
                elif LA30 == PHRASE:
                    alt30 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # SelectExpr.g:189:13: AS_LIST
                    pass 
                    AS_LIST75=self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_1932)
                    if self._state.backtracking == 0:

                        AS_LIST75_tree = self._adaptor.createWithPayload(AS_LIST75)
                        self._adaptor.addChild(root_0, AS_LIST75_tree)



                elif alt30 == 2:
                    # SelectExpr.g:189:23: AS_VALUE
                    pass 
                    AS_VALUE76=self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_1936)
                    if self._state.backtracking == 0:

                        AS_VALUE76_tree = self._adaptor.createWithPayload(AS_VALUE76)
                        self._adaptor.addChild(root_0, AS_VALUE76_tree)



                elif alt30 == 3:
                    # SelectExpr.g:189:34: AS_DICT
                    pass 
                    AS_DICT77=self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_1940)
                    if self._state.backtracking == 0:

                        AS_DICT77_tree = self._adaptor.createWithPayload(AS_DICT77)
                        self._adaptor.addChild(root_0, AS_DICT77_tree)



                elif alt30 == 4:
                    # SelectExpr.g:189:44: PHRASE ( '(' ( parameter )? ')' )?
                    pass 
                    PHRASE78=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_1944)
                    if self._state.backtracking == 0:

                        PHRASE78_tree = self._adaptor.createWithPayload(PHRASE78)
                        self._adaptor.addChild(root_0, PHRASE78_tree)

                    # SelectExpr.g:189:51: ( '(' ( parameter )? ')' )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == 107) :
                        alt29 = 1
                    if alt29 == 1:
                        # SelectExpr.g:189:52: '(' ( parameter )? ')'
                        pass 
                        char_literal79=self.match(self.input, 107, self.FOLLOW_107_in_as_1947)
                        # SelectExpr.g:189:57: ( parameter )?
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == NOT or (ADD <= LA28_0 <= SUB) or LA28_0 == IF or LA28_0 == LIST_BEGIN or LA28_0 == SELECT or LA28_0 == THIS or LA28_0 == STRING or (INTEGER <= LA28_0 <= FALSE) or LA28_0 == PHRASE or LA28_0 == 107) :
                            alt28 = 1
                        if alt28 == 1:
                            # SelectExpr.g:0:0: parameter
                            pass 
                            self._state.following.append(self.FOLLOW_parameter_in_as_1950)
                            parameter80 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter80.tree)



                        char_literal81=self.match(self.input, 108, self.FOLLOW_108_in_as_1953)









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
    # SelectExpr.g:192:1: expr : ( assign_expr | logic_expr );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_expr82 = None

        logic_expr83 = None



        try:
            try:
                # SelectExpr.g:192:6: ( assign_expr | logic_expr )
                alt31 = 2
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # SelectExpr.g:192:8: assign_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assign_expr_in_expr1967)
                    assign_expr82 = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assign_expr82.tree)


                elif alt31 == 2:
                    # SelectExpr.g:193:4: logic_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_logic_expr_in_expr1973)
                    logic_expr83 = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logic_expr83.tree)


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
    # SelectExpr.g:196:1: if_statement : IF '(' expr ( END parameter ( END parameter )? )? ')' -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? ) ;
    def if_statement(self, ):

        retval = self.if_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IF84 = None
        char_literal85 = None
        END87 = None
        END89 = None
        char_literal91 = None
        expr86 = None

        parameter88 = None

        parameter90 = None


        IF84_tree = None
        char_literal85_tree = None
        END87_tree = None
        END89_tree = None
        char_literal91_tree = None
        stream_107 = RewriteRuleTokenStream(self._adaptor, "token 107")
        stream_108 = RewriteRuleTokenStream(self._adaptor, "token 108")
        stream_END = RewriteRuleTokenStream(self._adaptor, "token END")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:196:14: ( IF '(' expr ( END parameter ( END parameter )? )? ')' -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? ) )
                # SelectExpr.g:196:16: IF '(' expr ( END parameter ( END parameter )? )? ')'
                pass 
                IF84=self.match(self.input, IF, self.FOLLOW_IF_in_if_statement1982) 
                if self._state.backtracking == 0:
                    stream_IF.add(IF84)
                char_literal85=self.match(self.input, 107, self.FOLLOW_107_in_if_statement1984) 
                if self._state.backtracking == 0:
                    stream_107.add(char_literal85)
                self._state.following.append(self.FOLLOW_expr_in_if_statement1986)
                expr86 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr86.tree)
                # SelectExpr.g:196:28: ( END parameter ( END parameter )? )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == END) :
                    alt33 = 1
                if alt33 == 1:
                    # SelectExpr.g:196:29: END parameter ( END parameter )?
                    pass 
                    END87=self.match(self.input, END, self.FOLLOW_END_in_if_statement1989) 
                    if self._state.backtracking == 0:
                        stream_END.add(END87)
                    self._state.following.append(self.FOLLOW_parameter_in_if_statement1991)
                    parameter88 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter88.tree)
                    # SelectExpr.g:196:43: ( END parameter )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == END) :
                        alt32 = 1
                    if alt32 == 1:
                        # SelectExpr.g:196:44: END parameter
                        pass 
                        END89=self.match(self.input, END, self.FOLLOW_END_in_if_statement1994) 
                        if self._state.backtracking == 0:
                            stream_END.add(END89)
                        self._state.following.append(self.FOLLOW_parameter_in_if_statement1996)
                        parameter90 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter90.tree)






                char_literal91=self.match(self.input, 108, self.FOLLOW_108_in_if_statement2002) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal91)

                # AST Rewrite
                # elements: IF, expr, parameter, parameter
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
                    # 196:66: -> ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? )
                    # SelectExpr.g:196:69: ^( IF expr ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IF.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # SelectExpr.g:196:79: ( ^( THEN parameter ( ^( ELSE parameter ) )? ) )?
                    if stream_parameter.hasNext() or stream_parameter.hasNext():
                        # SelectExpr.g:196:81: ^( THEN parameter ( ^( ELSE parameter ) )? )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(THEN, "THEN"), root_2)

                        self._adaptor.addChild(root_2, stream_parameter.nextTree())
                        # SelectExpr.g:196:98: ( ^( ELSE parameter ) )?
                        if stream_parameter.hasNext():
                            # SelectExpr.g:196:99: ^( ELSE parameter )
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
    # SelectExpr.g:200:1: assign_expr : ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) | this_ ASSIGN expr -> ^( ASSIGN this_ expr ) );
    def assign_expr(self, ):

        retval = self.assign_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE92 = None
        ASSIGN94 = None
        ASSIGN97 = None
        age93 = None

        expr95 = None

        this_96 = None

        expr98 = None


        PHRASE92_tree = None
        ASSIGN94_tree = None
        ASSIGN97_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_this_ = RewriteRuleSubtreeStream(self._adaptor, "rule this_")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:200:13: ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) | this_ ASSIGN expr -> ^( ASSIGN this_ expr ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == PHRASE) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == DOT) :
                        alt35 = 2
                    elif (LA35_1 == ASSIGN or LA35_1 == AGE_BEGIN) :
                        alt35 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae

                elif (LA35_0 == THIS) :
                    alt35 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # SelectExpr.g:200:15: PHRASE ( age )? ASSIGN expr
                    pass 
                    PHRASE92=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr2041) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE92)
                    # SelectExpr.g:200:22: ( age )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == AGE_BEGIN) :
                        alt34 = 1
                    if alt34 == 1:
                        # SelectExpr.g:200:23: age
                        pass 
                        self._state.following.append(self.FOLLOW_age_in_assign_expr2044)
                        age93 = self.age()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_age.add(age93.tree)



                    ASSIGN94=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2048) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN94)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2050)
                    expr95 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr95.tree)

                    # AST Rewrite
                    # elements: expr, PHRASE, age, ASSIGN
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
                        # 200:41: -> ^( ASSIGN PHRASE expr ( age )? )
                        # SelectExpr.g:200:44: ^( ASSIGN PHRASE expr ( age )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # SelectExpr.g:200:65: ( age )?
                        if stream_age.hasNext():
                            self._adaptor.addChild(root_1, stream_age.nextTree())


                        stream_age.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt35 == 2:
                    # SelectExpr.g:200:75: this_ ASSIGN expr
                    pass 
                    self._state.following.append(self.FOLLOW_this__in_assign_expr2069)
                    this_96 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_this_.add(this_96.tree)
                    ASSIGN97=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr2071) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN97)
                    self._state.following.append(self.FOLLOW_expr_in_assign_expr2073)
                    expr98 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr98.tree)

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
                        # 200:93: -> ^( ASSIGN this_ expr )
                        # SelectExpr.g:200:96: ^( ASSIGN this_ expr )
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
    # SelectExpr.g:202:1: logic_expr : logic_or ;
    def logic_expr(self, ):

        retval = self.logic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        logic_or99 = None



        try:
            try:
                # SelectExpr.g:202:12: ( logic_or )
                # SelectExpr.g:202:14: logic_or
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_or_in_logic_expr2092)
                logic_or99 = self.logic_or()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_or99.tree)



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
    # SelectExpr.g:203:1: logic_or : logic_xor ( OR logic_xor )* ;
    def logic_or(self, ):

        retval = self.logic_or_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR101 = None
        logic_xor100 = None

        logic_xor102 = None


        OR101_tree = None

        try:
            try:
                # SelectExpr.g:203:11: ( logic_xor ( OR logic_xor )* )
                # SelectExpr.g:203:13: logic_xor ( OR logic_xor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2101)
                logic_xor100 = self.logic_xor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_xor100.tree)
                # SelectExpr.g:203:23: ( OR logic_xor )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == OR) :
                        LA36_2 = self.input.LA(2)

                        if (self.synpred42_SelectExpr()) :
                            alt36 = 1




                    if alt36 == 1:
                        # SelectExpr.g:203:24: OR logic_xor
                        pass 
                        OR101=self.match(self.input, OR, self.FOLLOW_OR_in_logic_or2104)
                        if self._state.backtracking == 0:

                            OR101_tree = self._adaptor.createWithPayload(OR101)
                            root_0 = self._adaptor.becomeRoot(OR101_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_xor_in_logic_or2108)
                        logic_xor102 = self.logic_xor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_xor102.tree)


                    else:
                        break #loop36



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
    # SelectExpr.g:204:1: logic_xor : logic_and ( XOR logic_and )* ;
    def logic_xor(self, ):

        retval = self.logic_xor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        XOR104 = None
        logic_and103 = None

        logic_and105 = None


        XOR104_tree = None

        try:
            try:
                # SelectExpr.g:204:11: ( logic_and ( XOR logic_and )* )
                # SelectExpr.g:204:13: logic_and ( XOR logic_and )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2118)
                logic_and103 = self.logic_and()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_and103.tree)
                # SelectExpr.g:204:23: ( XOR logic_and )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == XOR) :
                        LA37_2 = self.input.LA(2)

                        if (self.synpred43_SelectExpr()) :
                            alt37 = 1




                    if alt37 == 1:
                        # SelectExpr.g:204:24: XOR logic_and
                        pass 
                        XOR104=self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_xor2121)
                        if self._state.backtracking == 0:

                            XOR104_tree = self._adaptor.createWithPayload(XOR104)
                            root_0 = self._adaptor.becomeRoot(XOR104_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_and_in_logic_xor2124)
                        logic_and105 = self.logic_and()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_and105.tree)


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

    # $ANTLR end "logic_xor"

    class logic_and_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_and_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_and"
    # SelectExpr.g:205:1: logic_and : logic_not ( AND logic_not )* ;
    def logic_and(self, ):

        retval = self.logic_and_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND107 = None
        logic_not106 = None

        logic_not108 = None


        AND107_tree = None

        try:
            try:
                # SelectExpr.g:205:11: ( logic_not ( AND logic_not )* )
                # SelectExpr.g:205:13: logic_not ( AND logic_not )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_not_in_logic_and2134)
                logic_not106 = self.logic_not()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_not106.tree)
                # SelectExpr.g:205:23: ( AND logic_not )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == AND) :
                        LA38_2 = self.input.LA(2)

                        if (self.synpred44_SelectExpr()) :
                            alt38 = 1




                    if alt38 == 1:
                        # SelectExpr.g:205:24: AND logic_not
                        pass 
                        AND107=self.match(self.input, AND, self.FOLLOW_AND_in_logic_and2137)
                        if self._state.backtracking == 0:

                            AND107_tree = self._adaptor.createWithPayload(AND107)
                            root_0 = self._adaptor.becomeRoot(AND107_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_not_in_logic_and2140)
                        logic_not108 = self.logic_not()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_not108.tree)


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

    # $ANTLR end "logic_and"

    class logic_not_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_not_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_not"
    # SelectExpr.g:206:1: logic_not : ( NOT )? compare_expr ;
    def logic_not(self, ):

        retval = self.logic_not_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT109 = None
        compare_expr110 = None


        NOT109_tree = None

        try:
            try:
                # SelectExpr.g:206:11: ( ( NOT )? compare_expr )
                # SelectExpr.g:206:13: ( NOT )? compare_expr
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:206:13: ( NOT )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == NOT) :
                    alt39 = 1
                if alt39 == 1:
                    # SelectExpr.g:206:14: NOT
                    pass 
                    NOT109=self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_not2151)
                    if self._state.backtracking == 0:

                        NOT109_tree = self._adaptor.createWithPayload(NOT109)
                        root_0 = self._adaptor.becomeRoot(NOT109_tree, root_0)




                self._state.following.append(self.FOLLOW_compare_expr_in_logic_not2156)
                compare_expr110 = self.compare_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_expr110.tree)



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
    # SelectExpr.g:208:1: compare_expr : compare_in ;
    def compare_expr(self, ):

        retval = self.compare_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        compare_in111 = None



        try:
            try:
                # SelectExpr.g:208:14: ( compare_in )
                # SelectExpr.g:208:16: compare_in
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_in_in_compare_expr2165)
                compare_in111 = self.compare_in()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_in111.tree)



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
    # SelectExpr.g:209:1: compare_in : compare_eq ( IN atom )* ;
    def compare_in(self, ):

        retval = self.compare_in_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IN113 = None
        compare_eq112 = None

        atom114 = None


        IN113_tree = None

        try:
            try:
                # SelectExpr.g:209:12: ( compare_eq ( IN atom )* )
                # SelectExpr.g:209:14: compare_eq ( IN atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_eq_in_compare_in2173)
                compare_eq112 = self.compare_eq()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_eq112.tree)
                # SelectExpr.g:209:25: ( IN atom )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == IN) :
                        LA40_2 = self.input.LA(2)

                        if (self.synpred46_SelectExpr()) :
                            alt40 = 1




                    if alt40 == 1:
                        # SelectExpr.g:209:26: IN atom
                        pass 
                        IN113=self.match(self.input, IN, self.FOLLOW_IN_in_compare_in2176)
                        if self._state.backtracking == 0:

                            IN113_tree = self._adaptor.createWithPayload(IN113)
                            root_0 = self._adaptor.becomeRoot(IN113_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_compare_in2179)
                        atom114 = self.atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, atom114.tree)


                    else:
                        break #loop40



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
    # SelectExpr.g:210:1: compare_eq : compare_ne ( EQ compare_ne )* ;
    def compare_eq(self, ):

        retval = self.compare_eq_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQ116 = None
        compare_ne115 = None

        compare_ne117 = None


        EQ116_tree = None

        try:
            try:
                # SelectExpr.g:210:12: ( compare_ne ( EQ compare_ne )* )
                # SelectExpr.g:210:14: compare_ne ( EQ compare_ne )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2189)
                compare_ne115 = self.compare_ne()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ne115.tree)
                # SelectExpr.g:210:25: ( EQ compare_ne )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == EQ) :
                        LA41_2 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt41 = 1




                    if alt41 == 1:
                        # SelectExpr.g:210:26: EQ compare_ne
                        pass 
                        EQ116=self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_eq2192)
                        if self._state.backtracking == 0:

                            EQ116_tree = self._adaptor.createWithPayload(EQ116)
                            root_0 = self._adaptor.becomeRoot(EQ116_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq2195)
                        compare_ne117 = self.compare_ne()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ne117.tree)


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

    # $ANTLR end "compare_eq"

    class compare_ne_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ne_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ne"
    # SelectExpr.g:211:1: compare_ne : compare_ge ( NE compare_ge )* ;
    def compare_ne(self, ):

        retval = self.compare_ne_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NE119 = None
        compare_ge118 = None

        compare_ge120 = None


        NE119_tree = None

        try:
            try:
                # SelectExpr.g:211:12: ( compare_ge ( NE compare_ge )* )
                # SelectExpr.g:211:14: compare_ge ( NE compare_ge )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2205)
                compare_ge118 = self.compare_ge()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ge118.tree)
                # SelectExpr.g:211:25: ( NE compare_ge )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == NE) :
                        LA42_2 = self.input.LA(2)

                        if (self.synpred48_SelectExpr()) :
                            alt42 = 1




                    if alt42 == 1:
                        # SelectExpr.g:211:26: NE compare_ge
                        pass 
                        NE119=self.match(self.input, NE, self.FOLLOW_NE_in_compare_ne2208)
                        if self._state.backtracking == 0:

                            NE119_tree = self._adaptor.createWithPayload(NE119)
                            root_0 = self._adaptor.becomeRoot(NE119_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne2211)
                        compare_ge120 = self.compare_ge()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ge120.tree)


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

    # $ANTLR end "compare_ne"

    class compare_ge_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ge_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ge"
    # SelectExpr.g:212:1: compare_ge : compare_gt ( GE compare_gt )* ;
    def compare_ge(self, ):

        retval = self.compare_ge_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GE122 = None
        compare_gt121 = None

        compare_gt123 = None


        GE122_tree = None

        try:
            try:
                # SelectExpr.g:212:12: ( compare_gt ( GE compare_gt )* )
                # SelectExpr.g:212:14: compare_gt ( GE compare_gt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2221)
                compare_gt121 = self.compare_gt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_gt121.tree)
                # SelectExpr.g:212:25: ( GE compare_gt )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == GE) :
                        LA43_2 = self.input.LA(2)

                        if (self.synpred49_SelectExpr()) :
                            alt43 = 1




                    if alt43 == 1:
                        # SelectExpr.g:212:26: GE compare_gt
                        pass 
                        GE122=self.match(self.input, GE, self.FOLLOW_GE_in_compare_ge2224)
                        if self._state.backtracking == 0:

                            GE122_tree = self._adaptor.createWithPayload(GE122)
                            root_0 = self._adaptor.becomeRoot(GE122_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2227)
                        compare_gt123 = self.compare_gt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_gt123.tree)


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

    # $ANTLR end "compare_ge"

    class compare_gt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_gt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_gt"
    # SelectExpr.g:213:1: compare_gt : compare_le ( GT compare_le )* ;
    def compare_gt(self, ):

        retval = self.compare_gt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GT125 = None
        compare_le124 = None

        compare_le126 = None


        GT125_tree = None

        try:
            try:
                # SelectExpr.g:213:12: ( compare_le ( GT compare_le )* )
                # SelectExpr.g:213:14: compare_le ( GT compare_le )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2237)
                compare_le124 = self.compare_le()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_le124.tree)
                # SelectExpr.g:213:25: ( GT compare_le )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == GT) :
                        LA44_2 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt44 = 1




                    if alt44 == 1:
                        # SelectExpr.g:213:26: GT compare_le
                        pass 
                        GT125=self.match(self.input, GT, self.FOLLOW_GT_in_compare_gt2240)
                        if self._state.backtracking == 0:

                            GT125_tree = self._adaptor.createWithPayload(GT125)
                            root_0 = self._adaptor.becomeRoot(GT125_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2243)
                        compare_le126 = self.compare_le()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_le126.tree)


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

    # $ANTLR end "compare_gt"

    class compare_le_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_le_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_le"
    # SelectExpr.g:214:1: compare_le : compare_lt ( LE compare_lt )* ;
    def compare_le(self, ):

        retval = self.compare_le_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LE128 = None
        compare_lt127 = None

        compare_lt129 = None


        LE128_tree = None

        try:
            try:
                # SelectExpr.g:214:12: ( compare_lt ( LE compare_lt )* )
                # SelectExpr.g:214:14: compare_lt ( LE compare_lt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2253)
                compare_lt127 = self.compare_lt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_lt127.tree)
                # SelectExpr.g:214:25: ( LE compare_lt )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LE) :
                        LA45_2 = self.input.LA(2)

                        if (self.synpred51_SelectExpr()) :
                            alt45 = 1




                    if alt45 == 1:
                        # SelectExpr.g:214:26: LE compare_lt
                        pass 
                        LE128=self.match(self.input, LE, self.FOLLOW_LE_in_compare_le2256)
                        if self._state.backtracking == 0:

                            LE128_tree = self._adaptor.createWithPayload(LE128)
                            root_0 = self._adaptor.becomeRoot(LE128_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2259)
                        compare_lt129 = self.compare_lt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_lt129.tree)


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

    # $ANTLR end "compare_le"

    class compare_lt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_lt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_lt"
    # SelectExpr.g:215:1: compare_lt : arithmetic_expr ( LT arithmetic_expr )* ;
    def compare_lt(self, ):

        retval = self.compare_lt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LT131 = None
        arithmetic_expr130 = None

        arithmetic_expr132 = None


        LT131_tree = None

        try:
            try:
                # SelectExpr.g:215:12: ( arithmetic_expr ( LT arithmetic_expr )* )
                # SelectExpr.g:215:14: arithmetic_expr ( LT arithmetic_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2269)
                arithmetic_expr130 = self.arithmetic_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_expr130.tree)
                # SelectExpr.g:215:30: ( LT arithmetic_expr )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == LT) :
                        LA46_2 = self.input.LA(2)

                        if (self.synpred52_SelectExpr()) :
                            alt46 = 1




                    if alt46 == 1:
                        # SelectExpr.g:215:31: LT arithmetic_expr
                        pass 
                        LT131=self.match(self.input, LT, self.FOLLOW_LT_in_compare_lt2272)
                        if self._state.backtracking == 0:

                            LT131_tree = self._adaptor.createWithPayload(LT131)
                            root_0 = self._adaptor.becomeRoot(LT131_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2275)
                        arithmetic_expr132 = self.arithmetic_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_expr132.tree)


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

    # $ANTLR end "compare_lt"

    class arithmetic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_expr"
    # SelectExpr.g:217:1: arithmetic_expr : arithmetic_sub_add ;
    def arithmetic_expr(self, ):

        retval = self.arithmetic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        arithmetic_sub_add133 = None



        try:
            try:
                # SelectExpr.g:217:17: ( arithmetic_sub_add )
                # SelectExpr.g:217:19: arithmetic_sub_add
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_sub_add_in_arithmetic_expr2286)
                arithmetic_sub_add133 = self.arithmetic_sub_add()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_sub_add133.tree)



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
    # SelectExpr.g:218:1: arithmetic_sub_add : arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* ;
    def arithmetic_sub_add(self, ):

        retval = self.arithmetic_sub_add_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB135 = None
        ADD136 = None
        arithmetic_mul_div_mod134 = None

        arithmetic_mul_div_mod137 = None


        SUB135_tree = None
        ADD136_tree = None

        try:
            try:
                # SelectExpr.g:218:20: ( arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* )
                # SelectExpr.g:218:22: arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2294)
                arithmetic_mul_div_mod134 = self.arithmetic_mul_div_mod()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_mul_div_mod134.tree)
                # SelectExpr.g:218:45: ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == SUB) :
                        LA48_2 = self.input.LA(2)

                        if (self.synpred54_SelectExpr()) :
                            alt48 = 1


                    elif (LA48_0 == ADD) :
                        LA48_3 = self.input.LA(2)

                        if (self.synpred54_SelectExpr()) :
                            alt48 = 1




                    if alt48 == 1:
                        # SelectExpr.g:218:46: ( SUB | ADD ) arithmetic_mul_div_mod
                        pass 
                        # SelectExpr.g:218:46: ( SUB | ADD )
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == SUB) :
                            alt47 = 1
                        elif (LA47_0 == ADD) :
                            alt47 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 47, 0, self.input)

                            raise nvae

                        if alt47 == 1:
                            # SelectExpr.g:218:47: SUB
                            pass 
                            SUB135=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_sub_add2298)
                            if self._state.backtracking == 0:

                                SUB135_tree = self._adaptor.createWithPayload(SUB135)
                                root_0 = self._adaptor.becomeRoot(SUB135_tree, root_0)



                        elif alt47 == 2:
                            # SelectExpr.g:218:52: ADD
                            pass 
                            ADD136=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_sub_add2301)
                            if self._state.backtracking == 0:

                                ADD136_tree = self._adaptor.createWithPayload(ADD136)
                                root_0 = self._adaptor.becomeRoot(ADD136_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2305)
                        arithmetic_mul_div_mod137 = self.arithmetic_mul_div_mod()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_mul_div_mod137.tree)


                    else:
                        break #loop48



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
    # SelectExpr.g:219:1: arithmetic_mul_div_mod : arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* ;
    def arithmetic_mul_div_mod(self, ):

        retval = self.arithmetic_mul_div_mod_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MUL139 = None
        DIV140 = None
        MOD141 = None
        arithmetic_pow138 = None

        arithmetic_pow142 = None


        MUL139_tree = None
        DIV140_tree = None
        MOD141_tree = None

        try:
            try:
                # SelectExpr.g:219:24: ( arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* )
                # SelectExpr.g:219:26: arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2315)
                arithmetic_pow138 = self.arithmetic_pow()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_pow138.tree)
                # SelectExpr.g:219:41: ( ( MUL | DIV | MOD ) arithmetic_pow )*
                while True: #loop50
                    alt50 = 2
                    LA50 = self.input.LA(1)
                    if LA50 == MUL:
                        LA50_2 = self.input.LA(2)

                        if (self.synpred57_SelectExpr()) :
                            alt50 = 1


                    elif LA50 == DIV:
                        LA50_3 = self.input.LA(2)

                        if (self.synpred57_SelectExpr()) :
                            alt50 = 1


                    elif LA50 == MOD:
                        LA50_4 = self.input.LA(2)

                        if (self.synpred57_SelectExpr()) :
                            alt50 = 1



                    if alt50 == 1:
                        # SelectExpr.g:219:42: ( MUL | DIV | MOD ) arithmetic_pow
                        pass 
                        # SelectExpr.g:219:42: ( MUL | DIV | MOD )
                        alt49 = 3
                        LA49 = self.input.LA(1)
                        if LA49 == MUL:
                            alt49 = 1
                        elif LA49 == DIV:
                            alt49 = 2
                        elif LA49 == MOD:
                            alt49 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 49, 0, self.input)

                            raise nvae

                        if alt49 == 1:
                            # SelectExpr.g:219:43: MUL
                            pass 
                            MUL139=self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_mul_div_mod2319)
                            if self._state.backtracking == 0:

                                MUL139_tree = self._adaptor.createWithPayload(MUL139)
                                root_0 = self._adaptor.becomeRoot(MUL139_tree, root_0)



                        elif alt49 == 2:
                            # SelectExpr.g:219:50: DIV
                            pass 
                            DIV140=self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_mul_div_mod2324)
                            if self._state.backtracking == 0:

                                DIV140_tree = self._adaptor.createWithPayload(DIV140)
                                root_0 = self._adaptor.becomeRoot(DIV140_tree, root_0)



                        elif alt49 == 3:
                            # SelectExpr.g:219:57: MOD
                            pass 
                            MOD141=self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_mul_div_mod2329)
                            if self._state.backtracking == 0:

                                MOD141_tree = self._adaptor.createWithPayload(MOD141)
                                root_0 = self._adaptor.becomeRoot(MOD141_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2333)
                        arithmetic_pow142 = self.arithmetic_pow()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_pow142.tree)


                    else:
                        break #loop50



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
    # SelectExpr.g:220:1: arithmetic_pow : arithmetic_unary ( POW arithmetic_unary )* ;
    def arithmetic_pow(self, ):

        retval = self.arithmetic_pow_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POW144 = None
        arithmetic_unary143 = None

        arithmetic_unary145 = None


        POW144_tree = None

        try:
            try:
                # SelectExpr.g:220:16: ( arithmetic_unary ( POW arithmetic_unary )* )
                # SelectExpr.g:220:18: arithmetic_unary ( POW arithmetic_unary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2343)
                arithmetic_unary143 = self.arithmetic_unary()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_unary143.tree)
                # SelectExpr.g:220:35: ( POW arithmetic_unary )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == POW) :
                        LA51_2 = self.input.LA(2)

                        if (self.synpred58_SelectExpr()) :
                            alt51 = 1




                    if alt51 == 1:
                        # SelectExpr.g:220:36: POW arithmetic_unary
                        pass 
                        POW144=self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_pow2346)
                        if self._state.backtracking == 0:

                            POW144_tree = self._adaptor.createWithPayload(POW144)
                            root_0 = self._adaptor.becomeRoot(POW144_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2349)
                        arithmetic_unary145 = self.arithmetic_unary()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_unary145.tree)


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

    # $ANTLR end "arithmetic_pow"

    class arithmetic_unary_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_unary_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_unary"
    # SelectExpr.g:221:1: arithmetic_unary : ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom LIST_BEGIN parameter LIST_END -> ^( ELEMENT atom parameter ) | atom );
    def arithmetic_unary(self, ):

        retval = self.arithmetic_unary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB146 = None
        ADD148 = None
        LIST_BEGIN151 = None
        LIST_END153 = None
        atom147 = None

        atom149 = None

        atom150 = None

        parameter152 = None

        atom154 = None


        SUB146_tree = None
        ADD148_tree = None
        LIST_BEGIN151_tree = None
        LIST_END153_tree = None
        stream_SUB = RewriteRuleTokenStream(self._adaptor, "token SUB")
        stream_ADD = RewriteRuleTokenStream(self._adaptor, "token ADD")
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # SelectExpr.g:221:18: ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom LIST_BEGIN parameter LIST_END -> ^( ELEMENT atom parameter ) | atom )
                alt52 = 4
                alt52 = self.dfa52.predict(self.input)
                if alt52 == 1:
                    # SelectExpr.g:222:2: SUB atom
                    pass 
                    SUB146=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_unary2360) 
                    if self._state.backtracking == 0:
                        stream_SUB.add(SUB146)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2362)
                    atom147 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom147.tree)

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
                        # 222:11: -> ^( NEG atom )
                        # SelectExpr.g:222:14: ^( NEG atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEG, "NEG"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt52 == 2:
                    # SelectExpr.g:223:5: ADD atom
                    pass 
                    ADD148=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_unary2376) 
                    if self._state.backtracking == 0:
                        stream_ADD.add(ADD148)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2378)
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
                        # 223:14: -> ^( POS atom )
                        # SelectExpr.g:223:17: ^( POS atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(POS, "POS"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt52 == 3:
                    # SelectExpr.g:224:5: atom LIST_BEGIN parameter LIST_END
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2392)
                    atom150 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom150.tree)
                    LIST_BEGIN151=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_arithmetic_unary2394) 
                    if self._state.backtracking == 0:
                        stream_LIST_BEGIN.add(LIST_BEGIN151)
                    self._state.following.append(self.FOLLOW_parameter_in_arithmetic_unary2396)
                    parameter152 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter152.tree)
                    LIST_END153=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_arithmetic_unary2398) 
                    if self._state.backtracking == 0:
                        stream_LIST_END.add(LIST_END153)

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
                        # 224:40: -> ^( ELEMENT atom parameter )
                        # SelectExpr.g:224:43: ^( ELEMENT atom parameter )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEMENT, "ELEMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt52 == 4:
                    # SelectExpr.g:225:5: atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2414)
                    atom154 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom154.tree)


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
    # SelectExpr.g:228:1: atom : ( value | variable | if_statement | function | '(' expr ')' | statement_select );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal159 = None
        char_literal161 = None
        value155 = None

        variable156 = None

        if_statement157 = None

        function158 = None

        expr160 = None

        statement_select162 = None


        char_literal159_tree = None
        char_literal161_tree = None

        try:
            try:
                # SelectExpr.g:229:2: ( value | variable | if_statement | function | '(' expr ')' | statement_select )
                alt53 = 6
                LA53 = self.input.LA(1)
                if LA53 == LIST_BEGIN or LA53 == THIS or LA53 == STRING or LA53 == INTEGER or LA53 == FLOAT or LA53 == TRUE or LA53 == FALSE:
                    alt53 = 1
                elif LA53 == PHRASE:
                    LA53 = self.input.LA(2)
                    if LA53 == DOT:
                        alt53 = 1
                    elif LA53 == 107:
                        alt53 = 4
                    elif LA53 == EOF or LA53 == SEP or LA53 == END or LA53 == AND or LA53 == XOR or LA53 == OR or LA53 == IN or LA53 == EQ or LA53 == NE or LA53 == LE or LA53 == GE or LA53 == LT or LA53 == GT or LA53 == ADD or LA53 == SUB or LA53 == MUL or LA53 == DIV or LA53 == MOD or LA53 == POW or LA53 == LIST_BEGIN or LA53 == LIST_END or LA53 == AGE_BEGIN or LA53 == AGE_END or LA53 == WHERE or LA53 == ORDER or LA53 == GROUP or LA53 == AS or LA53 == CONNECT or LA53 == START or LA53 == STOP or LA53 == 108:
                        alt53 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 53, 2, self.input)

                        raise nvae

                elif LA53 == IF:
                    alt53 = 3
                elif LA53 == 107:
                    alt53 = 5
                elif LA53 == SELECT:
                    alt53 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # SelectExpr.g:229:4: value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_value_in_atom2425)
                    value155 = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, value155.tree)


                elif alt53 == 2:
                    # SelectExpr.g:230:4: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_atom2430)
                    variable156 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable156.tree)


                elif alt53 == 3:
                    # SelectExpr.g:231:4: if_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_statement_in_atom2435)
                    if_statement157 = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_statement157.tree)


                elif alt53 == 4:
                    # SelectExpr.g:232:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_atom2440)
                    function158 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function158.tree)


                elif alt53 == 5:
                    # SelectExpr.g:233:4: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal159=self.match(self.input, 107, self.FOLLOW_107_in_atom2445)
                    self._state.following.append(self.FOLLOW_expr_in_atom2448)
                    expr160 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr160.tree)
                    char_literal161=self.match(self.input, 108, self.FOLLOW_108_in_atom2450)


                elif alt53 == 6:
                    # SelectExpr.g:234:4: statement_select
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_atom2456)
                    statement_select162 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select162.tree)


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
    # SelectExpr.g:237:1: function : PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE163 = None
        char_literal164 = None
        char_literal166 = None
        parameter165 = None


        PHRASE163_tree = None
        char_literal164_tree = None
        char_literal166_tree = None
        stream_107 = RewriteRuleTokenStream(self._adaptor, "token 107")
        stream_108 = RewriteRuleTokenStream(self._adaptor, "token 108")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # SelectExpr.g:237:10: ( PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) )
                # SelectExpr.g:237:12: PHRASE '(' ( parameter )? ')'
                pass 
                PHRASE163=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function2465) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE163)
                char_literal164=self.match(self.input, 107, self.FOLLOW_107_in_function2467) 
                if self._state.backtracking == 0:
                    stream_107.add(char_literal164)
                # SelectExpr.g:237:23: ( parameter )?
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == NOT or (ADD <= LA54_0 <= SUB) or LA54_0 == IF or LA54_0 == LIST_BEGIN or LA54_0 == SELECT or LA54_0 == THIS or LA54_0 == STRING or (INTEGER <= LA54_0 <= FALSE) or LA54_0 == PHRASE or LA54_0 == 107) :
                    alt54 = 1
                if alt54 == 1:
                    # SelectExpr.g:0:0: parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function2469)
                    parameter165 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter165.tree)



                char_literal166=self.match(self.input, 108, self.FOLLOW_108_in_function2472) 
                if self._state.backtracking == 0:
                    stream_108.add(char_literal166)

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
                    # 237:38: -> ^( FCT PHRASE ( parameter )? )
                    # SelectExpr.g:237:41: ^( FCT PHRASE ( parameter )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FCT, "FCT"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:237:54: ( parameter )?
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
    # SelectExpr.g:240:1: parameter : expr ( SEP expr )* ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEP168 = None
        expr167 = None

        expr169 = None


        SEP168_tree = None

        try:
            try:
                # SelectExpr.g:240:11: ( expr ( SEP expr )* )
                # SelectExpr.g:240:13: expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_parameter2492)
                expr167 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr167.tree)
                # SelectExpr.g:240:18: ( SEP expr )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == SEP) :
                        alt55 = 1


                    if alt55 == 1:
                        # SelectExpr.g:240:19: SEP expr
                        pass 
                        SEP168=self.match(self.input, SEP, self.FOLLOW_SEP_in_parameter2495)
                        self._state.following.append(self.FOLLOW_expr_in_parameter2498)
                        expr169 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr169.tree)


                    else:
                        break #loop55



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
    # SelectExpr.g:243:1: variable : PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) ;
    def variable(self, ):

        retval = self.variable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE170 = None
        age171 = None


        PHRASE170_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:243:10: ( PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) )
                # SelectExpr.g:243:12: PHRASE ( age )?
                pass 
                PHRASE170=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable2509) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE170)
                # SelectExpr.g:243:19: ( age )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == AGE_BEGIN) :
                    alt56 = 1
                if alt56 == 1:
                    # SelectExpr.g:243:20: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable2512)
                    age171 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age171.tree)




                # AST Rewrite
                # elements: age, PHRASE
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
                    # 243:26: -> ^( VAR PHRASE ( age )? )
                    # SelectExpr.g:243:29: ^( VAR PHRASE ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:243:42: ( age )?
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
    # SelectExpr.g:246:1: age : AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) ;
    def age(self, ):

        retval = self.age_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AGE_BEGIN172 = None
        AGE_END174 = None
        expr173 = None


        AGE_BEGIN172_tree = None
        AGE_END174_tree = None
        stream_AGE_BEGIN = RewriteRuleTokenStream(self._adaptor, "token AGE_BEGIN")
        stream_AGE_END = RewriteRuleTokenStream(self._adaptor, "token AGE_END")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:246:5: ( AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) )
                # SelectExpr.g:246:7: AGE_BEGIN ( expr )? AGE_END
                pass 
                AGE_BEGIN172=self.match(self.input, AGE_BEGIN, self.FOLLOW_AGE_BEGIN_in_age2536) 
                if self._state.backtracking == 0:
                    stream_AGE_BEGIN.add(AGE_BEGIN172)
                # SelectExpr.g:246:17: ( expr )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == NOT or (ADD <= LA57_0 <= SUB) or LA57_0 == IF or LA57_0 == LIST_BEGIN or LA57_0 == SELECT or LA57_0 == THIS or LA57_0 == STRING or (INTEGER <= LA57_0 <= FALSE) or LA57_0 == PHRASE or LA57_0 == 107) :
                    alt57 = 1
                if alt57 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_age2538)
                    expr173 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr173.tree)



                AGE_END174=self.match(self.input, AGE_END, self.FOLLOW_AGE_END_in_age2541) 
                if self._state.backtracking == 0:
                    stream_AGE_END.add(AGE_END174)

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
                    # 246:31: -> ^( AGE ( expr )? )
                    # SelectExpr.g:246:34: ^( AGE ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AGE, "AGE"), root_1)

                    # SelectExpr.g:246:40: ( expr )?
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
    # SelectExpr.g:249:1: value : ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRING175 = None
        FLOAT176 = None
        INTEGER177 = None
        TRUE178 = None
        FALSE179 = None
        this_180 = None

        list_181 = None


        STRING175_tree = None
        FLOAT176_tree = None
        INTEGER177_tree = None
        TRUE178_tree = None
        FALSE179_tree = None
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_TRUE = RewriteRuleTokenStream(self._adaptor, "token TRUE")
        stream_FALSE = RewriteRuleTokenStream(self._adaptor, "token FALSE")
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")

        try:
            try:
                # SelectExpr.g:249:7: ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ )
                alt58 = 7
                LA58 = self.input.LA(1)
                if LA58 == STRING:
                    alt58 = 1
                elif LA58 == FLOAT:
                    alt58 = 2
                elif LA58 == INTEGER:
                    alt58 = 3
                elif LA58 == TRUE:
                    alt58 = 4
                elif LA58 == FALSE:
                    alt58 = 5
                elif LA58 == THIS or LA58 == PHRASE:
                    alt58 = 6
                elif LA58 == LIST_BEGIN:
                    alt58 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # SelectExpr.g:249:9: STRING
                    pass 
                    STRING175=self.match(self.input, STRING, self.FOLLOW_STRING_in_value2559) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING175)

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
                        # 249:17: -> ^( VAL STRING )
                        # SelectExpr.g:249:20: ^( VAL STRING )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_STRING.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt58 == 2:
                    # SelectExpr.g:250:4: FLOAT
                    pass 
                    FLOAT176=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value2573) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT176)

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
                        # 250:11: -> ^( VAL FLOAT )
                        # SelectExpr.g:250:14: ^( VAL FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt58 == 3:
                    # SelectExpr.g:251:4: INTEGER
                    pass 
                    INTEGER177=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value2587) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER177)

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
                        # 251:12: -> ^( VAL INTEGER )
                        # SelectExpr.g:251:15: ^( VAL INTEGER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt58 == 4:
                    # SelectExpr.g:252:4: TRUE
                    pass 
                    TRUE178=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value2600) 
                    if self._state.backtracking == 0:
                        stream_TRUE.add(TRUE178)

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
                        # 252:10: -> ^( VAL TRUE )
                        # SelectExpr.g:252:13: ^( VAL TRUE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_TRUE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt58 == 5:
                    # SelectExpr.g:253:4: FALSE
                    pass 
                    FALSE179=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value2614) 
                    if self._state.backtracking == 0:
                        stream_FALSE.add(FALSE179)

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
                        # 253:11: -> ^( VAL FALSE )
                        # SelectExpr.g:253:14: ^( VAL FALSE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FALSE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt58 == 6:
                    # SelectExpr.g:254:4: this_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_this__in_value2628)
                    this_180 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, this_180.tree)


                elif alt58 == 7:
                    # SelectExpr.g:255:4: list_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list__in_value2633)
                    list_181 = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_181.tree)


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
    # SelectExpr.g:258:1: this_ : ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        retval = self.this__return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE182 = None
        DOT183 = None
        THIS184 = None

        PHRASE182_tree = None
        DOT183_tree = None
        THIS184_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")

        try:
            try:
                # SelectExpr.g:258:7: ( ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) )
                # SelectExpr.g:258:9: ( PHRASE DOT )? THIS
                pass 
                # SelectExpr.g:258:9: ( PHRASE DOT )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == PHRASE) :
                    alt59 = 1
                if alt59 == 1:
                    # SelectExpr.g:258:10: PHRASE DOT
                    pass 
                    PHRASE182=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_2644) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE182)
                    DOT183=self.match(self.input, DOT, self.FOLLOW_DOT_in_this_2646) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT183)



                THIS184=self.match(self.input, THIS, self.FOLLOW_THIS_in_this_2650) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS184)

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
                    # 258:29: -> ^( THIS ( PHRASE )? )
                    # SelectExpr.g:258:32: ^( THIS ( PHRASE )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_THIS.nextNode(), root_1)

                    # SelectExpr.g:258:39: ( PHRASE )?
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
    # SelectExpr.g:261:1: list_ : LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) ;
    def list_(self, ):

        retval = self.list__return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIST_BEGIN185 = None
        SEP187 = None
        LIST_END189 = None
        expr186 = None

        expr188 = None


        LIST_BEGIN185_tree = None
        SEP187_tree = None
        LIST_END189_tree = None
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_SEP = RewriteRuleTokenStream(self._adaptor, "token SEP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:261:7: ( LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) )
                # SelectExpr.g:261:10: LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END
                pass 
                LIST_BEGIN185=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_list_2671) 
                if self._state.backtracking == 0:
                    stream_LIST_BEGIN.add(LIST_BEGIN185)
                # SelectExpr.g:261:21: ( ( expr )? ( SEP expr )* )
                # SelectExpr.g:261:23: ( expr )? ( SEP expr )*
                pass 
                # SelectExpr.g:261:23: ( expr )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == NOT or (ADD <= LA60_0 <= SUB) or LA60_0 == IF or LA60_0 == LIST_BEGIN or LA60_0 == SELECT or LA60_0 == THIS or LA60_0 == STRING or (INTEGER <= LA60_0 <= FALSE) or LA60_0 == PHRASE or LA60_0 == 107) :
                    alt60 = 1
                if alt60 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_list_2675)
                    expr186 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr186.tree)



                # SelectExpr.g:261:29: ( SEP expr )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == SEP) :
                        alt61 = 1


                    if alt61 == 1:
                        # SelectExpr.g:261:30: SEP expr
                        pass 
                        SEP187=self.match(self.input, SEP, self.FOLLOW_SEP_in_list_2679) 
                        if self._state.backtracking == 0:
                            stream_SEP.add(SEP187)
                        self._state.following.append(self.FOLLOW_expr_in_list_2681)
                        expr188 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr188.tree)


                    else:
                        break #loop61



                LIST_END189=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_list_2687) 
                if self._state.backtracking == 0:
                    stream_LIST_END.add(LIST_END189)

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
                    # 261:52: -> ^( LIST ( expr )* )
                    # SelectExpr.g:261:55: ^( LIST ( expr )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # SelectExpr.g:261:62: ( expr )*
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
        # SelectExpr.g:150:13: ( statement_select END )
        # SelectExpr.g:150:13: statement_select END
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectExpr1513)
        self.statement_select()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred2_SelectExpr1515)


    # $ANTLR end "synpred2_SelectExpr"



    # $ANTLR start "synpred3_SelectExpr"
    def synpred3_SelectExpr_fragment(self, ):
        # SelectExpr.g:151:4: ( expr END )
        # SelectExpr.g:151:4: expr END
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred3_SelectExpr1521)
        self.expr()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred3_SelectExpr1523)


    # $ANTLR end "synpred3_SelectExpr"



    # $ANTLR start "synpred4_SelectExpr"
    def synpred4_SelectExpr_fragment(self, ):
        # SelectExpr.g:156:17: ( where_ )
        # SelectExpr.g:156:17: where_
        pass 
        self._state.following.append(self.FOLLOW_where__in_synpred4_SelectExpr1545)
        self.where_()

        self._state.following.pop()


    # $ANTLR end "synpred4_SelectExpr"



    # $ANTLR start "synpred6_SelectExpr"
    def synpred6_SelectExpr_fragment(self, ):
        # SelectExpr.g:156:27: ( ( start_ )? connect_ stop_ )
        # SelectExpr.g:156:27: ( start_ )? connect_ stop_
        pass 
        # SelectExpr.g:156:27: ( start_ )?
        alt62 = 2
        LA62_0 = self.input.LA(1)

        if (LA62_0 == START) :
            alt62 = 1
        if alt62 == 1:
            # SelectExpr.g:156:28: start_
            pass 
            self._state.following.append(self.FOLLOW_start__in_synpred6_SelectExpr1551)
            self.start_()

            self._state.following.pop()



        self._state.following.append(self.FOLLOW_connect__in_synpred6_SelectExpr1555)
        self.connect_()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_stop__in_synpred6_SelectExpr1557)
        self.stop_()

        self._state.following.pop()


    # $ANTLR end "synpred6_SelectExpr"



    # $ANTLR start "synpred8_SelectExpr"
    def synpred8_SelectExpr_fragment(self, ):
        # SelectExpr.g:156:55: ( group_ ( having_ )? )
        # SelectExpr.g:156:55: group_ ( having_ )?
        pass 
        self._state.following.append(self.FOLLOW_group__in_synpred8_SelectExpr1562)
        self.group_()

        self._state.following.pop()
        # SelectExpr.g:156:62: ( having_ )?
        alt63 = 2
        LA63_0 = self.input.LA(1)

        if (LA63_0 == HAVING) :
            alt63 = 1
        if alt63 == 1:
            # SelectExpr.g:156:63: having_
            pass 
            self._state.following.append(self.FOLLOW_having__in_synpred8_SelectExpr1565)
            self.having_()

            self._state.following.pop()





    # $ANTLR end "synpred8_SelectExpr"



    # $ANTLR start "synpred9_SelectExpr"
    def synpred9_SelectExpr_fragment(self, ):
        # SelectExpr.g:156:76: ( order_ )
        # SelectExpr.g:156:76: order_
        pass 
        self._state.following.append(self.FOLLOW_order__in_synpred9_SelectExpr1572)
        self.order_()

        self._state.following.pop()


    # $ANTLR end "synpred9_SelectExpr"



    # $ANTLR start "synpred10_SelectExpr"
    def synpred10_SelectExpr_fragment(self, ):
        # SelectExpr.g:156:86: ( as_ )
        # SelectExpr.g:156:86: as_
        pass 
        self._state.following.append(self.FOLLOW_as__in_synpred10_SelectExpr1577)
        self.as_()

        self._state.following.pop()


    # $ANTLR end "synpred10_SelectExpr"



    # $ANTLR start "synpred17_SelectExpr"
    def synpred17_SelectExpr_fragment(self, ):
        # SelectExpr.g:162:21: ( SEP expr )
        # SelectExpr.g:162:21: SEP expr
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred17_SelectExpr1694)
        self._state.following.append(self.FOLLOW_expr_in_synpred17_SelectExpr1697)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectExpr"



    # $ANTLR start "synpred26_SelectExpr"
    def synpred26_SelectExpr_fragment(self, ):
        # SelectExpr.g:177:44: ( SEP ( PHRASE | function ) )
        # SelectExpr.g:177:44: SEP ( PHRASE | function )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred26_SelectExpr1827)
        # SelectExpr.g:177:49: ( PHRASE | function )
        alt65 = 2
        LA65_0 = self.input.LA(1)

        if (LA65_0 == PHRASE) :
            LA65_1 = self.input.LA(2)

            if (LA65_1 == 107) :
                alt65 = 2
            elif (LA65_1 == EOF) :
                alt65 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 65, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 65, 0, self.input)

            raise nvae

        if alt65 == 1:
            # SelectExpr.g:177:51: PHRASE
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred26_SelectExpr1832)


        elif alt65 == 2:
            # SelectExpr.g:177:60: function
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred26_SelectExpr1836)
            self.function()

            self._state.following.pop()





    # $ANTLR end "synpred26_SelectExpr"



    # $ANTLR start "synpred29_SelectExpr"
    def synpred29_SelectExpr_fragment(self, ):
        # SelectExpr.g:183:66: ( SEP ( PHRASE direction_ | function direction_ ) )
        # SelectExpr.g:183:66: SEP ( PHRASE direction_ | function direction_ )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred29_SelectExpr1883)
        # SelectExpr.g:183:71: ( PHRASE direction_ | function direction_ )
        alt66 = 2
        LA66_0 = self.input.LA(1)

        if (LA66_0 == PHRASE) :
            LA66_1 = self.input.LA(2)

            if (LA66_1 == 107) :
                alt66 = 2
            elif (LA66_1 == EOF or (ASC <= LA66_1 <= DESC)) :
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
            # SelectExpr.g:183:73: PHRASE direction_
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred29_SelectExpr1888)
            self._state.following.append(self.FOLLOW_direction__in_synpred29_SelectExpr1890)
            self.direction_()

            self._state.following.pop()


        elif alt66 == 2:
            # SelectExpr.g:183:93: function direction_
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred29_SelectExpr1894)
            self.function()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_direction__in_synpred29_SelectExpr1896)
            self.direction_()

            self._state.following.pop()





    # $ANTLR end "synpred29_SelectExpr"



    # $ANTLR start "synpred37_SelectExpr"
    def synpred37_SelectExpr_fragment(self, ):
        # SelectExpr.g:192:8: ( assign_expr )
        # SelectExpr.g:192:8: assign_expr
        pass 
        self._state.following.append(self.FOLLOW_assign_expr_in_synpred37_SelectExpr1967)
        self.assign_expr()

        self._state.following.pop()


    # $ANTLR end "synpred37_SelectExpr"



    # $ANTLR start "synpred42_SelectExpr"
    def synpred42_SelectExpr_fragment(self, ):
        # SelectExpr.g:203:24: ( OR logic_xor )
        # SelectExpr.g:203:24: OR logic_xor
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred42_SelectExpr2104)
        self._state.following.append(self.FOLLOW_logic_xor_in_synpred42_SelectExpr2108)
        self.logic_xor()

        self._state.following.pop()


    # $ANTLR end "synpred42_SelectExpr"



    # $ANTLR start "synpred43_SelectExpr"
    def synpred43_SelectExpr_fragment(self, ):
        # SelectExpr.g:204:24: ( XOR logic_and )
        # SelectExpr.g:204:24: XOR logic_and
        pass 
        self.match(self.input, XOR, self.FOLLOW_XOR_in_synpred43_SelectExpr2121)
        self._state.following.append(self.FOLLOW_logic_and_in_synpred43_SelectExpr2124)
        self.logic_and()

        self._state.following.pop()


    # $ANTLR end "synpred43_SelectExpr"



    # $ANTLR start "synpred44_SelectExpr"
    def synpred44_SelectExpr_fragment(self, ):
        # SelectExpr.g:205:24: ( AND logic_not )
        # SelectExpr.g:205:24: AND logic_not
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred44_SelectExpr2137)
        self._state.following.append(self.FOLLOW_logic_not_in_synpred44_SelectExpr2140)
        self.logic_not()

        self._state.following.pop()


    # $ANTLR end "synpred44_SelectExpr"



    # $ANTLR start "synpred46_SelectExpr"
    def synpred46_SelectExpr_fragment(self, ):
        # SelectExpr.g:209:26: ( IN atom )
        # SelectExpr.g:209:26: IN atom
        pass 
        self.match(self.input, IN, self.FOLLOW_IN_in_synpred46_SelectExpr2176)
        self._state.following.append(self.FOLLOW_atom_in_synpred46_SelectExpr2179)
        self.atom()

        self._state.following.pop()


    # $ANTLR end "synpred46_SelectExpr"



    # $ANTLR start "synpred47_SelectExpr"
    def synpred47_SelectExpr_fragment(self, ):
        # SelectExpr.g:210:26: ( EQ compare_ne )
        # SelectExpr.g:210:26: EQ compare_ne
        pass 
        self.match(self.input, EQ, self.FOLLOW_EQ_in_synpred47_SelectExpr2192)
        self._state.following.append(self.FOLLOW_compare_ne_in_synpred47_SelectExpr2195)
        self.compare_ne()

        self._state.following.pop()


    # $ANTLR end "synpred47_SelectExpr"



    # $ANTLR start "synpred48_SelectExpr"
    def synpred48_SelectExpr_fragment(self, ):
        # SelectExpr.g:211:26: ( NE compare_ge )
        # SelectExpr.g:211:26: NE compare_ge
        pass 
        self.match(self.input, NE, self.FOLLOW_NE_in_synpred48_SelectExpr2208)
        self._state.following.append(self.FOLLOW_compare_ge_in_synpred48_SelectExpr2211)
        self.compare_ge()

        self._state.following.pop()


    # $ANTLR end "synpred48_SelectExpr"



    # $ANTLR start "synpred49_SelectExpr"
    def synpred49_SelectExpr_fragment(self, ):
        # SelectExpr.g:212:26: ( GE compare_gt )
        # SelectExpr.g:212:26: GE compare_gt
        pass 
        self.match(self.input, GE, self.FOLLOW_GE_in_synpred49_SelectExpr2224)
        self._state.following.append(self.FOLLOW_compare_gt_in_synpred49_SelectExpr2227)
        self.compare_gt()

        self._state.following.pop()


    # $ANTLR end "synpred49_SelectExpr"



    # $ANTLR start "synpred50_SelectExpr"
    def synpred50_SelectExpr_fragment(self, ):
        # SelectExpr.g:213:26: ( GT compare_le )
        # SelectExpr.g:213:26: GT compare_le
        pass 
        self.match(self.input, GT, self.FOLLOW_GT_in_synpred50_SelectExpr2240)
        self._state.following.append(self.FOLLOW_compare_le_in_synpred50_SelectExpr2243)
        self.compare_le()

        self._state.following.pop()


    # $ANTLR end "synpred50_SelectExpr"



    # $ANTLR start "synpred51_SelectExpr"
    def synpred51_SelectExpr_fragment(self, ):
        # SelectExpr.g:214:26: ( LE compare_lt )
        # SelectExpr.g:214:26: LE compare_lt
        pass 
        self.match(self.input, LE, self.FOLLOW_LE_in_synpred51_SelectExpr2256)
        self._state.following.append(self.FOLLOW_compare_lt_in_synpred51_SelectExpr2259)
        self.compare_lt()

        self._state.following.pop()


    # $ANTLR end "synpred51_SelectExpr"



    # $ANTLR start "synpred52_SelectExpr"
    def synpred52_SelectExpr_fragment(self, ):
        # SelectExpr.g:215:31: ( LT arithmetic_expr )
        # SelectExpr.g:215:31: LT arithmetic_expr
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred52_SelectExpr2272)
        self._state.following.append(self.FOLLOW_arithmetic_expr_in_synpred52_SelectExpr2275)
        self.arithmetic_expr()

        self._state.following.pop()


    # $ANTLR end "synpred52_SelectExpr"



    # $ANTLR start "synpred54_SelectExpr"
    def synpred54_SelectExpr_fragment(self, ):
        # SelectExpr.g:218:46: ( ( SUB | ADD ) arithmetic_mul_div_mod )
        # SelectExpr.g:218:46: ( SUB | ADD ) arithmetic_mul_div_mod
        pass 
        if (ADD <= self.input.LA(1) <= SUB):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_synpred54_SelectExpr2305)
        self.arithmetic_mul_div_mod()

        self._state.following.pop()


    # $ANTLR end "synpred54_SelectExpr"



    # $ANTLR start "synpred57_SelectExpr"
    def synpred57_SelectExpr_fragment(self, ):
        # SelectExpr.g:219:42: ( ( MUL | DIV | MOD ) arithmetic_pow )
        # SelectExpr.g:219:42: ( MUL | DIV | MOD ) arithmetic_pow
        pass 
        if (MUL <= self.input.LA(1) <= MOD):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_pow_in_synpred57_SelectExpr2333)
        self.arithmetic_pow()

        self._state.following.pop()


    # $ANTLR end "synpred57_SelectExpr"



    # $ANTLR start "synpred58_SelectExpr"
    def synpred58_SelectExpr_fragment(self, ):
        # SelectExpr.g:220:36: ( POW arithmetic_unary )
        # SelectExpr.g:220:36: POW arithmetic_unary
        pass 
        self.match(self.input, POW, self.FOLLOW_POW_in_synpred58_SelectExpr2346)
        self._state.following.append(self.FOLLOW_arithmetic_unary_in_synpred58_SelectExpr2349)
        self.arithmetic_unary()

        self._state.following.pop()


    # $ANTLR end "synpred58_SelectExpr"



    # $ANTLR start "synpred61_SelectExpr"
    def synpred61_SelectExpr_fragment(self, ):
        # SelectExpr.g:224:5: ( atom LIST_BEGIN parameter LIST_END )
        # SelectExpr.g:224:5: atom LIST_BEGIN parameter LIST_END
        pass 
        self._state.following.append(self.FOLLOW_atom_in_synpred61_SelectExpr2392)
        self.atom()

        self._state.following.pop()
        self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_synpred61_SelectExpr2394)
        self._state.following.append(self.FOLLOW_parameter_in_synpred61_SelectExpr2396)
        self.parameter()

        self._state.following.pop()
        self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_synpred61_SelectExpr2398)


    # $ANTLR end "synpred61_SelectExpr"




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

    def synpred42_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred42_SelectExpr_fragment()
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

    def synpred26_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred26_SelectExpr_fragment()
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

    def synpred37_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred37_SelectExpr_fragment()
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
        u"\1\153\1\0\17\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\14\uffff\1\3\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\17\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\17\13\uffff\1\2\11\uffff\2\2\5\uffff\1\2\2\uffff"
        u"\1\2\7\uffff\1\1\20\uffff\1\2\25\uffff\1\2\1\uffff\4\2\2\uffff"
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
    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\35\2\0\15\uffff"
        )

    DFA31_max = DFA.unpack(
        u"\1\153\2\0\15\uffff"
        )

    DFA31_accept = DFA.unpack(
        u"\3\uffff\1\2\13\uffff\1\1"
        )

    DFA31_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\15\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\1\3\11\uffff\2\3\5\uffff\1\3\2\uffff\1\3\7\uffff\1"
        u"\3\20\uffff\1\2\25\uffff\1\3\1\uffff\4\3\2\uffff\1\1\2\uffff\1"
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

    # class definition for DFA #31

    class DFA31(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA31_1 = input.LA(1)

                 
                index31_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred37_SelectExpr()):
                    s = 15

                elif (True):
                    s = 3

                 
                input.seek(index31_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA31_2 = input.LA(1)

                 
                index31_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred37_SelectExpr()):
                    s = 15

                elif (True):
                    s = 3

                 
                input.seek(index31_2)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 31, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\1\47\2\uffff\13\0\2\uffff"
        )

    DFA52_max = DFA.unpack(
        u"\1\153\2\uffff\13\0\2\uffff"
        )

    DFA52_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\13\uffff\1\3\1\4"
        )

    DFA52_special = DFA.unpack(
        u"\3\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\2\uffff"
        )

            
    DFA52_transition = [
        DFA.unpack(u"\1\2\1\1\5\uffff\1\13\2\uffff\1\12\7\uffff\1\15\20\uffff"
        u"\1\11\25\uffff\1\3\1\uffff\1\5\1\4\1\6\1\7\2\uffff\1\10\2\uffff"
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

    # class definition for DFA #52

    class DFA52(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA52_3 = input.LA(1)

                 
                index52_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA52_4 = input.LA(1)

                 
                index52_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_4)
                if s >= 0:
                    return s
            elif s == 2: 
                LA52_5 = input.LA(1)

                 
                index52_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_5)
                if s >= 0:
                    return s
            elif s == 3: 
                LA52_6 = input.LA(1)

                 
                index52_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_6)
                if s >= 0:
                    return s
            elif s == 4: 
                LA52_7 = input.LA(1)

                 
                index52_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_7)
                if s >= 0:
                    return s
            elif s == 5: 
                LA52_8 = input.LA(1)

                 
                index52_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_8)
                if s >= 0:
                    return s
            elif s == 6: 
                LA52_9 = input.LA(1)

                 
                index52_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_9)
                if s >= 0:
                    return s
            elif s == 7: 
                LA52_10 = input.LA(1)

                 
                index52_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_10)
                if s >= 0:
                    return s
            elif s == 8: 
                LA52_11 = input.LA(1)

                 
                index52_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_11)
                if s >= 0:
                    return s
            elif s == 9: 
                LA52_12 = input.LA(1)

                 
                index52_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_12)
                if s >= 0:
                    return s
            elif s == 10: 
                LA52_13 = input.LA(1)

                 
                index52_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_SelectExpr()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index52_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 52, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_prog_in_eval1493 = frozenset([1])
    FOLLOW_statement_in_prog1503 = frozenset([1, 17, 29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_statement_select_in_statement1513 = frozenset([17])
    FOLLOW_END_in_statement1515 = frozenset([1])
    FOLLOW_expr_in_statement1521 = frozenset([17])
    FOLLOW_END_in_statement1523 = frozenset([1])
    FOLLOW_END_in_statement1529 = frozenset([1])
    FOLLOW_select__in_statement_select1540 = frozenset([59])
    FOLLOW_from__in_statement_select1542 = frozenset([1, 62, 63, 67, 73, 76, 77])
    FOLLOW_where__in_statement_select1545 = frozenset([1, 63, 67, 73, 76, 77])
    FOLLOW_start__in_statement_select1551 = frozenset([76, 77])
    FOLLOW_connect__in_statement_select1555 = frozenset([78])
    FOLLOW_stop__in_statement_select1557 = frozenset([1, 63, 67, 73])
    FOLLOW_group__in_statement_select1562 = frozenset([1, 63, 69, 73])
    FOLLOW_having__in_statement_select1565 = frozenset([1, 63, 73])
    FOLLOW_order__in_statement_select1572 = frozenset([1, 73])
    FOLLOW_as__in_statement_select1577 = frozenset([1])
    FOLLOW_SELECT_in_select_1637 = frozenset([41, 74, 104])
    FOLLOW_MUL_in_select_1641 = frozenset([1])
    FOLLOW_PHRASE_in_select_1648 = frozenset([1, 16])
    FOLLOW_function_in_select_1652 = frozenset([1, 16])
    FOLLOW_this__in_select_1656 = frozenset([1, 16])
    FOLLOW_SEP_in_select_1660 = frozenset([74, 104])
    FOLLOW_PHRASE_in_select_1664 = frozenset([1, 16])
    FOLLOW_function_in_select_1668 = frozenset([1, 16])
    FOLLOW_this__in_select_1672 = frozenset([1, 16])
    FOLLOW_FROM_in_from_1688 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_from_1691 = frozenset([1, 16])
    FOLLOW_SEP_in_from_1694 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_from_1697 = frozenset([1, 16])
    FOLLOW_WHERE_in_where_1708 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_where_1711 = frozenset([1])
    FOLLOW_START_in_start_1720 = frozenset([79])
    FOLLOW_WITH_in_start_1723 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_start_1726 = frozenset([1, 16])
    FOLLOW_SEP_in_start_1729 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_start_1732 = frozenset([1, 16])
    FOLLOW_CONNECT_in_connect_1743 = frozenset([72])
    FOLLOW_BY_in_connect_1746 = frozenset([29, 39, 40, 46, 49, 57, 74, 80, 83, 85, 86, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_NO_in_connect_1750 = frozenset([81])
    FOLLOW_CYCLE_in_connect_1753 = frozenset([29, 39, 40, 46, 49, 57, 74, 83, 85, 86, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_UNIQUE_in_connect_1758 = frozenset([29, 39, 40, 46, 49, 57, 74, 85, 86, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_MEMORIZE_in_connect_1763 = frozenset([98])
    FOLLOW_INTEGER_in_connect_1765 = frozenset([29, 39, 40, 46, 49, 57, 74, 86, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_MAXIMUM_in_connect_1770 = frozenset([98])
    FOLLOW_INTEGER_in_connect_1772 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_connect_1776 = frozenset([1, 16])
    FOLLOW_SEP_in_connect_1779 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_connect_1782 = frozenset([1, 16])
    FOLLOW_STOP_in_stop_1795 = frozenset([79])
    FOLLOW_WITH_in_stop_1798 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_stop_1801 = frozenset([1])
    FOLLOW_GROUP_in_group_1810 = frozenset([72])
    FOLLOW_BY_in_group_1813 = frozenset([104])
    FOLLOW_PHRASE_in_group_1818 = frozenset([1, 16])
    FOLLOW_function_in_group_1822 = frozenset([1, 16])
    FOLLOW_SEP_in_group_1827 = frozenset([104])
    FOLLOW_PHRASE_in_group_1832 = frozenset([1, 16])
    FOLLOW_function_in_group_1836 = frozenset([1, 16])
    FOLLOW_HAVING_in_having_1850 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_having_1853 = frozenset([1])
    FOLLOW_ORDER_in_order_1862 = frozenset([72])
    FOLLOW_BY_in_order_1865 = frozenset([104])
    FOLLOW_PHRASE_in_order_1870 = frozenset([16, 87, 88])
    FOLLOW_direction__in_order_1872 = frozenset([1, 16])
    FOLLOW_function_in_order_1876 = frozenset([16, 87, 88])
    FOLLOW_direction__in_order_1878 = frozenset([1, 16])
    FOLLOW_SEP_in_order_1883 = frozenset([104])
    FOLLOW_PHRASE_in_order_1888 = frozenset([16, 87, 88])
    FOLLOW_direction__in_order_1890 = frozenset([1, 16])
    FOLLOW_function_in_order_1894 = frozenset([16, 87, 88])
    FOLLOW_direction__in_order_1896 = frozenset([1, 16])
    FOLLOW_set_in_direction_1911 = frozenset([1])
    FOLLOW_AS_in_as_1927 = frozenset([89, 90, 91, 104])
    FOLLOW_AS_LIST_in_as_1932 = frozenset([1])
    FOLLOW_AS_VALUE_in_as_1936 = frozenset([1])
    FOLLOW_AS_DICT_in_as_1940 = frozenset([1])
    FOLLOW_PHRASE_in_as_1944 = frozenset([1, 107])
    FOLLOW_107_in_as_1947 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107, 108])
    FOLLOW_parameter_in_as_1950 = frozenset([108])
    FOLLOW_108_in_as_1953 = frozenset([1])
    FOLLOW_assign_expr_in_expr1967 = frozenset([1])
    FOLLOW_logic_expr_in_expr1973 = frozenset([1])
    FOLLOW_IF_in_if_statement1982 = frozenset([107])
    FOLLOW_107_in_if_statement1984 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_if_statement1986 = frozenset([17, 108])
    FOLLOW_END_in_if_statement1989 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_parameter_in_if_statement1991 = frozenset([17, 108])
    FOLLOW_END_in_if_statement1994 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_parameter_in_if_statement1996 = frozenset([108])
    FOLLOW_108_in_if_statement2002 = frozenset([1])
    FOLLOW_PHRASE_in_assign_expr2041 = frozenset([32, 51])
    FOLLOW_age_in_assign_expr2044 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2048 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_assign_expr2050 = frozenset([1])
    FOLLOW_this__in_assign_expr2069 = frozenset([32])
    FOLLOW_ASSIGN_in_assign_expr2071 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_assign_expr2073 = frozenset([1])
    FOLLOW_logic_or_in_logic_expr2092 = frozenset([1])
    FOLLOW_logic_xor_in_logic_or2101 = frozenset([1, 27])
    FOLLOW_OR_in_logic_or2104 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_xor_in_logic_or2108 = frozenset([1, 27])
    FOLLOW_logic_and_in_logic_xor2118 = frozenset([1, 26])
    FOLLOW_XOR_in_logic_xor2121 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_and_in_logic_xor2124 = frozenset([1, 26])
    FOLLOW_logic_not_in_logic_and2134 = frozenset([1, 22])
    FOLLOW_AND_in_logic_and2137 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_not_in_logic_and2140 = frozenset([1, 22])
    FOLLOW_NOT_in_logic_not2151 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_expr_in_logic_not2156 = frozenset([1])
    FOLLOW_compare_in_in_compare_expr2165 = frozenset([1])
    FOLLOW_compare_eq_in_compare_in2173 = frozenset([1, 31])
    FOLLOW_IN_in_compare_in2176 = frozenset([46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_atom_in_compare_in2179 = frozenset([1, 31])
    FOLLOW_compare_ne_in_compare_eq2189 = frozenset([1, 33])
    FOLLOW_EQ_in_compare_eq2192 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_ne_in_compare_eq2195 = frozenset([1, 33])
    FOLLOW_compare_ge_in_compare_ne2205 = frozenset([1, 34])
    FOLLOW_NE_in_compare_ne2208 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_ge_in_compare_ne2211 = frozenset([1, 34])
    FOLLOW_compare_gt_in_compare_ge2221 = frozenset([1, 36])
    FOLLOW_GE_in_compare_ge2224 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_gt_in_compare_ge2227 = frozenset([1, 36])
    FOLLOW_compare_le_in_compare_gt2237 = frozenset([1, 38])
    FOLLOW_GT_in_compare_gt2240 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_le_in_compare_gt2243 = frozenset([1, 38])
    FOLLOW_compare_lt_in_compare_le2253 = frozenset([1, 35])
    FOLLOW_LE_in_compare_le2256 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_lt_in_compare_le2259 = frozenset([1, 35])
    FOLLOW_arithmetic_expr_in_compare_lt2269 = frozenset([1, 37])
    FOLLOW_LT_in_compare_lt2272 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_expr_in_compare_lt2275 = frozenset([1, 37])
    FOLLOW_arithmetic_sub_add_in_arithmetic_expr2286 = frozenset([1])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2294 = frozenset([1, 39, 40])
    FOLLOW_SUB_in_arithmetic_sub_add2298 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_ADD_in_arithmetic_sub_add2301 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2305 = frozenset([1, 39, 40])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2315 = frozenset([1, 41, 42, 43])
    FOLLOW_MUL_in_arithmetic_mul_div_mod2319 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_DIV_in_arithmetic_mul_div_mod2324 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_MOD_in_arithmetic_mul_div_mod2329 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2333 = frozenset([1, 41, 42, 43])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2343 = frozenset([1, 44])
    FOLLOW_POW_in_arithmetic_pow2346 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2349 = frozenset([1, 44])
    FOLLOW_SUB_in_arithmetic_unary2360 = frozenset([46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_atom_in_arithmetic_unary2362 = frozenset([1])
    FOLLOW_ADD_in_arithmetic_unary2376 = frozenset([46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_atom_in_arithmetic_unary2378 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2392 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_arithmetic_unary2394 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_parameter_in_arithmetic_unary2396 = frozenset([50])
    FOLLOW_LIST_END_in_arithmetic_unary2398 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2414 = frozenset([1])
    FOLLOW_value_in_atom2425 = frozenset([1])
    FOLLOW_variable_in_atom2430 = frozenset([1])
    FOLLOW_if_statement_in_atom2435 = frozenset([1])
    FOLLOW_function_in_atom2440 = frozenset([1])
    FOLLOW_107_in_atom2445 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_atom2448 = frozenset([108])
    FOLLOW_108_in_atom2450 = frozenset([1])
    FOLLOW_statement_select_in_atom2456 = frozenset([1])
    FOLLOW_PHRASE_in_function2465 = frozenset([107])
    FOLLOW_107_in_function2467 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107, 108])
    FOLLOW_parameter_in_function2469 = frozenset([108])
    FOLLOW_108_in_function2472 = frozenset([1])
    FOLLOW_expr_in_parameter2492 = frozenset([1, 16])
    FOLLOW_SEP_in_parameter2495 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_parameter2498 = frozenset([1, 16])
    FOLLOW_PHRASE_in_variable2509 = frozenset([1, 51])
    FOLLOW_age_in_variable2512 = frozenset([1])
    FOLLOW_AGE_BEGIN_in_age2536 = frozenset([29, 39, 40, 46, 49, 52, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_age2538 = frozenset([52])
    FOLLOW_AGE_END_in_age2541 = frozenset([1])
    FOLLOW_STRING_in_value2559 = frozenset([1])
    FOLLOW_FLOAT_in_value2573 = frozenset([1])
    FOLLOW_INTEGER_in_value2587 = frozenset([1])
    FOLLOW_TRUE_in_value2600 = frozenset([1])
    FOLLOW_FALSE_in_value2614 = frozenset([1])
    FOLLOW_this__in_value2628 = frozenset([1])
    FOLLOW_list__in_value2633 = frozenset([1])
    FOLLOW_PHRASE_in_this_2644 = frozenset([15])
    FOLLOW_DOT_in_this_2646 = frozenset([74])
    FOLLOW_THIS_in_this_2650 = frozenset([1])
    FOLLOW_LIST_BEGIN_in_list_2671 = frozenset([16, 29, 39, 40, 46, 49, 50, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_list_2675 = frozenset([16, 50])
    FOLLOW_SEP_in_list_2679 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_list_2681 = frozenset([16, 50])
    FOLLOW_LIST_END_in_list_2687 = frozenset([1])
    FOLLOW_statement_select_in_synpred2_SelectExpr1513 = frozenset([17])
    FOLLOW_END_in_synpred2_SelectExpr1515 = frozenset([1])
    FOLLOW_expr_in_synpred3_SelectExpr1521 = frozenset([17])
    FOLLOW_END_in_synpred3_SelectExpr1523 = frozenset([1])
    FOLLOW_where__in_synpred4_SelectExpr1545 = frozenset([1])
    FOLLOW_start__in_synpred6_SelectExpr1551 = frozenset([76, 77])
    FOLLOW_connect__in_synpred6_SelectExpr1555 = frozenset([78])
    FOLLOW_stop__in_synpred6_SelectExpr1557 = frozenset([1])
    FOLLOW_group__in_synpred8_SelectExpr1562 = frozenset([1, 69])
    FOLLOW_having__in_synpred8_SelectExpr1565 = frozenset([1])
    FOLLOW_order__in_synpred9_SelectExpr1572 = frozenset([1])
    FOLLOW_as__in_synpred10_SelectExpr1577 = frozenset([1])
    FOLLOW_SEP_in_synpred17_SelectExpr1694 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_expr_in_synpred17_SelectExpr1697 = frozenset([1])
    FOLLOW_SEP_in_synpred26_SelectExpr1827 = frozenset([104])
    FOLLOW_PHRASE_in_synpred26_SelectExpr1832 = frozenset([1])
    FOLLOW_function_in_synpred26_SelectExpr1836 = frozenset([1])
    FOLLOW_SEP_in_synpred29_SelectExpr1883 = frozenset([104])
    FOLLOW_PHRASE_in_synpred29_SelectExpr1888 = frozenset([87, 88])
    FOLLOW_direction__in_synpred29_SelectExpr1890 = frozenset([1])
    FOLLOW_function_in_synpred29_SelectExpr1894 = frozenset([87, 88])
    FOLLOW_direction__in_synpred29_SelectExpr1896 = frozenset([1])
    FOLLOW_assign_expr_in_synpred37_SelectExpr1967 = frozenset([1])
    FOLLOW_OR_in_synpred42_SelectExpr2104 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_xor_in_synpred42_SelectExpr2108 = frozenset([1])
    FOLLOW_XOR_in_synpred43_SelectExpr2121 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_and_in_synpred43_SelectExpr2124 = frozenset([1])
    FOLLOW_AND_in_synpred44_SelectExpr2137 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_logic_not_in_synpred44_SelectExpr2140 = frozenset([1])
    FOLLOW_IN_in_synpred46_SelectExpr2176 = frozenset([46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_atom_in_synpred46_SelectExpr2179 = frozenset([1])
    FOLLOW_EQ_in_synpred47_SelectExpr2192 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_ne_in_synpred47_SelectExpr2195 = frozenset([1])
    FOLLOW_NE_in_synpred48_SelectExpr2208 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_ge_in_synpred48_SelectExpr2211 = frozenset([1])
    FOLLOW_GE_in_synpred49_SelectExpr2224 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_gt_in_synpred49_SelectExpr2227 = frozenset([1])
    FOLLOW_GT_in_synpred50_SelectExpr2240 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_le_in_synpred50_SelectExpr2243 = frozenset([1])
    FOLLOW_LE_in_synpred51_SelectExpr2256 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_compare_lt_in_synpred51_SelectExpr2259 = frozenset([1])
    FOLLOW_LT_in_synpred52_SelectExpr2272 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_expr_in_synpred52_SelectExpr2275 = frozenset([1])
    FOLLOW_set_in_synpred54_SelectExpr2297 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_mul_div_mod_in_synpred54_SelectExpr2305 = frozenset([1])
    FOLLOW_set_in_synpred57_SelectExpr2318 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_pow_in_synpred57_SelectExpr2333 = frozenset([1])
    FOLLOW_POW_in_synpred58_SelectExpr2346 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_arithmetic_unary_in_synpred58_SelectExpr2349 = frozenset([1])
    FOLLOW_atom_in_synpred61_SelectExpr2392 = frozenset([49])
    FOLLOW_LIST_BEGIN_in_synpred61_SelectExpr2394 = frozenset([29, 39, 40, 46, 49, 57, 74, 96, 98, 99, 100, 101, 104, 107])
    FOLLOW_parameter_in_synpred61_SelectExpr2396 = frozenset([50])
    FOLLOW_LIST_END_in_synpred61_SelectExpr2398 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SelectExprLexer", SelectExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
