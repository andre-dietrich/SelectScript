# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2015-06-04 17:55:52

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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






    # $ANTLR start "T__107"
    def mT__107(self, ):

        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:7:8: ( '(' )
            # SelectExpr.g:7:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__107"



    # $ANTLR start "T__108"
    def mT__108(self, ):

        try:
            _type = T__108
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:8:8: ( ')' )
            # SelectExpr.g:8:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__108"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:40:6: ( '.' )
            # SelectExpr.g:40:8: '.'
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

            # SelectExpr.g:41:6: ( ',' )
            # SelectExpr.g:41:8: ','
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

            # SelectExpr.g:42:6: ( ';' )
            # SelectExpr.g:42:8: ';'
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

            # SelectExpr.g:43:8: ( ':' )
            # SelectExpr.g:43:10: ':'
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

            # SelectExpr.g:45:6: ( A N D )
            # SelectExpr.g:45:8: A N D
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

            # SelectExpr.g:46:6: ( X O R )
            # SelectExpr.g:46:8: X O R
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

            # SelectExpr.g:47:6: ( O R )
            # SelectExpr.g:47:8: O R
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

            # SelectExpr.g:48:6: ( N O T )
            # SelectExpr.g:48:8: N O T
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

            # SelectExpr.g:49:6: ( I N )
            # SelectExpr.g:49:8: I N
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

            # SelectExpr.g:51:8: ( '=' )
            # SelectExpr.g:51:11: '='
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

            # SelectExpr.g:53:4: ( '==' )
            # SelectExpr.g:53:6: '=='
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

            # SelectExpr.g:54:4: ( '!=' )
            # SelectExpr.g:54:6: '!='
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

            # SelectExpr.g:55:4: ( '<=' )
            # SelectExpr.g:55:6: '<='
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

            # SelectExpr.g:56:4: ( '>=' )
            # SelectExpr.g:56:6: '>='
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

            # SelectExpr.g:57:4: ( '<' )
            # SelectExpr.g:57:7: '<'
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

            # SelectExpr.g:58:4: ( '>' )
            # SelectExpr.g:58:7: '>'
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

            # SelectExpr.g:60:6: ( '+' )
            # SelectExpr.g:60:8: '+'
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

            # SelectExpr.g:61:6: ( '-' )
            # SelectExpr.g:61:8: '-'
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

            # SelectExpr.g:62:6: ( '*' )
            # SelectExpr.g:62:8: '*'
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

            # SelectExpr.g:63:6: ( '/' )
            # SelectExpr.g:63:8: '/'
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

            # SelectExpr.g:64:6: ( '%' )
            # SelectExpr.g:64:8: '%'
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

            # SelectExpr.g:65:6: ( '^' )
            # SelectExpr.g:65:8: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "POW"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:67:9: ( I F )
            # SelectExpr.g:67:11: I F
            pass 
            self.mI()
            self.mF()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "SQ"
    def mSQ(self, ):

        try:
            _type = SQ
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:69:5: ( '\\'' )
            # SelectExpr.g:69:7: '\\''
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

            # SelectExpr.g:70:5: ( '\\\"' )
            # SelectExpr.g:70:7: '\\\"'
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

            # SelectExpr.g:72:12: ( '[' )
            # SelectExpr.g:72:14: '['
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

            # SelectExpr.g:73:12: ( ']' )
            # SelectExpr.g:73:14: ']'
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

            # SelectExpr.g:75:11: ( '{' )
            # SelectExpr.g:75:13: '{'
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

            # SelectExpr.g:76:11: ( '}' )
            # SelectExpr.g:76:13: '}'
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

            # SelectExpr.g:78:8: ( S E L E C T )
            # SelectExpr.g:78:10: S E L E C T
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

            # SelectExpr.g:79:8: ( F R O M )
            # SelectExpr.g:79:10: F R O M
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

            # SelectExpr.g:80:8: ( W H E R E )
            # SelectExpr.g:80:10: W H E R E
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

            # SelectExpr.g:81:8: ( O R D E R )
            # SelectExpr.g:81:10: O R D E R
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

            # SelectExpr.g:82:8: ( G R O U P )
            # SelectExpr.g:82:10: G R O U P
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

            # SelectExpr.g:83:8: ( H A V I N G )
            # SelectExpr.g:83:10: H A V I N G
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

            # SelectExpr.g:84:8: ( B Y )
            # SelectExpr.g:84:10: B Y
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

            # SelectExpr.g:85:8: ( A S )
            # SelectExpr.g:85:10: A S
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

            # SelectExpr.g:87:8: ( T H I S )
            # SelectExpr.g:87:10: T H I S
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

            # SelectExpr.g:88:8: ( T I M E )
            # SelectExpr.g:88:10: T I M E
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

            # SelectExpr.g:90:8: ( C O N N E C T )
            # SelectExpr.g:90:10: C O N N E C T
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

            # SelectExpr.g:91:8: ( S T A R T )
            # SelectExpr.g:91:10: S T A R T
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

            # SelectExpr.g:92:8: ( S T O P )
            # SelectExpr.g:92:10: S T O P
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

            # SelectExpr.g:93:8: ( W I T H )
            # SelectExpr.g:93:10: W I T H
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



    # $ANTLR start "NO"
    def mNO(self, ):

        try:
            _type = NO
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:95:9: ( N O )
            # SelectExpr.g:95:11: N O
            pass 
            self.mN()
            self.mO()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NO"



    # $ANTLR start "CYCLE"
    def mCYCLE(self, ):

        try:
            _type = CYCLE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:96:9: ( C Y C L E )
            # SelectExpr.g:96:11: C Y C L E
            pass 
            self.mC()
            self.mY()
            self.mC()
            self.mL()
            self.mE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CYCLE"



    # $ANTLR start "UNIQUE"
    def mUNIQUE(self, ):

        try:
            _type = UNIQUE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:97:9: ( U N I Q U E )
            # SelectExpr.g:97:11: U N I Q U E
            pass 
            self.mU()
            self.mN()
            self.mI()
            self.mQ()
            self.mU()
            self.mE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNIQUE"



    # $ANTLR start "MEMORIZE"
    def mMEMORIZE(self, ):

        try:
            _type = MEMORIZE
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:98:9: ( M E M O R I Z E )
            # SelectExpr.g:98:11: M E M O R I Z E
            pass 
            self.mM()
            self.mE()
            self.mM()
            self.mO()
            self.mR()
            self.mI()
            self.mZ()
            self.mE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MEMORIZE"



    # $ANTLR start "MAXIMUM"
    def mMAXIMUM(self, ):

        try:
            _type = MAXIMUM
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:99:9: ( M A X I M U M )
            # SelectExpr.g:99:11: M A X I M U M
            pass 
            self.mM()
            self.mA()
            self.mX()
            self.mI()
            self.mM()
            self.mU()
            self.mM()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAXIMUM"



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:101:8: ( A S C ( E N D I N G )? )
            # SelectExpr.g:101:10: A S C ( E N D I N G )?
            pass 
            self.mA()
            self.mS()
            self.mC()
            # SelectExpr.g:101:16: ( E N D I N G )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 69 or LA1_0 == 101) :
                alt1 = 1
            if alt1 == 1:
                # SelectExpr.g:101:17: E N D I N G
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

            # SelectExpr.g:102:8: ( D E S C ( E N D I N G )? )
            # SelectExpr.g:102:10: D E S C ( E N D I N G )?
            pass 
            self.mD()
            self.mE()
            self.mS()
            self.mC()
            # SelectExpr.g:102:18: ( E N D I N G )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 69 or LA2_0 == 101) :
                alt2 = 1
            if alt2 == 1:
                # SelectExpr.g:102:19: E N D I N G
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

            # SelectExpr.g:104:9: ( L I S T )
            # SelectExpr.g:104:11: L I S T
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

            # SelectExpr.g:105:9: ( V A L ( U E )? )
            # SelectExpr.g:105:11: V A L ( U E )?
            pass 
            self.mV()
            self.mA()
            self.mL()
            # SelectExpr.g:105:17: ( U E )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 85 or LA3_0 == 117) :
                alt3 = 1
            if alt3 == 1:
                # SelectExpr.g:105:18: U E
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

            # SelectExpr.g:106:9: ( D I C T ( I O N A R Y )? )
            # SelectExpr.g:106:11: D I C T ( I O N A R Y )?
            pass 
            self.mD()
            self.mI()
            self.mC()
            self.mT()
            # SelectExpr.g:106:19: ( I O N A R Y )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 73 or LA4_0 == 105) :
                alt4 = 1
            if alt4 == 1:
                # SelectExpr.g:106:20: I O N A R Y
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

            # SelectExpr.g:108:9: ( ( ( '\\r' )? '\\n' ) )
            # SelectExpr.g:108:11: ( ( '\\r' )? '\\n' )
            pass 
            # SelectExpr.g:108:11: ( ( '\\r' )? '\\n' )
            # SelectExpr.g:108:12: ( '\\r' )? '\\n'
            pass 
            # SelectExpr.g:108:12: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # SelectExpr.g:108:12: '\\r'
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

            # SelectExpr.g:109:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # SelectExpr.g:109:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # SelectExpr.g:109:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
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

            # SelectExpr.g:111:9: ( '/*' ( . )* '*/' )
            # SelectExpr.g:111:11: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # SelectExpr.g:111:16: ( . )*
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
                    # SelectExpr.g:111:16: .
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

            # SelectExpr.g:112:14: ( '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # SelectExpr.g:112:16: '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # SelectExpr.g:112:20: (~ ( '\\n' | '\\r' ) )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((0 <= LA8_0 <= 9) or (11 <= LA8_0 <= 12) or (14 <= LA8_0 <= 65535)) :
                    alt8 = 1


                if alt8 == 1:
                    # SelectExpr.g:112:20: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop8
            # SelectExpr.g:112:34: ( '\\r' )?
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 13) :
                alt9 = 1
            if alt9 == 1:
                # SelectExpr.g:112:34: '\\r'
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

            # SelectExpr.g:114:9: ( DQ (~ ( DQ ) )* DQ | SQ (~ ( SQ ) )* SQ )
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
                # SelectExpr.g:114:11: DQ (~ ( DQ ) )* DQ
                pass 
                self.mDQ()
                # SelectExpr.g:114:14: (~ ( DQ ) )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 65535)) :
                        alt10 = 1


                    if alt10 == 1:
                        # SelectExpr.g:114:15: ~ ( DQ )
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
                # SelectExpr.g:114:28: SQ (~ ( SQ ) )* SQ
                pass 
                self.mSQ()
                # SelectExpr.g:114:31: (~ ( SQ ) )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((0 <= LA11_0 <= 38) or (40 <= LA11_0 <= 65535)) :
                        alt11 = 1


                    if alt11 == 1:
                        # SelectExpr.g:114:32: ~ ( SQ )
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

            # SelectExpr.g:115:9: ( ( DIGIT )+ )
            # SelectExpr.g:115:11: ( DIGIT )+
            pass 
            # SelectExpr.g:115:11: ( DIGIT )+
            cnt13 = 0
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if ((48 <= LA13_0 <= 57)) :
                    alt13 = 1


                if alt13 == 1:
                    # SelectExpr.g:115:11: DIGIT
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

            # SelectExpr.g:116:8: ( ( DIGIT )* DOT ( DIGIT )* )
            # SelectExpr.g:116:10: ( DIGIT )* DOT ( DIGIT )*
            pass 
            # SelectExpr.g:116:10: ( DIGIT )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((48 <= LA14_0 <= 57)) :
                    alt14 = 1


                if alt14 == 1:
                    # SelectExpr.g:116:10: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop14
            self.mDOT()
            # SelectExpr.g:116:21: ( DIGIT )*
            while True: #loop15
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if ((48 <= LA15_0 <= 57)) :
                    alt15 = 1


                if alt15 == 1:
                    # SelectExpr.g:116:21: DIGIT
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

            # SelectExpr.g:117:7: ( ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )
            # SelectExpr.g:117:9: ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' )
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

            # SelectExpr.g:118:8: ( ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )
            # SelectExpr.g:118:10: ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' )
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

            # SelectExpr.g:120:8: ( ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )* )
            # SelectExpr.g:120:10: ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SelectExpr.g:120:32: ( DIGIT | CHARACTER | SPECIAL )*
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
            # SelectExpr.g:122:20: ( '0' .. '9' )
            # SelectExpr.g:122:22: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "CHARACTER"
    def mCHARACTER(self, ):

        try:
            # SelectExpr.g:123:20: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # SelectExpr.g:123:22: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # SelectExpr.g:124:20: ( '_' )
            # SelectExpr.g:124:22: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "SPECIAL"



    # $ANTLR start "A"
    def mA(self, ):

        try:
            # SelectExpr.g:126:12: ( ( 'A' | 'a' ) )
            # SelectExpr.g:126:14: ( 'A' | 'a' )
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
            # SelectExpr.g:126:12: ( ( 'N' | 'n' ) )
            # SelectExpr.g:126:14: ( 'N' | 'n' )
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
            # SelectExpr.g:127:12: ( ( 'B' | 'b' ) )
            # SelectExpr.g:127:14: ( 'B' | 'b' )
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
            # SelectExpr.g:127:12: ( ( 'O' | 'o' ) )
            # SelectExpr.g:127:14: ( 'O' | 'o' )
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
            # SelectExpr.g:128:12: ( ( 'C' | 'c' ) )
            # SelectExpr.g:128:14: ( 'C' | 'c' )
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
            # SelectExpr.g:128:12: ( ( 'P' | 'p' ) )
            # SelectExpr.g:128:14: ( 'P' | 'p' )
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
            # SelectExpr.g:129:12: ( ( 'D' | 'd' ) )
            # SelectExpr.g:129:14: ( 'D' | 'd' )
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
            # SelectExpr.g:129:12: ( ( 'Q' | 'q' ) )
            # SelectExpr.g:129:14: ( 'Q' | 'q' )
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
            # SelectExpr.g:130:12: ( ( 'E' | 'e' ) )
            # SelectExpr.g:130:14: ( 'E' | 'e' )
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
            # SelectExpr.g:130:12: ( ( 'R' | 'r' ) )
            # SelectExpr.g:130:14: ( 'R' | 'r' )
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
            # SelectExpr.g:131:12: ( ( 'F' | 'f' ) )
            # SelectExpr.g:131:14: ( 'F' | 'f' )
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
            # SelectExpr.g:131:12: ( ( 'S' | 's' ) )
            # SelectExpr.g:131:14: ( 'S' | 's' )
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
            # SelectExpr.g:132:12: ( ( 'G' | 'g' ) )
            # SelectExpr.g:132:14: ( 'G' | 'g' )
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
            # SelectExpr.g:132:12: ( ( 'T' | 't' ) )
            # SelectExpr.g:132:14: ( 'T' | 't' )
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
            # SelectExpr.g:133:12: ( ( 'H' | 'h' ) )
            # SelectExpr.g:133:14: ( 'H' | 'h' )
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
            # SelectExpr.g:133:12: ( ( 'U' | 'u' ) )
            # SelectExpr.g:133:14: ( 'U' | 'u' )
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
            # SelectExpr.g:134:12: ( ( 'I' | 'i' ) )
            # SelectExpr.g:134:14: ( 'I' | 'i' )
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
            # SelectExpr.g:134:12: ( ( 'V' | 'v' ) )
            # SelectExpr.g:134:14: ( 'V' | 'v' )
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
            # SelectExpr.g:135:12: ( ( 'J' | 'j' ) )
            # SelectExpr.g:135:14: ( 'J' | 'j' )
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
            # SelectExpr.g:135:12: ( ( 'W' | 'w' ) )
            # SelectExpr.g:135:14: ( 'W' | 'w' )
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
            # SelectExpr.g:136:12: ( ( 'K' | 'k' ) )
            # SelectExpr.g:136:14: ( 'K' | 'k' )
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
            # SelectExpr.g:136:12: ( ( 'X' | 'x' ) )
            # SelectExpr.g:136:14: ( 'X' | 'x' )
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
            # SelectExpr.g:137:12: ( ( 'L' | 'l' ) )
            # SelectExpr.g:137:14: ( 'L' | 'l' )
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
            # SelectExpr.g:137:12: ( ( 'Y' | 'y' ) )
            # SelectExpr.g:137:14: ( 'Y' | 'y' )
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
            # SelectExpr.g:138:12: ( ( 'M' | 'm' ) )
            # SelectExpr.g:138:14: ( 'M' | 'm' )
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
            # SelectExpr.g:138:12: ( ( 'Z' | 'z' ) )
            # SelectExpr.g:138:14: ( 'Z' | 'z' )
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
        # SelectExpr.g:1:8: ( T__107 | T__108 | DOT | SEP | END | COLON | AND | XOR | OR | NOT | IN | ASSIGN | EQ | NE | LE | GE | LT | GT | ADD | SUB | MUL | DIV | MOD | POW | IF | SQ | DQ | LIST_BEGIN | LIST_END | AGE_BEGIN | AGE_END | SELECT | FROM | WHERE | ORDER | GROUP | HAVING | BY | AS | THIS | TIME | CONNECT | START | STOP | WITH | NO | CYCLE | UNIQUE | MEMORIZE | MAXIMUM | ASC | DESC | AS_LIST | AS_VALUE | AS_DICT | NEWLINE | WS | COMMENT | LINE_COMMENT | STRING | INTEGER | FLOAT | TRUE | FALSE | PHRASE )
        alt17 = 65
        alt17 = self.dfa17.predict(self.input)
        if alt17 == 1:
            # SelectExpr.g:1:10: T__107
            pass 
            self.mT__107()


        elif alt17 == 2:
            # SelectExpr.g:1:17: T__108
            pass 
            self.mT__108()


        elif alt17 == 3:
            # SelectExpr.g:1:24: DOT
            pass 
            self.mDOT()


        elif alt17 == 4:
            # SelectExpr.g:1:28: SEP
            pass 
            self.mSEP()


        elif alt17 == 5:
            # SelectExpr.g:1:32: END
            pass 
            self.mEND()


        elif alt17 == 6:
            # SelectExpr.g:1:36: COLON
            pass 
            self.mCOLON()


        elif alt17 == 7:
            # SelectExpr.g:1:42: AND
            pass 
            self.mAND()


        elif alt17 == 8:
            # SelectExpr.g:1:46: XOR
            pass 
            self.mXOR()


        elif alt17 == 9:
            # SelectExpr.g:1:50: OR
            pass 
            self.mOR()


        elif alt17 == 10:
            # SelectExpr.g:1:53: NOT
            pass 
            self.mNOT()


        elif alt17 == 11:
            # SelectExpr.g:1:57: IN
            pass 
            self.mIN()


        elif alt17 == 12:
            # SelectExpr.g:1:60: ASSIGN
            pass 
            self.mASSIGN()


        elif alt17 == 13:
            # SelectExpr.g:1:67: EQ
            pass 
            self.mEQ()


        elif alt17 == 14:
            # SelectExpr.g:1:70: NE
            pass 
            self.mNE()


        elif alt17 == 15:
            # SelectExpr.g:1:73: LE
            pass 
            self.mLE()


        elif alt17 == 16:
            # SelectExpr.g:1:76: GE
            pass 
            self.mGE()


        elif alt17 == 17:
            # SelectExpr.g:1:79: LT
            pass 
            self.mLT()


        elif alt17 == 18:
            # SelectExpr.g:1:82: GT
            pass 
            self.mGT()


        elif alt17 == 19:
            # SelectExpr.g:1:85: ADD
            pass 
            self.mADD()


        elif alt17 == 20:
            # SelectExpr.g:1:89: SUB
            pass 
            self.mSUB()


        elif alt17 == 21:
            # SelectExpr.g:1:93: MUL
            pass 
            self.mMUL()


        elif alt17 == 22:
            # SelectExpr.g:1:97: DIV
            pass 
            self.mDIV()


        elif alt17 == 23:
            # SelectExpr.g:1:101: MOD
            pass 
            self.mMOD()


        elif alt17 == 24:
            # SelectExpr.g:1:105: POW
            pass 
            self.mPOW()


        elif alt17 == 25:
            # SelectExpr.g:1:109: IF
            pass 
            self.mIF()


        elif alt17 == 26:
            # SelectExpr.g:1:112: SQ
            pass 
            self.mSQ()


        elif alt17 == 27:
            # SelectExpr.g:1:115: DQ
            pass 
            self.mDQ()


        elif alt17 == 28:
            # SelectExpr.g:1:118: LIST_BEGIN
            pass 
            self.mLIST_BEGIN()


        elif alt17 == 29:
            # SelectExpr.g:1:129: LIST_END
            pass 
            self.mLIST_END()


        elif alt17 == 30:
            # SelectExpr.g:1:138: AGE_BEGIN
            pass 
            self.mAGE_BEGIN()


        elif alt17 == 31:
            # SelectExpr.g:1:148: AGE_END
            pass 
            self.mAGE_END()


        elif alt17 == 32:
            # SelectExpr.g:1:156: SELECT
            pass 
            self.mSELECT()


        elif alt17 == 33:
            # SelectExpr.g:1:163: FROM
            pass 
            self.mFROM()


        elif alt17 == 34:
            # SelectExpr.g:1:168: WHERE
            pass 
            self.mWHERE()


        elif alt17 == 35:
            # SelectExpr.g:1:174: ORDER
            pass 
            self.mORDER()


        elif alt17 == 36:
            # SelectExpr.g:1:180: GROUP
            pass 
            self.mGROUP()


        elif alt17 == 37:
            # SelectExpr.g:1:186: HAVING
            pass 
            self.mHAVING()


        elif alt17 == 38:
            # SelectExpr.g:1:193: BY
            pass 
            self.mBY()


        elif alt17 == 39:
            # SelectExpr.g:1:196: AS
            pass 
            self.mAS()


        elif alt17 == 40:
            # SelectExpr.g:1:199: THIS
            pass 
            self.mTHIS()


        elif alt17 == 41:
            # SelectExpr.g:1:204: TIME
            pass 
            self.mTIME()


        elif alt17 == 42:
            # SelectExpr.g:1:209: CONNECT
            pass 
            self.mCONNECT()


        elif alt17 == 43:
            # SelectExpr.g:1:217: START
            pass 
            self.mSTART()


        elif alt17 == 44:
            # SelectExpr.g:1:223: STOP
            pass 
            self.mSTOP()


        elif alt17 == 45:
            # SelectExpr.g:1:228: WITH
            pass 
            self.mWITH()


        elif alt17 == 46:
            # SelectExpr.g:1:233: NO
            pass 
            self.mNO()


        elif alt17 == 47:
            # SelectExpr.g:1:236: CYCLE
            pass 
            self.mCYCLE()


        elif alt17 == 48:
            # SelectExpr.g:1:242: UNIQUE
            pass 
            self.mUNIQUE()


        elif alt17 == 49:
            # SelectExpr.g:1:249: MEMORIZE
            pass 
            self.mMEMORIZE()


        elif alt17 == 50:
            # SelectExpr.g:1:258: MAXIMUM
            pass 
            self.mMAXIMUM()


        elif alt17 == 51:
            # SelectExpr.g:1:266: ASC
            pass 
            self.mASC()


        elif alt17 == 52:
            # SelectExpr.g:1:270: DESC
            pass 
            self.mDESC()


        elif alt17 == 53:
            # SelectExpr.g:1:275: AS_LIST
            pass 
            self.mAS_LIST()


        elif alt17 == 54:
            # SelectExpr.g:1:283: AS_VALUE
            pass 
            self.mAS_VALUE()


        elif alt17 == 55:
            # SelectExpr.g:1:292: AS_DICT
            pass 
            self.mAS_DICT()


        elif alt17 == 56:
            # SelectExpr.g:1:300: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt17 == 57:
            # SelectExpr.g:1:308: WS
            pass 
            self.mWS()


        elif alt17 == 58:
            # SelectExpr.g:1:311: COMMENT
            pass 
            self.mCOMMENT()


        elif alt17 == 59:
            # SelectExpr.g:1:319: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt17 == 60:
            # SelectExpr.g:1:332: STRING
            pass 
            self.mSTRING()


        elif alt17 == 61:
            # SelectExpr.g:1:339: INTEGER
            pass 
            self.mINTEGER()


        elif alt17 == 62:
            # SelectExpr.g:1:347: FLOAT
            pass 
            self.mFLOAT()


        elif alt17 == 63:
            # SelectExpr.g:1:353: TRUE
            pass 
            self.mTRUE()


        elif alt17 == 64:
            # SelectExpr.g:1:358: FALSE
            pass 
            self.mFALSE()


        elif alt17 == 65:
            # SelectExpr.g:1:364: PHRASE
            pass 
            self.mPHRASE()







    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\3\uffff\1\57\3\uffff\5\56\1\71\1\uffff\1\73\1\75\3\uffff\1\77"
        u"\2\uffff\1\100\1\102\4\uffff\15\56\1\53\1\130\2\uffff\1\131\3\uffff"
        u"\1\56\1\133\1\56\1\136\1\140\1\142\1\143\13\uffff\10\56\1\155\14"
        u"\56\2\uffff\1\172\1\uffff\1\173\1\175\1\uffff\1\56\1\uffff\1\177"
        u"\2\uffff\11\56\1\uffff\13\56\1\u0094\2\uffff\1\56\1\uffff\1\56"
        u"\1\uffff\1\u0098\3\56\1\u009c\1\56\1\u009e\2\56\1\u00a1\1\u00a2"
        u"\1\u00a3\5\56\1\u00a9\1\u00ab\1\u00ad\1\uffff\2\56\1\u00b0\1\uffff"
        u"\1\u00b1\1\56\1\u00b3\1\uffff\1\u00b4\1\uffff\1\u00b5\1\56\3\uffff"
        u"\1\56\1\u00b8\3\56\1\uffff\1\56\1\uffff\1\56\1\uffff\1\u0094\1"
        u"\56\2\uffff\1\u00bf\3\uffff\1\u00c0\1\56\1\uffff\1\u00c2\5\56\2"
        u"\uffff\1\u00c8\1\uffff\1\56\1\u00ca\3\56\1\uffff\1\u00ce\1\uffff"
        u"\2\56\1\173\1\uffff\2\56\1\u00a9\1\u00ab"
        )

    DFA17_eof = DFA.unpack(
        u"\u00d3\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\11\2\uffff\1\60\3\uffff\1\116\1\117\1\122\1\117\1\106\1\75\1"
        u"\uffff\2\75\3\uffff\1\52\2\uffff\2\0\4\uffff\1\105\1\101\1\110"
        u"\1\122\1\101\1\131\1\110\1\117\1\116\1\101\1\105\1\111\1\101\1"
        u"\12\1\11\2\uffff\1\56\3\uffff\1\104\1\60\1\122\4\60\13\uffff\1"
        u"\101\2\114\1\117\1\105\1\124\1\117\1\126\1\60\1\125\1\115\1\111"
        u"\1\116\1\103\1\111\1\115\1\130\1\103\2\123\1\114\2\uffff\1\60\1"
        u"\uffff\2\60\1\uffff\1\105\1\uffff\1\60\2\uffff\1\120\1\122\1\105"
        u"\1\123\1\115\1\122\1\110\1\125\1\111\1\uffff\2\105\1\123\1\116"
        u"\1\114\1\121\1\117\1\111\1\124\1\103\1\124\1\60\2\uffff\1\116\1"
        u"\uffff\1\122\1\uffff\1\60\1\124\1\103\1\105\1\60\1\105\1\60\1\120"
        u"\1\116\3\60\2\105\1\125\1\122\1\115\3\60\1\uffff\1\105\1\104\1"
        u"\60\1\uffff\1\60\1\124\1\60\1\uffff\1\60\1\uffff\1\60\1\107\3\uffff"
        u"\1\103\1\60\1\105\1\111\1\125\1\uffff\1\117\1\uffff\1\116\1\uffff"
        u"\1\60\1\111\2\uffff\1\60\3\uffff\1\60\1\124\1\uffff\1\60\1\132"
        u"\1\115\1\116\1\104\1\116\2\uffff\1\60\1\uffff\1\105\1\60\1\101"
        u"\1\111\1\107\1\uffff\1\60\1\uffff\1\122\1\116\1\60\1\uffff\1\131"
        u"\1\107\2\60"
        )

    DFA17_max = DFA.unpack(
        u"\1\175\2\uffff\1\71\3\uffff\1\163\1\157\1\162\1\157\1\156\1\75"
        u"\1\uffff\2\75\3\uffff\1\52\2\uffff\2\uffff\4\uffff\1\164\1\162"
        u"\1\151\1\162\1\141\1\171\1\162\1\171\1\156\1\145\2\151\1\141\1"
        u"\12\1\40\2\uffff\1\71\3\uffff\1\144\1\172\1\162\4\172\13\uffff"
        u"\1\157\2\154\1\157\1\145\1\164\1\157\1\166\1\172\1\165\1\155\1"
        u"\151\1\156\1\143\1\151\1\155\1\170\1\143\2\163\1\154\2\uffff\1"
        u"\172\1\uffff\2\172\1\uffff\1\145\1\uffff\1\172\2\uffff\1\160\1"
        u"\162\1\145\1\163\1\155\1\162\1\150\1\165\1\151\1\uffff\2\145\1"
        u"\163\1\156\1\154\1\161\1\157\1\151\1\164\1\143\1\164\1\172\2\uffff"
        u"\1\156\1\uffff\1\162\1\uffff\1\172\1\164\1\143\1\145\1\172\1\145"
        u"\1\172\1\160\1\156\3\172\2\145\1\165\1\162\1\155\3\172\1\uffff"
        u"\1\145\1\144\1\172\1\uffff\1\172\1\164\1\172\1\uffff\1\172\1\uffff"
        u"\1\172\1\147\3\uffff\1\143\1\172\1\145\1\151\1\165\1\uffff\1\157"
        u"\1\uffff\1\156\1\uffff\1\172\1\151\2\uffff\1\172\3\uffff\1\172"
        u"\1\164\1\uffff\2\172\1\155\1\156\1\144\1\156\2\uffff\1\172\1\uffff"
        u"\1\145\1\172\1\141\1\151\1\147\1\uffff\1\172\1\uffff\1\162\1\156"
        u"\1\172\1\uffff\1\171\1\147\2\172"
        )

    DFA17_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\uffff\1\4\1\5\1\6\6\uffff\1\16\2\uffff\1\23"
        u"\1\24\1\25\1\uffff\1\27\1\30\2\uffff\1\34\1\35\1\36\1\37\17\uffff"
        u"\1\71\1\73\1\uffff\1\101\1\3\1\76\7\uffff\1\15\1\14\1\17\1\21\1"
        u"\20\1\22\1\72\1\26\1\32\1\74\1\33\25\uffff\1\70\1\75\1\uffff\1"
        u"\47\2\uffff\1\11\1\uffff\1\56\1\uffff\1\31\1\13\11\uffff\1\46\14"
        u"\uffff\1\7\1\63\1\uffff\1\10\1\uffff\1\12\24\uffff\1\66\3\uffff"
        u"\1\54\3\uffff\1\41\1\uffff\1\55\2\uffff\1\77\1\51\1\50\5\uffff"
        u"\1\67\1\uffff\1\64\1\uffff\1\65\2\uffff\1\43\1\53\1\uffff\1\100"
        u"\1\42\1\44\2\uffff\1\57\6\uffff\1\40\1\45\1\uffff\1\60\5\uffff"
        u"\1\52\1\uffff\1\62\3\uffff\1\61\4\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\26\uffff\1\1\1\0\u00bb\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\53\1\52\2\uffff\1\51\22\uffff\1\53\1\15\1\27\1\54"
        u"\1\uffff\1\24\1\uffff\1\26\1\1\1\2\1\22\1\20\1\4\1\21\1\3\1\23"
        u"\12\55\1\6\1\5\1\16\1\14\1\17\2\uffff\1\7\1\41\1\43\1\46\1\56\1"
        u"\35\1\37\1\40\1\13\2\56\1\47\1\45\1\12\1\11\3\56\1\34\1\42\1\44"
        u"\1\50\1\36\1\10\2\56\1\30\1\uffff\1\31\1\25\1\56\1\uffff\1\7\1"
        u"\41\1\43\1\46\1\56\1\35\1\37\1\40\1\13\2\56\1\47\1\45\1\12\1\11"
        u"\3\56\1\34\1\42\1\44\1\50\1\36\1\10\2\56\1\32\1\uffff\1\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\60"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\4\uffff\1\62\32\uffff\1\61\4\uffff\1\62"),
        DFA.unpack(u"\1\63\37\uffff\1\63"),
        DFA.unpack(u"\1\64\37\uffff\1\64"),
        DFA.unpack(u"\1\65\37\uffff\1\65"),
        DFA.unpack(u"\1\66\7\uffff\1\67\27\uffff\1\66\7\uffff\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\0\101"),
        DFA.unpack(u"\0\101"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104\16\uffff\1\103\20\uffff\1\104\16\uffff\1\103"),
        DFA.unpack(u"\1\105\20\uffff\1\106\16\uffff\1\105\20\uffff\1\106"),
        DFA.unpack(u"\1\107\1\110\36\uffff\1\107\1\110"),
        DFA.unpack(u"\1\111\37\uffff\1\111"),
        DFA.unpack(u"\1\112\37\uffff\1\112"),
        DFA.unpack(u"\1\113\37\uffff\1\113"),
        DFA.unpack(u"\1\116\1\115\10\uffff\1\114\25\uffff\1\116\1\115\10"
        u"\uffff\1\114"),
        DFA.unpack(u"\1\117\11\uffff\1\120\25\uffff\1\117\11\uffff\1\120"),
        DFA.unpack(u"\1\121\37\uffff\1\121"),
        DFA.unpack(u"\1\123\3\uffff\1\122\33\uffff\1\123\3\uffff\1\122"),
        DFA.unpack(u"\1\125\3\uffff\1\124\33\uffff\1\125\3\uffff\1\124"),
        DFA.unpack(u"\1\126\37\uffff\1\126"),
        DFA.unpack(u"\1\127\37\uffff\1\127"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\2\53\2\uffff\1\53\22\uffff\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60\1\uffff\12\55"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\132\37\uffff\1\132"),
        DFA.unpack(u"\12\56\7\uffff\2\56\1\134\27\56\4\uffff\1\56\1\uffff"
        u"\2\56\1\134\27\56"),
        DFA.unpack(u"\1\135\37\uffff\1\135"),
        DFA.unpack(u"\12\56\7\uffff\3\56\1\137\26\56\4\uffff\1\56\1\uffff"
        u"\3\56\1\137\26\56"),
        DFA.unpack(u"\12\56\7\uffff\23\56\1\141\6\56\4\uffff\1\56\1\uffff"
        u"\23\56\1\141\6\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
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
        DFA.unpack(u"\1\145\15\uffff\1\144\21\uffff\1\145\15\uffff\1\144"),
        DFA.unpack(u"\1\146\37\uffff\1\146"),
        DFA.unpack(u"\1\147\37\uffff\1\147"),
        DFA.unpack(u"\1\150\37\uffff\1\150"),
        DFA.unpack(u"\1\151\37\uffff\1\151"),
        DFA.unpack(u"\1\152\37\uffff\1\152"),
        DFA.unpack(u"\1\153\37\uffff\1\153"),
        DFA.unpack(u"\1\154\37\uffff\1\154"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\156\37\uffff\1\156"),
        DFA.unpack(u"\1\157\37\uffff\1\157"),
        DFA.unpack(u"\1\160\37\uffff\1\160"),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u"\1\162\37\uffff\1\162"),
        DFA.unpack(u"\1\163\37\uffff\1\163"),
        DFA.unpack(u"\1\164\37\uffff\1\164"),
        DFA.unpack(u"\1\165\37\uffff\1\165"),
        DFA.unpack(u"\1\166\37\uffff\1\166"),
        DFA.unpack(u"\1\167\37\uffff\1\167"),
        DFA.unpack(u"\1\170\37\uffff\1\170"),
        DFA.unpack(u"\1\171\37\uffff\1\171"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\4\56\1\174\25\56\4\uffff\1\56\1\uffff"
        u"\4\56\1\174\25\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\176\37\uffff\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0080\37\uffff\1\u0080"),
        DFA.unpack(u"\1\u0081\37\uffff\1\u0081"),
        DFA.unpack(u"\1\u0082\37\uffff\1\u0082"),
        DFA.unpack(u"\1\u0083\37\uffff\1\u0083"),
        DFA.unpack(u"\1\u0084\37\uffff\1\u0084"),
        DFA.unpack(u"\1\u0085\37\uffff\1\u0085"),
        DFA.unpack(u"\1\u0086\37\uffff\1\u0086"),
        DFA.unpack(u"\1\u0087\37\uffff\1\u0087"),
        DFA.unpack(u"\1\u0088\37\uffff\1\u0088"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0089\37\uffff\1\u0089"),
        DFA.unpack(u"\1\u008a\37\uffff\1\u008a"),
        DFA.unpack(u"\1\u008b\37\uffff\1\u008b"),
        DFA.unpack(u"\1\u008c\37\uffff\1\u008c"),
        DFA.unpack(u"\1\u008d\37\uffff\1\u008d"),
        DFA.unpack(u"\1\u008e\37\uffff\1\u008e"),
        DFA.unpack(u"\1\u008f\37\uffff\1\u008f"),
        DFA.unpack(u"\1\u0090\37\uffff\1\u0090"),
        DFA.unpack(u"\1\u0091\37\uffff\1\u0091"),
        DFA.unpack(u"\1\u0092\37\uffff\1\u0092"),
        DFA.unpack(u"\1\u0093\37\uffff\1\u0093"),
        DFA.unpack(u"\12\56\7\uffff\24\56\1\u0095\5\56\4\uffff\1\56\1\uffff"
        u"\24\56\1\u0095\5\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0096\37\uffff\1\u0096"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0097\37\uffff\1\u0097"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u0099\37\uffff\1\u0099"),
        DFA.unpack(u"\1\u009a\37\uffff\1\u009a"),
        DFA.unpack(u"\1\u009b\37\uffff\1\u009b"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u009d\37\uffff\1\u009d"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u009f\37\uffff\1\u009f"),
        DFA.unpack(u"\1\u00a0\37\uffff\1\u00a0"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00a4\37\uffff\1\u00a4"),
        DFA.unpack(u"\1\u00a5\37\uffff\1\u00a5"),
        DFA.unpack(u"\1\u00a6\37\uffff\1\u00a6"),
        DFA.unpack(u"\1\u00a7\37\uffff\1\u00a7"),
        DFA.unpack(u"\1\u00a8\37\uffff\1\u00a8"),
        DFA.unpack(u"\12\56\7\uffff\10\56\1\u00aa\21\56\4\uffff\1\56\1\uffff"
        u"\10\56\1\u00aa\21\56"),
        DFA.unpack(u"\12\56\7\uffff\4\56\1\u00ac\25\56\4\uffff\1\56\1\uffff"
        u"\4\56\1\u00ac\25\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ae\37\uffff\1\u00ae"),
        DFA.unpack(u"\1\u00af\37\uffff\1\u00af"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00b2\37\uffff\1\u00b2"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00b6\37\uffff\1\u00b6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b7\37\uffff\1\u00b7"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00b9\37\uffff\1\u00b9"),
        DFA.unpack(u"\1\u00ba\37\uffff\1\u00ba"),
        DFA.unpack(u"\1\u00bb\37\uffff\1\u00bb"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bc\37\uffff\1\u00bc"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bd\37\uffff\1\u00bd"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00be\37\uffff\1\u00be"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00c1\37\uffff\1\u00c1"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00c3\37\uffff\1\u00c3"),
        DFA.unpack(u"\1\u00c4\37\uffff\1\u00c4"),
        DFA.unpack(u"\1\u00c5\37\uffff\1\u00c5"),
        DFA.unpack(u"\1\u00c6\37\uffff\1\u00c6"),
        DFA.unpack(u"\1\u00c7\37\uffff\1\u00c7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c9\37\uffff\1\u00c9"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\1\u00cb\37\uffff\1\u00cb"),
        DFA.unpack(u"\1\u00cc\37\uffff\1\u00cc"),
        DFA.unpack(u"\1\u00cd\37\uffff\1\u00cd"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cf\37\uffff\1\u00cf"),
        DFA.unpack(u"\1\u00d0\37\uffff\1\u00d0"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d1\37\uffff\1\u00d1"),
        DFA.unpack(u"\1\u00d2\37\uffff\1\u00d2"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56"),
        DFA.unpack(u"\12\56\7\uffff\32\56\4\uffff\1\56\1\uffff\32\56")
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
                    s = 65

                else:
                    s = 66

                if s >= 0:
                    return s
            elif s == 1: 
                LA17_22 = input.LA(1)

                s = -1
                if ((0 <= LA17_22 <= 65535)):
                    s = 65

                else:
                    s = 64

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
