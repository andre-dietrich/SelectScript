# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2014-11-19 16:00:41

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

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
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
    # SelectExpr.g:133:1: eval : prog ;
    def eval(self, ):

        retval = self.eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prog1 = None



        try:
            try:
                # SelectExpr.g:133:6: ( prog )
                # SelectExpr.g:133:8: prog
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_prog_in_eval1373)
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
    # SelectExpr.g:136:1: prog : ( statement )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None



        try:
            try:
                # SelectExpr.g:136:6: ( ( statement )+ )
                # SelectExpr.g:136:8: ( statement )+
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:136:8: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == END or LA1_0 == NOT or (ADD <= LA1_0 <= SUB) or LA1_0 == LIST_BEGIN or LA1_0 == SELECT or LA1_0 == THIS or LA1_0 == STRING or (INTEGER <= LA1_0 <= FALSE) or LA1_0 == PHRASE or LA1_0 == 98) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectExpr.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_prog1383)
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
    # SelectExpr.g:139:1: statement : ( statement_select END | expr END | END );
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
                # SelectExpr.g:139:11: ( statement_select END | expr END | END )
                alt2 = 3
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectExpr.g:139:13: statement_select END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_statement1393)
                    statement_select3 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select3.tree)
                    END4=self.match(self.input, END, self.FOLLOW_END_in_statement1395)


                elif alt2 == 2:
                    # SelectExpr.g:140:4: expr END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_statement1401)
                    expr5 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr5.tree)
                    END6=self.match(self.input, END, self.FOLLOW_END_in_statement1403)


                elif alt2 == 3:
                    # SelectExpr.g:141:4: END
                    pass 
                    root_0 = self._adaptor.nil()

                    END7=self.match(self.input, END, self.FOLLOW_END_in_statement1409)


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
    # SelectExpr.g:144:1: statement_select : select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) ;
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
                # SelectExpr.g:144:18: ( select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? ) )
                # SelectExpr.g:145:2: select_ from_ ( where_ )? ( ( start_ )? connect_ stop_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )?
                pass 
                self._state.following.append(self.FOLLOW_select__in_statement_select1420)
                select_8 = self.select_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_select_.add(select_8.tree)
                self._state.following.append(self.FOLLOW_from__in_statement_select1422)
                from_9 = self.from_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_from_.add(from_9.tree)
                # SelectExpr.g:145:16: ( where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    LA3_1 = self.input.LA(2)

                    if (self.synpred4_SelectExpr()) :
                        alt3 = 1
                if alt3 == 1:
                    # SelectExpr.g:145:17: where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select1425)
                    where_10 = self.where_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where_.add(where_10.tree)



                # SelectExpr.g:145:26: ( ( start_ )? connect_ stop_ )?
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
                    # SelectExpr.g:145:27: ( start_ )? connect_ stop_
                    pass 
                    # SelectExpr.g:145:27: ( start_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == START) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectExpr.g:145:28: start_
                        pass 
                        self._state.following.append(self.FOLLOW_start__in_statement_select1431)
                        start_11 = self.start_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_start_.add(start_11.tree)



                    self._state.following.append(self.FOLLOW_connect__in_statement_select1435)
                    connect_12 = self.connect_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_connect_.add(connect_12.tree)
                    self._state.following.append(self.FOLLOW_stop__in_statement_select1437)
                    stop_13 = self.stop_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_stop_.add(stop_13.tree)



                # SelectExpr.g:145:54: ( group_ ( having_ )? )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == GROUP) :
                    LA7_1 = self.input.LA(2)

                    if (self.synpred8_SelectExpr()) :
                        alt7 = 1
                if alt7 == 1:
                    # SelectExpr.g:145:55: group_ ( having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select1442)
                    group_14 = self.group_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_group_.add(group_14.tree)
                    # SelectExpr.g:145:62: ( having_ )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == HAVING) :
                        alt6 = 1
                    if alt6 == 1:
                        # SelectExpr.g:145:63: having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select1445)
                        having_15 = self.having_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_having_.add(having_15.tree)






                # SelectExpr.g:145:75: ( order_ )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ORDER) :
                    LA8_1 = self.input.LA(2)

                    if (self.synpred9_SelectExpr()) :
                        alt8 = 1
                if alt8 == 1:
                    # SelectExpr.g:145:76: order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select1452)
                    order_16 = self.order_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_order_.add(order_16.tree)



                # SelectExpr.g:145:85: ( as_ )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == AS) :
                    LA9_1 = self.input.LA(2)

                    if (self.synpred10_SelectExpr()) :
                        alt9 = 1
                if alt9 == 1:
                    # SelectExpr.g:145:86: as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select1457)
                    as_17 = self.as_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_as_.add(as_17.tree)




                # AST Rewrite
                # elements: select_, group_, from_, connect_, as_, start_, where_, having_, stop_, order_
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
                    # 145:92: -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    # SelectExpr.g:145:96: ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ( ( start_ )? connect_ stop_ )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STMT_SELECT, "STMT_SELECT"), root_1)

                    self._adaptor.addChild(root_1, stream_select_.nextTree())
                    self._adaptor.addChild(root_1, stream_from_.nextTree())
                    # SelectExpr.g:145:124: ( where_ )?
                    if stream_where_.hasNext():
                        self._adaptor.addChild(root_1, stream_where_.nextTree())


                    stream_where_.reset();
                    # SelectExpr.g:145:134: ( group_ ( having_ )? )?
                    if stream_group_.hasNext() or stream_having_.hasNext():
                        self._adaptor.addChild(root_1, stream_group_.nextTree())
                        # SelectExpr.g:145:142: ( having_ )?
                        if stream_having_.hasNext():
                            self._adaptor.addChild(root_1, stream_having_.nextTree())


                        stream_having_.reset();


                    stream_group_.reset();
                    stream_having_.reset();
                    # SelectExpr.g:145:155: ( order_ )?
                    if stream_order_.hasNext():
                        self._adaptor.addChild(root_1, stream_order_.nextTree())


                    stream_order_.reset();
                    # SelectExpr.g:145:165: ( as_ )?
                    if stream_as_.hasNext():
                        self._adaptor.addChild(root_1, stream_as_.nextTree())


                    stream_as_.reset();
                    # SelectExpr.g:145:172: ( ( start_ )? connect_ stop_ )?
                    if stream_connect_.hasNext() or stream_start_.hasNext() or stream_stop_.hasNext():
                        # SelectExpr.g:145:173: ( start_ )?
                        if stream_start_.hasNext():
                            self._adaptor.addChild(root_1, stream_start_.nextTree())


                        stream_start_.reset();
                        self._adaptor.addChild(root_1, stream_connect_.nextTree())
                        self._adaptor.addChild(root_1, stream_stop_.nextTree())


                    stream_connect_.reset();
                    stream_start_.reset();
                    stream_stop_.reset();

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
    # SelectExpr.g:148:1: select_ : SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) ;
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
                # SelectExpr.g:148:9: ( SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) )
                # SelectExpr.g:148:11: SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                pass 
                root_0 = self._adaptor.nil()

                SELECT18=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_1517)
                if self._state.backtracking == 0:

                    SELECT18_tree = self._adaptor.createWithPayload(SELECT18)
                    root_0 = self._adaptor.becomeRoot(SELECT18_tree, root_0)

                # SelectExpr.g:148:19: ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
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
                    # SelectExpr.g:148:20: MUL
                    pass 
                    MUL19=self.match(self.input, MUL, self.FOLLOW_MUL_in_select_1521)


                elif alt13 == 2:
                    # SelectExpr.g:148:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    pass 
                    # SelectExpr.g:148:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    # SelectExpr.g:148:28: ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )*
                    pass 
                    # SelectExpr.g:148:28: ( PHRASE | function | this_ )
                    alt10 = 3
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == PHRASE) :
                        LA10 = self.input.LA(2)
                        if LA10 == 98:
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
                        # SelectExpr.g:148:29: PHRASE
                        pass 
                        PHRASE20=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1528)
                        if self._state.backtracking == 0:

                            PHRASE20_tree = self._adaptor.createWithPayload(PHRASE20)
                            self._adaptor.addChild(root_0, PHRASE20_tree)



                    elif alt10 == 2:
                        # SelectExpr.g:148:38: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_select_1532)
                        function21 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, function21.tree)


                    elif alt10 == 3:
                        # SelectExpr.g:148:49: this_
                        pass 
                        self._state.following.append(self.FOLLOW_this__in_select_1536)
                        this_22 = self.this_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, this_22.tree)



                    # SelectExpr.g:148:56: ( SEP ( PHRASE | function | this_ ) )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == SEP) :
                            alt12 = 1


                        if alt12 == 1:
                            # SelectExpr.g:148:57: SEP ( PHRASE | function | this_ )
                            pass 
                            SEP23=self.match(self.input, SEP, self.FOLLOW_SEP_in_select_1540)
                            # SelectExpr.g:148:62: ( PHRASE | function | this_ )
                            alt11 = 3
                            LA11_0 = self.input.LA(1)

                            if (LA11_0 == PHRASE) :
                                LA11 = self.input.LA(2)
                                if LA11 == 98:
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
                                # SelectExpr.g:148:63: PHRASE
                                pass 
                                PHRASE24=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1544)
                                if self._state.backtracking == 0:

                                    PHRASE24_tree = self._adaptor.createWithPayload(PHRASE24)
                                    self._adaptor.addChild(root_0, PHRASE24_tree)



                            elif alt11 == 2:
                                # SelectExpr.g:148:72: function
                                pass 
                                self._state.following.append(self.FOLLOW_function_in_select_1548)
                                function25 = self.function()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, function25.tree)


                            elif alt11 == 3:
                                # SelectExpr.g:148:83: this_
                                pass 
                                self._state.following.append(self.FOLLOW_this__in_select_1552)
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
    # SelectExpr.g:151:1: from_ : FROM expr ( SEP expr )* ;
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
                # SelectExpr.g:151:7: ( FROM expr ( SEP expr )* )
                # SelectExpr.g:151:9: FROM expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                FROM27=self.match(self.input, FROM, self.FOLLOW_FROM_in_from_1568)
                if self._state.backtracking == 0:

                    FROM27_tree = self._adaptor.createWithPayload(FROM27)
                    root_0 = self._adaptor.becomeRoot(FROM27_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_from_1571)
                expr28 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr28.tree)
                # SelectExpr.g:151:20: ( SEP expr )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == SEP) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred17_SelectExpr()) :
                            alt14 = 1




                    if alt14 == 1:
                        # SelectExpr.g:151:21: SEP expr
                        pass 
                        SEP29=self.match(self.input, SEP, self.FOLLOW_SEP_in_from_1574)
                        self._state.following.append(self.FOLLOW_expr_in_from_1577)
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
    # SelectExpr.g:154:1: where_ : WHERE expr ;
    def where_(self, ):

        retval = self.where__return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHERE31 = None
        expr32 = None


        WHERE31_tree = None

        try:
            try:
                # SelectExpr.g:154:8: ( WHERE expr )
                # SelectExpr.g:154:10: WHERE expr
                pass 
                root_0 = self._adaptor.nil()

                WHERE31=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_1588)
                if self._state.backtracking == 0:

                    WHERE31_tree = self._adaptor.createWithPayload(WHERE31)
                    root_0 = self._adaptor.becomeRoot(WHERE31_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_where_1591)
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
    # SelectExpr.g:157:1: start_ : START WITH expr ( SEP expr )* ;
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
                # SelectExpr.g:157:8: ( START WITH expr ( SEP expr )* )
                # SelectExpr.g:157:10: START WITH expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                START33=self.match(self.input, START, self.FOLLOW_START_in_start_1600)
                if self._state.backtracking == 0:

                    START33_tree = self._adaptor.createWithPayload(START33)
                    root_0 = self._adaptor.becomeRoot(START33_tree, root_0)

                WITH34=self.match(self.input, WITH, self.FOLLOW_WITH_in_start_1603)
                self._state.following.append(self.FOLLOW_expr_in_start_1606)
                expr35 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr35.tree)
                # SelectExpr.g:157:28: ( SEP expr )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SEP) :
                        alt15 = 1


                    if alt15 == 1:
                        # SelectExpr.g:157:29: SEP expr
                        pass 
                        SEP36=self.match(self.input, SEP, self.FOLLOW_SEP_in_start_1609)
                        self._state.following.append(self.FOLLOW_expr_in_start_1612)
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
    # SelectExpr.g:160:1: connect_ : CONNECT BY expr ( SEP expr )* ;
    def connect_(self, ):

        retval = self.connect__return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONNECT38 = None
        BY39 = None
        SEP41 = None
        expr40 = None

        expr42 = None


        CONNECT38_tree = None
        BY39_tree = None
        SEP41_tree = None

        try:
            try:
                # SelectExpr.g:160:10: ( CONNECT BY expr ( SEP expr )* )
                # SelectExpr.g:160:12: CONNECT BY expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                CONNECT38=self.match(self.input, CONNECT, self.FOLLOW_CONNECT_in_connect_1623)
                if self._state.backtracking == 0:

                    CONNECT38_tree = self._adaptor.createWithPayload(CONNECT38)
                    root_0 = self._adaptor.becomeRoot(CONNECT38_tree, root_0)

                BY39=self.match(self.input, BY, self.FOLLOW_BY_in_connect_1626)
                self._state.following.append(self.FOLLOW_expr_in_connect_1629)
                expr40 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr40.tree)
                # SelectExpr.g:160:30: ( SEP expr )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == SEP) :
                        alt16 = 1


                    if alt16 == 1:
                        # SelectExpr.g:160:31: SEP expr
                        pass 
                        SEP41=self.match(self.input, SEP, self.FOLLOW_SEP_in_connect_1632)
                        self._state.following.append(self.FOLLOW_expr_in_connect_1635)
                        expr42 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr42.tree)


                    else:
                        break #loop16



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
    # SelectExpr.g:163:1: stop_ : STOP WITH expr ;
    def stop_(self, ):

        retval = self.stop__return()
        retval.start = self.input.LT(1)

        root_0 = None

        STOP43 = None
        WITH44 = None
        expr45 = None


        STOP43_tree = None
        WITH44_tree = None

        try:
            try:
                # SelectExpr.g:163:7: ( STOP WITH expr )
                # SelectExpr.g:163:9: STOP WITH expr
                pass 
                root_0 = self._adaptor.nil()

                STOP43=self.match(self.input, STOP, self.FOLLOW_STOP_in_stop_1646)
                if self._state.backtracking == 0:

                    STOP43_tree = self._adaptor.createWithPayload(STOP43)
                    root_0 = self._adaptor.becomeRoot(STOP43_tree, root_0)

                WITH44=self.match(self.input, WITH, self.FOLLOW_WITH_in_stop_1649)
                self._state.following.append(self.FOLLOW_expr_in_stop_1652)
                expr45 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr45.tree)



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
    # SelectExpr.g:166:1: group_ : GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* ;
    def group_(self, ):

        retval = self.group__return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP46 = None
        BY47 = None
        PHRASE48 = None
        SEP50 = None
        PHRASE51 = None
        function49 = None

        function52 = None


        GROUP46_tree = None
        BY47_tree = None
        PHRASE48_tree = None
        SEP50_tree = None
        PHRASE51_tree = None

        try:
            try:
                # SelectExpr.g:166:8: ( GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* )
                # SelectExpr.g:166:10: GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )*
                pass 
                root_0 = self._adaptor.nil()

                GROUP46=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_1661)
                if self._state.backtracking == 0:

                    GROUP46_tree = self._adaptor.createWithPayload(GROUP46)
                    root_0 = self._adaptor.becomeRoot(GROUP46_tree, root_0)

                BY47=self.match(self.input, BY, self.FOLLOW_BY_in_group_1664)
                # SelectExpr.g:166:21: ( PHRASE | function )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == PHRASE) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == 98) :
                        alt17 = 2
                    elif (LA17_1 == EOF or (SEP <= LA17_1 <= END) or LA17_1 == AND or (XOR <= LA17_1 <= OR) or LA17_1 == IN or (EQ <= LA17_1 <= POW) or LA17_1 == LIST_END or LA17_1 == AGE_END or (WHERE <= LA17_1 <= ORDER) or LA17_1 == GROUP or LA17_1 == HAVING or LA17_1 == AS or (CONNECT <= LA17_1 <= STOP) or LA17_1 == 99) :
                        alt17 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # SelectExpr.g:166:23: PHRASE
                    pass 
                    PHRASE48=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1669)
                    if self._state.backtracking == 0:

                        PHRASE48_tree = self._adaptor.createWithPayload(PHRASE48)
                        self._adaptor.addChild(root_0, PHRASE48_tree)



                elif alt17 == 2:
                    # SelectExpr.g:166:32: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_group_1673)
                    function49 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function49.tree)



                # SelectExpr.g:166:43: ( SEP ( PHRASE | function ) )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == SEP) :
                        LA19_2 = self.input.LA(2)

                        if (LA19_2 == PHRASE) :
                            LA19_3 = self.input.LA(3)

                            if (self.synpred22_SelectExpr()) :
                                alt19 = 1






                    if alt19 == 1:
                        # SelectExpr.g:166:44: SEP ( PHRASE | function )
                        pass 
                        SEP50=self.match(self.input, SEP, self.FOLLOW_SEP_in_group_1678)
                        # SelectExpr.g:166:49: ( PHRASE | function )
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == PHRASE) :
                            LA18_1 = self.input.LA(2)

                            if (LA18_1 == 98) :
                                alt18 = 2
                            elif (LA18_1 == EOF or (SEP <= LA18_1 <= END) or LA18_1 == AND or (XOR <= LA18_1 <= OR) or LA18_1 == IN or (EQ <= LA18_1 <= POW) or LA18_1 == LIST_END or LA18_1 == AGE_END or (WHERE <= LA18_1 <= ORDER) or LA18_1 == GROUP or LA18_1 == HAVING or LA18_1 == AS or (CONNECT <= LA18_1 <= STOP) or LA18_1 == 99) :
                                alt18 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 18, 1, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 18, 0, self.input)

                            raise nvae

                        if alt18 == 1:
                            # SelectExpr.g:166:51: PHRASE
                            pass 
                            PHRASE51=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1683)
                            if self._state.backtracking == 0:

                                PHRASE51_tree = self._adaptor.createWithPayload(PHRASE51)
                                self._adaptor.addChild(root_0, PHRASE51_tree)



                        elif alt18 == 2:
                            # SelectExpr.g:166:60: function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_group_1687)
                            function52 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function52.tree)





                    else:
                        break #loop19



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
    # SelectExpr.g:169:1: having_ : HAVING expr ;
    def having_(self, ):

        retval = self.having__return()
        retval.start = self.input.LT(1)

        root_0 = None

        HAVING53 = None
        expr54 = None


        HAVING53_tree = None

        try:
            try:
                # SelectExpr.g:169:9: ( HAVING expr )
                # SelectExpr.g:169:11: HAVING expr
                pass 
                root_0 = self._adaptor.nil()

                HAVING53=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_1701)
                if self._state.backtracking == 0:

                    HAVING53_tree = self._adaptor.createWithPayload(HAVING53)
                    root_0 = self._adaptor.becomeRoot(HAVING53_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_having_1704)
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

    # $ANTLR end "having_"

    class order__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.order__return, self).__init__()

            self.tree = None




    # $ANTLR start "order_"
    # SelectExpr.g:172:1: order_ : ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* ;
    def order_(self, ):

        retval = self.order__return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER55 = None
        BY56 = None
        PHRASE57 = None
        SEP61 = None
        PHRASE62 = None
        direction_58 = None

        function59 = None

        direction_60 = None

        direction_63 = None

        function64 = None

        direction_65 = None


        ORDER55_tree = None
        BY56_tree = None
        PHRASE57_tree = None
        SEP61_tree = None
        PHRASE62_tree = None

        try:
            try:
                # SelectExpr.g:172:8: ( ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* )
                # SelectExpr.g:172:10: ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )*
                pass 
                root_0 = self._adaptor.nil()

                ORDER55=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_1713)
                if self._state.backtracking == 0:

                    ORDER55_tree = self._adaptor.createWithPayload(ORDER55)
                    root_0 = self._adaptor.becomeRoot(ORDER55_tree, root_0)

                BY56=self.match(self.input, BY, self.FOLLOW_BY_in_order_1716)
                # SelectExpr.g:172:21: ( PHRASE direction_ | function direction_ )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == PHRASE) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 98) :
                        alt20 = 2
                    elif (LA20_1 == EOF or (SEP <= LA20_1 <= END) or LA20_1 == AND or (XOR <= LA20_1 <= OR) or LA20_1 == IN or (EQ <= LA20_1 <= POW) or LA20_1 == LIST_END or LA20_1 == AGE_END or (WHERE <= LA20_1 <= ORDER) or LA20_1 == GROUP or LA20_1 == AS or (CONNECT <= LA20_1 <= STOP) or (ASC <= LA20_1 <= DESC) or LA20_1 == 99) :
                        alt20 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # SelectExpr.g:172:23: PHRASE direction_
                    pass 
                    PHRASE57=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1721)
                    if self._state.backtracking == 0:

                        PHRASE57_tree = self._adaptor.createWithPayload(PHRASE57)
                        self._adaptor.addChild(root_0, PHRASE57_tree)

                    self._state.following.append(self.FOLLOW_direction__in_order_1723)
                    direction_58 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_58.tree)


                elif alt20 == 2:
                    # SelectExpr.g:172:43: function direction_
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_order_1727)
                    function59 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function59.tree)
                    self._state.following.append(self.FOLLOW_direction__in_order_1729)
                    direction_60 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_60.tree)



                # SelectExpr.g:172:65: ( SEP ( PHRASE direction_ | function direction_ ) )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == SEP) :
                        LA22_2 = self.input.LA(2)

                        if (LA22_2 == PHRASE) :
                            LA22_3 = self.input.LA(3)

                            if (self.synpred25_SelectExpr()) :
                                alt22 = 1






                    if alt22 == 1:
                        # SelectExpr.g:172:66: SEP ( PHRASE direction_ | function direction_ )
                        pass 
                        SEP61=self.match(self.input, SEP, self.FOLLOW_SEP_in_order_1734)
                        # SelectExpr.g:172:71: ( PHRASE direction_ | function direction_ )
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == PHRASE) :
                            LA21_1 = self.input.LA(2)

                            if (LA21_1 == 98) :
                                alt21 = 2
                            elif (LA21_1 == EOF or (SEP <= LA21_1 <= END) or LA21_1 == AND or (XOR <= LA21_1 <= OR) or LA21_1 == IN or (EQ <= LA21_1 <= POW) or LA21_1 == LIST_END or LA21_1 == AGE_END or (WHERE <= LA21_1 <= ORDER) or LA21_1 == GROUP or LA21_1 == AS or (CONNECT <= LA21_1 <= STOP) or (ASC <= LA21_1 <= DESC) or LA21_1 == 99) :
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
                            # SelectExpr.g:172:73: PHRASE direction_
                            pass 
                            PHRASE62=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1739)
                            if self._state.backtracking == 0:

                                PHRASE62_tree = self._adaptor.createWithPayload(PHRASE62)
                                self._adaptor.addChild(root_0, PHRASE62_tree)

                            self._state.following.append(self.FOLLOW_direction__in_order_1741)
                            direction_63 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_63.tree)


                        elif alt21 == 2:
                            # SelectExpr.g:172:93: function direction_
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_order_1745)
                            function64 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function64.tree)
                            self._state.following.append(self.FOLLOW_direction__in_order_1747)
                            direction_65 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_65.tree)





                    else:
                        break #loop22



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
    # SelectExpr.g:175:1: direction_ : ( ASC | DESC )? ;
    def direction_(self, ):

        retval = self.direction__return()
        retval.start = self.input.LT(1)

        root_0 = None

        set66 = None

        set66_tree = None

        try:
            try:
                # SelectExpr.g:175:12: ( ( ASC | DESC )? )
                # SelectExpr.g:175:14: ( ASC | DESC )?
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:175:14: ( ASC | DESC )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((ASC <= LA23_0 <= DESC)) :
                    alt23 = 1
                if alt23 == 1:
                    # SelectExpr.g:
                    pass 
                    set66 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set66))
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
    # SelectExpr.g:178:1: as_ : AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) ;
    def as_(self, ):

        retval = self.as__return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS67 = None
        AS_LIST68 = None
        AS_VALUE69 = None
        AS_DICT70 = None
        PHRASE71 = None
        char_literal72 = None
        char_literal74 = None
        parameter73 = None


        AS67_tree = None
        AS_LIST68_tree = None
        AS_VALUE69_tree = None
        AS_DICT70_tree = None
        PHRASE71_tree = None
        char_literal72_tree = None
        char_literal74_tree = None

        try:
            try:
                # SelectExpr.g:178:5: ( AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) )
                # SelectExpr.g:178:7: AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                pass 
                root_0 = self._adaptor.nil()

                AS67=self.match(self.input, AS, self.FOLLOW_AS_in_as_1778)
                if self._state.backtracking == 0:

                    AS67_tree = self._adaptor.createWithPayload(AS67)
                    root_0 = self._adaptor.becomeRoot(AS67_tree, root_0)

                # SelectExpr.g:178:11: ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                alt26 = 4
                LA26 = self.input.LA(1)
                if LA26 == AS_LIST:
                    alt26 = 1
                elif LA26 == AS_VALUE:
                    alt26 = 2
                elif LA26 == AS_DICT:
                    alt26 = 3
                elif LA26 == PHRASE:
                    alt26 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # SelectExpr.g:178:13: AS_LIST
                    pass 
                    AS_LIST68=self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_1783)
                    if self._state.backtracking == 0:

                        AS_LIST68_tree = self._adaptor.createWithPayload(AS_LIST68)
                        self._adaptor.addChild(root_0, AS_LIST68_tree)



                elif alt26 == 2:
                    # SelectExpr.g:178:23: AS_VALUE
                    pass 
                    AS_VALUE69=self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_1787)
                    if self._state.backtracking == 0:

                        AS_VALUE69_tree = self._adaptor.createWithPayload(AS_VALUE69)
                        self._adaptor.addChild(root_0, AS_VALUE69_tree)



                elif alt26 == 3:
                    # SelectExpr.g:178:34: AS_DICT
                    pass 
                    AS_DICT70=self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_1791)
                    if self._state.backtracking == 0:

                        AS_DICT70_tree = self._adaptor.createWithPayload(AS_DICT70)
                        self._adaptor.addChild(root_0, AS_DICT70_tree)



                elif alt26 == 4:
                    # SelectExpr.g:178:44: PHRASE ( '(' ( parameter )? ')' )?
                    pass 
                    PHRASE71=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_1795)
                    if self._state.backtracking == 0:

                        PHRASE71_tree = self._adaptor.createWithPayload(PHRASE71)
                        self._adaptor.addChild(root_0, PHRASE71_tree)

                    # SelectExpr.g:178:51: ( '(' ( parameter )? ')' )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == 98) :
                        alt25 = 1
                    if alt25 == 1:
                        # SelectExpr.g:178:52: '(' ( parameter )? ')'
                        pass 
                        char_literal72=self.match(self.input, 98, self.FOLLOW_98_in_as_1798)
                        # SelectExpr.g:178:57: ( parameter )?
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == NOT or (ADD <= LA24_0 <= SUB) or LA24_0 == LIST_BEGIN or LA24_0 == SELECT or LA24_0 == THIS or LA24_0 == STRING or (INTEGER <= LA24_0 <= FALSE) or LA24_0 == PHRASE or LA24_0 == 98) :
                            alt24 = 1
                        if alt24 == 1:
                            # SelectExpr.g:0:0: parameter
                            pass 
                            self._state.following.append(self.FOLLOW_parameter_in_as_1801)
                            parameter73 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter73.tree)



                        char_literal74=self.match(self.input, 99, self.FOLLOW_99_in_as_1804)









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
    # SelectExpr.g:181:1: expr : ( assign_expr | logic_expr );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_expr75 = None

        logic_expr76 = None



        try:
            try:
                # SelectExpr.g:181:6: ( assign_expr | logic_expr )
                alt27 = 2
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # SelectExpr.g:181:8: assign_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assign_expr_in_expr1818)
                    assign_expr75 = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assign_expr75.tree)


                elif alt27 == 2:
                    # SelectExpr.g:182:4: logic_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_logic_expr_in_expr1824)
                    logic_expr76 = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logic_expr76.tree)


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

    class assign_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.assign_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "assign_expr"
    # SelectExpr.g:185:1: assign_expr : PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) ;
    def assign_expr(self, ):

        retval = self.assign_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE77 = None
        ASSIGN79 = None
        age78 = None

        expr80 = None


        PHRASE77_tree = None
        ASSIGN79_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:185:13: ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) )
                # SelectExpr.g:185:15: PHRASE ( age )? ASSIGN expr
                pass 
                PHRASE77=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr1833) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE77)
                # SelectExpr.g:185:22: ( age )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == AGE_BEGIN) :
                    alt28 = 1
                if alt28 == 1:
                    # SelectExpr.g:185:23: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr1836)
                    age78 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age78.tree)



                ASSIGN79=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr1840) 
                if self._state.backtracking == 0:
                    stream_ASSIGN.add(ASSIGN79)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr1842)
                expr80 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr80.tree)

                # AST Rewrite
                # elements: age, expr, PHRASE, ASSIGN
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
                    # 185:41: -> ^( ASSIGN PHRASE expr ( age )? )
                    # SelectExpr.g:185:44: ^( ASSIGN PHRASE expr ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # SelectExpr.g:185:65: ( age )?
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

    # $ANTLR end "assign_expr"

    class logic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_expr"
    # SelectExpr.g:187:1: logic_expr : logic_or ;
    def logic_expr(self, ):

        retval = self.logic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        logic_or81 = None



        try:
            try:
                # SelectExpr.g:187:12: ( logic_or )
                # SelectExpr.g:187:14: logic_or
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_or_in_logic_expr1865)
                logic_or81 = self.logic_or()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_or81.tree)



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
    # SelectExpr.g:188:1: logic_or : logic_xor ( OR logic_xor )* ;
    def logic_or(self, ):

        retval = self.logic_or_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR83 = None
        logic_xor82 = None

        logic_xor84 = None


        OR83_tree = None

        try:
            try:
                # SelectExpr.g:188:11: ( logic_xor ( OR logic_xor )* )
                # SelectExpr.g:188:13: logic_xor ( OR logic_xor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_xor_in_logic_or1874)
                logic_xor82 = self.logic_xor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_xor82.tree)
                # SelectExpr.g:188:23: ( OR logic_xor )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == OR) :
                        LA29_2 = self.input.LA(2)

                        if (self.synpred35_SelectExpr()) :
                            alt29 = 1




                    if alt29 == 1:
                        # SelectExpr.g:188:24: OR logic_xor
                        pass 
                        OR83=self.match(self.input, OR, self.FOLLOW_OR_in_logic_or1877)
                        if self._state.backtracking == 0:

                            OR83_tree = self._adaptor.createWithPayload(OR83)
                            root_0 = self._adaptor.becomeRoot(OR83_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_xor_in_logic_or1881)
                        logic_xor84 = self.logic_xor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_xor84.tree)


                    else:
                        break #loop29



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
    # SelectExpr.g:189:1: logic_xor : logic_and ( XOR logic_and )* ;
    def logic_xor(self, ):

        retval = self.logic_xor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        XOR86 = None
        logic_and85 = None

        logic_and87 = None


        XOR86_tree = None

        try:
            try:
                # SelectExpr.g:189:11: ( logic_and ( XOR logic_and )* )
                # SelectExpr.g:189:13: logic_and ( XOR logic_and )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_and_in_logic_xor1891)
                logic_and85 = self.logic_and()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_and85.tree)
                # SelectExpr.g:189:23: ( XOR logic_and )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == XOR) :
                        LA30_2 = self.input.LA(2)

                        if (self.synpred36_SelectExpr()) :
                            alt30 = 1




                    if alt30 == 1:
                        # SelectExpr.g:189:24: XOR logic_and
                        pass 
                        XOR86=self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_xor1894)
                        if self._state.backtracking == 0:

                            XOR86_tree = self._adaptor.createWithPayload(XOR86)
                            root_0 = self._adaptor.becomeRoot(XOR86_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_and_in_logic_xor1897)
                        logic_and87 = self.logic_and()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_and87.tree)


                    else:
                        break #loop30



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
    # SelectExpr.g:190:1: logic_and : logic_not ( AND logic_not )* ;
    def logic_and(self, ):

        retval = self.logic_and_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND89 = None
        logic_not88 = None

        logic_not90 = None


        AND89_tree = None

        try:
            try:
                # SelectExpr.g:190:11: ( logic_not ( AND logic_not )* )
                # SelectExpr.g:190:13: logic_not ( AND logic_not )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_not_in_logic_and1907)
                logic_not88 = self.logic_not()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_not88.tree)
                # SelectExpr.g:190:23: ( AND logic_not )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == AND) :
                        LA31_2 = self.input.LA(2)

                        if (self.synpred37_SelectExpr()) :
                            alt31 = 1




                    if alt31 == 1:
                        # SelectExpr.g:190:24: AND logic_not
                        pass 
                        AND89=self.match(self.input, AND, self.FOLLOW_AND_in_logic_and1910)
                        if self._state.backtracking == 0:

                            AND89_tree = self._adaptor.createWithPayload(AND89)
                            root_0 = self._adaptor.becomeRoot(AND89_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_not_in_logic_and1913)
                        logic_not90 = self.logic_not()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_not90.tree)


                    else:
                        break #loop31



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
    # SelectExpr.g:191:1: logic_not : ( NOT )? compare_expr ;
    def logic_not(self, ):

        retval = self.logic_not_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT91 = None
        compare_expr92 = None


        NOT91_tree = None

        try:
            try:
                # SelectExpr.g:191:11: ( ( NOT )? compare_expr )
                # SelectExpr.g:191:13: ( NOT )? compare_expr
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:191:13: ( NOT )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == NOT) :
                    alt32 = 1
                if alt32 == 1:
                    # SelectExpr.g:191:14: NOT
                    pass 
                    NOT91=self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_not1924)
                    if self._state.backtracking == 0:

                        NOT91_tree = self._adaptor.createWithPayload(NOT91)
                        root_0 = self._adaptor.becomeRoot(NOT91_tree, root_0)




                self._state.following.append(self.FOLLOW_compare_expr_in_logic_not1929)
                compare_expr92 = self.compare_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_expr92.tree)



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
    # SelectExpr.g:193:1: compare_expr : compare_in ;
    def compare_expr(self, ):

        retval = self.compare_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        compare_in93 = None



        try:
            try:
                # SelectExpr.g:193:14: ( compare_in )
                # SelectExpr.g:193:16: compare_in
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_in_in_compare_expr1938)
                compare_in93 = self.compare_in()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_in93.tree)



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
    # SelectExpr.g:194:1: compare_in : compare_eq ( IN atom )* ;
    def compare_in(self, ):

        retval = self.compare_in_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IN95 = None
        compare_eq94 = None

        atom96 = None


        IN95_tree = None

        try:
            try:
                # SelectExpr.g:194:12: ( compare_eq ( IN atom )* )
                # SelectExpr.g:194:14: compare_eq ( IN atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_eq_in_compare_in1946)
                compare_eq94 = self.compare_eq()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_eq94.tree)
                # SelectExpr.g:194:25: ( IN atom )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == IN) :
                        LA33_2 = self.input.LA(2)

                        if (self.synpred39_SelectExpr()) :
                            alt33 = 1




                    if alt33 == 1:
                        # SelectExpr.g:194:26: IN atom
                        pass 
                        IN95=self.match(self.input, IN, self.FOLLOW_IN_in_compare_in1949)
                        if self._state.backtracking == 0:

                            IN95_tree = self._adaptor.createWithPayload(IN95)
                            root_0 = self._adaptor.becomeRoot(IN95_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_compare_in1952)
                        atom96 = self.atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, atom96.tree)


                    else:
                        break #loop33



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
    # SelectExpr.g:195:1: compare_eq : compare_ne ( EQ compare_ne )* ;
    def compare_eq(self, ):

        retval = self.compare_eq_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQ98 = None
        compare_ne97 = None

        compare_ne99 = None


        EQ98_tree = None

        try:
            try:
                # SelectExpr.g:195:12: ( compare_ne ( EQ compare_ne )* )
                # SelectExpr.g:195:14: compare_ne ( EQ compare_ne )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq1962)
                compare_ne97 = self.compare_ne()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ne97.tree)
                # SelectExpr.g:195:25: ( EQ compare_ne )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == EQ) :
                        LA34_2 = self.input.LA(2)

                        if (self.synpred40_SelectExpr()) :
                            alt34 = 1




                    if alt34 == 1:
                        # SelectExpr.g:195:26: EQ compare_ne
                        pass 
                        EQ98=self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_eq1965)
                        if self._state.backtracking == 0:

                            EQ98_tree = self._adaptor.createWithPayload(EQ98)
                            root_0 = self._adaptor.becomeRoot(EQ98_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq1968)
                        compare_ne99 = self.compare_ne()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ne99.tree)


                    else:
                        break #loop34



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
    # SelectExpr.g:196:1: compare_ne : compare_ge ( NE compare_ge )* ;
    def compare_ne(self, ):

        retval = self.compare_ne_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NE101 = None
        compare_ge100 = None

        compare_ge102 = None


        NE101_tree = None

        try:
            try:
                # SelectExpr.g:196:12: ( compare_ge ( NE compare_ge )* )
                # SelectExpr.g:196:14: compare_ge ( NE compare_ge )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne1978)
                compare_ge100 = self.compare_ge()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ge100.tree)
                # SelectExpr.g:196:25: ( NE compare_ge )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == NE) :
                        LA35_2 = self.input.LA(2)

                        if (self.synpred41_SelectExpr()) :
                            alt35 = 1




                    if alt35 == 1:
                        # SelectExpr.g:196:26: NE compare_ge
                        pass 
                        NE101=self.match(self.input, NE, self.FOLLOW_NE_in_compare_ne1981)
                        if self._state.backtracking == 0:

                            NE101_tree = self._adaptor.createWithPayload(NE101)
                            root_0 = self._adaptor.becomeRoot(NE101_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne1984)
                        compare_ge102 = self.compare_ge()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ge102.tree)


                    else:
                        break #loop35



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
    # SelectExpr.g:197:1: compare_ge : compare_gt ( GE compare_gt )* ;
    def compare_ge(self, ):

        retval = self.compare_ge_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GE104 = None
        compare_gt103 = None

        compare_gt105 = None


        GE104_tree = None

        try:
            try:
                # SelectExpr.g:197:12: ( compare_gt ( GE compare_gt )* )
                # SelectExpr.g:197:14: compare_gt ( GE compare_gt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge1994)
                compare_gt103 = self.compare_gt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_gt103.tree)
                # SelectExpr.g:197:25: ( GE compare_gt )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == GE) :
                        LA36_2 = self.input.LA(2)

                        if (self.synpred42_SelectExpr()) :
                            alt36 = 1




                    if alt36 == 1:
                        # SelectExpr.g:197:26: GE compare_gt
                        pass 
                        GE104=self.match(self.input, GE, self.FOLLOW_GE_in_compare_ge1997)
                        if self._state.backtracking == 0:

                            GE104_tree = self._adaptor.createWithPayload(GE104)
                            root_0 = self._adaptor.becomeRoot(GE104_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge2000)
                        compare_gt105 = self.compare_gt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_gt105.tree)


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

    # $ANTLR end "compare_ge"

    class compare_gt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_gt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_gt"
    # SelectExpr.g:198:1: compare_gt : compare_le ( GT compare_le )* ;
    def compare_gt(self, ):

        retval = self.compare_gt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GT107 = None
        compare_le106 = None

        compare_le108 = None


        GT107_tree = None

        try:
            try:
                # SelectExpr.g:198:12: ( compare_le ( GT compare_le )* )
                # SelectExpr.g:198:14: compare_le ( GT compare_le )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2010)
                compare_le106 = self.compare_le()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_le106.tree)
                # SelectExpr.g:198:25: ( GT compare_le )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == GT) :
                        LA37_2 = self.input.LA(2)

                        if (self.synpred43_SelectExpr()) :
                            alt37 = 1




                    if alt37 == 1:
                        # SelectExpr.g:198:26: GT compare_le
                        pass 
                        GT107=self.match(self.input, GT, self.FOLLOW_GT_in_compare_gt2013)
                        if self._state.backtracking == 0:

                            GT107_tree = self._adaptor.createWithPayload(GT107)
                            root_0 = self._adaptor.becomeRoot(GT107_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_le_in_compare_gt2016)
                        compare_le108 = self.compare_le()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_le108.tree)


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

    # $ANTLR end "compare_gt"

    class compare_le_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_le_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_le"
    # SelectExpr.g:199:1: compare_le : compare_lt ( LE compare_lt )* ;
    def compare_le(self, ):

        retval = self.compare_le_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LE110 = None
        compare_lt109 = None

        compare_lt111 = None


        LE110_tree = None

        try:
            try:
                # SelectExpr.g:199:12: ( compare_lt ( LE compare_lt )* )
                # SelectExpr.g:199:14: compare_lt ( LE compare_lt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2026)
                compare_lt109 = self.compare_lt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_lt109.tree)
                # SelectExpr.g:199:25: ( LE compare_lt )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == LE) :
                        LA38_2 = self.input.LA(2)

                        if (self.synpred44_SelectExpr()) :
                            alt38 = 1




                    if alt38 == 1:
                        # SelectExpr.g:199:26: LE compare_lt
                        pass 
                        LE110=self.match(self.input, LE, self.FOLLOW_LE_in_compare_le2029)
                        if self._state.backtracking == 0:

                            LE110_tree = self._adaptor.createWithPayload(LE110)
                            root_0 = self._adaptor.becomeRoot(LE110_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_lt_in_compare_le2032)
                        compare_lt111 = self.compare_lt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_lt111.tree)


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

    # $ANTLR end "compare_le"

    class compare_lt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_lt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_lt"
    # SelectExpr.g:200:1: compare_lt : arithmetic_expr ( LT arithmetic_expr )* ;
    def compare_lt(self, ):

        retval = self.compare_lt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LT113 = None
        arithmetic_expr112 = None

        arithmetic_expr114 = None


        LT113_tree = None

        try:
            try:
                # SelectExpr.g:200:12: ( arithmetic_expr ( LT arithmetic_expr )* )
                # SelectExpr.g:200:14: arithmetic_expr ( LT arithmetic_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2042)
                arithmetic_expr112 = self.arithmetic_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_expr112.tree)
                # SelectExpr.g:200:30: ( LT arithmetic_expr )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == LT) :
                        LA39_2 = self.input.LA(2)

                        if (self.synpred45_SelectExpr()) :
                            alt39 = 1




                    if alt39 == 1:
                        # SelectExpr.g:200:31: LT arithmetic_expr
                        pass 
                        LT113=self.match(self.input, LT, self.FOLLOW_LT_in_compare_lt2045)
                        if self._state.backtracking == 0:

                            LT113_tree = self._adaptor.createWithPayload(LT113)
                            root_0 = self._adaptor.becomeRoot(LT113_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt2048)
                        arithmetic_expr114 = self.arithmetic_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_expr114.tree)


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

    # $ANTLR end "compare_lt"

    class arithmetic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_expr"
    # SelectExpr.g:202:1: arithmetic_expr : arithmetic_sub_add ;
    def arithmetic_expr(self, ):

        retval = self.arithmetic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        arithmetic_sub_add115 = None



        try:
            try:
                # SelectExpr.g:202:17: ( arithmetic_sub_add )
                # SelectExpr.g:202:19: arithmetic_sub_add
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_sub_add_in_arithmetic_expr2059)
                arithmetic_sub_add115 = self.arithmetic_sub_add()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_sub_add115.tree)



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
    # SelectExpr.g:203:1: arithmetic_sub_add : arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* ;
    def arithmetic_sub_add(self, ):

        retval = self.arithmetic_sub_add_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB117 = None
        ADD118 = None
        arithmetic_mul_div_mod116 = None

        arithmetic_mul_div_mod119 = None


        SUB117_tree = None
        ADD118_tree = None

        try:
            try:
                # SelectExpr.g:203:20: ( arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* )
                # SelectExpr.g:203:22: arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2067)
                arithmetic_mul_div_mod116 = self.arithmetic_mul_div_mod()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_mul_div_mod116.tree)
                # SelectExpr.g:203:45: ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == SUB) :
                        LA41_2 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt41 = 1


                    elif (LA41_0 == ADD) :
                        LA41_3 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt41 = 1




                    if alt41 == 1:
                        # SelectExpr.g:203:46: ( SUB | ADD ) arithmetic_mul_div_mod
                        pass 
                        # SelectExpr.g:203:46: ( SUB | ADD )
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == SUB) :
                            alt40 = 1
                        elif (LA40_0 == ADD) :
                            alt40 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 40, 0, self.input)

                            raise nvae

                        if alt40 == 1:
                            # SelectExpr.g:203:47: SUB
                            pass 
                            SUB117=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_sub_add2071)
                            if self._state.backtracking == 0:

                                SUB117_tree = self._adaptor.createWithPayload(SUB117)
                                root_0 = self._adaptor.becomeRoot(SUB117_tree, root_0)



                        elif alt40 == 2:
                            # SelectExpr.g:203:52: ADD
                            pass 
                            ADD118=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_sub_add2074)
                            if self._state.backtracking == 0:

                                ADD118_tree = self._adaptor.createWithPayload(ADD118)
                                root_0 = self._adaptor.becomeRoot(ADD118_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2078)
                        arithmetic_mul_div_mod119 = self.arithmetic_mul_div_mod()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_mul_div_mod119.tree)


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

    # $ANTLR end "arithmetic_sub_add"

    class arithmetic_mul_div_mod_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_mul_div_mod_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_mul_div_mod"
    # SelectExpr.g:204:1: arithmetic_mul_div_mod : arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* ;
    def arithmetic_mul_div_mod(self, ):

        retval = self.arithmetic_mul_div_mod_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MUL121 = None
        DIV122 = None
        MOD123 = None
        arithmetic_pow120 = None

        arithmetic_pow124 = None


        MUL121_tree = None
        DIV122_tree = None
        MOD123_tree = None

        try:
            try:
                # SelectExpr.g:204:24: ( arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* )
                # SelectExpr.g:204:26: arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2088)
                arithmetic_pow120 = self.arithmetic_pow()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_pow120.tree)
                # SelectExpr.g:204:41: ( ( MUL | DIV | MOD ) arithmetic_pow )*
                while True: #loop43
                    alt43 = 2
                    LA43 = self.input.LA(1)
                    if LA43 == MUL:
                        LA43_2 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt43 = 1


                    elif LA43 == DIV:
                        LA43_3 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt43 = 1


                    elif LA43 == MOD:
                        LA43_4 = self.input.LA(2)

                        if (self.synpred50_SelectExpr()) :
                            alt43 = 1



                    if alt43 == 1:
                        # SelectExpr.g:204:42: ( MUL | DIV | MOD ) arithmetic_pow
                        pass 
                        # SelectExpr.g:204:42: ( MUL | DIV | MOD )
                        alt42 = 3
                        LA42 = self.input.LA(1)
                        if LA42 == MUL:
                            alt42 = 1
                        elif LA42 == DIV:
                            alt42 = 2
                        elif LA42 == MOD:
                            alt42 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 42, 0, self.input)

                            raise nvae

                        if alt42 == 1:
                            # SelectExpr.g:204:43: MUL
                            pass 
                            MUL121=self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_mul_div_mod2092)
                            if self._state.backtracking == 0:

                                MUL121_tree = self._adaptor.createWithPayload(MUL121)
                                root_0 = self._adaptor.becomeRoot(MUL121_tree, root_0)



                        elif alt42 == 2:
                            # SelectExpr.g:204:50: DIV
                            pass 
                            DIV122=self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_mul_div_mod2097)
                            if self._state.backtracking == 0:

                                DIV122_tree = self._adaptor.createWithPayload(DIV122)
                                root_0 = self._adaptor.becomeRoot(DIV122_tree, root_0)



                        elif alt42 == 3:
                            # SelectExpr.g:204:57: MOD
                            pass 
                            MOD123=self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_mul_div_mod2102)
                            if self._state.backtracking == 0:

                                MOD123_tree = self._adaptor.createWithPayload(MOD123)
                                root_0 = self._adaptor.becomeRoot(MOD123_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2106)
                        arithmetic_pow124 = self.arithmetic_pow()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_pow124.tree)


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

    # $ANTLR end "arithmetic_mul_div_mod"

    class arithmetic_pow_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_pow_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_pow"
    # SelectExpr.g:205:1: arithmetic_pow : arithmetic_unary ( POW arithmetic_unary )* ;
    def arithmetic_pow(self, ):

        retval = self.arithmetic_pow_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POW126 = None
        arithmetic_unary125 = None

        arithmetic_unary127 = None


        POW126_tree = None

        try:
            try:
                # SelectExpr.g:205:16: ( arithmetic_unary ( POW arithmetic_unary )* )
                # SelectExpr.g:205:18: arithmetic_unary ( POW arithmetic_unary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2116)
                arithmetic_unary125 = self.arithmetic_unary()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_unary125.tree)
                # SelectExpr.g:205:35: ( POW arithmetic_unary )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == POW) :
                        LA44_2 = self.input.LA(2)

                        if (self.synpred51_SelectExpr()) :
                            alt44 = 1




                    if alt44 == 1:
                        # SelectExpr.g:205:36: POW arithmetic_unary
                        pass 
                        POW126=self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_pow2119)
                        if self._state.backtracking == 0:

                            POW126_tree = self._adaptor.createWithPayload(POW126)
                            root_0 = self._adaptor.becomeRoot(POW126_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow2122)
                        arithmetic_unary127 = self.arithmetic_unary()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_unary127.tree)


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

    # $ANTLR end "arithmetic_pow"

    class arithmetic_unary_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_unary_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_unary"
    # SelectExpr.g:206:1: arithmetic_unary : ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom );
    def arithmetic_unary(self, ):

        retval = self.arithmetic_unary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB128 = None
        ADD130 = None
        atom129 = None

        atom131 = None

        atom132 = None


        SUB128_tree = None
        ADD130_tree = None
        stream_SUB = RewriteRuleTokenStream(self._adaptor, "token SUB")
        stream_ADD = RewriteRuleTokenStream(self._adaptor, "token ADD")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # SelectExpr.g:206:18: ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom )
                alt45 = 3
                LA45 = self.input.LA(1)
                if LA45 == SUB:
                    alt45 = 1
                elif LA45 == ADD:
                    alt45 = 2
                elif LA45 == LIST_BEGIN or LA45 == SELECT or LA45 == THIS or LA45 == STRING or LA45 == INTEGER or LA45 == FLOAT or LA45 == TRUE or LA45 == FALSE or LA45 == PHRASE or LA45 == 98:
                    alt45 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # SelectExpr.g:207:2: SUB atom
                    pass 
                    SUB128=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_unary2133) 
                    if self._state.backtracking == 0:
                        stream_SUB.add(SUB128)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2135)
                    atom129 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom129.tree)

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
                        # 207:11: -> ^( NEG atom )
                        # SelectExpr.g:207:14: ^( NEG atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEG, "NEG"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt45 == 2:
                    # SelectExpr.g:208:5: ADD atom
                    pass 
                    ADD130=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_unary2149) 
                    if self._state.backtracking == 0:
                        stream_ADD.add(ADD130)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2151)
                    atom131 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom131.tree)

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
                        # 208:14: -> ^( POS atom )
                        # SelectExpr.g:208:17: ^( POS atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(POS, "POS"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt45 == 3:
                    # SelectExpr.g:209:5: atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2165)
                    atom132 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom132.tree)


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
    # SelectExpr.g:212:1: atom : ( value | variable | function | '(' expr ')' | statement_select );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal136 = None
        char_literal138 = None
        value133 = None

        variable134 = None

        function135 = None

        expr137 = None

        statement_select139 = None


        char_literal136_tree = None
        char_literal138_tree = None

        try:
            try:
                # SelectExpr.g:213:2: ( value | variable | function | '(' expr ')' | statement_select )
                alt46 = 5
                LA46 = self.input.LA(1)
                if LA46 == LIST_BEGIN or LA46 == THIS or LA46 == STRING or LA46 == INTEGER or LA46 == FLOAT or LA46 == TRUE or LA46 == FALSE:
                    alt46 = 1
                elif LA46 == PHRASE:
                    LA46 = self.input.LA(2)
                    if LA46 == DOT:
                        alt46 = 1
                    elif LA46 == 98:
                        alt46 = 3
                    elif LA46 == EOF or LA46 == SEP or LA46 == END or LA46 == AND or LA46 == XOR or LA46 == OR or LA46 == IN or LA46 == EQ or LA46 == NE or LA46 == LE or LA46 == GE or LA46 == LT or LA46 == GT or LA46 == ADD or LA46 == SUB or LA46 == MUL or LA46 == DIV or LA46 == MOD or LA46 == POW or LA46 == LIST_END or LA46 == AGE_BEGIN or LA46 == AGE_END or LA46 == WHERE or LA46 == ORDER or LA46 == GROUP or LA46 == AS or LA46 == CONNECT or LA46 == START or LA46 == STOP or LA46 == 99:
                        alt46 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 46, 2, self.input)

                        raise nvae

                elif LA46 == 98:
                    alt46 = 4
                elif LA46 == SELECT:
                    alt46 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # SelectExpr.g:213:4: value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_value_in_atom2176)
                    value133 = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, value133.tree)


                elif alt46 == 2:
                    # SelectExpr.g:214:4: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_atom2181)
                    variable134 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable134.tree)


                elif alt46 == 3:
                    # SelectExpr.g:215:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_atom2186)
                    function135 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function135.tree)


                elif alt46 == 4:
                    # SelectExpr.g:216:4: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal136=self.match(self.input, 98, self.FOLLOW_98_in_atom2191)
                    self._state.following.append(self.FOLLOW_expr_in_atom2194)
                    expr137 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr137.tree)
                    char_literal138=self.match(self.input, 99, self.FOLLOW_99_in_atom2196)


                elif alt46 == 5:
                    # SelectExpr.g:217:4: statement_select
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_atom2202)
                    statement_select139 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select139.tree)


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
    # SelectExpr.g:220:1: function : PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE140 = None
        char_literal141 = None
        char_literal143 = None
        parameter142 = None


        PHRASE140_tree = None
        char_literal141_tree = None
        char_literal143_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # SelectExpr.g:220:10: ( PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) )
                # SelectExpr.g:220:12: PHRASE '(' ( parameter )? ')'
                pass 
                PHRASE140=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function2211) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE140)
                char_literal141=self.match(self.input, 98, self.FOLLOW_98_in_function2213) 
                if self._state.backtracking == 0:
                    stream_98.add(char_literal141)
                # SelectExpr.g:220:23: ( parameter )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == NOT or (ADD <= LA47_0 <= SUB) or LA47_0 == LIST_BEGIN or LA47_0 == SELECT or LA47_0 == THIS or LA47_0 == STRING or (INTEGER <= LA47_0 <= FALSE) or LA47_0 == PHRASE or LA47_0 == 98) :
                    alt47 = 1
                if alt47 == 1:
                    # SelectExpr.g:0:0: parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function2215)
                    parameter142 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter142.tree)



                char_literal143=self.match(self.input, 99, self.FOLLOW_99_in_function2218) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal143)

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
                    # 220:38: -> ^( FCT PHRASE ( parameter )? )
                    # SelectExpr.g:220:41: ^( FCT PHRASE ( parameter )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FCT, "FCT"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:220:54: ( parameter )?
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
    # SelectExpr.g:223:1: parameter : expr ( SEP expr )* ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEP145 = None
        expr144 = None

        expr146 = None


        SEP145_tree = None

        try:
            try:
                # SelectExpr.g:223:11: ( expr ( SEP expr )* )
                # SelectExpr.g:223:13: expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_parameter2238)
                expr144 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr144.tree)
                # SelectExpr.g:223:18: ( SEP expr )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == SEP) :
                        alt48 = 1


                    if alt48 == 1:
                        # SelectExpr.g:223:19: SEP expr
                        pass 
                        SEP145=self.match(self.input, SEP, self.FOLLOW_SEP_in_parameter2241)
                        self._state.following.append(self.FOLLOW_expr_in_parameter2244)
                        expr146 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr146.tree)


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

    # $ANTLR end "parameter"

    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.variable_return, self).__init__()

            self.tree = None




    # $ANTLR start "variable"
    # SelectExpr.g:226:1: variable : PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) ;
    def variable(self, ):

        retval = self.variable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE147 = None
        age148 = None


        PHRASE147_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:226:10: ( PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) )
                # SelectExpr.g:226:12: PHRASE ( age )?
                pass 
                PHRASE147=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable2255) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE147)
                # SelectExpr.g:226:19: ( age )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == AGE_BEGIN) :
                    alt49 = 1
                if alt49 == 1:
                    # SelectExpr.g:226:20: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable2258)
                    age148 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age148.tree)




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
                    # 226:26: -> ^( VAR PHRASE ( age )? )
                    # SelectExpr.g:226:29: ^( VAR PHRASE ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:226:42: ( age )?
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
    # SelectExpr.g:229:1: age : AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) ;
    def age(self, ):

        retval = self.age_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AGE_BEGIN149 = None
        AGE_END151 = None
        expr150 = None


        AGE_BEGIN149_tree = None
        AGE_END151_tree = None
        stream_AGE_BEGIN = RewriteRuleTokenStream(self._adaptor, "token AGE_BEGIN")
        stream_AGE_END = RewriteRuleTokenStream(self._adaptor, "token AGE_END")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:229:5: ( AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) )
                # SelectExpr.g:229:7: AGE_BEGIN ( expr )? AGE_END
                pass 
                AGE_BEGIN149=self.match(self.input, AGE_BEGIN, self.FOLLOW_AGE_BEGIN_in_age2282) 
                if self._state.backtracking == 0:
                    stream_AGE_BEGIN.add(AGE_BEGIN149)
                # SelectExpr.g:229:17: ( expr )?
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if (LA50_0 == NOT or (ADD <= LA50_0 <= SUB) or LA50_0 == LIST_BEGIN or LA50_0 == SELECT or LA50_0 == THIS or LA50_0 == STRING or (INTEGER <= LA50_0 <= FALSE) or LA50_0 == PHRASE or LA50_0 == 98) :
                    alt50 = 1
                if alt50 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_age2284)
                    expr150 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr150.tree)



                AGE_END151=self.match(self.input, AGE_END, self.FOLLOW_AGE_END_in_age2287) 
                if self._state.backtracking == 0:
                    stream_AGE_END.add(AGE_END151)

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
                    # 229:31: -> ^( AGE ( expr )? )
                    # SelectExpr.g:229:34: ^( AGE ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AGE, "AGE"), root_1)

                    # SelectExpr.g:229:40: ( expr )?
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
    # SelectExpr.g:232:1: value : ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRING152 = None
        FLOAT153 = None
        INTEGER154 = None
        TRUE155 = None
        FALSE156 = None
        this_157 = None

        list_158 = None


        STRING152_tree = None
        FLOAT153_tree = None
        INTEGER154_tree = None
        TRUE155_tree = None
        FALSE156_tree = None
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_TRUE = RewriteRuleTokenStream(self._adaptor, "token TRUE")
        stream_FALSE = RewriteRuleTokenStream(self._adaptor, "token FALSE")
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")

        try:
            try:
                # SelectExpr.g:232:7: ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ )
                alt51 = 7
                LA51 = self.input.LA(1)
                if LA51 == STRING:
                    alt51 = 1
                elif LA51 == FLOAT:
                    alt51 = 2
                elif LA51 == INTEGER:
                    alt51 = 3
                elif LA51 == TRUE:
                    alt51 = 4
                elif LA51 == FALSE:
                    alt51 = 5
                elif LA51 == THIS or LA51 == PHRASE:
                    alt51 = 6
                elif LA51 == LIST_BEGIN:
                    alt51 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # SelectExpr.g:232:9: STRING
                    pass 
                    STRING152=self.match(self.input, STRING, self.FOLLOW_STRING_in_value2305) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING152)

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
                        # 232:17: -> ^( VAL STRING )
                        # SelectExpr.g:232:20: ^( VAL STRING )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_STRING.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 2:
                    # SelectExpr.g:233:4: FLOAT
                    pass 
                    FLOAT153=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value2319) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT153)

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
                        # 233:11: -> ^( VAL FLOAT )
                        # SelectExpr.g:233:14: ^( VAL FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 3:
                    # SelectExpr.g:234:4: INTEGER
                    pass 
                    INTEGER154=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value2333) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER154)

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
                        # 234:12: -> ^( VAL INTEGER )
                        # SelectExpr.g:234:15: ^( VAL INTEGER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 4:
                    # SelectExpr.g:235:4: TRUE
                    pass 
                    TRUE155=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value2346) 
                    if self._state.backtracking == 0:
                        stream_TRUE.add(TRUE155)

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
                        # 235:10: -> ^( VAL TRUE )
                        # SelectExpr.g:235:13: ^( VAL TRUE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_TRUE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 5:
                    # SelectExpr.g:236:4: FALSE
                    pass 
                    FALSE156=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value2360) 
                    if self._state.backtracking == 0:
                        stream_FALSE.add(FALSE156)

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
                        # 236:11: -> ^( VAL FALSE )
                        # SelectExpr.g:236:14: ^( VAL FALSE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FALSE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 6:
                    # SelectExpr.g:237:4: this_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_this__in_value2374)
                    this_157 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, this_157.tree)


                elif alt51 == 7:
                    # SelectExpr.g:238:4: list_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list__in_value2379)
                    list_158 = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_158.tree)


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
    # SelectExpr.g:241:1: this_ : ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        retval = self.this__return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE159 = None
        DOT160 = None
        THIS161 = None

        PHRASE159_tree = None
        DOT160_tree = None
        THIS161_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")

        try:
            try:
                # SelectExpr.g:241:7: ( ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) )
                # SelectExpr.g:241:9: ( PHRASE DOT )? THIS
                pass 
                # SelectExpr.g:241:9: ( PHRASE DOT )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == PHRASE) :
                    alt52 = 1
                if alt52 == 1:
                    # SelectExpr.g:241:10: PHRASE DOT
                    pass 
                    PHRASE159=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_2390) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE159)
                    DOT160=self.match(self.input, DOT, self.FOLLOW_DOT_in_this_2392) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT160)



                THIS161=self.match(self.input, THIS, self.FOLLOW_THIS_in_this_2396) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS161)

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
                    # 241:29: -> ^( THIS ( PHRASE )? )
                    # SelectExpr.g:241:32: ^( THIS ( PHRASE )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_THIS.nextNode(), root_1)

                    # SelectExpr.g:241:39: ( PHRASE )?
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
    # SelectExpr.g:244:1: list_ : LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) ;
    def list_(self, ):

        retval = self.list__return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIST_BEGIN162 = None
        SEP164 = None
        LIST_END166 = None
        expr163 = None

        expr165 = None


        LIST_BEGIN162_tree = None
        SEP164_tree = None
        LIST_END166_tree = None
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_SEP = RewriteRuleTokenStream(self._adaptor, "token SEP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:244:7: ( LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) )
                # SelectExpr.g:244:10: LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END
                pass 
                LIST_BEGIN162=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_list_2417) 
                if self._state.backtracking == 0:
                    stream_LIST_BEGIN.add(LIST_BEGIN162)
                # SelectExpr.g:244:21: ( ( expr )? ( SEP expr )* )
                # SelectExpr.g:244:23: ( expr )? ( SEP expr )*
                pass 
                # SelectExpr.g:244:23: ( expr )?
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == NOT or (ADD <= LA53_0 <= SUB) or LA53_0 == LIST_BEGIN or LA53_0 == SELECT or LA53_0 == THIS or LA53_0 == STRING or (INTEGER <= LA53_0 <= FALSE) or LA53_0 == PHRASE or LA53_0 == 98) :
                    alt53 = 1
                if alt53 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_list_2421)
                    expr163 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr163.tree)



                # SelectExpr.g:244:29: ( SEP expr )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == SEP) :
                        alt54 = 1


                    if alt54 == 1:
                        # SelectExpr.g:244:30: SEP expr
                        pass 
                        SEP164=self.match(self.input, SEP, self.FOLLOW_SEP_in_list_2425) 
                        if self._state.backtracking == 0:
                            stream_SEP.add(SEP164)
                        self._state.following.append(self.FOLLOW_expr_in_list_2427)
                        expr165 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr165.tree)


                    else:
                        break #loop54



                LIST_END166=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_list_2433) 
                if self._state.backtracking == 0:
                    stream_LIST_END.add(LIST_END166)

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
                    # 244:52: -> ^( LIST ( expr )* )
                    # SelectExpr.g:244:55: ^( LIST ( expr )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # SelectExpr.g:244:62: ( expr )*
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
        # SelectExpr.g:139:13: ( statement_select END )
        # SelectExpr.g:139:13: statement_select END
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectExpr1393)
        self.statement_select()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred2_SelectExpr1395)


    # $ANTLR end "synpred2_SelectExpr"



    # $ANTLR start "synpred3_SelectExpr"
    def synpred3_SelectExpr_fragment(self, ):
        # SelectExpr.g:140:4: ( expr END )
        # SelectExpr.g:140:4: expr END
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred3_SelectExpr1401)
        self.expr()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred3_SelectExpr1403)


    # $ANTLR end "synpred3_SelectExpr"



    # $ANTLR start "synpred4_SelectExpr"
    def synpred4_SelectExpr_fragment(self, ):
        # SelectExpr.g:145:17: ( where_ )
        # SelectExpr.g:145:17: where_
        pass 
        self._state.following.append(self.FOLLOW_where__in_synpred4_SelectExpr1425)
        self.where_()

        self._state.following.pop()


    # $ANTLR end "synpred4_SelectExpr"



    # $ANTLR start "synpred6_SelectExpr"
    def synpred6_SelectExpr_fragment(self, ):
        # SelectExpr.g:145:27: ( ( start_ )? connect_ stop_ )
        # SelectExpr.g:145:27: ( start_ )? connect_ stop_
        pass 
        # SelectExpr.g:145:27: ( start_ )?
        alt55 = 2
        LA55_0 = self.input.LA(1)

        if (LA55_0 == START) :
            alt55 = 1
        if alt55 == 1:
            # SelectExpr.g:145:28: start_
            pass 
            self._state.following.append(self.FOLLOW_start__in_synpred6_SelectExpr1431)
            self.start_()

            self._state.following.pop()



        self._state.following.append(self.FOLLOW_connect__in_synpred6_SelectExpr1435)
        self.connect_()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_stop__in_synpred6_SelectExpr1437)
        self.stop_()

        self._state.following.pop()


    # $ANTLR end "synpred6_SelectExpr"



    # $ANTLR start "synpred8_SelectExpr"
    def synpred8_SelectExpr_fragment(self, ):
        # SelectExpr.g:145:55: ( group_ ( having_ )? )
        # SelectExpr.g:145:55: group_ ( having_ )?
        pass 
        self._state.following.append(self.FOLLOW_group__in_synpred8_SelectExpr1442)
        self.group_()

        self._state.following.pop()
        # SelectExpr.g:145:62: ( having_ )?
        alt56 = 2
        LA56_0 = self.input.LA(1)

        if (LA56_0 == HAVING) :
            alt56 = 1
        if alt56 == 1:
            # SelectExpr.g:145:63: having_
            pass 
            self._state.following.append(self.FOLLOW_having__in_synpred8_SelectExpr1445)
            self.having_()

            self._state.following.pop()





    # $ANTLR end "synpred8_SelectExpr"



    # $ANTLR start "synpred9_SelectExpr"
    def synpred9_SelectExpr_fragment(self, ):
        # SelectExpr.g:145:76: ( order_ )
        # SelectExpr.g:145:76: order_
        pass 
        self._state.following.append(self.FOLLOW_order__in_synpred9_SelectExpr1452)
        self.order_()

        self._state.following.pop()


    # $ANTLR end "synpred9_SelectExpr"



    # $ANTLR start "synpred10_SelectExpr"
    def synpred10_SelectExpr_fragment(self, ):
        # SelectExpr.g:145:86: ( as_ )
        # SelectExpr.g:145:86: as_
        pass 
        self._state.following.append(self.FOLLOW_as__in_synpred10_SelectExpr1457)
        self.as_()

        self._state.following.pop()


    # $ANTLR end "synpred10_SelectExpr"



    # $ANTLR start "synpred17_SelectExpr"
    def synpred17_SelectExpr_fragment(self, ):
        # SelectExpr.g:151:21: ( SEP expr )
        # SelectExpr.g:151:21: SEP expr
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred17_SelectExpr1574)
        self._state.following.append(self.FOLLOW_expr_in_synpred17_SelectExpr1577)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred17_SelectExpr"



    # $ANTLR start "synpred22_SelectExpr"
    def synpred22_SelectExpr_fragment(self, ):
        # SelectExpr.g:166:44: ( SEP ( PHRASE | function ) )
        # SelectExpr.g:166:44: SEP ( PHRASE | function )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred22_SelectExpr1678)
        # SelectExpr.g:166:49: ( PHRASE | function )
        alt58 = 2
        LA58_0 = self.input.LA(1)

        if (LA58_0 == PHRASE) :
            LA58_1 = self.input.LA(2)

            if (LA58_1 == 98) :
                alt58 = 2
            elif (LA58_1 == EOF) :
                alt58 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 58, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 58, 0, self.input)

            raise nvae

        if alt58 == 1:
            # SelectExpr.g:166:51: PHRASE
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred22_SelectExpr1683)


        elif alt58 == 2:
            # SelectExpr.g:166:60: function
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred22_SelectExpr1687)
            self.function()

            self._state.following.pop()





    # $ANTLR end "synpred22_SelectExpr"



    # $ANTLR start "synpred25_SelectExpr"
    def synpred25_SelectExpr_fragment(self, ):
        # SelectExpr.g:172:66: ( SEP ( PHRASE direction_ | function direction_ ) )
        # SelectExpr.g:172:66: SEP ( PHRASE direction_ | function direction_ )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred25_SelectExpr1734)
        # SelectExpr.g:172:71: ( PHRASE direction_ | function direction_ )
        alt59 = 2
        LA59_0 = self.input.LA(1)

        if (LA59_0 == PHRASE) :
            LA59_1 = self.input.LA(2)

            if (LA59_1 == 98) :
                alt59 = 2
            elif (LA59_1 == EOF or (ASC <= LA59_1 <= DESC)) :
                alt59 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 59, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 59, 0, self.input)

            raise nvae

        if alt59 == 1:
            # SelectExpr.g:172:73: PHRASE direction_
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred25_SelectExpr1739)
            self._state.following.append(self.FOLLOW_direction__in_synpred25_SelectExpr1741)
            self.direction_()

            self._state.following.pop()


        elif alt59 == 2:
            # SelectExpr.g:172:93: function direction_
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred25_SelectExpr1745)
            self.function()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_direction__in_synpred25_SelectExpr1747)
            self.direction_()

            self._state.following.pop()





    # $ANTLR end "synpred25_SelectExpr"



    # $ANTLR start "synpred33_SelectExpr"
    def synpred33_SelectExpr_fragment(self, ):
        # SelectExpr.g:181:8: ( assign_expr )
        # SelectExpr.g:181:8: assign_expr
        pass 
        self._state.following.append(self.FOLLOW_assign_expr_in_synpred33_SelectExpr1818)
        self.assign_expr()

        self._state.following.pop()


    # $ANTLR end "synpred33_SelectExpr"



    # $ANTLR start "synpred35_SelectExpr"
    def synpred35_SelectExpr_fragment(self, ):
        # SelectExpr.g:188:24: ( OR logic_xor )
        # SelectExpr.g:188:24: OR logic_xor
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred35_SelectExpr1877)
        self._state.following.append(self.FOLLOW_logic_xor_in_synpred35_SelectExpr1881)
        self.logic_xor()

        self._state.following.pop()


    # $ANTLR end "synpred35_SelectExpr"



    # $ANTLR start "synpred36_SelectExpr"
    def synpred36_SelectExpr_fragment(self, ):
        # SelectExpr.g:189:24: ( XOR logic_and )
        # SelectExpr.g:189:24: XOR logic_and
        pass 
        self.match(self.input, XOR, self.FOLLOW_XOR_in_synpred36_SelectExpr1894)
        self._state.following.append(self.FOLLOW_logic_and_in_synpred36_SelectExpr1897)
        self.logic_and()

        self._state.following.pop()


    # $ANTLR end "synpred36_SelectExpr"



    # $ANTLR start "synpred37_SelectExpr"
    def synpred37_SelectExpr_fragment(self, ):
        # SelectExpr.g:190:24: ( AND logic_not )
        # SelectExpr.g:190:24: AND logic_not
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred37_SelectExpr1910)
        self._state.following.append(self.FOLLOW_logic_not_in_synpred37_SelectExpr1913)
        self.logic_not()

        self._state.following.pop()


    # $ANTLR end "synpred37_SelectExpr"



    # $ANTLR start "synpred39_SelectExpr"
    def synpred39_SelectExpr_fragment(self, ):
        # SelectExpr.g:194:26: ( IN atom )
        # SelectExpr.g:194:26: IN atom
        pass 
        self.match(self.input, IN, self.FOLLOW_IN_in_synpred39_SelectExpr1949)
        self._state.following.append(self.FOLLOW_atom_in_synpred39_SelectExpr1952)
        self.atom()

        self._state.following.pop()


    # $ANTLR end "synpred39_SelectExpr"



    # $ANTLR start "synpred40_SelectExpr"
    def synpred40_SelectExpr_fragment(self, ):
        # SelectExpr.g:195:26: ( EQ compare_ne )
        # SelectExpr.g:195:26: EQ compare_ne
        pass 
        self.match(self.input, EQ, self.FOLLOW_EQ_in_synpred40_SelectExpr1965)
        self._state.following.append(self.FOLLOW_compare_ne_in_synpred40_SelectExpr1968)
        self.compare_ne()

        self._state.following.pop()


    # $ANTLR end "synpred40_SelectExpr"



    # $ANTLR start "synpred41_SelectExpr"
    def synpred41_SelectExpr_fragment(self, ):
        # SelectExpr.g:196:26: ( NE compare_ge )
        # SelectExpr.g:196:26: NE compare_ge
        pass 
        self.match(self.input, NE, self.FOLLOW_NE_in_synpred41_SelectExpr1981)
        self._state.following.append(self.FOLLOW_compare_ge_in_synpred41_SelectExpr1984)
        self.compare_ge()

        self._state.following.pop()


    # $ANTLR end "synpred41_SelectExpr"



    # $ANTLR start "synpred42_SelectExpr"
    def synpred42_SelectExpr_fragment(self, ):
        # SelectExpr.g:197:26: ( GE compare_gt )
        # SelectExpr.g:197:26: GE compare_gt
        pass 
        self.match(self.input, GE, self.FOLLOW_GE_in_synpred42_SelectExpr1997)
        self._state.following.append(self.FOLLOW_compare_gt_in_synpred42_SelectExpr2000)
        self.compare_gt()

        self._state.following.pop()


    # $ANTLR end "synpred42_SelectExpr"



    # $ANTLR start "synpred43_SelectExpr"
    def synpred43_SelectExpr_fragment(self, ):
        # SelectExpr.g:198:26: ( GT compare_le )
        # SelectExpr.g:198:26: GT compare_le
        pass 
        self.match(self.input, GT, self.FOLLOW_GT_in_synpred43_SelectExpr2013)
        self._state.following.append(self.FOLLOW_compare_le_in_synpred43_SelectExpr2016)
        self.compare_le()

        self._state.following.pop()


    # $ANTLR end "synpred43_SelectExpr"



    # $ANTLR start "synpred44_SelectExpr"
    def synpred44_SelectExpr_fragment(self, ):
        # SelectExpr.g:199:26: ( LE compare_lt )
        # SelectExpr.g:199:26: LE compare_lt
        pass 
        self.match(self.input, LE, self.FOLLOW_LE_in_synpred44_SelectExpr2029)
        self._state.following.append(self.FOLLOW_compare_lt_in_synpred44_SelectExpr2032)
        self.compare_lt()

        self._state.following.pop()


    # $ANTLR end "synpred44_SelectExpr"



    # $ANTLR start "synpred45_SelectExpr"
    def synpred45_SelectExpr_fragment(self, ):
        # SelectExpr.g:200:31: ( LT arithmetic_expr )
        # SelectExpr.g:200:31: LT arithmetic_expr
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred45_SelectExpr2045)
        self._state.following.append(self.FOLLOW_arithmetic_expr_in_synpred45_SelectExpr2048)
        self.arithmetic_expr()

        self._state.following.pop()


    # $ANTLR end "synpred45_SelectExpr"



    # $ANTLR start "synpred47_SelectExpr"
    def synpred47_SelectExpr_fragment(self, ):
        # SelectExpr.g:203:46: ( ( SUB | ADD ) arithmetic_mul_div_mod )
        # SelectExpr.g:203:46: ( SUB | ADD ) arithmetic_mul_div_mod
        pass 
        if (ADD <= self.input.LA(1) <= SUB):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_synpred47_SelectExpr2078)
        self.arithmetic_mul_div_mod()

        self._state.following.pop()


    # $ANTLR end "synpred47_SelectExpr"



    # $ANTLR start "synpred50_SelectExpr"
    def synpred50_SelectExpr_fragment(self, ):
        # SelectExpr.g:204:42: ( ( MUL | DIV | MOD ) arithmetic_pow )
        # SelectExpr.g:204:42: ( MUL | DIV | MOD ) arithmetic_pow
        pass 
        if (MUL <= self.input.LA(1) <= MOD):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_pow_in_synpred50_SelectExpr2106)
        self.arithmetic_pow()

        self._state.following.pop()


    # $ANTLR end "synpred50_SelectExpr"



    # $ANTLR start "synpred51_SelectExpr"
    def synpred51_SelectExpr_fragment(self, ):
        # SelectExpr.g:205:36: ( POW arithmetic_unary )
        # SelectExpr.g:205:36: POW arithmetic_unary
        pass 
        self.match(self.input, POW, self.FOLLOW_POW_in_synpred51_SelectExpr2119)
        self._state.following.append(self.FOLLOW_arithmetic_unary_in_synpred51_SelectExpr2122)
        self.arithmetic_unary()

        self._state.following.pop()


    # $ANTLR end "synpred51_SelectExpr"




    # Delegated rules

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

    def synpred39_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred39_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred22_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred22_SelectExpr_fragment()
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

    def synpred36_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred36_SelectExpr_fragment()
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

    def synpred25_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred25_SelectExpr_fragment()
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

    def synpred41_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred41_SelectExpr_fragment()
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

    def synpred35_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred35_SelectExpr_fragment()
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

    def synpred33_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred33_SelectExpr_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\16\1\0\16\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\142\1\0\16\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\13\uffff\1\3\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\16\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\16\13\uffff\1\2\11\uffff\2\2\6\uffff\1\2\7\uffff"
        u"\1\1\21\uffff\1\2\16\uffff\1\2\1\uffff\4\2\2\uffff\1\2\4\uffff"
        u"\1\2"),
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
                    s = 15

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
    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\1\32\1\0\15\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\1\142\1\0\15\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\2\uffff\1\2\13\uffff\1\1"
        )

    DFA27_special = DFA.unpack(
        u"\1\uffff\1\0\15\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\2\11\uffff\2\2\6\uffff\1\2\7\uffff\1\2\21\uffff\1"
        u"\2\16\uffff\1\2\1\uffff\4\2\2\uffff\1\1\4\uffff\1\2"),
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

    # class definition for DFA #27

    class DFA27(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA27_1 = input.LA(1)

                 
                index27_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred33_SelectExpr()):
                    s = 14

                elif (True):
                    s = 2

                 
                input.seek(index27_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 27, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_prog_in_eval1373 = frozenset([1])
    FOLLOW_statement_in_prog1383 = frozenset([1, 14, 26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_statement_select_in_statement1393 = frozenset([14])
    FOLLOW_END_in_statement1395 = frozenset([1])
    FOLLOW_expr_in_statement1401 = frozenset([14])
    FOLLOW_END_in_statement1403 = frozenset([1])
    FOLLOW_END_in_statement1409 = frozenset([1])
    FOLLOW_select__in_statement_select1420 = frozenset([55])
    FOLLOW_from__in_statement_select1422 = frozenset([1, 58, 59, 63, 69, 72, 73])
    FOLLOW_where__in_statement_select1425 = frozenset([1, 59, 63, 69, 72, 73])
    FOLLOW_start__in_statement_select1431 = frozenset([72, 73])
    FOLLOW_connect__in_statement_select1435 = frozenset([74])
    FOLLOW_stop__in_statement_select1437 = frozenset([1, 59, 63, 69])
    FOLLOW_group__in_statement_select1442 = frozenset([1, 59, 65, 69])
    FOLLOW_having__in_statement_select1445 = frozenset([1, 59, 69])
    FOLLOW_order__in_statement_select1452 = frozenset([1, 69])
    FOLLOW_as__in_statement_select1457 = frozenset([1])
    FOLLOW_SELECT_in_select_1517 = frozenset([38, 70, 93])
    FOLLOW_MUL_in_select_1521 = frozenset([1])
    FOLLOW_PHRASE_in_select_1528 = frozenset([1, 13])
    FOLLOW_function_in_select_1532 = frozenset([1, 13])
    FOLLOW_this__in_select_1536 = frozenset([1, 13])
    FOLLOW_SEP_in_select_1540 = frozenset([70, 93])
    FOLLOW_PHRASE_in_select_1544 = frozenset([1, 13])
    FOLLOW_function_in_select_1548 = frozenset([1, 13])
    FOLLOW_this__in_select_1552 = frozenset([1, 13])
    FOLLOW_FROM_in_from_1568 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_from_1571 = frozenset([1, 13])
    FOLLOW_SEP_in_from_1574 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_from_1577 = frozenset([1, 13])
    FOLLOW_WHERE_in_where_1588 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_where_1591 = frozenset([1])
    FOLLOW_START_in_start_1600 = frozenset([75])
    FOLLOW_WITH_in_start_1603 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_start_1606 = frozenset([1, 13])
    FOLLOW_SEP_in_start_1609 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_start_1612 = frozenset([1, 13])
    FOLLOW_CONNECT_in_connect_1623 = frozenset([68])
    FOLLOW_BY_in_connect_1626 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_connect_1629 = frozenset([1, 13])
    FOLLOW_SEP_in_connect_1632 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_connect_1635 = frozenset([1, 13])
    FOLLOW_STOP_in_stop_1646 = frozenset([75])
    FOLLOW_WITH_in_stop_1649 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_stop_1652 = frozenset([1])
    FOLLOW_GROUP_in_group_1661 = frozenset([68])
    FOLLOW_BY_in_group_1664 = frozenset([93])
    FOLLOW_PHRASE_in_group_1669 = frozenset([1, 13])
    FOLLOW_function_in_group_1673 = frozenset([1, 13])
    FOLLOW_SEP_in_group_1678 = frozenset([93])
    FOLLOW_PHRASE_in_group_1683 = frozenset([1, 13])
    FOLLOW_function_in_group_1687 = frozenset([1, 13])
    FOLLOW_HAVING_in_having_1701 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_having_1704 = frozenset([1])
    FOLLOW_ORDER_in_order_1713 = frozenset([68])
    FOLLOW_BY_in_order_1716 = frozenset([93])
    FOLLOW_PHRASE_in_order_1721 = frozenset([13, 76, 77])
    FOLLOW_direction__in_order_1723 = frozenset([1, 13])
    FOLLOW_function_in_order_1727 = frozenset([13, 76, 77])
    FOLLOW_direction__in_order_1729 = frozenset([1, 13])
    FOLLOW_SEP_in_order_1734 = frozenset([93])
    FOLLOW_PHRASE_in_order_1739 = frozenset([13, 76, 77])
    FOLLOW_direction__in_order_1741 = frozenset([1, 13])
    FOLLOW_function_in_order_1745 = frozenset([13, 76, 77])
    FOLLOW_direction__in_order_1747 = frozenset([1, 13])
    FOLLOW_set_in_direction_1762 = frozenset([1])
    FOLLOW_AS_in_as_1778 = frozenset([78, 79, 80, 93])
    FOLLOW_AS_LIST_in_as_1783 = frozenset([1])
    FOLLOW_AS_VALUE_in_as_1787 = frozenset([1])
    FOLLOW_AS_DICT_in_as_1791 = frozenset([1])
    FOLLOW_PHRASE_in_as_1795 = frozenset([1, 98])
    FOLLOW_98_in_as_1798 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98, 99])
    FOLLOW_parameter_in_as_1801 = frozenset([99])
    FOLLOW_99_in_as_1804 = frozenset([1])
    FOLLOW_assign_expr_in_expr1818 = frozenset([1])
    FOLLOW_logic_expr_in_expr1824 = frozenset([1])
    FOLLOW_PHRASE_in_assign_expr1833 = frozenset([29, 46])
    FOLLOW_age_in_assign_expr1836 = frozenset([29])
    FOLLOW_ASSIGN_in_assign_expr1840 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_assign_expr1842 = frozenset([1])
    FOLLOW_logic_or_in_logic_expr1865 = frozenset([1])
    FOLLOW_logic_xor_in_logic_or1874 = frozenset([1, 24])
    FOLLOW_OR_in_logic_or1877 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_xor_in_logic_or1881 = frozenset([1, 24])
    FOLLOW_logic_and_in_logic_xor1891 = frozenset([1, 23])
    FOLLOW_XOR_in_logic_xor1894 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_and_in_logic_xor1897 = frozenset([1, 23])
    FOLLOW_logic_not_in_logic_and1907 = frozenset([1, 19])
    FOLLOW_AND_in_logic_and1910 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_not_in_logic_and1913 = frozenset([1, 19])
    FOLLOW_NOT_in_logic_not1924 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_expr_in_logic_not1929 = frozenset([1])
    FOLLOW_compare_in_in_compare_expr1938 = frozenset([1])
    FOLLOW_compare_eq_in_compare_in1946 = frozenset([1, 28])
    FOLLOW_IN_in_compare_in1949 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_atom_in_compare_in1952 = frozenset([1, 28])
    FOLLOW_compare_ne_in_compare_eq1962 = frozenset([1, 30])
    FOLLOW_EQ_in_compare_eq1965 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_ne_in_compare_eq1968 = frozenset([1, 30])
    FOLLOW_compare_ge_in_compare_ne1978 = frozenset([1, 31])
    FOLLOW_NE_in_compare_ne1981 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_ge_in_compare_ne1984 = frozenset([1, 31])
    FOLLOW_compare_gt_in_compare_ge1994 = frozenset([1, 33])
    FOLLOW_GE_in_compare_ge1997 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_gt_in_compare_ge2000 = frozenset([1, 33])
    FOLLOW_compare_le_in_compare_gt2010 = frozenset([1, 35])
    FOLLOW_GT_in_compare_gt2013 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_le_in_compare_gt2016 = frozenset([1, 35])
    FOLLOW_compare_lt_in_compare_le2026 = frozenset([1, 32])
    FOLLOW_LE_in_compare_le2029 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_lt_in_compare_le2032 = frozenset([1, 32])
    FOLLOW_arithmetic_expr_in_compare_lt2042 = frozenset([1, 34])
    FOLLOW_LT_in_compare_lt2045 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_expr_in_compare_lt2048 = frozenset([1, 34])
    FOLLOW_arithmetic_sub_add_in_arithmetic_expr2059 = frozenset([1])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2067 = frozenset([1, 36, 37])
    FOLLOW_SUB_in_arithmetic_sub_add2071 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_ADD_in_arithmetic_sub_add2074 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add2078 = frozenset([1, 36, 37])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2088 = frozenset([1, 38, 39, 40])
    FOLLOW_MUL_in_arithmetic_mul_div_mod2092 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_DIV_in_arithmetic_mul_div_mod2097 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_MOD_in_arithmetic_mul_div_mod2102 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod2106 = frozenset([1, 38, 39, 40])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2116 = frozenset([1, 41])
    FOLLOW_POW_in_arithmetic_pow2119 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_unary_in_arithmetic_pow2122 = frozenset([1, 41])
    FOLLOW_SUB_in_arithmetic_unary2133 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_atom_in_arithmetic_unary2135 = frozenset([1])
    FOLLOW_ADD_in_arithmetic_unary2149 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_atom_in_arithmetic_unary2151 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2165 = frozenset([1])
    FOLLOW_value_in_atom2176 = frozenset([1])
    FOLLOW_variable_in_atom2181 = frozenset([1])
    FOLLOW_function_in_atom2186 = frozenset([1])
    FOLLOW_98_in_atom2191 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_atom2194 = frozenset([99])
    FOLLOW_99_in_atom2196 = frozenset([1])
    FOLLOW_statement_select_in_atom2202 = frozenset([1])
    FOLLOW_PHRASE_in_function2211 = frozenset([98])
    FOLLOW_98_in_function2213 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98, 99])
    FOLLOW_parameter_in_function2215 = frozenset([99])
    FOLLOW_99_in_function2218 = frozenset([1])
    FOLLOW_expr_in_parameter2238 = frozenset([1, 13])
    FOLLOW_SEP_in_parameter2241 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_parameter2244 = frozenset([1, 13])
    FOLLOW_PHRASE_in_variable2255 = frozenset([1, 46])
    FOLLOW_age_in_variable2258 = frozenset([1])
    FOLLOW_AGE_BEGIN_in_age2282 = frozenset([26, 36, 37, 44, 47, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_age2284 = frozenset([47])
    FOLLOW_AGE_END_in_age2287 = frozenset([1])
    FOLLOW_STRING_in_value2305 = frozenset([1])
    FOLLOW_FLOAT_in_value2319 = frozenset([1])
    FOLLOW_INTEGER_in_value2333 = frozenset([1])
    FOLLOW_TRUE_in_value2346 = frozenset([1])
    FOLLOW_FALSE_in_value2360 = frozenset([1])
    FOLLOW_this__in_value2374 = frozenset([1])
    FOLLOW_list__in_value2379 = frozenset([1])
    FOLLOW_PHRASE_in_this_2390 = frozenset([12])
    FOLLOW_DOT_in_this_2392 = frozenset([70])
    FOLLOW_THIS_in_this_2396 = frozenset([1])
    FOLLOW_LIST_BEGIN_in_list_2417 = frozenset([13, 26, 36, 37, 44, 45, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_list_2421 = frozenset([13, 45])
    FOLLOW_SEP_in_list_2425 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_list_2427 = frozenset([13, 45])
    FOLLOW_LIST_END_in_list_2433 = frozenset([1])
    FOLLOW_statement_select_in_synpred2_SelectExpr1393 = frozenset([14])
    FOLLOW_END_in_synpred2_SelectExpr1395 = frozenset([1])
    FOLLOW_expr_in_synpred3_SelectExpr1401 = frozenset([14])
    FOLLOW_END_in_synpred3_SelectExpr1403 = frozenset([1])
    FOLLOW_where__in_synpred4_SelectExpr1425 = frozenset([1])
    FOLLOW_start__in_synpred6_SelectExpr1431 = frozenset([72, 73])
    FOLLOW_connect__in_synpred6_SelectExpr1435 = frozenset([74])
    FOLLOW_stop__in_synpred6_SelectExpr1437 = frozenset([1])
    FOLLOW_group__in_synpred8_SelectExpr1442 = frozenset([1, 65])
    FOLLOW_having__in_synpred8_SelectExpr1445 = frozenset([1])
    FOLLOW_order__in_synpred9_SelectExpr1452 = frozenset([1])
    FOLLOW_as__in_synpred10_SelectExpr1457 = frozenset([1])
    FOLLOW_SEP_in_synpred17_SelectExpr1574 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_expr_in_synpred17_SelectExpr1577 = frozenset([1])
    FOLLOW_SEP_in_synpred22_SelectExpr1678 = frozenset([93])
    FOLLOW_PHRASE_in_synpred22_SelectExpr1683 = frozenset([1])
    FOLLOW_function_in_synpred22_SelectExpr1687 = frozenset([1])
    FOLLOW_SEP_in_synpred25_SelectExpr1734 = frozenset([93])
    FOLLOW_PHRASE_in_synpred25_SelectExpr1739 = frozenset([76, 77])
    FOLLOW_direction__in_synpred25_SelectExpr1741 = frozenset([1])
    FOLLOW_function_in_synpred25_SelectExpr1745 = frozenset([76, 77])
    FOLLOW_direction__in_synpred25_SelectExpr1747 = frozenset([1])
    FOLLOW_assign_expr_in_synpred33_SelectExpr1818 = frozenset([1])
    FOLLOW_OR_in_synpred35_SelectExpr1877 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_xor_in_synpred35_SelectExpr1881 = frozenset([1])
    FOLLOW_XOR_in_synpred36_SelectExpr1894 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_and_in_synpred36_SelectExpr1897 = frozenset([1])
    FOLLOW_AND_in_synpred37_SelectExpr1910 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_logic_not_in_synpred37_SelectExpr1913 = frozenset([1])
    FOLLOW_IN_in_synpred39_SelectExpr1949 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_atom_in_synpred39_SelectExpr1952 = frozenset([1])
    FOLLOW_EQ_in_synpred40_SelectExpr1965 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_ne_in_synpred40_SelectExpr1968 = frozenset([1])
    FOLLOW_NE_in_synpred41_SelectExpr1981 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_ge_in_synpred41_SelectExpr1984 = frozenset([1])
    FOLLOW_GE_in_synpred42_SelectExpr1997 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_gt_in_synpred42_SelectExpr2000 = frozenset([1])
    FOLLOW_GT_in_synpred43_SelectExpr2013 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_le_in_synpred43_SelectExpr2016 = frozenset([1])
    FOLLOW_LE_in_synpred44_SelectExpr2029 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_compare_lt_in_synpred44_SelectExpr2032 = frozenset([1])
    FOLLOW_LT_in_synpred45_SelectExpr2045 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_expr_in_synpred45_SelectExpr2048 = frozenset([1])
    FOLLOW_set_in_synpred47_SelectExpr2070 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_mul_div_mod_in_synpred47_SelectExpr2078 = frozenset([1])
    FOLLOW_set_in_synpred50_SelectExpr2091 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_pow_in_synpred50_SelectExpr2106 = frozenset([1])
    FOLLOW_POW_in_synpred51_SelectExpr2119 = frozenset([26, 36, 37, 44, 52, 70, 85, 87, 88, 89, 90, 93, 98])
    FOLLOW_arithmetic_unary_in_synpred51_SelectExpr2122 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SelectExprLexer", SelectExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
