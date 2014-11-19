# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2014-11-19 16:00:41

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class SelectExprLexer(Lexer):

    grammarFileName = "SelectExpr.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SelectExprLexer, self).__init__(input, state)


        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )






    # $ANTLR start "T__98"
    def mT__98(self, ):

        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:7:7: ( '(' )
            # SelectExpr.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):

        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:8:7: ( ')' )
            # SelectExpr.g:8:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__99"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:36:6: ( '.' )
            # SelectExpr.g:36:8: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "SEP"
    def mSEP(self, ):

        try:
            _type = SEP
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:37:6: ( ',' )
            # SelectExpr.g:37:8: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEP"



    # $ANTLR start "END"
    def mEND(self, ):

        try:
            _type = END
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:38:6: ( ';' )
            # SelectExpr.g:38:8: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "END"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:39:8: ( ':' )
            # SelectExpr.g:39:10: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:41:6: ( A N D )
            # SelectExpr.g:41:8: A N D
            pass 
            self.mA()
            self.mN()
            self.mD()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "XOR"
    def mXOR(self, ):

        try:
            _type = XOR
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:42:6: ( X O R )
            # SelectExpr.g:42:8: X O R
            pass 
            self.mX()
            self.mO()
            self.mR()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "XOR"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:43:6: ( O R )
            # SelectExpr.g:43:8: O R
            pass 
            self.mO()
            self.mR()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:44:6: ( N O T )
            # SelectExpr.g:44:8: N O T
            pass 
            self.mN()
            self.mO()
            self.mT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:45:6: ( I N )
            # SelectExpr.g:45:8: I N
            pass 
            self.mI()
            self.mN()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:47:8: ( '=' )
            # SelectExpr.g:47:11: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "EQ"
    def mEQ(self, ):

        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:49:4: ( '==' )
            # SelectExpr.g:49:6: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQ"



    # $ANTLR start "NE"
    def mNE(self, ):

        try:
            _type = NE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:50:4: ( '!=' )
            # SelectExpr.g:50:6: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NE"



    # $ANTLR start "LE"
    def mLE(self, ):

        try:
            _type = LE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:51:4: ( '<=' )
            # SelectExpr.g:51:6: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LE"



    # $ANTLR start "GE"
    def mGE(self, ):

        try:
            _type = GE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:52:4: ( '>=' )
            # SelectExpr.g:52:6: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GE"



    # $ANTLR start "LT"
    def mLT(self, ):

        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:53:4: ( '<' )
            # SelectExpr.g:53:7: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LT"



    # $ANTLR start "GT"
    def mGT(self, ):

        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:54:4: ( '>' )
            # SelectExpr.g:54:7: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GT"



    # $ANTLR start "ADD"
    def mADD(self, ):

        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:56:6: ( '+' )
            # SelectExpr.g:56:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ADD"



    # $ANTLR start "SUB"
    def mSUB(self, ):

        try:
            _type = SUB
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:57:6: ( '-' )
            # SelectExpr.g:57:8: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUB"



    # $ANTLR start "MUL"
    def mMUL(self, ):

        try:
            _type = MUL
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:58:6: ( '*' )
            # SelectExpr.g:58:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MUL"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:59:6: ( '/' )
            # SelectExpr.g:59:8: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "MOD"
    def mMOD(self, ):

        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:60:6: ( '%' )
            # SelectExpr.g:60:8: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOD"



    # $ANTLR start "POW"
    def mPOW(self, ):

        try:
            _type = POW
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:61:6: ( '^' )
            # SelectExpr.g:61:8: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "POW"



    # $ANTLR start "SQ"
    def mSQ(self, ):

        try:
            _type = SQ
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:63:5: ( '\\'' )
            # SelectExpr.g:63:7: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SQ"



    # $ANTLR start "DQ"
    def mDQ(self, ):

        try:
            _type = DQ
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:64:5: ( '\\\"' )
            # SelectExpr.g:64:7: '\\\"'
            pass 
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DQ"



    # $ANTLR start "LIST_BEGIN"
    def mLIST_BEGIN(self, ):

        try:
            _type = LIST_BEGIN
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:66:12: ( '[' )
            # SelectExpr.g:66:14: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIST_BEGIN"



    # $ANTLR start "LIST_END"
    def mLIST_END(self, ):

        try:
            _type = LIST_END
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:67:12: ( ']' )
            # SelectExpr.g:67:14: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIST_END"



    # $ANTLR start "AGE_BEGIN"
    def mAGE_BEGIN(self, ):

        try:
            _type = AGE_BEGIN
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:69:11: ( '{' )
            # SelectExpr.g:69:13: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AGE_BEGIN"



    # $ANTLR start "AGE_END"
    def mAGE_END(self, ):

        try:
            _type = AGE_END
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:70:11: ( '}' )
            # SelectExpr.g:70:13: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AGE_END"



    # $ANTLR start "SELECT"
    def mSELECT(self, ):

        try:
            _type = SELECT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:72:8: ( S E L E C T )
            # SelectExpr.g:72:10: S E L E C T
            pass 
            self.mS()
            self.mE()
            self.mL()
            self.mE()
            self.mC()
            self.mT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SELECT"



    # $ANTLR start "FROM"
    def mFROM(self, ):

        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:73:8: ( F R O M )
            # SelectExpr.g:73:10: F R O M
            pass 
            self.mF()
            self.mR()
            self.mO()
            self.mM()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROM"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):

        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:74:8: ( W H E R E )
            # SelectExpr.g:74:10: W H E R E
            pass 
            self.mW()
            self.mH()
            self.mE()
            self.mR()
            self.mE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "ORDER"
    def mORDER(self, ):

        try:
            _type = ORDER
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:75:8: ( O R D E R )
            # SelectExpr.g:75:10: O R D E R
            pass 
            self.mO()
            self.mR()
            self.mD()
            self.mE()
            self.mR()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORDER"



    # $ANTLR start "GROUP"
    def mGROUP(self, ):

        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:76:8: ( G R O U P )
            # SelectExpr.g:76:10: G R O U P
            pass 
            self.mG()
            self.mR()
            self.mO()
            self.mU()
            self.mP()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GROUP"



    # $ANTLR start "HAVING"
    def mHAVING(self, ):

        try:
            _type = HAVING
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:77:8: ( H A V I N G )
            # SelectExpr.g:77:10: H A V I N G
            pass 
            self.mH()
            self.mA()
            self.mV()
            self.mI()
            self.mN()
            self.mG()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HAVING"



    # $ANTLR start "BY"
    def mBY(self, ):

        try:
            _type = BY
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:78:8: ( B Y )
            # SelectExpr.g:78:10: B Y
            pass 
            self.mB()
            self.mY()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BY"



    # $ANTLR start "AS"
    def mAS(self, ):

        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:79:8: ( A S )
            # SelectExpr.g:79:10: A S
            pass 
            self.mA()
            self.mS()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS"



    # $ANTLR start "THIS"
    def mTHIS(self, ):

        try:
            _type = THIS
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:81:8: ( T H I S )
            # SelectExpr.g:81:10: T H I S
            pass 
            self.mT()
            self.mH()
            self.mI()
            self.mS()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THIS"



    # $ANTLR start "TIME"
    def mTIME(self, ):

        try:
            _type = TIME
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:82:8: ( T I M E )
            # SelectExpr.g:82:10: T I M E
            pass 
            self.mT()
            self.mI()
            self.mM()
            self.mE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TIME"



    # $ANTLR start "CONNECT"
    def mCONNECT(self, ):

        try:
            _type = CONNECT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:84:8: ( C O N N E C T )
            # SelectExpr.g:84:10: C O N N E C T
            pass 
            self.mC()
            self.mO()
            self.mN()
            self.mN()
            self.mE()
            self.mC()
            self.mT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONNECT"



    # $ANTLR start "START"
    def mSTART(self, ):

        try:
            _type = START
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:85:8: ( S T A R T )
            # SelectExpr.g:85:10: S T A R T
            pass 
            self.mS()
            self.mT()
            self.mA()
            self.mR()
            self.mT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "START"



    # $ANTLR start "STOP"
    def mSTOP(self, ):

        try:
            _type = STOP
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:86:8: ( S T O P )
            # SelectExpr.g:86:10: S T O P
            pass 
            self.mS()
            self.mT()
            self.mO()
            self.mP()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STOP"



    # $ANTLR start "WITH"
    def mWITH(self, ):

        try:
            _type = WITH
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:87:8: ( W I T H )
            # SelectExpr.g:87:10: W I T H
            pass 
            self.mW()
            self.mI()
            self.mT()
            self.mH()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WITH"



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:90:8: ( A S C ( E N D I N G )? )
            # SelectExpr.g:90:10: A S C ( E N D I N G )?
            pass 
            self.mA()
            self.mS()
            self.mC()
            # SelectExpr.g:90:16: ( E N D I N G )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 69 or LA1_0 == 101) :
                alt1 = 1
            if alt1 == 1:
                # SelectExpr.g:90:17: E N D I N G
                pass 
                self.mE()
                self.mN()
                self.mD()
                self.mI()
                self.mN()
                self.mG()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASC"



    # $ANTLR start "DESC"
    def mDESC(self, ):

        try:
            _type = DESC
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:91:8: ( D E S C ( E N D I N G )? )
            # SelectExpr.g:91:10: D E S C ( E N D I N G )?
            pass 
            self.mD()
            self.mE()
            self.mS()
            self.mC()
            # SelectExpr.g:91:18: ( E N D I N G )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 69 or LA2_0 == 101) :
                alt2 = 1
            if alt2 == 1:
                # SelectExpr.g:91:19: E N D I N G
                pass 
                self.mE()
                self.mN()
                self.mD()
                self.mI()
                self.mN()
                self.mG()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DESC"



    # $ANTLR start "AS_LIST"
    def mAS_LIST(self, ):

        try:
            _type = AS_LIST
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:93:9: ( L I S T )
            # SelectExpr.g:93:11: L I S T
            pass 
            self.mL()
            self.mI()
            self.mS()
            self.mT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS_LIST"



    # $ANTLR start "AS_VALUE"
    def mAS_VALUE(self, ):

        try:
            _type = AS_VALUE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:94:9: ( V A L ( U E )? )
            # SelectExpr.g:94:11: V A L ( U E )?
            pass 
            self.mV()
            self.mA()
            self.mL()
            # SelectExpr.g:94:17: ( U E )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 85 or LA3_0 == 117) :
                alt3 = 1
            if alt3 == 1:
                # SelectExpr.g:94:18: U E
                pass 
                self.mU()
                self.mE()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS_VALUE"



    # $ANTLR start "AS_DICT"
    def mAS_DICT(self, ):

        try:
            _type = AS_DICT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:95:9: ( D I C T ( I O N A R Y )? )
            # SelectExpr.g:95:11: D I C T ( I O N A R Y )?
            pass 
            self.mD()
            self.mI()
            self.mC()
            self.mT()
            # SelectExpr.g:95:19: ( I O N A R Y )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 73 or LA4_0 == 105) :
                alt4 = 1
            if alt4 == 1:
                # SelectExpr.g:95:20: I O N A R Y
                pass 
                self.mI()
                self.mO()
                self.mN()
                self.mA()
                self.mR()
                self.mY()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS_DICT"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:97:9: ( ( ( '\\r' )? '\\n' ) )
            # SelectExpr.g:97:11: ( ( '\\r' )? '\\n' )
            pass 
            # SelectExpr.g:97:11: ( ( '\\r' )? '\\n' )
            # SelectExpr.g:97:12: ( '\\r' )? '\\n'
            pass 
            # SelectExpr.g:97:12: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # SelectExpr.g:97:12: '\\r'
                pass 
                self.match(13)



            self.match(10)



            #action start
            self.skip()
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:98:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # SelectExpr.g:98:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # SelectExpr.g:98:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((9 <= LA6_0 <= 10) or LA6_0 == 13 or LA6_0 == 32) :
                    alt6 = 1


                if alt6 == 1:
                    # SelectExpr.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1
            #action start
            self.skip()
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:100:9: ( '/*' ( . )* '*/' )
            # SelectExpr.g:100:11: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # SelectExpr.g:100:16: ( . )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 42) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 47) :
                        alt7 = 2
                    elif ((0 <= LA7_1 <= 46) or (48 <= LA7_1 <= 65535)) :
                        alt7 = 1


                elif ((0 <= LA7_0 <= 41) or (43 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # SelectExpr.g:100:16: .
                    pass 
                    self.matchAny()


                else:
                    break #loop7
            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:101:14: ( '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # SelectExpr.g:101:16: '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # SelectExpr.g:101:20: (~ ( '\\n' | '\\r' ) )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((0 <= LA8_0 <= 9) or (11 <= LA8_0 <= 12) or (14 <= LA8_0 <= 65535)) :
                    alt8 = 1


                if alt8 == 1:
                    # SelectExpr.g:101:20: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop8
            # SelectExpr.g:101:34: ( '\\r' )?
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 13) :
                alt9 = 1
            if alt9 == 1:
                # SelectExpr.g:101:34: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:103:9: ( DQ (~ ( DQ ) )* DQ | SQ (~ ( SQ ) )* SQ )
            alt12 = 2
            LA12_0 = self.input.LA(1)

            if (LA12_0 == 34) :
                alt12 = 1
            elif (LA12_0 == 39) :
                alt12 = 2
            else:
                nvae = NoViableAltException("", 12, 0, self.input)

                raise nvae

            if alt12 == 1:
                # SelectExpr.g:103:11: DQ (~ ( DQ ) )* DQ
                pass 
                self.mDQ()
                # SelectExpr.g:103:14: (~ ( DQ ) )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 65535)) :
                        alt10 = 1


                    if alt10 == 1:
                        # SelectExpr.g:103:15: ~ ( DQ )
                        pass 
                        if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop10
                self.mDQ()


            elif alt12 == 2:
                # SelectExpr.g:103:28: SQ (~ ( SQ ) )* SQ
                pass 
                self.mSQ()
                # SelectExpr.g:103:31: (~ ( SQ ) )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((0 <= LA11_0 <= 38) or (40 <= LA11_0 <= 65535)) :
                        alt11 = 1


                    if alt11 == 1:
                        # SelectExpr.g:103:32: ~ ( SQ )
                        pass 
                        if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop11
                self.mSQ()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:104:9: ( ( DIGIT )+ )
            # SelectExpr.g:104:11: ( DIGIT )+
            pass 
            # SelectExpr.g:104:11: ( DIGIT )+
            cnt13 = 0
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if ((48 <= LA13_0 <= 57)) :
                    alt13 = 1


                if alt13 == 1:
                    # SelectExpr.g:104:11: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt13 >= 1:
                        break #loop13

                    eee = EarlyExitException(13, self.input)
                    raise eee

                cnt13 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:105:8: ( ( DIGIT )* DOT ( DIGIT )* )
            # SelectExpr.g:105:10: ( DIGIT )* DOT ( DIGIT )*
            pass 
            # SelectExpr.g:105:10: ( DIGIT )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((48 <= LA14_0 <= 57)) :
                    alt14 = 1


                if alt14 == 1:
                    # SelectExpr.g:105:10: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop14
            self.mDOT()
            # SelectExpr.g:105:21: ( DIGIT )*
            while True: #loop15
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if ((48 <= LA15_0 <= 57)) :
                    alt15 = 1


                if alt15 == 1:
                    # SelectExpr.g:105:21: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop15



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:106:7: ( ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )
            # SelectExpr.g:106:9: ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:107:8: ( ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )
            # SelectExpr.g:107:10: ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "PHRASE"
    def mPHRASE(self, ):

        try:
            _type = PHRASE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:109:8: ( ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )* )
            # SelectExpr.g:109:10: ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SelectExpr.g:109:32: ( DIGIT | CHARACTER | SPECIAL )*
            while True: #loop16
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((48 <= LA16_0 <= 57) or (65 <= LA16_0 <= 90) or LA16_0 == 95 or (97 <= LA16_0 <= 122)) :
                    alt16 = 1


                if alt16 == 1:
                    # SelectExpr.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop16



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PHRASE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # SelectExpr.g:111:20: ( '0' .. '9' )
            # SelectExpr.g:111:22: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "CHARACTER"
    def mCHARACTER(self, ):

        try:
            # SelectExpr.g:112:20: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # SelectExpr.g:112:22: ( 'a' .. 'z' | 'A' .. 'Z' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "CHARACTER"



    # $ANTLR start "SPECIAL"
    def mSPECIAL(self, ):

        try:
            # SelectExpr.g:113:20: ( '_' )
            # SelectExpr.g:113:22: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "SPECIAL"



    # $ANTLR start "A"
    def mA(self, ):

        try:
            # SelectExpr.g:115:12: ( ( 'A' | 'a' ) )
            # SelectExpr.g:115:14: ( 'A' | 'a' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "A"



    # $ANTLR start "N"
    def mN(self, ):

        try:
            # SelectExpr.g:115:12: ( ( 'N' | 'n' ) )
            # SelectExpr.g:115:14: ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "N"



    # $ANTLR start "B"
    def mB(self, ):

        try:
            # SelectExpr.g:116:12: ( ( 'B' | 'b' ) )
            # SelectExpr.g:116:14: ( 'B' | 'b' )
            pass 
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "B"



    # $ANTLR start "O"
    def mO(self, ):

        try:
            # SelectExpr.g:116:12: ( ( 'O' | 'o' ) )
            # SelectExpr.g:116:14: ( 'O' | 'o' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "O"



    # $ANTLR start "C"
    def mC(self, ):

        try:
            # SelectExpr.g:117:12: ( ( 'C' | 'c' ) )
            # SelectExpr.g:117:14: ( 'C' | 'c' )
            pass 
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "C"



    # $ANTLR start "P"
    def mP(self, ):

        try:
            # SelectExpr.g:117:12: ( ( 'P' | 'p' ) )
            # SelectExpr.g:117:14: ( 'P' | 'p' )
            pass 
            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "P"



    # $ANTLR start "D"
    def mD(self, ):

        try:
            # SelectExpr.g:118:12: ( ( 'D' | 'd' ) )
            # SelectExpr.g:118:14: ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "D"



    # $ANTLR start "Q"
    def mQ(self, ):

        try:
            # SelectExpr.g:118:12: ( ( 'Q' | 'q' ) )
            # SelectExpr.g:118:14: ( 'Q' | 'q' )
            pass 
            if self.input.LA(1) == 81 or self.input.LA(1) == 113:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Q"



    # $ANTLR start "E"
    def mE(self, ):

        try:
            # SelectExpr.g:119:12: ( ( 'E' | 'e' ) )
            # SelectExpr.g:119:14: ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "E"



    # $ANTLR start "R"
    def mR(self, ):

        try:
            # SelectExpr.g:119:12: ( ( 'R' | 'r' ) )
            # SelectExpr.g:119:14: ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "R"



    # $ANTLR start "F"
    def mF(self, ):

        try:
            # SelectExpr.g:120:12: ( ( 'F' | 'f' ) )
            # SelectExpr.g:120:14: ( 'F' | 'f' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "F"



    # $ANTLR start "S"
    def mS(self, ):

        try:
            # SelectExpr.g:120:12: ( ( 'S' | 's' ) )
            # SelectExpr.g:120:14: ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "S"



    # $ANTLR start "G"
    def mG(self, ):

        try:
            # SelectExpr.g:121:12: ( ( 'G' | 'g' ) )
            # SelectExpr.g:121:14: ( 'G' | 'g' )
            pass 
            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "G"



    # $ANTLR start "T"
    def mT(self, ):

        try:
            # SelectExpr.g:121:12: ( ( 'T' | 't' ) )
            # SelectExpr.g:121:14: ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "T"



    # $ANTLR start "H"
    def mH(self, ):

        try:
            # SelectExpr.g:122:12: ( ( 'H' | 'h' ) )
            # SelectExpr.g:122:14: ( 'H' | 'h' )
            pass 
            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "H"



    # $ANTLR start "U"
    def mU(self, ):

        try:
            # SelectExpr.g:122:12: ( ( 'U' | 'u' ) )
            # SelectExpr.g:122:14: ( 'U' | 'u' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "U"



    # $ANTLR start "I"
    def mI(self, ):

        try:
            # SelectExpr.g:123:12: ( ( 'I' | 'i' ) )
            # SelectExpr.g:123:14: ( 'I' | 'i' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "I"



    # $ANTLR start "V"
    def mV(self, ):

        try:
            # SelectExpr.g:123:12: ( ( 'V' | 'v' ) )
            # SelectExpr.g:123:14: ( 'V' | 'v' )
            pass 
            if self.input.LA(1) == 86 or self.input.LA(1) == 118:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "V"



    # $ANTLR start "J"
    def mJ(self, ):

        try:
            # SelectExpr.g:124:12: ( ( 'J' | 'j' ) )
            # SelectExpr.g:124:14: ( 'J' | 'j' )
            pass 
            if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "J"



    # $ANTLR start "W"
    def mW(self, ):

        try:
            # SelectExpr.g:124:12: ( ( 'W' | 'w' ) )
            # SelectExpr.g:124:14: ( 'W' | 'w' )
            pass 
            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "W"



    # $ANTLR start "K"
    def mK(self, ):

        try:
            # SelectExpr.g:125:12: ( ( 'K' | 'k' ) )
            # SelectExpr.g:125:14: ( 'K' | 'k' )
            pass 
            if self.input.LA(1) == 75 or self.input.LA(1) == 107:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "K"



    # $ANTLR start "X"
    def mX(self, ):

        try:
            # SelectExpr.g:125:12: ( ( 'X' | 'x' ) )
            # SelectExpr.g:125:14: ( 'X' | 'x' )
            pass 
            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "X"



    # $ANTLR start "L"
    def mL(self, ):

        try:
            # SelectExpr.g:126:12: ( ( 'L' | 'l' ) )
            # SelectExpr.g:126:14: ( 'L' | 'l' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "L"



    # $ANTLR start "Y"
    def mY(self, ):

        try:
            # SelectExpr.g:126:12: ( ( 'Y' | 'y' ) )
            # SelectExpr.g:126:14: ( 'Y' | 'y' )
            pass 
            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Y"



    # $ANTLR start "M"
    def mM(self, ):

        try:
            # SelectExpr.g:127:12: ( ( 'M' | 'm' ) )
            # SelectExpr.g:127:14: ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "M"



    # $ANTLR start "Z"
    def mZ(self, ):

        try:
            # SelectExpr.g:127:12: ( ( 'Z' | 'z' ) )
            # SelectExpr.g:127:14: ( 'Z' | 'z' )
            pass 
            if self.input.LA(1) == 90 or self.input.LA(1) == 122:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Z"



    def mTokens(self):
        # SelectExpr.g:1:8: ( T__98 | T__99 | DOT | SEP | END | COLON | AND | XOR | OR | NOT | IN | ASSIGN | EQ | NE | LE | GE | LT | GT | ADD | SUB | MUL | DIV | MOD | POW | SQ | DQ | LIST_BEGIN | LIST_END | AGE_BEGIN | AGE_END | SELECT | FROM | WHERE | ORDER | GROUP | HAVING | BY | AS | THIS | TIME | CONNECT | START | STOP | WITH | ASC | DESC | AS_LIST | AS_VALUE | AS_DICT | NEWLINE | WS | COMMENT | LINE_COMMENT | STRING | INTEGER | FLOAT | TRUE | FALSE | PHRASE )
        alt17 = 59
        alt17 = self.dfa17.predict(self.input)
        if alt17 == 1:
            # SelectExpr.g:1:10: T__98
            pass 
            self.mT__98()


        elif alt17 == 2:
            # SelectExpr.g:1:16: T__99
            pass 
            self.mT__99()


        elif alt17 == 3:
            # SelectExpr.g:1:22: DOT
            pass 
            self.mDOT()


        elif alt17 == 4:
            # SelectExpr.g:1:26: SEP
            pass 
            self.mSEP()


        elif alt17 == 5:
            # SelectExpr.g:1:30: END
            pass 
            self.mEND()


        elif alt17 == 6:
            # SelectExpr.g:1:34: COLON
            pass 
            self.mCOLON()


        elif alt17 == 7:
            # SelectExpr.g:1:40: AND
            pass 
            self.mAND()


        elif alt17 == 8:
            # SelectExpr.g:1:44: XOR
            pass 
            self.mXOR()


        elif alt17 == 9:
            # SelectExpr.g:1:48: OR
            pass 
            self.mOR()


        elif alt17 == 10:
            # SelectExpr.g:1:51: NOT
            pass 
            self.mNOT()


        elif alt17 == 11:
            # SelectExpr.g:1:55: IN
            pass 
            self.mIN()


        elif alt17 == 12:
            # SelectExpr.g:1:58: ASSIGN
            pass 
            self.mASSIGN()


        elif alt17 == 13:
            # SelectExpr.g:1:65: EQ
            pass 
            self.mEQ()


        elif alt17 == 14:
            # SelectExpr.g:1:68: NE
            pass 
            self.mNE()


        elif alt17 == 15:
            # SelectExpr.g:1:71: LE
            pass 
            self.mLE()


        elif alt17 == 16:
            # SelectExpr.g:1:74: GE
            pass 
            self.mGE()


        elif alt17 == 17:
            # SelectExpr.g:1:77: LT
            pass 
            self.mLT()


        elif alt17 == 18:
            # SelectExpr.g:1:80: GT
            pass 
            self.mGT()


        elif alt17 == 19:
            # SelectExpr.g:1:83: ADD
            pass 
            self.mADD()


        elif alt17 == 20:
            # SelectExpr.g:1:87: SUB
            pass 
            self.mSUB()


        elif alt17 == 21:
            # SelectExpr.g:1:91: MUL
            pass 
            self.mMUL()


        elif alt17 == 22:
            # SelectExpr.g:1:95: DIV
            pass 
            self.mDIV()


        elif alt17 == 23:
            # SelectExpr.g:1:99: MOD
            pass 
            self.mMOD()


        elif alt17 == 24:
            # SelectExpr.g:1:103: POW
            pass 
            self.mPOW()


        elif alt17 == 25:
            # SelectExpr.g:1:107: SQ
            pass 
            self.mSQ()


        elif alt17 == 26:
            # SelectExpr.g:1:110: DQ
            pass 
            self.mDQ()


        elif alt17 == 27:
            # SelectExpr.g:1:113: LIST_BEGIN
            pass 
            self.mLIST_BEGIN()


        elif alt17 == 28:
            # SelectExpr.g:1:124: LIST_END
            pass 
            self.mLIST_END()


        elif alt17 == 29:
            # SelectExpr.g:1:133: AGE_BEGIN
            pass 
            self.mAGE_BEGIN()


        elif alt17 == 30:
            # SelectExpr.g:1:143: AGE_END
            pass 
            self.mAGE_END()


        elif alt17 == 31:
            # SelectExpr.g:1:151: SELECT
            pass 
            self.mSELECT()


        elif alt17 == 32:
            # SelectExpr.g:1:158: FROM
            pass 
            self.mFROM()


        elif alt17 == 33:
            # SelectExpr.g:1:163: WHERE
            pass 
            self.mWHERE()


        elif alt17 == 34:
            # SelectExpr.g:1:169: ORDER
            pass 
            self.mORDER()


        elif alt17 == 35:
            # SelectExpr.g:1:175: GROUP
            pass 
            self.mGROUP()


        elif alt17 == 36:
            # SelectExpr.g:1:181: HAVING
            pass 
            self.mHAVING()


        elif alt17 == 37:
            # SelectExpr.g:1:188: BY
            pass 
            self.mBY()


        elif alt17 == 38:
            # SelectExpr.g:1:191: AS
            pass 
            self.mAS()


        elif alt17 == 39:
            # SelectExpr.g:1:194: THIS
            pass 
            self.mTHIS()


        elif alt17 == 40:
            # SelectExpr.g:1:199: TIME
            pass 
            self.mTIME()


        elif alt17 == 41:
            # SelectExpr.g:1:204: CONNECT
            pass 
            self.mCONNECT()


        elif alt17 == 42:
            # SelectExpr.g:1:212: START
            pass 
            self.mSTART()


        elif alt17 == 43:
            # SelectExpr.g:1:218: STOP
            pass 
            self.mSTOP()


        elif alt17 == 44:
            # SelectExpr.g:1:223: WITH
            pass 
            self.mWITH()


        elif alt17 == 45:
            # SelectExpr.g:1:228: ASC
            pass 
            self.mASC()


        elif alt17 == 46:
            # SelectExpr.g:1:232: DESC
            pass 
            self.mDESC()


        elif alt17 == 47:
            # SelectExpr.g:1:237: AS_LIST
            pass 
            self.mAS_LIST()


        elif alt17 == 48:
            # SelectExpr.g:1:245: AS_VALUE
            pass 
            self.mAS_VALUE()


        elif alt17 == 49:
            # SelectExpr.g:1:254: AS_DICT
            pass 
            self.mAS_DICT()


        elif alt17 == 50:
            # SelectExpr.g:1:262: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt17 == 51:
            # SelectExpr.g:1:270: WS
            pass 
            self.mWS()


        elif alt17 == 52:
            # SelectExpr.g:1:273: COMMENT
            pass 
            self.mCOMMENT()


        elif alt17 == 53:
            # SelectExpr.g:1:281: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt17 == 54:
            # SelectExpr.g:1:294: STRING
            pass 
            self.mSTRING()


        elif alt17 == 55:
            # SelectExpr.g:1:301: INTEGER
            pass 
            self.mINTEGER()


        elif alt17 == 56:
            # SelectExpr.g:1:309: FLOAT
            pass 
            self.mFLOAT()


        elif alt17 == 57:
            # SelectExpr.g:1:315: TRUE
            pass 
            self.mTRUE()


        elif alt17 == 58:
            # SelectExpr.g:1:320: FALSE
            pass 
            self.mFALSE()


        elif alt17 == 59:
            # SelectExpr.g:1:326: PHRASE
            pass 
            self.mPHRASE()







    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\3\uffff\1\55\3\uffff\5\54\1\66\1\uffff\1\70\1\72\3\uffff\1\74"
        u"\2\uffff\1\75\1\77\4\uffff\13\54\1\51\1\121\2\uffff\1\122\3\uffff"
        u"\1\123\2\54\1\127\1\54\1\132\13\uffff\10\54\1\144\10\54\3\uffff"
        u"\1\155\1\157\1\160\1\uffff\1\54\1\162\1\uffff\11\54\1\uffff\7\54"
        u"\1\u0083\1\uffff\1\54\2\uffff\1\54\1\uffff\1\u0087\3\54\1\u008b"
        u"\1\54\1\u008d\2\54\1\u0090\1\u0091\1\u0092\1\54\1\u0094\1\u0096"
        u"\1\u0098\1\uffff\2\54\1\u009b\1\uffff\1\u009c\1\54\1\u009e\1\uffff"
        u"\1\u009f\1\uffff\1\u00a0\1\54\3\uffff\1\54\1\uffff\1\54\1\uffff"
        u"\1\54\1\uffff\1\u0083\1\54\2\uffff\1\u00a6\3\uffff\1\u00a7\4\54"
        u"\2\uffff\1\u00ac\3\54\1\uffff\2\54\1\155\2\54\1\u0094\1\u0096"
        )

    DFA17_eof = DFA.unpack(
        u"\u00b4\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\11\2\uffff\1\60\3\uffff\1\116\1\117\1\122\1\117\1\116\1\75\1"
        u"\uffff\2\75\3\uffff\1\52\2\uffff\2\0\4\uffff\1\105\1\101\1\110"
        u"\1\122\1\101\1\131\1\110\1\117\1\105\1\111\1\101\1\12\1\11\2\uffff"
        u"\1\56\3\uffff\1\60\1\104\1\122\1\60\1\124\1\60\13\uffff\1\101\2"
        u"\114\1\117\1\105\1\124\1\117\1\126\1\60\1\125\1\115\1\111\1\116"
        u"\1\103\2\123\1\114\3\uffff\3\60\1\uffff\1\105\1\60\1\uffff\1\120"
        u"\1\122\1\105\1\123\1\115\1\122\1\110\1\125\1\111\1\uffff\2\105"
        u"\1\123\1\116\1\124\1\103\1\124\1\60\1\uffff\1\116\2\uffff\1\122"
        u"\1\uffff\1\60\1\124\1\103\1\105\1\60\1\105\1\60\1\120\1\116\3\60"
        u"\1\105\3\60\1\uffff\1\105\1\104\1\60\1\uffff\1\60\1\124\1\60\1"
        u"\uffff\1\60\1\uffff\1\60\1\107\3\uffff\1\103\1\uffff\1\117\1\uffff"
        u"\1\116\1\uffff\1\60\1\111\2\uffff\1\60\3\uffff\1\60\1\124\1\116"
        u"\1\104\1\116\2\uffff\1\60\1\101\1\111\1\107\1\uffff\1\122\1\116"
        u"\1\60\1\131\1\107\2\60"
        )

    DFA17_max = DFA.unpack(
        u"\1\175\2\uffff\1\71\3\uffff\1\163\1\157\1\162\1\157\1\156\1\75"
        u"\1\uffff\2\75\3\uffff\1\52\2\uffff\2\uffff\4\uffff\1\164\1\162"
        u"\1\151\1\162\1\141\1\171\1\162\1\157\2\151\1\141\1\12\1\40\2\uffff"
        u"\1\71\3\uffff\1\172\1\144\1\162\1\172\1\164\1\172\13\uffff\1\157"
        u"\2\154\1\157\1\145\1\164\1\157\1\166\1\172\1\165\1\155\1\151\1"
        u"\156\1\143\2\163\1\154\3\uffff\3\172\1\uffff\1\145\1\172\1\uffff"
        u"\1\160\1\162\1\145\1\163\1\155\1\162\1\150\1\165\1\151\1\uffff"
        u"\2\145\1\163\1\156\1\164\1\143\1\164\1\172\1\uffff\1\156\2\uffff"
        u"\1\162\1\uffff\1\172\1\164\1\143\1\145\1\172\1\145\1\172\1\160"
        u"\1\156\3\172\1\145\3\172\1\uffff\1\145\1\144\1\172\1\uffff\1\172"
        u"\1\164\1\172\1\uffff\1\172\1\uffff\1\172\1\147\3\uffff\1\143\1"
        u"\uffff\1\157\1\uffff\1\156\1\uffff\1\172\1\151\2\uffff\1\172\3"
        u"\uffff\1\172\1\164\1\156\1\144\1\156\2\uffff\1\172\1\141\1\151"
        u"\1\147\1\uffff\1\162\1\156\1\172\1\171\1\147\2\172"
        )

    DFA17_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\uffff\1\4\1\5\1\6\6\uffff\1\16\2\uffff\1\23"
        u"\1\24\1\25\1\uffff\1\27\1\30\2\uffff\1\33\1\34\1\35\1\36\15\uffff"
        u"\1\63\1\65\1\uffff\1\73\1\3\1\70\6\uffff\1\15\1\14\1\17\1\21\1"
        u"\20\1\22\1\64\1\26\1\31\1\66\1\32\21\uffff\1\62\1\67\1\46\3\uffff"
        u"\1\11\2\uffff\1\13\11\uffff\1\45\10\uffff\1\55\1\uffff\1\7\1\10"
        u"\1\uffff\1\12\20\uffff\1\60\3\uffff\1\53\3\uffff\1\40\1\uffff\1"
        u"\54\2\uffff\1\71\1\50\1\47\1\uffff\1\61\1\uffff\1\56\1\uffff\1"
        u"\57\2\uffff\1\42\1\52\1\uffff\1\72\1\41\1\43\5\uffff\1\37\1\44"
        u"\4\uffff\1\51\7\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\26\uffff\1\1\1\0\u009c\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\51\1\50\2\uffff\1\47\22\uffff\1\51\1\15\1\27\1\52"
        u"\1\uffff\1\24\1\uffff\1\26\1\1\1\2\1\22\1\20\1\4\1\21\1\3\1\23"
        u"\12\53\1\6\1\5\1\16\1\14\1\17\2\uffff\1\7\1\41\1\43\1\44\1\54\1"
        u"\35\1\37\1\40\1\13\2\54\1\45\1\54\1\12\1\11\3\54\1\34\1\42\1\54"
        u"\1\46\1\36\1\10\2\54\1\30\1\uffff\1\31\1\25\1\54\1\uffff\1\7\1"
        u"\41\1\43\1\44\1\54\1\35\1\37\1\40\1\13\2\54\1\45\1\54\1\12\1\11"
        u"\3\54\1\34\1\42\1\54\1\46\1\36\1\10\2\54\1\32\1\uffff\1\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60\4\uffff\1\57\32\uffff\1\60\4\uffff\1\57"),
        DFA.unpack(u"\1\61\37\uffff\1\61"),
        DFA.unpack(u"\1\62\37\uffff\1\62"),
        DFA.unpack(u"\1\63\37\uffff\1\63"),
        DFA.unpack(u"\1\64\37\uffff\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\0\76"),
        DFA.unpack(u"\0\76"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101\16\uffff\1\100\20\uffff\1\101\16\uffff\1\100"),
        DFA.unpack(u"\1\102\20\uffff\1\103\16\uffff\1\102\20\uffff\1\103"),
        DFA.unpack(u"\1\104\1\105\36\uffff\1\104\1\105"),
        DFA.unpack(u"\1\106\37\uffff\1\106"),
        DFA.unpack(u"\1\107\37\uffff\1\107"),
        DFA.unpack(u"\1\110\37\uffff\1\110"),
        DFA.unpack(u"\1\113\1\112\10\uffff\1\111\25\uffff\1\113\1\112\10"
        u"\uffff\1\111"),
        DFA.unpack(u"\1\114\37\uffff\1\114"),
        DFA.unpack(u"\1\116\3\uffff\1\115\33\uffff\1\116\3\uffff\1\115"),
        DFA.unpack(u"\1\117\37\uffff\1\117"),
        DFA.unpack(u"\1\120\37\uffff\1\120"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\2\51\2\uffff\1\51\22\uffff\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56\1\uffff\12\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\2\54\1\124\27\54\4\uffff\1\54\1\uffff"
        u"\2\54\1\124\27\54"),
        DFA.unpack(u"\1\125\37\uffff\1\125"),
        DFA.unpack(u"\1\126\37\uffff\1\126"),
        DFA.unpack(u"\12\54\7\uffff\3\54\1\130\26\54\4\uffff\1\54\1\uffff"
        u"\3\54\1\130\26\54"),
        DFA.unpack(u"\1\131\37\uffff\1\131"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
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
        DFA.unpack(u"\1\134\15\uffff\1\133\21\uffff\1\134\15\uffff\1\133"),
        DFA.unpack(u"\1\135\37\uffff\1\135"),
        DFA.unpack(u"\1\136\37\uffff\1\136"),
        DFA.unpack(u"\1\137\37\uffff\1\137"),
        DFA.unpack(u"\1\140\37\uffff\1\140"),
        DFA.unpack(u"\1\141\37\uffff\1\141"),
        DFA.unpack(u"\1\142\37\uffff\1\142"),
        DFA.unpack(u"\1\143\37\uffff\1\143"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\145\37\uffff\1\145"),
        DFA.unpack(u"\1\146\37\uffff\1\146"),
        DFA.unpack(u"\1\147\37\uffff\1\147"),
        DFA.unpack(u"\1\150\37\uffff\1\150"),
        DFA.unpack(u"\1\151\37\uffff\1\151"),
        DFA.unpack(u"\1\152\37\uffff\1\152"),
        DFA.unpack(u"\1\153\37\uffff\1\153"),
        DFA.unpack(u"\1\154\37\uffff\1\154"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\4\54\1\156\25\54\4\uffff\1\54\1\uffff"
        u"\4\54\1\156\25\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\163\37\uffff\1\163"),
        DFA.unpack(u"\1\164\37\uffff\1\164"),
        DFA.unpack(u"\1\165\37\uffff\1\165"),
        DFA.unpack(u"\1\166\37\uffff\1\166"),
        DFA.unpack(u"\1\167\37\uffff\1\167"),
        DFA.unpack(u"\1\170\37\uffff\1\170"),
        DFA.unpack(u"\1\171\37\uffff\1\171"),
        DFA.unpack(u"\1\172\37\uffff\1\172"),
        DFA.unpack(u"\1\173\37\uffff\1\173"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\174\37\uffff\1\174"),
        DFA.unpack(u"\1\175\37\uffff\1\175"),
        DFA.unpack(u"\1\176\37\uffff\1\176"),
        DFA.unpack(u"\1\177\37\uffff\1\177"),
        DFA.unpack(u"\1\u0080\37\uffff\1\u0080"),
        DFA.unpack(u"\1\u0081\37\uffff\1\u0081"),
        DFA.unpack(u"\1\u0082\37\uffff\1\u0082"),
        DFA.unpack(u"\12\54\7\uffff\24\54\1\u0084\5\54\4\uffff\1\54\1\uffff"
        u"\24\54\1\u0084\5\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0085\37\uffff\1\u0085"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0086\37\uffff\1\u0086"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u0088\37\uffff\1\u0088"),
        DFA.unpack(u"\1\u0089\37\uffff\1\u0089"),
        DFA.unpack(u"\1\u008a\37\uffff\1\u008a"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u008c\37\uffff\1\u008c"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u008e\37\uffff\1\u008e"),
        DFA.unpack(u"\1\u008f\37\uffff\1\u008f"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u0093\37\uffff\1\u0093"),
        DFA.unpack(u"\12\54\7\uffff\10\54\1\u0095\21\54\4\uffff\1\54\1\uffff"
        u"\10\54\1\u0095\21\54"),
        DFA.unpack(u"\12\54\7\uffff\4\54\1\u0097\25\54\4\uffff\1\54\1\uffff"
        u"\4\54\1\u0097\25\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0099\37\uffff\1\u0099"),
        DFA.unpack(u"\1\u009a\37\uffff\1\u009a"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u009d\37\uffff\1\u009d"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00a1\37\uffff\1\u00a1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a2\37\uffff\1\u00a2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a3\37\uffff\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4\37\uffff\1\u00a4"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00a5\37\uffff\1\u00a5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00a8\37\uffff\1\u00a8"),
        DFA.unpack(u"\1\u00a9\37\uffff\1\u00a9"),
        DFA.unpack(u"\1\u00aa\37\uffff\1\u00aa"),
        DFA.unpack(u"\1\u00ab\37\uffff\1\u00ab"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00ad\37\uffff\1\u00ad"),
        DFA.unpack(u"\1\u00ae\37\uffff\1\u00ae"),
        DFA.unpack(u"\1\u00af\37\uffff\1\u00af"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b0\37\uffff\1\u00b0"),
        DFA.unpack(u"\1\u00b1\37\uffff\1\u00b1"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00b2\37\uffff\1\u00b2"),
        DFA.unpack(u"\1\u00b3\37\uffff\1\u00b3"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA17_23 = input.LA(1)

                s = -1
                if ((0 <= LA17_23 <= 65535)):
                    s = 62

                else:
                    s = 63

                if s >= 0:
                    return s
            elif s == 1: 
                LA17_22 = input.LA(1)

                s = -1
                if ((0 <= LA17_22 <= 65535)):
                    s = 62

                else:
                    s = 61

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 17, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SelectExprLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
