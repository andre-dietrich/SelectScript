# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2014-11-06 18:12:00

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

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
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
    # SelectExpr.g:125:1: eval : prog ;
    def eval(self, ):

        retval = self.eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        prog1 = None



        try:
            try:
                # SelectExpr.g:125:6: ( prog )
                # SelectExpr.g:125:8: prog
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_prog_in_eval1314)
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
    # SelectExpr.g:128:1: prog : ( statement )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None



        try:
            try:
                # SelectExpr.g:128:6: ( ( statement )+ )
                # SelectExpr.g:128:8: ( statement )+
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:128:8: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == END or LA1_0 == NOT or (ADD <= LA1_0 <= SUB) or LA1_0 == LIST_BEGIN or LA1_0 == SELECT or LA1_0 == THIS or LA1_0 == STRING or (INTEGER <= LA1_0 <= FALSE) or LA1_0 == PHRASE or LA1_0 == 94) :
                        alt1 = 1


                    if alt1 == 1:
                        # SelectExpr.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_prog1324)
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
    # SelectExpr.g:131:1: statement : ( statement_select END | expr END | END );
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
                # SelectExpr.g:131:11: ( statement_select END | expr END | END )
                alt2 = 3
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # SelectExpr.g:131:13: statement_select END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_statement1334)
                    statement_select3 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select3.tree)
                    END4=self.match(self.input, END, self.FOLLOW_END_in_statement1336)


                elif alt2 == 2:
                    # SelectExpr.g:132:4: expr END
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_statement1342)
                    expr5 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr5.tree)
                    END6=self.match(self.input, END, self.FOLLOW_END_in_statement1344)


                elif alt2 == 3:
                    # SelectExpr.g:133:4: END
                    pass 
                    root_0 = self._adaptor.nil()

                    END7=self.match(self.input, END, self.FOLLOW_END_in_statement1350)


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
    # SelectExpr.g:136:1: statement_select : select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ) ;
    def statement_select(self, ):

        retval = self.statement_select_return()
        retval.start = self.input.LT(1)

        root_0 = None

        select_8 = None

        from_9 = None

        where_10 = None

        group_11 = None

        having_12 = None

        order_13 = None

        as_14 = None


        stream_where_ = RewriteRuleSubtreeStream(self._adaptor, "rule where_")
        stream_select_ = RewriteRuleSubtreeStream(self._adaptor, "rule select_")
        stream_having_ = RewriteRuleSubtreeStream(self._adaptor, "rule having_")
        stream_from_ = RewriteRuleSubtreeStream(self._adaptor, "rule from_")
        stream_as_ = RewriteRuleSubtreeStream(self._adaptor, "rule as_")
        stream_group_ = RewriteRuleSubtreeStream(self._adaptor, "rule group_")
        stream_order_ = RewriteRuleSubtreeStream(self._adaptor, "rule order_")
        try:
            try:
                # SelectExpr.g:136:18: ( select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? ) )
                # SelectExpr.g:137:2: select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )?
                pass 
                self._state.following.append(self.FOLLOW_select__in_statement_select1361)
                select_8 = self.select_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_select_.add(select_8.tree)
                self._state.following.append(self.FOLLOW_from__in_statement_select1363)
                from_9 = self.from_()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_from_.add(from_9.tree)
                # SelectExpr.g:137:16: ( where_ )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == WHERE) :
                    LA3_1 = self.input.LA(2)

                    if (self.synpred4_SelectExpr()) :
                        alt3 = 1
                if alt3 == 1:
                    # SelectExpr.g:137:17: where_
                    pass 
                    self._state.following.append(self.FOLLOW_where__in_statement_select1366)
                    where_10 = self.where_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where_.add(where_10.tree)



                # SelectExpr.g:137:26: ( group_ ( having_ )? )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == GROUP) :
                    LA5_1 = self.input.LA(2)

                    if (self.synpred6_SelectExpr()) :
                        alt5 = 1
                if alt5 == 1:
                    # SelectExpr.g:137:27: group_ ( having_ )?
                    pass 
                    self._state.following.append(self.FOLLOW_group__in_statement_select1371)
                    group_11 = self.group_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_group_.add(group_11.tree)
                    # SelectExpr.g:137:34: ( having_ )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == HAVING) :
                        alt4 = 1
                    if alt4 == 1:
                        # SelectExpr.g:137:35: having_
                        pass 
                        self._state.following.append(self.FOLLOW_having__in_statement_select1374)
                        having_12 = self.having_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_having_.add(having_12.tree)






                # SelectExpr.g:137:47: ( order_ )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ORDER) :
                    LA6_1 = self.input.LA(2)

                    if (self.synpred7_SelectExpr()) :
                        alt6 = 1
                if alt6 == 1:
                    # SelectExpr.g:137:48: order_
                    pass 
                    self._state.following.append(self.FOLLOW_order__in_statement_select1381)
                    order_13 = self.order_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_order_.add(order_13.tree)



                # SelectExpr.g:137:57: ( as_ )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == AS) :
                    LA7_1 = self.input.LA(2)

                    if (self.synpred8_SelectExpr()) :
                        alt7 = 1
                if alt7 == 1:
                    # SelectExpr.g:137:58: as_
                    pass 
                    self._state.following.append(self.FOLLOW_as__in_statement_select1386)
                    as_14 = self.as_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_as_.add(as_14.tree)




                # AST Rewrite
                # elements: order_, where_, having_, from_, group_, as_, select_
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
                    # 137:64: -> ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? )
                    # SelectExpr.g:137:68: ^( STMT_SELECT select_ from_ ( where_ )? ( group_ ( having_ )? )? ( order_ )? ( as_ )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STMT_SELECT, "STMT_SELECT"), root_1)

                    self._adaptor.addChild(root_1, stream_select_.nextTree())
                    self._adaptor.addChild(root_1, stream_from_.nextTree())
                    # SelectExpr.g:137:96: ( where_ )?
                    if stream_where_.hasNext():
                        self._adaptor.addChild(root_1, stream_where_.nextTree())


                    stream_where_.reset();
                    # SelectExpr.g:137:106: ( group_ ( having_ )? )?
                    if stream_having_.hasNext() or stream_group_.hasNext():
                        self._adaptor.addChild(root_1, stream_group_.nextTree())
                        # SelectExpr.g:137:114: ( having_ )?
                        if stream_having_.hasNext():
                            self._adaptor.addChild(root_1, stream_having_.nextTree())


                        stream_having_.reset();


                    stream_having_.reset();
                    stream_group_.reset();
                    # SelectExpr.g:137:127: ( order_ )?
                    if stream_order_.hasNext():
                        self._adaptor.addChild(root_1, stream_order_.nextTree())


                    stream_order_.reset();
                    # SelectExpr.g:137:137: ( as_ )?
                    if stream_as_.hasNext():
                        self._adaptor.addChild(root_1, stream_as_.nextTree())


                    stream_as_.reset();

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
    # SelectExpr.g:140:1: select_ : SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) ;
    def select_(self, ):

        retval = self.select__return()
        retval.start = self.input.LT(1)

        root_0 = None

        SELECT15 = None
        MUL16 = None
        PHRASE17 = None
        SEP20 = None
        PHRASE21 = None
        function18 = None

        this_19 = None

        function22 = None

        this_23 = None


        SELECT15_tree = None
        MUL16_tree = None
        PHRASE17_tree = None
        SEP20_tree = None
        PHRASE21_tree = None

        try:
            try:
                # SelectExpr.g:140:9: ( SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) ) )
                # SelectExpr.g:140:11: SELECT ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                pass 
                root_0 = self._adaptor.nil()

                SELECT15=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_select_1434)
                if self._state.backtracking == 0:

                    SELECT15_tree = self._adaptor.createWithPayload(SELECT15)
                    root_0 = self._adaptor.becomeRoot(SELECT15_tree, root_0)

                # SelectExpr.g:140:19: ( MUL | ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == MUL) :
                    alt11 = 1
                elif (LA11_0 == THIS or LA11_0 == PHRASE) :
                    alt11 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # SelectExpr.g:140:20: MUL
                    pass 
                    MUL16=self.match(self.input, MUL, self.FOLLOW_MUL_in_select_1438)


                elif alt11 == 2:
                    # SelectExpr.g:140:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    pass 
                    # SelectExpr.g:140:27: ( ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )* )
                    # SelectExpr.g:140:28: ( PHRASE | function | this_ ) ( SEP ( PHRASE | function | this_ ) )*
                    pass 
                    # SelectExpr.g:140:28: ( PHRASE | function | this_ )
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == PHRASE) :
                        LA8 = self.input.LA(2)
                        if LA8 == 94:
                            alt8 = 2
                        elif LA8 == DOT:
                            alt8 = 3
                        elif LA8 == SEP or LA8 == FROM:
                            alt8 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 8, 1, self.input)

                            raise nvae

                    elif (LA8_0 == THIS) :
                        alt8 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 8, 0, self.input)

                        raise nvae

                    if alt8 == 1:
                        # SelectExpr.g:140:29: PHRASE
                        pass 
                        PHRASE17=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1445)
                        if self._state.backtracking == 0:

                            PHRASE17_tree = self._adaptor.createWithPayload(PHRASE17)
                            self._adaptor.addChild(root_0, PHRASE17_tree)



                    elif alt8 == 2:
                        # SelectExpr.g:140:38: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_select_1449)
                        function18 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, function18.tree)


                    elif alt8 == 3:
                        # SelectExpr.g:140:49: this_
                        pass 
                        self._state.following.append(self.FOLLOW_this__in_select_1453)
                        this_19 = self.this_()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, this_19.tree)



                    # SelectExpr.g:140:56: ( SEP ( PHRASE | function | this_ ) )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == SEP) :
                            alt10 = 1


                        if alt10 == 1:
                            # SelectExpr.g:140:57: SEP ( PHRASE | function | this_ )
                            pass 
                            SEP20=self.match(self.input, SEP, self.FOLLOW_SEP_in_select_1457)
                            # SelectExpr.g:140:62: ( PHRASE | function | this_ )
                            alt9 = 3
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == PHRASE) :
                                LA9 = self.input.LA(2)
                                if LA9 == 94:
                                    alt9 = 2
                                elif LA9 == DOT:
                                    alt9 = 3
                                elif LA9 == SEP or LA9 == FROM:
                                    alt9 = 1
                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    nvae = NoViableAltException("", 9, 1, self.input)

                                    raise nvae

                            elif (LA9_0 == THIS) :
                                alt9 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 9, 0, self.input)

                                raise nvae

                            if alt9 == 1:
                                # SelectExpr.g:140:63: PHRASE
                                pass 
                                PHRASE21=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_select_1461)
                                if self._state.backtracking == 0:

                                    PHRASE21_tree = self._adaptor.createWithPayload(PHRASE21)
                                    self._adaptor.addChild(root_0, PHRASE21_tree)



                            elif alt9 == 2:
                                # SelectExpr.g:140:72: function
                                pass 
                                self._state.following.append(self.FOLLOW_function_in_select_1465)
                                function22 = self.function()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, function22.tree)


                            elif alt9 == 3:
                                # SelectExpr.g:140:83: this_
                                pass 
                                self._state.following.append(self.FOLLOW_this__in_select_1469)
                                this_23 = self.this_()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, this_23.tree)





                        else:
                            break #loop10









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
    # SelectExpr.g:143:1: from_ : FROM expr ( SEP expr )* ;
    def from_(self, ):

        retval = self.from__return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROM24 = None
        SEP26 = None
        expr25 = None

        expr27 = None


        FROM24_tree = None
        SEP26_tree = None

        try:
            try:
                # SelectExpr.g:143:7: ( FROM expr ( SEP expr )* )
                # SelectExpr.g:143:9: FROM expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                FROM24=self.match(self.input, FROM, self.FOLLOW_FROM_in_from_1485)
                if self._state.backtracking == 0:

                    FROM24_tree = self._adaptor.createWithPayload(FROM24)
                    root_0 = self._adaptor.becomeRoot(FROM24_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_from_1488)
                expr25 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr25.tree)
                # SelectExpr.g:143:20: ( SEP expr )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == SEP) :
                        LA12_2 = self.input.LA(2)

                        if (self.synpred15_SelectExpr()) :
                            alt12 = 1




                    if alt12 == 1:
                        # SelectExpr.g:143:21: SEP expr
                        pass 
                        SEP26=self.match(self.input, SEP, self.FOLLOW_SEP_in_from_1491)
                        self._state.following.append(self.FOLLOW_expr_in_from_1494)
                        expr27 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr27.tree)


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

    # $ANTLR end "from_"

    class where__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.where__return, self).__init__()

            self.tree = None




    # $ANTLR start "where_"
    # SelectExpr.g:146:1: where_ : WHERE expr ;
    def where_(self, ):

        retval = self.where__return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHERE28 = None
        expr29 = None


        WHERE28_tree = None

        try:
            try:
                # SelectExpr.g:146:8: ( WHERE expr )
                # SelectExpr.g:146:10: WHERE expr
                pass 
                root_0 = self._adaptor.nil()

                WHERE28=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where_1505)
                if self._state.backtracking == 0:

                    WHERE28_tree = self._adaptor.createWithPayload(WHERE28)
                    root_0 = self._adaptor.becomeRoot(WHERE28_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_where_1508)
                expr29 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr29.tree)



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

    class group__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.group__return, self).__init__()

            self.tree = None




    # $ANTLR start "group_"
    # SelectExpr.g:149:1: group_ : GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* ;
    def group_(self, ):

        retval = self.group__return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP30 = None
        BY31 = None
        PHRASE32 = None
        SEP34 = None
        PHRASE35 = None
        function33 = None

        function36 = None


        GROUP30_tree = None
        BY31_tree = None
        PHRASE32_tree = None
        SEP34_tree = None
        PHRASE35_tree = None

        try:
            try:
                # SelectExpr.g:149:8: ( GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )* )
                # SelectExpr.g:149:10: GROUP BY ( PHRASE | function ) ( SEP ( PHRASE | function ) )*
                pass 
                root_0 = self._adaptor.nil()

                GROUP30=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_1517)
                if self._state.backtracking == 0:

                    GROUP30_tree = self._adaptor.createWithPayload(GROUP30)
                    root_0 = self._adaptor.becomeRoot(GROUP30_tree, root_0)

                BY31=self.match(self.input, BY, self.FOLLOW_BY_in_group_1520)
                # SelectExpr.g:149:21: ( PHRASE | function )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == PHRASE) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == 94) :
                        alt13 = 2
                    elif (LA13_1 == EOF or (SEP <= LA13_1 <= END) or LA13_1 == AND or (XOR <= LA13_1 <= OR) or LA13_1 == IN or (EQ <= LA13_1 <= POW) or LA13_1 == LIST_END or LA13_1 == AGE_END or (WHERE <= LA13_1 <= ORDER) or LA13_1 == GROUP or LA13_1 == HAVING or LA13_1 == AS or LA13_1 == 95) :
                        alt13 = 1
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
                    # SelectExpr.g:149:23: PHRASE
                    pass 
                    PHRASE32=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1525)
                    if self._state.backtracking == 0:

                        PHRASE32_tree = self._adaptor.createWithPayload(PHRASE32)
                        self._adaptor.addChild(root_0, PHRASE32_tree)



                elif alt13 == 2:
                    # SelectExpr.g:149:32: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_group_1529)
                    function33 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function33.tree)



                # SelectExpr.g:149:43: ( SEP ( PHRASE | function ) )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SEP) :
                        LA15_2 = self.input.LA(2)

                        if (LA15_2 == PHRASE) :
                            LA15_3 = self.input.LA(3)

                            if (self.synpred18_SelectExpr()) :
                                alt15 = 1






                    if alt15 == 1:
                        # SelectExpr.g:149:44: SEP ( PHRASE | function )
                        pass 
                        SEP34=self.match(self.input, SEP, self.FOLLOW_SEP_in_group_1534)
                        # SelectExpr.g:149:49: ( PHRASE | function )
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == PHRASE) :
                            LA14_1 = self.input.LA(2)

                            if (LA14_1 == 94) :
                                alt14 = 2
                            elif (LA14_1 == EOF or (SEP <= LA14_1 <= END) or LA14_1 == AND or (XOR <= LA14_1 <= OR) or LA14_1 == IN or (EQ <= LA14_1 <= POW) or LA14_1 == LIST_END or LA14_1 == AGE_END or (WHERE <= LA14_1 <= ORDER) or LA14_1 == GROUP or LA14_1 == HAVING or LA14_1 == AS or LA14_1 == 95) :
                                alt14 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 14, 1, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 14, 0, self.input)

                            raise nvae

                        if alt14 == 1:
                            # SelectExpr.g:149:51: PHRASE
                            pass 
                            PHRASE35=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_group_1539)
                            if self._state.backtracking == 0:

                                PHRASE35_tree = self._adaptor.createWithPayload(PHRASE35)
                                self._adaptor.addChild(root_0, PHRASE35_tree)



                        elif alt14 == 2:
                            # SelectExpr.g:149:60: function
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_group_1543)
                            function36 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function36.tree)





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

    # $ANTLR end "group_"

    class having__return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.having__return, self).__init__()

            self.tree = None




    # $ANTLR start "having_"
    # SelectExpr.g:152:1: having_ : HAVING expr ;
    def having_(self, ):

        retval = self.having__return()
        retval.start = self.input.LT(1)

        root_0 = None

        HAVING37 = None
        expr38 = None


        HAVING37_tree = None

        try:
            try:
                # SelectExpr.g:152:9: ( HAVING expr )
                # SelectExpr.g:152:11: HAVING expr
                pass 
                root_0 = self._adaptor.nil()

                HAVING37=self.match(self.input, HAVING, self.FOLLOW_HAVING_in_having_1557)
                if self._state.backtracking == 0:

                    HAVING37_tree = self._adaptor.createWithPayload(HAVING37)
                    root_0 = self._adaptor.becomeRoot(HAVING37_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_having_1560)
                expr38 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr38.tree)



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
    # SelectExpr.g:155:1: order_ : ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* ;
    def order_(self, ):

        retval = self.order__return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER39 = None
        BY40 = None
        PHRASE41 = None
        SEP45 = None
        PHRASE46 = None
        direction_42 = None

        function43 = None

        direction_44 = None

        direction_47 = None

        function48 = None

        direction_49 = None


        ORDER39_tree = None
        BY40_tree = None
        PHRASE41_tree = None
        SEP45_tree = None
        PHRASE46_tree = None

        try:
            try:
                # SelectExpr.g:155:8: ( ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )* )
                # SelectExpr.g:155:10: ORDER BY ( PHRASE direction_ | function direction_ ) ( SEP ( PHRASE direction_ | function direction_ ) )*
                pass 
                root_0 = self._adaptor.nil()

                ORDER39=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_1569)
                if self._state.backtracking == 0:

                    ORDER39_tree = self._adaptor.createWithPayload(ORDER39)
                    root_0 = self._adaptor.becomeRoot(ORDER39_tree, root_0)

                BY40=self.match(self.input, BY, self.FOLLOW_BY_in_order_1572)
                # SelectExpr.g:155:21: ( PHRASE direction_ | function direction_ )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == PHRASE) :
                    LA16_1 = self.input.LA(2)

                    if (LA16_1 == 94) :
                        alt16 = 2
                    elif (LA16_1 == EOF or (SEP <= LA16_1 <= END) or LA16_1 == AND or (XOR <= LA16_1 <= OR) or LA16_1 == IN or (EQ <= LA16_1 <= POW) or LA16_1 == LIST_END or LA16_1 == AGE_END or (WHERE <= LA16_1 <= ORDER) or LA16_1 == GROUP or LA16_1 == AS or (ASC <= LA16_1 <= DESC) or LA16_1 == 95) :
                        alt16 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # SelectExpr.g:155:23: PHRASE direction_
                    pass 
                    PHRASE41=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1577)
                    if self._state.backtracking == 0:

                        PHRASE41_tree = self._adaptor.createWithPayload(PHRASE41)
                        self._adaptor.addChild(root_0, PHRASE41_tree)

                    self._state.following.append(self.FOLLOW_direction__in_order_1579)
                    direction_42 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_42.tree)


                elif alt16 == 2:
                    # SelectExpr.g:155:43: function direction_
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_order_1583)
                    function43 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function43.tree)
                    self._state.following.append(self.FOLLOW_direction__in_order_1585)
                    direction_44 = self.direction_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, direction_44.tree)



                # SelectExpr.g:155:65: ( SEP ( PHRASE direction_ | function direction_ ) )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == SEP) :
                        LA18_2 = self.input.LA(2)

                        if (LA18_2 == PHRASE) :
                            LA18_3 = self.input.LA(3)

                            if (self.synpred21_SelectExpr()) :
                                alt18 = 1






                    if alt18 == 1:
                        # SelectExpr.g:155:66: SEP ( PHRASE direction_ | function direction_ )
                        pass 
                        SEP45=self.match(self.input, SEP, self.FOLLOW_SEP_in_order_1590)
                        # SelectExpr.g:155:71: ( PHRASE direction_ | function direction_ )
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == PHRASE) :
                            LA17_1 = self.input.LA(2)

                            if (LA17_1 == 94) :
                                alt17 = 2
                            elif (LA17_1 == EOF or (SEP <= LA17_1 <= END) or LA17_1 == AND or (XOR <= LA17_1 <= OR) or LA17_1 == IN or (EQ <= LA17_1 <= POW) or LA17_1 == LIST_END or LA17_1 == AGE_END or (WHERE <= LA17_1 <= ORDER) or LA17_1 == GROUP or LA17_1 == AS or (ASC <= LA17_1 <= DESC) or LA17_1 == 95) :
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
                            # SelectExpr.g:155:73: PHRASE direction_
                            pass 
                            PHRASE46=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_order_1595)
                            if self._state.backtracking == 0:

                                PHRASE46_tree = self._adaptor.createWithPayload(PHRASE46)
                                self._adaptor.addChild(root_0, PHRASE46_tree)

                            self._state.following.append(self.FOLLOW_direction__in_order_1597)
                            direction_47 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_47.tree)


                        elif alt17 == 2:
                            # SelectExpr.g:155:93: function direction_
                            pass 
                            self._state.following.append(self.FOLLOW_function_in_order_1601)
                            function48 = self.function()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, function48.tree)
                            self._state.following.append(self.FOLLOW_direction__in_order_1603)
                            direction_49 = self.direction_()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, direction_49.tree)





                    else:
                        break #loop18



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
    # SelectExpr.g:158:1: direction_ : ( ASC | DESC )? ;
    def direction_(self, ):

        retval = self.direction__return()
        retval.start = self.input.LT(1)

        root_0 = None

        set50 = None

        set50_tree = None

        try:
            try:
                # SelectExpr.g:158:12: ( ( ASC | DESC )? )
                # SelectExpr.g:158:14: ( ASC | DESC )?
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:158:14: ( ASC | DESC )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((ASC <= LA19_0 <= DESC)) :
                    alt19 = 1
                if alt19 == 1:
                    # SelectExpr.g:
                    pass 
                    set50 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set50))
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
    # SelectExpr.g:161:1: as_ : AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) ;
    def as_(self, ):

        retval = self.as__return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS51 = None
        AS_LIST52 = None
        AS_VALUE53 = None
        AS_DICT54 = None
        PHRASE55 = None
        char_literal56 = None
        char_literal58 = None
        parameter57 = None


        AS51_tree = None
        AS_LIST52_tree = None
        AS_VALUE53_tree = None
        AS_DICT54_tree = None
        PHRASE55_tree = None
        char_literal56_tree = None
        char_literal58_tree = None

        try:
            try:
                # SelectExpr.g:161:5: ( AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? ) )
                # SelectExpr.g:161:7: AS ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                pass 
                root_0 = self._adaptor.nil()

                AS51=self.match(self.input, AS, self.FOLLOW_AS_in_as_1634)
                if self._state.backtracking == 0:

                    AS51_tree = self._adaptor.createWithPayload(AS51)
                    root_0 = self._adaptor.becomeRoot(AS51_tree, root_0)

                # SelectExpr.g:161:11: ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ( '(' ( parameter )? ')' )? )
                alt22 = 4
                LA22 = self.input.LA(1)
                if LA22 == AS_LIST:
                    alt22 = 1
                elif LA22 == AS_VALUE:
                    alt22 = 2
                elif LA22 == AS_DICT:
                    alt22 = 3
                elif LA22 == PHRASE:
                    alt22 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # SelectExpr.g:161:13: AS_LIST
                    pass 
                    AS_LIST52=self.match(self.input, AS_LIST, self.FOLLOW_AS_LIST_in_as_1639)
                    if self._state.backtracking == 0:

                        AS_LIST52_tree = self._adaptor.createWithPayload(AS_LIST52)
                        self._adaptor.addChild(root_0, AS_LIST52_tree)



                elif alt22 == 2:
                    # SelectExpr.g:161:23: AS_VALUE
                    pass 
                    AS_VALUE53=self.match(self.input, AS_VALUE, self.FOLLOW_AS_VALUE_in_as_1643)
                    if self._state.backtracking == 0:

                        AS_VALUE53_tree = self._adaptor.createWithPayload(AS_VALUE53)
                        self._adaptor.addChild(root_0, AS_VALUE53_tree)



                elif alt22 == 3:
                    # SelectExpr.g:161:34: AS_DICT
                    pass 
                    AS_DICT54=self.match(self.input, AS_DICT, self.FOLLOW_AS_DICT_in_as_1647)
                    if self._state.backtracking == 0:

                        AS_DICT54_tree = self._adaptor.createWithPayload(AS_DICT54)
                        self._adaptor.addChild(root_0, AS_DICT54_tree)



                elif alt22 == 4:
                    # SelectExpr.g:161:44: PHRASE ( '(' ( parameter )? ')' )?
                    pass 
                    PHRASE55=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_as_1651)
                    if self._state.backtracking == 0:

                        PHRASE55_tree = self._adaptor.createWithPayload(PHRASE55)
                        self._adaptor.addChild(root_0, PHRASE55_tree)

                    # SelectExpr.g:161:51: ( '(' ( parameter )? ')' )?
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 94) :
                        alt21 = 1
                    if alt21 == 1:
                        # SelectExpr.g:161:52: '(' ( parameter )? ')'
                        pass 
                        char_literal56=self.match(self.input, 94, self.FOLLOW_94_in_as_1654)
                        # SelectExpr.g:161:57: ( parameter )?
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == NOT or (ADD <= LA20_0 <= SUB) or LA20_0 == LIST_BEGIN or LA20_0 == SELECT or LA20_0 == THIS or LA20_0 == STRING or (INTEGER <= LA20_0 <= FALSE) or LA20_0 == PHRASE or LA20_0 == 94) :
                            alt20 = 1
                        if alt20 == 1:
                            # SelectExpr.g:0:0: parameter
                            pass 
                            self._state.following.append(self.FOLLOW_parameter_in_as_1657)
                            parameter57 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter57.tree)



                        char_literal58=self.match(self.input, 95, self.FOLLOW_95_in_as_1660)









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
    # SelectExpr.g:164:1: expr : ( assign_expr | logic_expr );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assign_expr59 = None

        logic_expr60 = None



        try:
            try:
                # SelectExpr.g:164:6: ( assign_expr | logic_expr )
                alt23 = 2
                alt23 = self.dfa23.predict(self.input)
                if alt23 == 1:
                    # SelectExpr.g:164:8: assign_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assign_expr_in_expr1674)
                    assign_expr59 = self.assign_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assign_expr59.tree)


                elif alt23 == 2:
                    # SelectExpr.g:165:4: logic_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_logic_expr_in_expr1680)
                    logic_expr60 = self.logic_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logic_expr60.tree)


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
    # SelectExpr.g:168:1: assign_expr : PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) ;
    def assign_expr(self, ):

        retval = self.assign_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE61 = None
        ASSIGN63 = None
        age62 = None

        expr64 = None


        PHRASE61_tree = None
        ASSIGN63_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:168:13: ( PHRASE ( age )? ASSIGN expr -> ^( ASSIGN PHRASE expr ( age )? ) )
                # SelectExpr.g:168:15: PHRASE ( age )? ASSIGN expr
                pass 
                PHRASE61=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_assign_expr1689) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE61)
                # SelectExpr.g:168:22: ( age )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == AGE_BEGIN) :
                    alt24 = 1
                if alt24 == 1:
                    # SelectExpr.g:168:23: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_assign_expr1692)
                    age62 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age62.tree)



                ASSIGN63=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assign_expr1696) 
                if self._state.backtracking == 0:
                    stream_ASSIGN.add(ASSIGN63)
                self._state.following.append(self.FOLLOW_expr_in_assign_expr1698)
                expr64 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr64.tree)

                # AST Rewrite
                # elements: ASSIGN, age, PHRASE, expr
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
                    # 168:41: -> ^( ASSIGN PHRASE expr ( age )? )
                    # SelectExpr.g:168:44: ^( ASSIGN PHRASE expr ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # SelectExpr.g:168:65: ( age )?
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
    # SelectExpr.g:170:1: logic_expr : logic_or ;
    def logic_expr(self, ):

        retval = self.logic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        logic_or65 = None



        try:
            try:
                # SelectExpr.g:170:12: ( logic_or )
                # SelectExpr.g:170:14: logic_or
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_or_in_logic_expr1721)
                logic_or65 = self.logic_or()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_or65.tree)



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
    # SelectExpr.g:171:1: logic_or : logic_xor ( OR logic_xor )* ;
    def logic_or(self, ):

        retval = self.logic_or_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR67 = None
        logic_xor66 = None

        logic_xor68 = None


        OR67_tree = None

        try:
            try:
                # SelectExpr.g:171:11: ( logic_xor ( OR logic_xor )* )
                # SelectExpr.g:171:13: logic_xor ( OR logic_xor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_xor_in_logic_or1730)
                logic_xor66 = self.logic_xor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_xor66.tree)
                # SelectExpr.g:171:23: ( OR logic_xor )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == OR) :
                        LA25_2 = self.input.LA(2)

                        if (self.synpred31_SelectExpr()) :
                            alt25 = 1




                    if alt25 == 1:
                        # SelectExpr.g:171:24: OR logic_xor
                        pass 
                        OR67=self.match(self.input, OR, self.FOLLOW_OR_in_logic_or1733)
                        if self._state.backtracking == 0:

                            OR67_tree = self._adaptor.createWithPayload(OR67)
                            root_0 = self._adaptor.becomeRoot(OR67_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_xor_in_logic_or1737)
                        logic_xor68 = self.logic_xor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_xor68.tree)


                    else:
                        break #loop25



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
    # SelectExpr.g:172:1: logic_xor : logic_and ( XOR logic_and )* ;
    def logic_xor(self, ):

        retval = self.logic_xor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        XOR70 = None
        logic_and69 = None

        logic_and71 = None


        XOR70_tree = None

        try:
            try:
                # SelectExpr.g:172:11: ( logic_and ( XOR logic_and )* )
                # SelectExpr.g:172:13: logic_and ( XOR logic_and )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_and_in_logic_xor1747)
                logic_and69 = self.logic_and()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_and69.tree)
                # SelectExpr.g:172:23: ( XOR logic_and )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == XOR) :
                        LA26_2 = self.input.LA(2)

                        if (self.synpred32_SelectExpr()) :
                            alt26 = 1




                    if alt26 == 1:
                        # SelectExpr.g:172:24: XOR logic_and
                        pass 
                        XOR70=self.match(self.input, XOR, self.FOLLOW_XOR_in_logic_xor1750)
                        if self._state.backtracking == 0:

                            XOR70_tree = self._adaptor.createWithPayload(XOR70)
                            root_0 = self._adaptor.becomeRoot(XOR70_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_and_in_logic_xor1753)
                        logic_and71 = self.logic_and()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_and71.tree)


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

    # $ANTLR end "logic_xor"

    class logic_and_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_and_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_and"
    # SelectExpr.g:173:1: logic_and : logic_not ( AND logic_not )* ;
    def logic_and(self, ):

        retval = self.logic_and_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND73 = None
        logic_not72 = None

        logic_not74 = None


        AND73_tree = None

        try:
            try:
                # SelectExpr.g:173:11: ( logic_not ( AND logic_not )* )
                # SelectExpr.g:173:13: logic_not ( AND logic_not )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logic_not_in_logic_and1763)
                logic_not72 = self.logic_not()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logic_not72.tree)
                # SelectExpr.g:173:23: ( AND logic_not )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == AND) :
                        LA27_2 = self.input.LA(2)

                        if (self.synpred33_SelectExpr()) :
                            alt27 = 1




                    if alt27 == 1:
                        # SelectExpr.g:173:24: AND logic_not
                        pass 
                        AND73=self.match(self.input, AND, self.FOLLOW_AND_in_logic_and1766)
                        if self._state.backtracking == 0:

                            AND73_tree = self._adaptor.createWithPayload(AND73)
                            root_0 = self._adaptor.becomeRoot(AND73_tree, root_0)

                        self._state.following.append(self.FOLLOW_logic_not_in_logic_and1769)
                        logic_not74 = self.logic_not()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logic_not74.tree)


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

    # $ANTLR end "logic_and"

    class logic_not_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.logic_not_return, self).__init__()

            self.tree = None




    # $ANTLR start "logic_not"
    # SelectExpr.g:174:1: logic_not : ( NOT )? compare_expr ;
    def logic_not(self, ):

        retval = self.logic_not_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT75 = None
        compare_expr76 = None


        NOT75_tree = None

        try:
            try:
                # SelectExpr.g:174:11: ( ( NOT )? compare_expr )
                # SelectExpr.g:174:13: ( NOT )? compare_expr
                pass 
                root_0 = self._adaptor.nil()

                # SelectExpr.g:174:13: ( NOT )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == NOT) :
                    alt28 = 1
                if alt28 == 1:
                    # SelectExpr.g:174:14: NOT
                    pass 
                    NOT75=self.match(self.input, NOT, self.FOLLOW_NOT_in_logic_not1780)
                    if self._state.backtracking == 0:

                        NOT75_tree = self._adaptor.createWithPayload(NOT75)
                        root_0 = self._adaptor.becomeRoot(NOT75_tree, root_0)




                self._state.following.append(self.FOLLOW_compare_expr_in_logic_not1785)
                compare_expr76 = self.compare_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_expr76.tree)



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
    # SelectExpr.g:176:1: compare_expr : compare_in ;
    def compare_expr(self, ):

        retval = self.compare_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        compare_in77 = None



        try:
            try:
                # SelectExpr.g:176:14: ( compare_in )
                # SelectExpr.g:176:16: compare_in
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_in_in_compare_expr1794)
                compare_in77 = self.compare_in()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_in77.tree)



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
    # SelectExpr.g:177:1: compare_in : compare_eq ( IN atom )* ;
    def compare_in(self, ):

        retval = self.compare_in_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IN79 = None
        compare_eq78 = None

        atom80 = None


        IN79_tree = None

        try:
            try:
                # SelectExpr.g:177:12: ( compare_eq ( IN atom )* )
                # SelectExpr.g:177:14: compare_eq ( IN atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_eq_in_compare_in1802)
                compare_eq78 = self.compare_eq()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_eq78.tree)
                # SelectExpr.g:177:25: ( IN atom )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IN) :
                        LA29_2 = self.input.LA(2)

                        if (self.synpred35_SelectExpr()) :
                            alt29 = 1




                    if alt29 == 1:
                        # SelectExpr.g:177:26: IN atom
                        pass 
                        IN79=self.match(self.input, IN, self.FOLLOW_IN_in_compare_in1805)
                        if self._state.backtracking == 0:

                            IN79_tree = self._adaptor.createWithPayload(IN79)
                            root_0 = self._adaptor.becomeRoot(IN79_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_compare_in1808)
                        atom80 = self.atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, atom80.tree)


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

    # $ANTLR end "compare_in"

    class compare_eq_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_eq_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_eq"
    # SelectExpr.g:178:1: compare_eq : compare_ne ( EQ compare_ne )* ;
    def compare_eq(self, ):

        retval = self.compare_eq_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQ82 = None
        compare_ne81 = None

        compare_ne83 = None


        EQ82_tree = None

        try:
            try:
                # SelectExpr.g:178:12: ( compare_ne ( EQ compare_ne )* )
                # SelectExpr.g:178:14: compare_ne ( EQ compare_ne )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq1818)
                compare_ne81 = self.compare_ne()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ne81.tree)
                # SelectExpr.g:178:25: ( EQ compare_ne )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == EQ) :
                        LA30_2 = self.input.LA(2)

                        if (self.synpred36_SelectExpr()) :
                            alt30 = 1




                    if alt30 == 1:
                        # SelectExpr.g:178:26: EQ compare_ne
                        pass 
                        EQ82=self.match(self.input, EQ, self.FOLLOW_EQ_in_compare_eq1821)
                        if self._state.backtracking == 0:

                            EQ82_tree = self._adaptor.createWithPayload(EQ82)
                            root_0 = self._adaptor.becomeRoot(EQ82_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ne_in_compare_eq1824)
                        compare_ne83 = self.compare_ne()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ne83.tree)


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

    # $ANTLR end "compare_eq"

    class compare_ne_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ne_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ne"
    # SelectExpr.g:179:1: compare_ne : compare_ge ( NE compare_ge )* ;
    def compare_ne(self, ):

        retval = self.compare_ne_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NE85 = None
        compare_ge84 = None

        compare_ge86 = None


        NE85_tree = None

        try:
            try:
                # SelectExpr.g:179:12: ( compare_ge ( NE compare_ge )* )
                # SelectExpr.g:179:14: compare_ge ( NE compare_ge )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne1834)
                compare_ge84 = self.compare_ge()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_ge84.tree)
                # SelectExpr.g:179:25: ( NE compare_ge )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == NE) :
                        LA31_2 = self.input.LA(2)

                        if (self.synpred37_SelectExpr()) :
                            alt31 = 1




                    if alt31 == 1:
                        # SelectExpr.g:179:26: NE compare_ge
                        pass 
                        NE85=self.match(self.input, NE, self.FOLLOW_NE_in_compare_ne1837)
                        if self._state.backtracking == 0:

                            NE85_tree = self._adaptor.createWithPayload(NE85)
                            root_0 = self._adaptor.becomeRoot(NE85_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_ge_in_compare_ne1840)
                        compare_ge86 = self.compare_ge()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_ge86.tree)


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

    # $ANTLR end "compare_ne"

    class compare_ge_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_ge_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_ge"
    # SelectExpr.g:180:1: compare_ge : compare_gt ( GE compare_gt )* ;
    def compare_ge(self, ):

        retval = self.compare_ge_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GE88 = None
        compare_gt87 = None

        compare_gt89 = None


        GE88_tree = None

        try:
            try:
                # SelectExpr.g:180:12: ( compare_gt ( GE compare_gt )* )
                # SelectExpr.g:180:14: compare_gt ( GE compare_gt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge1850)
                compare_gt87 = self.compare_gt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_gt87.tree)
                # SelectExpr.g:180:25: ( GE compare_gt )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == GE) :
                        LA32_2 = self.input.LA(2)

                        if (self.synpred38_SelectExpr()) :
                            alt32 = 1




                    if alt32 == 1:
                        # SelectExpr.g:180:26: GE compare_gt
                        pass 
                        GE88=self.match(self.input, GE, self.FOLLOW_GE_in_compare_ge1853)
                        if self._state.backtracking == 0:

                            GE88_tree = self._adaptor.createWithPayload(GE88)
                            root_0 = self._adaptor.becomeRoot(GE88_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_gt_in_compare_ge1856)
                        compare_gt89 = self.compare_gt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_gt89.tree)


                    else:
                        break #loop32



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
    # SelectExpr.g:181:1: compare_gt : compare_le ( GT compare_le )* ;
    def compare_gt(self, ):

        retval = self.compare_gt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GT91 = None
        compare_le90 = None

        compare_le92 = None


        GT91_tree = None

        try:
            try:
                # SelectExpr.g:181:12: ( compare_le ( GT compare_le )* )
                # SelectExpr.g:181:14: compare_le ( GT compare_le )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_le_in_compare_gt1866)
                compare_le90 = self.compare_le()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_le90.tree)
                # SelectExpr.g:181:25: ( GT compare_le )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == GT) :
                        LA33_2 = self.input.LA(2)

                        if (self.synpred39_SelectExpr()) :
                            alt33 = 1




                    if alt33 == 1:
                        # SelectExpr.g:181:26: GT compare_le
                        pass 
                        GT91=self.match(self.input, GT, self.FOLLOW_GT_in_compare_gt1869)
                        if self._state.backtracking == 0:

                            GT91_tree = self._adaptor.createWithPayload(GT91)
                            root_0 = self._adaptor.becomeRoot(GT91_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_le_in_compare_gt1872)
                        compare_le92 = self.compare_le()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_le92.tree)


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

    # $ANTLR end "compare_gt"

    class compare_le_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_le_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_le"
    # SelectExpr.g:182:1: compare_le : compare_lt ( LE compare_lt )* ;
    def compare_le(self, ):

        retval = self.compare_le_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LE94 = None
        compare_lt93 = None

        compare_lt95 = None


        LE94_tree = None

        try:
            try:
                # SelectExpr.g:182:12: ( compare_lt ( LE compare_lt )* )
                # SelectExpr.g:182:14: compare_lt ( LE compare_lt )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_compare_lt_in_compare_le1882)
                compare_lt93 = self.compare_lt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, compare_lt93.tree)
                # SelectExpr.g:182:25: ( LE compare_lt )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == LE) :
                        LA34_2 = self.input.LA(2)

                        if (self.synpred40_SelectExpr()) :
                            alt34 = 1




                    if alt34 == 1:
                        # SelectExpr.g:182:26: LE compare_lt
                        pass 
                        LE94=self.match(self.input, LE, self.FOLLOW_LE_in_compare_le1885)
                        if self._state.backtracking == 0:

                            LE94_tree = self._adaptor.createWithPayload(LE94)
                            root_0 = self._adaptor.becomeRoot(LE94_tree, root_0)

                        self._state.following.append(self.FOLLOW_compare_lt_in_compare_le1888)
                        compare_lt95 = self.compare_lt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, compare_lt95.tree)


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

    # $ANTLR end "compare_le"

    class compare_lt_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.compare_lt_return, self).__init__()

            self.tree = None




    # $ANTLR start "compare_lt"
    # SelectExpr.g:183:1: compare_lt : arithmetic_expr ( LT arithmetic_expr )* ;
    def compare_lt(self, ):

        retval = self.compare_lt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LT97 = None
        arithmetic_expr96 = None

        arithmetic_expr98 = None


        LT97_tree = None

        try:
            try:
                # SelectExpr.g:183:12: ( arithmetic_expr ( LT arithmetic_expr )* )
                # SelectExpr.g:183:14: arithmetic_expr ( LT arithmetic_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt1898)
                arithmetic_expr96 = self.arithmetic_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_expr96.tree)
                # SelectExpr.g:183:30: ( LT arithmetic_expr )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == LT) :
                        LA35_2 = self.input.LA(2)

                        if (self.synpred41_SelectExpr()) :
                            alt35 = 1




                    if alt35 == 1:
                        # SelectExpr.g:183:31: LT arithmetic_expr
                        pass 
                        LT97=self.match(self.input, LT, self.FOLLOW_LT_in_compare_lt1901)
                        if self._state.backtracking == 0:

                            LT97_tree = self._adaptor.createWithPayload(LT97)
                            root_0 = self._adaptor.becomeRoot(LT97_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_expr_in_compare_lt1904)
                        arithmetic_expr98 = self.arithmetic_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_expr98.tree)


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

    # $ANTLR end "compare_lt"

    class arithmetic_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_expr"
    # SelectExpr.g:185:1: arithmetic_expr : arithmetic_sub_add ;
    def arithmetic_expr(self, ):

        retval = self.arithmetic_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        arithmetic_sub_add99 = None



        try:
            try:
                # SelectExpr.g:185:17: ( arithmetic_sub_add )
                # SelectExpr.g:185:19: arithmetic_sub_add
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_sub_add_in_arithmetic_expr1915)
                arithmetic_sub_add99 = self.arithmetic_sub_add()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_sub_add99.tree)



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
    # SelectExpr.g:186:1: arithmetic_sub_add : arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* ;
    def arithmetic_sub_add(self, ):

        retval = self.arithmetic_sub_add_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB101 = None
        ADD102 = None
        arithmetic_mul_div_mod100 = None

        arithmetic_mul_div_mod103 = None


        SUB101_tree = None
        ADD102_tree = None

        try:
            try:
                # SelectExpr.g:186:20: ( arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )* )
                # SelectExpr.g:186:22: arithmetic_mul_div_mod ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add1923)
                arithmetic_mul_div_mod100 = self.arithmetic_mul_div_mod()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_mul_div_mod100.tree)
                # SelectExpr.g:186:45: ( ( SUB | ADD ) arithmetic_mul_div_mod )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == SUB) :
                        LA37_2 = self.input.LA(2)

                        if (self.synpred43_SelectExpr()) :
                            alt37 = 1


                    elif (LA37_0 == ADD) :
                        LA37_3 = self.input.LA(2)

                        if (self.synpred43_SelectExpr()) :
                            alt37 = 1




                    if alt37 == 1:
                        # SelectExpr.g:186:46: ( SUB | ADD ) arithmetic_mul_div_mod
                        pass 
                        # SelectExpr.g:186:46: ( SUB | ADD )
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == SUB) :
                            alt36 = 1
                        elif (LA36_0 == ADD) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 36, 0, self.input)

                            raise nvae

                        if alt36 == 1:
                            # SelectExpr.g:186:47: SUB
                            pass 
                            SUB101=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_sub_add1927)
                            if self._state.backtracking == 0:

                                SUB101_tree = self._adaptor.createWithPayload(SUB101)
                                root_0 = self._adaptor.becomeRoot(SUB101_tree, root_0)



                        elif alt36 == 2:
                            # SelectExpr.g:186:52: ADD
                            pass 
                            ADD102=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_sub_add1930)
                            if self._state.backtracking == 0:

                                ADD102_tree = self._adaptor.createWithPayload(ADD102)
                                root_0 = self._adaptor.becomeRoot(ADD102_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add1934)
                        arithmetic_mul_div_mod103 = self.arithmetic_mul_div_mod()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_mul_div_mod103.tree)


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

    # $ANTLR end "arithmetic_sub_add"

    class arithmetic_mul_div_mod_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_mul_div_mod_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_mul_div_mod"
    # SelectExpr.g:187:1: arithmetic_mul_div_mod : arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* ;
    def arithmetic_mul_div_mod(self, ):

        retval = self.arithmetic_mul_div_mod_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MUL105 = None
        DIV106 = None
        MOD107 = None
        arithmetic_pow104 = None

        arithmetic_pow108 = None


        MUL105_tree = None
        DIV106_tree = None
        MOD107_tree = None

        try:
            try:
                # SelectExpr.g:187:24: ( arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )* )
                # SelectExpr.g:187:26: arithmetic_pow ( ( MUL | DIV | MOD ) arithmetic_pow )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod1944)
                arithmetic_pow104 = self.arithmetic_pow()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_pow104.tree)
                # SelectExpr.g:187:41: ( ( MUL | DIV | MOD ) arithmetic_pow )*
                while True: #loop39
                    alt39 = 2
                    LA39 = self.input.LA(1)
                    if LA39 == MUL:
                        LA39_2 = self.input.LA(2)

                        if (self.synpred46_SelectExpr()) :
                            alt39 = 1


                    elif LA39 == DIV:
                        LA39_3 = self.input.LA(2)

                        if (self.synpred46_SelectExpr()) :
                            alt39 = 1


                    elif LA39 == MOD:
                        LA39_4 = self.input.LA(2)

                        if (self.synpred46_SelectExpr()) :
                            alt39 = 1



                    if alt39 == 1:
                        # SelectExpr.g:187:42: ( MUL | DIV | MOD ) arithmetic_pow
                        pass 
                        # SelectExpr.g:187:42: ( MUL | DIV | MOD )
                        alt38 = 3
                        LA38 = self.input.LA(1)
                        if LA38 == MUL:
                            alt38 = 1
                        elif LA38 == DIV:
                            alt38 = 2
                        elif LA38 == MOD:
                            alt38 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 38, 0, self.input)

                            raise nvae

                        if alt38 == 1:
                            # SelectExpr.g:187:43: MUL
                            pass 
                            MUL105=self.match(self.input, MUL, self.FOLLOW_MUL_in_arithmetic_mul_div_mod1948)
                            if self._state.backtracking == 0:

                                MUL105_tree = self._adaptor.createWithPayload(MUL105)
                                root_0 = self._adaptor.becomeRoot(MUL105_tree, root_0)



                        elif alt38 == 2:
                            # SelectExpr.g:187:50: DIV
                            pass 
                            DIV106=self.match(self.input, DIV, self.FOLLOW_DIV_in_arithmetic_mul_div_mod1953)
                            if self._state.backtracking == 0:

                                DIV106_tree = self._adaptor.createWithPayload(DIV106)
                                root_0 = self._adaptor.becomeRoot(DIV106_tree, root_0)



                        elif alt38 == 3:
                            # SelectExpr.g:187:57: MOD
                            pass 
                            MOD107=self.match(self.input, MOD, self.FOLLOW_MOD_in_arithmetic_mul_div_mod1958)
                            if self._state.backtracking == 0:

                                MOD107_tree = self._adaptor.createWithPayload(MOD107)
                                root_0 = self._adaptor.becomeRoot(MOD107_tree, root_0)




                        self._state.following.append(self.FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod1962)
                        arithmetic_pow108 = self.arithmetic_pow()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_pow108.tree)


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

    # $ANTLR end "arithmetic_mul_div_mod"

    class arithmetic_pow_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_pow_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_pow"
    # SelectExpr.g:188:1: arithmetic_pow : arithmetic_unary ( POW arithmetic_unary )* ;
    def arithmetic_pow(self, ):

        retval = self.arithmetic_pow_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POW110 = None
        arithmetic_unary109 = None

        arithmetic_unary111 = None


        POW110_tree = None

        try:
            try:
                # SelectExpr.g:188:16: ( arithmetic_unary ( POW arithmetic_unary )* )
                # SelectExpr.g:188:18: arithmetic_unary ( POW arithmetic_unary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow1972)
                arithmetic_unary109 = self.arithmetic_unary()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arithmetic_unary109.tree)
                # SelectExpr.g:188:35: ( POW arithmetic_unary )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == POW) :
                        LA40_2 = self.input.LA(2)

                        if (self.synpred47_SelectExpr()) :
                            alt40 = 1




                    if alt40 == 1:
                        # SelectExpr.g:188:36: POW arithmetic_unary
                        pass 
                        POW110=self.match(self.input, POW, self.FOLLOW_POW_in_arithmetic_pow1975)
                        if self._state.backtracking == 0:

                            POW110_tree = self._adaptor.createWithPayload(POW110)
                            root_0 = self._adaptor.becomeRoot(POW110_tree, root_0)

                        self._state.following.append(self.FOLLOW_arithmetic_unary_in_arithmetic_pow1978)
                        arithmetic_unary111 = self.arithmetic_unary()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arithmetic_unary111.tree)


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

    # $ANTLR end "arithmetic_pow"

    class arithmetic_unary_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.arithmetic_unary_return, self).__init__()

            self.tree = None




    # $ANTLR start "arithmetic_unary"
    # SelectExpr.g:189:1: arithmetic_unary : ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom );
    def arithmetic_unary(self, ):

        retval = self.arithmetic_unary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUB112 = None
        ADD114 = None
        atom113 = None

        atom115 = None

        atom116 = None


        SUB112_tree = None
        ADD114_tree = None
        stream_SUB = RewriteRuleTokenStream(self._adaptor, "token SUB")
        stream_ADD = RewriteRuleTokenStream(self._adaptor, "token ADD")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # SelectExpr.g:189:18: ( SUB atom -> ^( NEG atom ) | ADD atom -> ^( POS atom ) | atom )
                alt41 = 3
                LA41 = self.input.LA(1)
                if LA41 == SUB:
                    alt41 = 1
                elif LA41 == ADD:
                    alt41 = 2
                elif LA41 == LIST_BEGIN or LA41 == SELECT or LA41 == THIS or LA41 == STRING or LA41 == INTEGER or LA41 == FLOAT or LA41 == TRUE or LA41 == FALSE or LA41 == PHRASE or LA41 == 94:
                    alt41 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # SelectExpr.g:190:2: SUB atom
                    pass 
                    SUB112=self.match(self.input, SUB, self.FOLLOW_SUB_in_arithmetic_unary1989) 
                    if self._state.backtracking == 0:
                        stream_SUB.add(SUB112)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary1991)
                    atom113 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom113.tree)

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
                        # 190:11: -> ^( NEG atom )
                        # SelectExpr.g:190:14: ^( NEG atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEG, "NEG"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt41 == 2:
                    # SelectExpr.g:191:5: ADD atom
                    pass 
                    ADD114=self.match(self.input, ADD, self.FOLLOW_ADD_in_arithmetic_unary2005) 
                    if self._state.backtracking == 0:
                        stream_ADD.add(ADD114)
                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2007)
                    atom115 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atom.add(atom115.tree)

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
                        # 191:14: -> ^( POS atom )
                        # SelectExpr.g:191:17: ^( POS atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(POS, "POS"), root_1)

                        self._adaptor.addChild(root_1, stream_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt41 == 3:
                    # SelectExpr.g:192:5: atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atom_in_arithmetic_unary2021)
                    atom116 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom116.tree)


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
    # SelectExpr.g:195:1: atom : ( value | variable | function | '(' expr ')' | statement_select );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal120 = None
        char_literal122 = None
        value117 = None

        variable118 = None

        function119 = None

        expr121 = None

        statement_select123 = None


        char_literal120_tree = None
        char_literal122_tree = None

        try:
            try:
                # SelectExpr.g:196:2: ( value | variable | function | '(' expr ')' | statement_select )
                alt42 = 5
                LA42 = self.input.LA(1)
                if LA42 == LIST_BEGIN or LA42 == THIS or LA42 == STRING or LA42 == INTEGER or LA42 == FLOAT or LA42 == TRUE or LA42 == FALSE:
                    alt42 = 1
                elif LA42 == PHRASE:
                    LA42 = self.input.LA(2)
                    if LA42 == DOT:
                        alt42 = 1
                    elif LA42 == 94:
                        alt42 = 3
                    elif LA42 == EOF or LA42 == SEP or LA42 == END or LA42 == AND or LA42 == XOR or LA42 == OR or LA42 == IN or LA42 == EQ or LA42 == NE or LA42 == LE or LA42 == GE or LA42 == LT or LA42 == GT or LA42 == ADD or LA42 == SUB or LA42 == MUL or LA42 == DIV or LA42 == MOD or LA42 == POW or LA42 == LIST_END or LA42 == AGE_BEGIN or LA42 == AGE_END or LA42 == WHERE or LA42 == ORDER or LA42 == GROUP or LA42 == AS or LA42 == 95:
                        alt42 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 42, 2, self.input)

                        raise nvae

                elif LA42 == 94:
                    alt42 = 4
                elif LA42 == SELECT:
                    alt42 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # SelectExpr.g:196:4: value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_value_in_atom2032)
                    value117 = self.value()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, value117.tree)


                elif alt42 == 2:
                    # SelectExpr.g:197:4: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_atom2037)
                    variable118 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable118.tree)


                elif alt42 == 3:
                    # SelectExpr.g:198:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_atom2042)
                    function119 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function119.tree)


                elif alt42 == 4:
                    # SelectExpr.g:199:4: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal120=self.match(self.input, 94, self.FOLLOW_94_in_atom2047)
                    self._state.following.append(self.FOLLOW_expr_in_atom2050)
                    expr121 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr121.tree)
                    char_literal122=self.match(self.input, 95, self.FOLLOW_95_in_atom2052)


                elif alt42 == 5:
                    # SelectExpr.g:200:4: statement_select
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_select_in_atom2058)
                    statement_select123 = self.statement_select()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement_select123.tree)


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
    # SelectExpr.g:203:1: function : PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE124 = None
        char_literal125 = None
        char_literal127 = None
        parameter126 = None


        PHRASE124_tree = None
        char_literal125_tree = None
        char_literal127_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # SelectExpr.g:203:10: ( PHRASE '(' ( parameter )? ')' -> ^( FCT PHRASE ( parameter )? ) )
                # SelectExpr.g:203:12: PHRASE '(' ( parameter )? ')'
                pass 
                PHRASE124=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_function2067) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE124)
                char_literal125=self.match(self.input, 94, self.FOLLOW_94_in_function2069) 
                if self._state.backtracking == 0:
                    stream_94.add(char_literal125)
                # SelectExpr.g:203:23: ( parameter )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == NOT or (ADD <= LA43_0 <= SUB) or LA43_0 == LIST_BEGIN or LA43_0 == SELECT or LA43_0 == THIS or LA43_0 == STRING or (INTEGER <= LA43_0 <= FALSE) or LA43_0 == PHRASE or LA43_0 == 94) :
                    alt43 = 1
                if alt43 == 1:
                    # SelectExpr.g:0:0: parameter
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_function2071)
                    parameter126 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter126.tree)



                char_literal127=self.match(self.input, 95, self.FOLLOW_95_in_function2074) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal127)

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
                    # 203:38: -> ^( FCT PHRASE ( parameter )? )
                    # SelectExpr.g:203:41: ^( FCT PHRASE ( parameter )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FCT, "FCT"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:203:54: ( parameter )?
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
    # SelectExpr.g:206:1: parameter : expr ( SEP expr )* ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEP129 = None
        expr128 = None

        expr130 = None


        SEP129_tree = None

        try:
            try:
                # SelectExpr.g:206:11: ( expr ( SEP expr )* )
                # SelectExpr.g:206:13: expr ( SEP expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_parameter2094)
                expr128 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr128.tree)
                # SelectExpr.g:206:18: ( SEP expr )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == SEP) :
                        alt44 = 1


                    if alt44 == 1:
                        # SelectExpr.g:206:19: SEP expr
                        pass 
                        SEP129=self.match(self.input, SEP, self.FOLLOW_SEP_in_parameter2097)
                        self._state.following.append(self.FOLLOW_expr_in_parameter2100)
                        expr130 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr130.tree)


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

    # $ANTLR end "parameter"

    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            super(SelectExprParser.variable_return, self).__init__()

            self.tree = None




    # $ANTLR start "variable"
    # SelectExpr.g:209:1: variable : PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) ;
    def variable(self, ):

        retval = self.variable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE131 = None
        age132 = None


        PHRASE131_tree = None
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_age = RewriteRuleSubtreeStream(self._adaptor, "rule age")
        try:
            try:
                # SelectExpr.g:209:10: ( PHRASE ( age )? -> ^( VAR PHRASE ( age )? ) )
                # SelectExpr.g:209:12: PHRASE ( age )?
                pass 
                PHRASE131=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_variable2111) 
                if self._state.backtracking == 0:
                    stream_PHRASE.add(PHRASE131)
                # SelectExpr.g:209:19: ( age )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == AGE_BEGIN) :
                    alt45 = 1
                if alt45 == 1:
                    # SelectExpr.g:209:20: age
                    pass 
                    self._state.following.append(self.FOLLOW_age_in_variable2114)
                    age132 = self.age()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_age.add(age132.tree)




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
                    # 209:26: -> ^( VAR PHRASE ( age )? )
                    # SelectExpr.g:209:29: ^( VAR PHRASE ( age )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                    self._adaptor.addChild(root_1, stream_PHRASE.nextNode())
                    # SelectExpr.g:209:42: ( age )?
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
    # SelectExpr.g:212:1: age : AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) ;
    def age(self, ):

        retval = self.age_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AGE_BEGIN133 = None
        AGE_END135 = None
        expr134 = None


        AGE_BEGIN133_tree = None
        AGE_END135_tree = None
        stream_AGE_BEGIN = RewriteRuleTokenStream(self._adaptor, "token AGE_BEGIN")
        stream_AGE_END = RewriteRuleTokenStream(self._adaptor, "token AGE_END")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:212:5: ( AGE_BEGIN ( expr )? AGE_END -> ^( AGE ( expr )? ) )
                # SelectExpr.g:212:7: AGE_BEGIN ( expr )? AGE_END
                pass 
                AGE_BEGIN133=self.match(self.input, AGE_BEGIN, self.FOLLOW_AGE_BEGIN_in_age2138) 
                if self._state.backtracking == 0:
                    stream_AGE_BEGIN.add(AGE_BEGIN133)
                # SelectExpr.g:212:17: ( expr )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == NOT or (ADD <= LA46_0 <= SUB) or LA46_0 == LIST_BEGIN or LA46_0 == SELECT or LA46_0 == THIS or LA46_0 == STRING or (INTEGER <= LA46_0 <= FALSE) or LA46_0 == PHRASE or LA46_0 == 94) :
                    alt46 = 1
                if alt46 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_age2140)
                    expr134 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr134.tree)



                AGE_END135=self.match(self.input, AGE_END, self.FOLLOW_AGE_END_in_age2143) 
                if self._state.backtracking == 0:
                    stream_AGE_END.add(AGE_END135)

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
                    # 212:31: -> ^( AGE ( expr )? )
                    # SelectExpr.g:212:34: ^( AGE ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AGE, "AGE"), root_1)

                    # SelectExpr.g:212:40: ( expr )?
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
    # SelectExpr.g:215:1: value : ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRING136 = None
        FLOAT137 = None
        INTEGER138 = None
        TRUE139 = None
        FALSE140 = None
        this_141 = None

        list_142 = None


        STRING136_tree = None
        FLOAT137_tree = None
        INTEGER138_tree = None
        TRUE139_tree = None
        FALSE140_tree = None
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_TRUE = RewriteRuleTokenStream(self._adaptor, "token TRUE")
        stream_FALSE = RewriteRuleTokenStream(self._adaptor, "token FALSE")
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")

        try:
            try:
                # SelectExpr.g:215:7: ( STRING -> ^( VAL STRING ) | FLOAT -> ^( VAL FLOAT ) | INTEGER -> ^( VAL INTEGER ) | TRUE -> ^( VAL TRUE ) | FALSE -> ^( VAL FALSE ) | this_ | list_ )
                alt47 = 7
                LA47 = self.input.LA(1)
                if LA47 == STRING:
                    alt47 = 1
                elif LA47 == FLOAT:
                    alt47 = 2
                elif LA47 == INTEGER:
                    alt47 = 3
                elif LA47 == TRUE:
                    alt47 = 4
                elif LA47 == FALSE:
                    alt47 = 5
                elif LA47 == THIS or LA47 == PHRASE:
                    alt47 = 6
                elif LA47 == LIST_BEGIN:
                    alt47 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # SelectExpr.g:215:9: STRING
                    pass 
                    STRING136=self.match(self.input, STRING, self.FOLLOW_STRING_in_value2161) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING136)

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
                        # 215:17: -> ^( VAL STRING )
                        # SelectExpr.g:215:20: ^( VAL STRING )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_STRING.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 2:
                    # SelectExpr.g:216:4: FLOAT
                    pass 
                    FLOAT137=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value2175) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT137)

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
                        # 216:11: -> ^( VAL FLOAT )
                        # SelectExpr.g:216:14: ^( VAL FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 3:
                    # SelectExpr.g:217:4: INTEGER
                    pass 
                    INTEGER138=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_value2189) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER138)

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
                        # 217:12: -> ^( VAL INTEGER )
                        # SelectExpr.g:217:15: ^( VAL INTEGER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 4:
                    # SelectExpr.g:218:4: TRUE
                    pass 
                    TRUE139=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_value2202) 
                    if self._state.backtracking == 0:
                        stream_TRUE.add(TRUE139)

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
                        # 218:10: -> ^( VAL TRUE )
                        # SelectExpr.g:218:13: ^( VAL TRUE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_TRUE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 5:
                    # SelectExpr.g:219:4: FALSE
                    pass 
                    FALSE140=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_value2216) 
                    if self._state.backtracking == 0:
                        stream_FALSE.add(FALSE140)

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
                        # 219:11: -> ^( VAL FALSE )
                        # SelectExpr.g:219:14: ^( VAL FALSE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAL, "VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_FALSE.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 6:
                    # SelectExpr.g:220:4: this_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_this__in_value2230)
                    this_141 = self.this_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, this_141.tree)


                elif alt47 == 7:
                    # SelectExpr.g:221:4: list_
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list__in_value2235)
                    list_142 = self.list_()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_142.tree)


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
    # SelectExpr.g:224:1: this_ : ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) ;
    def this_(self, ):

        retval = self.this__return()
        retval.start = self.input.LT(1)

        root_0 = None

        PHRASE143 = None
        DOT144 = None
        THIS145 = None

        PHRASE143_tree = None
        DOT144_tree = None
        THIS145_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_PHRASE = RewriteRuleTokenStream(self._adaptor, "token PHRASE")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")

        try:
            try:
                # SelectExpr.g:224:7: ( ( PHRASE DOT )? THIS -> ^( THIS ( PHRASE )? ) )
                # SelectExpr.g:224:9: ( PHRASE DOT )? THIS
                pass 
                # SelectExpr.g:224:9: ( PHRASE DOT )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == PHRASE) :
                    alt48 = 1
                if alt48 == 1:
                    # SelectExpr.g:224:10: PHRASE DOT
                    pass 
                    PHRASE143=self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_this_2246) 
                    if self._state.backtracking == 0:
                        stream_PHRASE.add(PHRASE143)
                    DOT144=self.match(self.input, DOT, self.FOLLOW_DOT_in_this_2248) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT144)



                THIS145=self.match(self.input, THIS, self.FOLLOW_THIS_in_this_2252) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS145)

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
                    # 224:29: -> ^( THIS ( PHRASE )? )
                    # SelectExpr.g:224:32: ^( THIS ( PHRASE )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_THIS.nextNode(), root_1)

                    # SelectExpr.g:224:39: ( PHRASE )?
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
    # SelectExpr.g:227:1: list_ : LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) ;
    def list_(self, ):

        retval = self.list__return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIST_BEGIN146 = None
        SEP148 = None
        LIST_END150 = None
        expr147 = None

        expr149 = None


        LIST_BEGIN146_tree = None
        SEP148_tree = None
        LIST_END150_tree = None
        stream_LIST_END = RewriteRuleTokenStream(self._adaptor, "token LIST_END")
        stream_LIST_BEGIN = RewriteRuleTokenStream(self._adaptor, "token LIST_BEGIN")
        stream_SEP = RewriteRuleTokenStream(self._adaptor, "token SEP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # SelectExpr.g:227:7: ( LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END -> ^( LIST ( expr )* ) )
                # SelectExpr.g:227:10: LIST_BEGIN ( ( expr )? ( SEP expr )* ) LIST_END
                pass 
                LIST_BEGIN146=self.match(self.input, LIST_BEGIN, self.FOLLOW_LIST_BEGIN_in_list_2273) 
                if self._state.backtracking == 0:
                    stream_LIST_BEGIN.add(LIST_BEGIN146)
                # SelectExpr.g:227:21: ( ( expr )? ( SEP expr )* )
                # SelectExpr.g:227:23: ( expr )? ( SEP expr )*
                pass 
                # SelectExpr.g:227:23: ( expr )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == NOT or (ADD <= LA49_0 <= SUB) or LA49_0 == LIST_BEGIN or LA49_0 == SELECT or LA49_0 == THIS or LA49_0 == STRING or (INTEGER <= LA49_0 <= FALSE) or LA49_0 == PHRASE or LA49_0 == 94) :
                    alt49 = 1
                if alt49 == 1:
                    # SelectExpr.g:0:0: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_list_2277)
                    expr147 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr147.tree)



                # SelectExpr.g:227:29: ( SEP expr )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == SEP) :
                        alt50 = 1


                    if alt50 == 1:
                        # SelectExpr.g:227:30: SEP expr
                        pass 
                        SEP148=self.match(self.input, SEP, self.FOLLOW_SEP_in_list_2281) 
                        if self._state.backtracking == 0:
                            stream_SEP.add(SEP148)
                        self._state.following.append(self.FOLLOW_expr_in_list_2283)
                        expr149 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expr.add(expr149.tree)


                    else:
                        break #loop50



                LIST_END150=self.match(self.input, LIST_END, self.FOLLOW_LIST_END_in_list_2289) 
                if self._state.backtracking == 0:
                    stream_LIST_END.add(LIST_END150)

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
                    # 227:52: -> ^( LIST ( expr )* )
                    # SelectExpr.g:227:55: ^( LIST ( expr )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # SelectExpr.g:227:62: ( expr )*
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
        # SelectExpr.g:131:13: ( statement_select END )
        # SelectExpr.g:131:13: statement_select END
        pass 
        self._state.following.append(self.FOLLOW_statement_select_in_synpred2_SelectExpr1334)
        self.statement_select()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred2_SelectExpr1336)


    # $ANTLR end "synpred2_SelectExpr"



    # $ANTLR start "synpred3_SelectExpr"
    def synpred3_SelectExpr_fragment(self, ):
        # SelectExpr.g:132:4: ( expr END )
        # SelectExpr.g:132:4: expr END
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred3_SelectExpr1342)
        self.expr()

        self._state.following.pop()
        self.match(self.input, END, self.FOLLOW_END_in_synpred3_SelectExpr1344)


    # $ANTLR end "synpred3_SelectExpr"



    # $ANTLR start "synpred4_SelectExpr"
    def synpred4_SelectExpr_fragment(self, ):
        # SelectExpr.g:137:17: ( where_ )
        # SelectExpr.g:137:17: where_
        pass 
        self._state.following.append(self.FOLLOW_where__in_synpred4_SelectExpr1366)
        self.where_()

        self._state.following.pop()


    # $ANTLR end "synpred4_SelectExpr"



    # $ANTLR start "synpred6_SelectExpr"
    def synpred6_SelectExpr_fragment(self, ):
        # SelectExpr.g:137:27: ( group_ ( having_ )? )
        # SelectExpr.g:137:27: group_ ( having_ )?
        pass 
        self._state.following.append(self.FOLLOW_group__in_synpred6_SelectExpr1371)
        self.group_()

        self._state.following.pop()
        # SelectExpr.g:137:34: ( having_ )?
        alt51 = 2
        LA51_0 = self.input.LA(1)

        if (LA51_0 == HAVING) :
            alt51 = 1
        if alt51 == 1:
            # SelectExpr.g:137:35: having_
            pass 
            self._state.following.append(self.FOLLOW_having__in_synpred6_SelectExpr1374)
            self.having_()

            self._state.following.pop()





    # $ANTLR end "synpred6_SelectExpr"



    # $ANTLR start "synpred7_SelectExpr"
    def synpred7_SelectExpr_fragment(self, ):
        # SelectExpr.g:137:48: ( order_ )
        # SelectExpr.g:137:48: order_
        pass 
        self._state.following.append(self.FOLLOW_order__in_synpred7_SelectExpr1381)
        self.order_()

        self._state.following.pop()


    # $ANTLR end "synpred7_SelectExpr"



    # $ANTLR start "synpred8_SelectExpr"
    def synpred8_SelectExpr_fragment(self, ):
        # SelectExpr.g:137:58: ( as_ )
        # SelectExpr.g:137:58: as_
        pass 
        self._state.following.append(self.FOLLOW_as__in_synpred8_SelectExpr1386)
        self.as_()

        self._state.following.pop()


    # $ANTLR end "synpred8_SelectExpr"



    # $ANTLR start "synpred15_SelectExpr"
    def synpred15_SelectExpr_fragment(self, ):
        # SelectExpr.g:143:21: ( SEP expr )
        # SelectExpr.g:143:21: SEP expr
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred15_SelectExpr1491)
        self._state.following.append(self.FOLLOW_expr_in_synpred15_SelectExpr1494)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred15_SelectExpr"



    # $ANTLR start "synpred18_SelectExpr"
    def synpred18_SelectExpr_fragment(self, ):
        # SelectExpr.g:149:44: ( SEP ( PHRASE | function ) )
        # SelectExpr.g:149:44: SEP ( PHRASE | function )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred18_SelectExpr1534)
        # SelectExpr.g:149:49: ( PHRASE | function )
        alt53 = 2
        LA53_0 = self.input.LA(1)

        if (LA53_0 == PHRASE) :
            LA53_1 = self.input.LA(2)

            if (LA53_1 == 94) :
                alt53 = 2
            elif (LA53_1 == EOF) :
                alt53 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 53, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 53, 0, self.input)

            raise nvae

        if alt53 == 1:
            # SelectExpr.g:149:51: PHRASE
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred18_SelectExpr1539)


        elif alt53 == 2:
            # SelectExpr.g:149:60: function
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred18_SelectExpr1543)
            self.function()

            self._state.following.pop()





    # $ANTLR end "synpred18_SelectExpr"



    # $ANTLR start "synpred21_SelectExpr"
    def synpred21_SelectExpr_fragment(self, ):
        # SelectExpr.g:155:66: ( SEP ( PHRASE direction_ | function direction_ ) )
        # SelectExpr.g:155:66: SEP ( PHRASE direction_ | function direction_ )
        pass 
        self.match(self.input, SEP, self.FOLLOW_SEP_in_synpred21_SelectExpr1590)
        # SelectExpr.g:155:71: ( PHRASE direction_ | function direction_ )
        alt54 = 2
        LA54_0 = self.input.LA(1)

        if (LA54_0 == PHRASE) :
            LA54_1 = self.input.LA(2)

            if (LA54_1 == 94) :
                alt54 = 2
            elif (LA54_1 == EOF or (ASC <= LA54_1 <= DESC)) :
                alt54 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 54, 1, self.input)

                raise nvae

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 54, 0, self.input)

            raise nvae

        if alt54 == 1:
            # SelectExpr.g:155:73: PHRASE direction_
            pass 
            self.match(self.input, PHRASE, self.FOLLOW_PHRASE_in_synpred21_SelectExpr1595)
            self._state.following.append(self.FOLLOW_direction__in_synpred21_SelectExpr1597)
            self.direction_()

            self._state.following.pop()


        elif alt54 == 2:
            # SelectExpr.g:155:93: function direction_
            pass 
            self._state.following.append(self.FOLLOW_function_in_synpred21_SelectExpr1601)
            self.function()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_direction__in_synpred21_SelectExpr1603)
            self.direction_()

            self._state.following.pop()





    # $ANTLR end "synpred21_SelectExpr"



    # $ANTLR start "synpred29_SelectExpr"
    def synpred29_SelectExpr_fragment(self, ):
        # SelectExpr.g:164:8: ( assign_expr )
        # SelectExpr.g:164:8: assign_expr
        pass 
        self._state.following.append(self.FOLLOW_assign_expr_in_synpred29_SelectExpr1674)
        self.assign_expr()

        self._state.following.pop()


    # $ANTLR end "synpred29_SelectExpr"



    # $ANTLR start "synpred31_SelectExpr"
    def synpred31_SelectExpr_fragment(self, ):
        # SelectExpr.g:171:24: ( OR logic_xor )
        # SelectExpr.g:171:24: OR logic_xor
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred31_SelectExpr1733)
        self._state.following.append(self.FOLLOW_logic_xor_in_synpred31_SelectExpr1737)
        self.logic_xor()

        self._state.following.pop()


    # $ANTLR end "synpred31_SelectExpr"



    # $ANTLR start "synpred32_SelectExpr"
    def synpred32_SelectExpr_fragment(self, ):
        # SelectExpr.g:172:24: ( XOR logic_and )
        # SelectExpr.g:172:24: XOR logic_and
        pass 
        self.match(self.input, XOR, self.FOLLOW_XOR_in_synpred32_SelectExpr1750)
        self._state.following.append(self.FOLLOW_logic_and_in_synpred32_SelectExpr1753)
        self.logic_and()

        self._state.following.pop()


    # $ANTLR end "synpred32_SelectExpr"



    # $ANTLR start "synpred33_SelectExpr"
    def synpred33_SelectExpr_fragment(self, ):
        # SelectExpr.g:173:24: ( AND logic_not )
        # SelectExpr.g:173:24: AND logic_not
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred33_SelectExpr1766)
        self._state.following.append(self.FOLLOW_logic_not_in_synpred33_SelectExpr1769)
        self.logic_not()

        self._state.following.pop()


    # $ANTLR end "synpred33_SelectExpr"



    # $ANTLR start "synpred35_SelectExpr"
    def synpred35_SelectExpr_fragment(self, ):
        # SelectExpr.g:177:26: ( IN atom )
        # SelectExpr.g:177:26: IN atom
        pass 
        self.match(self.input, IN, self.FOLLOW_IN_in_synpred35_SelectExpr1805)
        self._state.following.append(self.FOLLOW_atom_in_synpred35_SelectExpr1808)
        self.atom()

        self._state.following.pop()


    # $ANTLR end "synpred35_SelectExpr"



    # $ANTLR start "synpred36_SelectExpr"
    def synpred36_SelectExpr_fragment(self, ):
        # SelectExpr.g:178:26: ( EQ compare_ne )
        # SelectExpr.g:178:26: EQ compare_ne
        pass 
        self.match(self.input, EQ, self.FOLLOW_EQ_in_synpred36_SelectExpr1821)
        self._state.following.append(self.FOLLOW_compare_ne_in_synpred36_SelectExpr1824)
        self.compare_ne()

        self._state.following.pop()


    # $ANTLR end "synpred36_SelectExpr"



    # $ANTLR start "synpred37_SelectExpr"
    def synpred37_SelectExpr_fragment(self, ):
        # SelectExpr.g:179:26: ( NE compare_ge )
        # SelectExpr.g:179:26: NE compare_ge
        pass 
        self.match(self.input, NE, self.FOLLOW_NE_in_synpred37_SelectExpr1837)
        self._state.following.append(self.FOLLOW_compare_ge_in_synpred37_SelectExpr1840)
        self.compare_ge()

        self._state.following.pop()


    # $ANTLR end "synpred37_SelectExpr"



    # $ANTLR start "synpred38_SelectExpr"
    def synpred38_SelectExpr_fragment(self, ):
        # SelectExpr.g:180:26: ( GE compare_gt )
        # SelectExpr.g:180:26: GE compare_gt
        pass 
        self.match(self.input, GE, self.FOLLOW_GE_in_synpred38_SelectExpr1853)
        self._state.following.append(self.FOLLOW_compare_gt_in_synpred38_SelectExpr1856)
        self.compare_gt()

        self._state.following.pop()


    # $ANTLR end "synpred38_SelectExpr"



    # $ANTLR start "synpred39_SelectExpr"
    def synpred39_SelectExpr_fragment(self, ):
        # SelectExpr.g:181:26: ( GT compare_le )
        # SelectExpr.g:181:26: GT compare_le
        pass 
        self.match(self.input, GT, self.FOLLOW_GT_in_synpred39_SelectExpr1869)
        self._state.following.append(self.FOLLOW_compare_le_in_synpred39_SelectExpr1872)
        self.compare_le()

        self._state.following.pop()


    # $ANTLR end "synpred39_SelectExpr"



    # $ANTLR start "synpred40_SelectExpr"
    def synpred40_SelectExpr_fragment(self, ):
        # SelectExpr.g:182:26: ( LE compare_lt )
        # SelectExpr.g:182:26: LE compare_lt
        pass 
        self.match(self.input, LE, self.FOLLOW_LE_in_synpred40_SelectExpr1885)
        self._state.following.append(self.FOLLOW_compare_lt_in_synpred40_SelectExpr1888)
        self.compare_lt()

        self._state.following.pop()


    # $ANTLR end "synpred40_SelectExpr"



    # $ANTLR start "synpred41_SelectExpr"
    def synpred41_SelectExpr_fragment(self, ):
        # SelectExpr.g:183:31: ( LT arithmetic_expr )
        # SelectExpr.g:183:31: LT arithmetic_expr
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred41_SelectExpr1901)
        self._state.following.append(self.FOLLOW_arithmetic_expr_in_synpred41_SelectExpr1904)
        self.arithmetic_expr()

        self._state.following.pop()


    # $ANTLR end "synpred41_SelectExpr"



    # $ANTLR start "synpred43_SelectExpr"
    def synpred43_SelectExpr_fragment(self, ):
        # SelectExpr.g:186:46: ( ( SUB | ADD ) arithmetic_mul_div_mod )
        # SelectExpr.g:186:46: ( SUB | ADD ) arithmetic_mul_div_mod
        pass 
        if (ADD <= self.input.LA(1) <= SUB):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_mul_div_mod_in_synpred43_SelectExpr1934)
        self.arithmetic_mul_div_mod()

        self._state.following.pop()


    # $ANTLR end "synpred43_SelectExpr"



    # $ANTLR start "synpred46_SelectExpr"
    def synpred46_SelectExpr_fragment(self, ):
        # SelectExpr.g:187:42: ( ( MUL | DIV | MOD ) arithmetic_pow )
        # SelectExpr.g:187:42: ( MUL | DIV | MOD ) arithmetic_pow
        pass 
        if (MUL <= self.input.LA(1) <= MOD):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_arithmetic_pow_in_synpred46_SelectExpr1962)
        self.arithmetic_pow()

        self._state.following.pop()


    # $ANTLR end "synpred46_SelectExpr"



    # $ANTLR start "synpred47_SelectExpr"
    def synpred47_SelectExpr_fragment(self, ):
        # SelectExpr.g:188:36: ( POW arithmetic_unary )
        # SelectExpr.g:188:36: POW arithmetic_unary
        pass 
        self.match(self.input, POW, self.FOLLOW_POW_in_synpred47_SelectExpr1975)
        self._state.following.append(self.FOLLOW_arithmetic_unary_in_synpred47_SelectExpr1978)
        self.arithmetic_unary()

        self._state.following.pop()


    # $ANTLR end "synpred47_SelectExpr"




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

    def synpred18_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred18_SelectExpr_fragment()
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

    def synpred7_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred7_SelectExpr_fragment()
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

    def synpred21_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred21_SelectExpr_fragment()
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

    def synpred31_SelectExpr(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred31_SelectExpr_fragment()
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
        u"\1\136\1\0\16\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\13\uffff\1\3\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\16\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\16\13\uffff\1\2\11\uffff\2\2\6\uffff\1\2\7\uffff"
        u"\1\1\21\uffff\1\2\12\uffff\1\2\1\uffff\4\2\2\uffff\1\2\4\uffff"
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
    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA23_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA23_min = DFA.unpack(
        u"\1\32\1\0\15\uffff"
        )

    DFA23_max = DFA.unpack(
        u"\1\136\1\0\15\uffff"
        )

    DFA23_accept = DFA.unpack(
        u"\2\uffff\1\2\13\uffff\1\1"
        )

    DFA23_special = DFA.unpack(
        u"\1\uffff\1\0\15\uffff"
        )

            
    DFA23_transition = [
        DFA.unpack(u"\1\2\11\uffff\2\2\6\uffff\1\2\7\uffff\1\2\21\uffff\1"
        u"\2\12\uffff\1\2\1\uffff\4\2\2\uffff\1\1\4\uffff\1\2"),
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

    # class definition for DFA #23

    class DFA23(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA23_1 = input.LA(1)

                 
                index23_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred29_SelectExpr()):
                    s = 14

                elif (True):
                    s = 2

                 
                input.seek(index23_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 23, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_prog_in_eval1314 = frozenset([1])
    FOLLOW_statement_in_prog1324 = frozenset([1, 14, 26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_statement_select_in_statement1334 = frozenset([14])
    FOLLOW_END_in_statement1336 = frozenset([1])
    FOLLOW_expr_in_statement1342 = frozenset([14])
    FOLLOW_END_in_statement1344 = frozenset([1])
    FOLLOW_END_in_statement1350 = frozenset([1])
    FOLLOW_select__in_statement_select1361 = frozenset([55])
    FOLLOW_from__in_statement_select1363 = frozenset([1, 58, 59, 63, 69])
    FOLLOW_where__in_statement_select1366 = frozenset([1, 59, 63, 69])
    FOLLOW_group__in_statement_select1371 = frozenset([1, 59, 65, 69])
    FOLLOW_having__in_statement_select1374 = frozenset([1, 59, 69])
    FOLLOW_order__in_statement_select1381 = frozenset([1, 69])
    FOLLOW_as__in_statement_select1386 = frozenset([1])
    FOLLOW_SELECT_in_select_1434 = frozenset([38, 70, 89])
    FOLLOW_MUL_in_select_1438 = frozenset([1])
    FOLLOW_PHRASE_in_select_1445 = frozenset([1, 13])
    FOLLOW_function_in_select_1449 = frozenset([1, 13])
    FOLLOW_this__in_select_1453 = frozenset([1, 13])
    FOLLOW_SEP_in_select_1457 = frozenset([70, 89])
    FOLLOW_PHRASE_in_select_1461 = frozenset([1, 13])
    FOLLOW_function_in_select_1465 = frozenset([1, 13])
    FOLLOW_this__in_select_1469 = frozenset([1, 13])
    FOLLOW_FROM_in_from_1485 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_from_1488 = frozenset([1, 13])
    FOLLOW_SEP_in_from_1491 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_from_1494 = frozenset([1, 13])
    FOLLOW_WHERE_in_where_1505 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_where_1508 = frozenset([1])
    FOLLOW_GROUP_in_group_1517 = frozenset([68])
    FOLLOW_BY_in_group_1520 = frozenset([89])
    FOLLOW_PHRASE_in_group_1525 = frozenset([1, 13])
    FOLLOW_function_in_group_1529 = frozenset([1, 13])
    FOLLOW_SEP_in_group_1534 = frozenset([89])
    FOLLOW_PHRASE_in_group_1539 = frozenset([1, 13])
    FOLLOW_function_in_group_1543 = frozenset([1, 13])
    FOLLOW_HAVING_in_having_1557 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_having_1560 = frozenset([1])
    FOLLOW_ORDER_in_order_1569 = frozenset([68])
    FOLLOW_BY_in_order_1572 = frozenset([89])
    FOLLOW_PHRASE_in_order_1577 = frozenset([13, 72, 73])
    FOLLOW_direction__in_order_1579 = frozenset([1, 13])
    FOLLOW_function_in_order_1583 = frozenset([13, 72, 73])
    FOLLOW_direction__in_order_1585 = frozenset([1, 13])
    FOLLOW_SEP_in_order_1590 = frozenset([89])
    FOLLOW_PHRASE_in_order_1595 = frozenset([13, 72, 73])
    FOLLOW_direction__in_order_1597 = frozenset([1, 13])
    FOLLOW_function_in_order_1601 = frozenset([13, 72, 73])
    FOLLOW_direction__in_order_1603 = frozenset([1, 13])
    FOLLOW_set_in_direction_1618 = frozenset([1])
    FOLLOW_AS_in_as_1634 = frozenset([74, 75, 76, 89])
    FOLLOW_AS_LIST_in_as_1639 = frozenset([1])
    FOLLOW_AS_VALUE_in_as_1643 = frozenset([1])
    FOLLOW_AS_DICT_in_as_1647 = frozenset([1])
    FOLLOW_PHRASE_in_as_1651 = frozenset([1, 94])
    FOLLOW_94_in_as_1654 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94, 95])
    FOLLOW_parameter_in_as_1657 = frozenset([95])
    FOLLOW_95_in_as_1660 = frozenset([1])
    FOLLOW_assign_expr_in_expr1674 = frozenset([1])
    FOLLOW_logic_expr_in_expr1680 = frozenset([1])
    FOLLOW_PHRASE_in_assign_expr1689 = frozenset([29, 46])
    FOLLOW_age_in_assign_expr1692 = frozenset([29])
    FOLLOW_ASSIGN_in_assign_expr1696 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_assign_expr1698 = frozenset([1])
    FOLLOW_logic_or_in_logic_expr1721 = frozenset([1])
    FOLLOW_logic_xor_in_logic_or1730 = frozenset([1, 24])
    FOLLOW_OR_in_logic_or1733 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_xor_in_logic_or1737 = frozenset([1, 24])
    FOLLOW_logic_and_in_logic_xor1747 = frozenset([1, 23])
    FOLLOW_XOR_in_logic_xor1750 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_and_in_logic_xor1753 = frozenset([1, 23])
    FOLLOW_logic_not_in_logic_and1763 = frozenset([1, 19])
    FOLLOW_AND_in_logic_and1766 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_not_in_logic_and1769 = frozenset([1, 19])
    FOLLOW_NOT_in_logic_not1780 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_expr_in_logic_not1785 = frozenset([1])
    FOLLOW_compare_in_in_compare_expr1794 = frozenset([1])
    FOLLOW_compare_eq_in_compare_in1802 = frozenset([1, 28])
    FOLLOW_IN_in_compare_in1805 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_atom_in_compare_in1808 = frozenset([1, 28])
    FOLLOW_compare_ne_in_compare_eq1818 = frozenset([1, 30])
    FOLLOW_EQ_in_compare_eq1821 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_ne_in_compare_eq1824 = frozenset([1, 30])
    FOLLOW_compare_ge_in_compare_ne1834 = frozenset([1, 31])
    FOLLOW_NE_in_compare_ne1837 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_ge_in_compare_ne1840 = frozenset([1, 31])
    FOLLOW_compare_gt_in_compare_ge1850 = frozenset([1, 33])
    FOLLOW_GE_in_compare_ge1853 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_gt_in_compare_ge1856 = frozenset([1, 33])
    FOLLOW_compare_le_in_compare_gt1866 = frozenset([1, 35])
    FOLLOW_GT_in_compare_gt1869 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_le_in_compare_gt1872 = frozenset([1, 35])
    FOLLOW_compare_lt_in_compare_le1882 = frozenset([1, 32])
    FOLLOW_LE_in_compare_le1885 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_lt_in_compare_le1888 = frozenset([1, 32])
    FOLLOW_arithmetic_expr_in_compare_lt1898 = frozenset([1, 34])
    FOLLOW_LT_in_compare_lt1901 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_expr_in_compare_lt1904 = frozenset([1, 34])
    FOLLOW_arithmetic_sub_add_in_arithmetic_expr1915 = frozenset([1])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add1923 = frozenset([1, 36, 37])
    FOLLOW_SUB_in_arithmetic_sub_add1927 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_ADD_in_arithmetic_sub_add1930 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_mul_div_mod_in_arithmetic_sub_add1934 = frozenset([1, 36, 37])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod1944 = frozenset([1, 38, 39, 40])
    FOLLOW_MUL_in_arithmetic_mul_div_mod1948 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_DIV_in_arithmetic_mul_div_mod1953 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_MOD_in_arithmetic_mul_div_mod1958 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_pow_in_arithmetic_mul_div_mod1962 = frozenset([1, 38, 39, 40])
    FOLLOW_arithmetic_unary_in_arithmetic_pow1972 = frozenset([1, 41])
    FOLLOW_POW_in_arithmetic_pow1975 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_unary_in_arithmetic_pow1978 = frozenset([1, 41])
    FOLLOW_SUB_in_arithmetic_unary1989 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_atom_in_arithmetic_unary1991 = frozenset([1])
    FOLLOW_ADD_in_arithmetic_unary2005 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_atom_in_arithmetic_unary2007 = frozenset([1])
    FOLLOW_atom_in_arithmetic_unary2021 = frozenset([1])
    FOLLOW_value_in_atom2032 = frozenset([1])
    FOLLOW_variable_in_atom2037 = frozenset([1])
    FOLLOW_function_in_atom2042 = frozenset([1])
    FOLLOW_94_in_atom2047 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_atom2050 = frozenset([95])
    FOLLOW_95_in_atom2052 = frozenset([1])
    FOLLOW_statement_select_in_atom2058 = frozenset([1])
    FOLLOW_PHRASE_in_function2067 = frozenset([94])
    FOLLOW_94_in_function2069 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94, 95])
    FOLLOW_parameter_in_function2071 = frozenset([95])
    FOLLOW_95_in_function2074 = frozenset([1])
    FOLLOW_expr_in_parameter2094 = frozenset([1, 13])
    FOLLOW_SEP_in_parameter2097 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_parameter2100 = frozenset([1, 13])
    FOLLOW_PHRASE_in_variable2111 = frozenset([1, 46])
    FOLLOW_age_in_variable2114 = frozenset([1])
    FOLLOW_AGE_BEGIN_in_age2138 = frozenset([26, 36, 37, 44, 47, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_age2140 = frozenset([47])
    FOLLOW_AGE_END_in_age2143 = frozenset([1])
    FOLLOW_STRING_in_value2161 = frozenset([1])
    FOLLOW_FLOAT_in_value2175 = frozenset([1])
    FOLLOW_INTEGER_in_value2189 = frozenset([1])
    FOLLOW_TRUE_in_value2202 = frozenset([1])
    FOLLOW_FALSE_in_value2216 = frozenset([1])
    FOLLOW_this__in_value2230 = frozenset([1])
    FOLLOW_list__in_value2235 = frozenset([1])
    FOLLOW_PHRASE_in_this_2246 = frozenset([12])
    FOLLOW_DOT_in_this_2248 = frozenset([70])
    FOLLOW_THIS_in_this_2252 = frozenset([1])
    FOLLOW_LIST_BEGIN_in_list_2273 = frozenset([13, 26, 36, 37, 44, 45, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_list_2277 = frozenset([13, 45])
    FOLLOW_SEP_in_list_2281 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_list_2283 = frozenset([13, 45])
    FOLLOW_LIST_END_in_list_2289 = frozenset([1])
    FOLLOW_statement_select_in_synpred2_SelectExpr1334 = frozenset([14])
    FOLLOW_END_in_synpred2_SelectExpr1336 = frozenset([1])
    FOLLOW_expr_in_synpred3_SelectExpr1342 = frozenset([14])
    FOLLOW_END_in_synpred3_SelectExpr1344 = frozenset([1])
    FOLLOW_where__in_synpred4_SelectExpr1366 = frozenset([1])
    FOLLOW_group__in_synpred6_SelectExpr1371 = frozenset([1, 65])
    FOLLOW_having__in_synpred6_SelectExpr1374 = frozenset([1])
    FOLLOW_order__in_synpred7_SelectExpr1381 = frozenset([1])
    FOLLOW_as__in_synpred8_SelectExpr1386 = frozenset([1])
    FOLLOW_SEP_in_synpred15_SelectExpr1491 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_expr_in_synpred15_SelectExpr1494 = frozenset([1])
    FOLLOW_SEP_in_synpred18_SelectExpr1534 = frozenset([89])
    FOLLOW_PHRASE_in_synpred18_SelectExpr1539 = frozenset([1])
    FOLLOW_function_in_synpred18_SelectExpr1543 = frozenset([1])
    FOLLOW_SEP_in_synpred21_SelectExpr1590 = frozenset([89])
    FOLLOW_PHRASE_in_synpred21_SelectExpr1595 = frozenset([72, 73])
    FOLLOW_direction__in_synpred21_SelectExpr1597 = frozenset([1])
    FOLLOW_function_in_synpred21_SelectExpr1601 = frozenset([72, 73])
    FOLLOW_direction__in_synpred21_SelectExpr1603 = frozenset([1])
    FOLLOW_assign_expr_in_synpred29_SelectExpr1674 = frozenset([1])
    FOLLOW_OR_in_synpred31_SelectExpr1733 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_xor_in_synpred31_SelectExpr1737 = frozenset([1])
    FOLLOW_XOR_in_synpred32_SelectExpr1750 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_and_in_synpred32_SelectExpr1753 = frozenset([1])
    FOLLOW_AND_in_synpred33_SelectExpr1766 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_logic_not_in_synpred33_SelectExpr1769 = frozenset([1])
    FOLLOW_IN_in_synpred35_SelectExpr1805 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_atom_in_synpred35_SelectExpr1808 = frozenset([1])
    FOLLOW_EQ_in_synpred36_SelectExpr1821 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_ne_in_synpred36_SelectExpr1824 = frozenset([1])
    FOLLOW_NE_in_synpred37_SelectExpr1837 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_ge_in_synpred37_SelectExpr1840 = frozenset([1])
    FOLLOW_GE_in_synpred38_SelectExpr1853 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_gt_in_synpred38_SelectExpr1856 = frozenset([1])
    FOLLOW_GT_in_synpred39_SelectExpr1869 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_le_in_synpred39_SelectExpr1872 = frozenset([1])
    FOLLOW_LE_in_synpred40_SelectExpr1885 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_compare_lt_in_synpred40_SelectExpr1888 = frozenset([1])
    FOLLOW_LT_in_synpred41_SelectExpr1901 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_expr_in_synpred41_SelectExpr1904 = frozenset([1])
    FOLLOW_set_in_synpred43_SelectExpr1926 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_mul_div_mod_in_synpred43_SelectExpr1934 = frozenset([1])
    FOLLOW_set_in_synpred46_SelectExpr1947 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_pow_in_synpred46_SelectExpr1962 = frozenset([1])
    FOLLOW_POW_in_synpred47_SelectExpr1975 = frozenset([26, 36, 37, 44, 52, 70, 81, 83, 84, 85, 86, 89, 94])
    FOLLOW_arithmetic_unary_in_synpred47_SelectExpr1978 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SelectExprLexer", SelectExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
