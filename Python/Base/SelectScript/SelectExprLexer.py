# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 SelectExpr.g 2014-10-22 20:43:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class SelectExprLexer(Lexer):

    grammarFileName = "SelectExpr.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SelectExprLexer, self).__init__(input, state)


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






    # $ANTLR start "T__94"
    def mT__94(self, ):

        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:7:7: ( '(' )
            # SelectExpr.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):

        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:8:7: ( ')' )
            # SelectExpr.g:8:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__95"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:35:6: ( '.' )
            # SelectExpr.g:35:8: '.'
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

            # SelectExpr.g:36:6: ( ',' )
            # SelectExpr.g:36:8: ','
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

            # SelectExpr.g:37:6: ( ';' )
            # SelectExpr.g:37:8: ';'
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

            # SelectExpr.g:38:8: ( ':' )
            # SelectExpr.g:38:10: ':'
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

            # SelectExpr.g:40:6: ( A N D )
            # SelectExpr.g:40:8: A N D
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

            # SelectExpr.g:41:6: ( X O R )
            # SelectExpr.g:41:8: X O R
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

            # SelectExpr.g:42:6: ( O R )
            # SelectExpr.g:42:8: O R
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

            # SelectExpr.g:43:6: ( N O T )
            # SelectExpr.g:43:8: N O T
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

            # SelectExpr.g:44:6: ( I N )
            # SelectExpr.g:44:8: I N
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

            # SelectExpr.g:46:8: ( '=' )
            # SelectExpr.g:46:11: '='
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

            # SelectExpr.g:48:4: ( '==' )
            # SelectExpr.g:48:6: '=='
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

            # SelectExpr.g:49:4: ( '!=' )
            # SelectExpr.g:49:6: '!='
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

            # SelectExpr.g:50:4: ( '<=' )
            # SelectExpr.g:50:6: '<='
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

            # SelectExpr.g:51:4: ( '>=' )
            # SelectExpr.g:51:6: '>='
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

            # SelectExpr.g:52:4: ( '<' )
            # SelectExpr.g:52:7: '<'
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

            # SelectExpr.g:53:4: ( '>' )
            # SelectExpr.g:53:7: '>'
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

            # SelectExpr.g:55:6: ( '+' )
            # SelectExpr.g:55:8: '+'
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

            # SelectExpr.g:56:6: ( '-' )
            # SelectExpr.g:56:8: '-'
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

            # SelectExpr.g:57:6: ( '*' )
            # SelectExpr.g:57:8: '*'
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

            # SelectExpr.g:58:6: ( '/' )
            # SelectExpr.g:58:8: '/'
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

            # SelectExpr.g:59:6: ( '%' )
            # SelectExpr.g:59:8: '%'
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

            # SelectExpr.g:60:6: ( '^' )
            # SelectExpr.g:60:8: '^'
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

            # SelectExpr.g:62:5: ( '\\'' )
            # SelectExpr.g:62:7: '\\''
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

            # SelectExpr.g:63:5: ( '\\\"' )
            # SelectExpr.g:63:7: '\\\"'
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

            # SelectExpr.g:65:12: ( '[' )
            # SelectExpr.g:65:14: '['
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

            # SelectExpr.g:66:12: ( ']' )
            # SelectExpr.g:66:14: ']'
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

            # SelectExpr.g:68:11: ( '{' )
            # SelectExpr.g:68:13: '{'
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

            # SelectExpr.g:69:11: ( '}' )
            # SelectExpr.g:69:13: '}'
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

            # SelectExpr.g:71:8: ( S E L E C T )
            # SelectExpr.g:71:10: S E L E C T
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

            # SelectExpr.g:72:8: ( F R O M )
            # SelectExpr.g:72:10: F R O M
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

            # SelectExpr.g:73:8: ( W H E R E )
            # SelectExpr.g:73:10: W H E R E
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

            # SelectExpr.g:74:8: ( O R D E R )
            # SelectExpr.g:74:10: O R D E R
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

            # SelectExpr.g:75:8: ( G R O U P )
            # SelectExpr.g:75:10: G R O U P
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

            # SelectExpr.g:76:8: ( H A V I N G )
            # SelectExpr.g:76:10: H A V I N G
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

            # SelectExpr.g:77:8: ( B Y )
            # SelectExpr.g:77:10: B Y
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

            # SelectExpr.g:78:8: ( A S )
            # SelectExpr.g:78:10: A S
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

            # SelectExpr.g:79:8: ( T H I S )
            # SelectExpr.g:79:10: T H I S
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

            # SelectExpr.g:80:8: ( T I M E )
            # SelectExpr.g:80:10: T I M E
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



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # SelectExpr.g:82:8: ( A S C ( E N D I N G )? )
            # SelectExpr.g:82:10: A S C ( E N D I N G )?
            pass 
            self.mA()
            self.mS()
            self.mC()
            # SelectExpr.g:82:16: ( E N D I N G )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 69 or LA1_0 == 101) :
                alt1 = 1
            if alt1 == 1:
                # SelectExpr.g:82:17: E N D I N G
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

            # SelectExpr.g:83:8: ( D E S C ( E N D I N G )? )
            # SelectExpr.g:83:10: D E S C ( E N D I N G )?
            pass 
            self.mD()
            self.mE()
            self.mS()
            self.mC()
            # SelectExpr.g:83:18: ( E N D I N G )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 69 or LA2_0 == 101) :
                alt2 = 1
            if alt2 == 1:
                # SelectExpr.g:83:19: E N D I N G
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

            # SelectExpr.g:85:9: ( L ( I S T )? )
            # SelectExpr.g:85:11: L ( I S T )?
            pass 
            self.mL()
            # SelectExpr.g:85:13: ( I S T )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 73 or LA3_0 == 105) :
                alt3 = 1
            if alt3 == 1:
                # SelectExpr.g:85:14: I S T
                pass 
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

            # SelectExpr.g:86:9: ( V ( A L ( U E )? )? )
            # SelectExpr.g:86:11: V ( A L ( U E )? )?
            pass 
            self.mV()
            # SelectExpr.g:86:13: ( A L ( U E )? )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 65 or LA5_0 == 97) :
                alt5 = 1
            if alt5 == 1:
                # SelectExpr.g:86:14: A L ( U E )?
                pass 
                self.mA()
                self.mL()
                # SelectExpr.g:86:18: ( U E )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 85 or LA4_0 == 117) :
                    alt4 = 1
                if alt4 == 1:
                    # SelectExpr.g:86:19: U E
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

            # SelectExpr.g:87:9: ( D ( I C T ( I O N A R Y )? )? )
            # SelectExpr.g:87:11: D ( I C T ( I O N A R Y )? )?
            pass 
            self.mD()
            # SelectExpr.g:87:13: ( I C T ( I O N A R Y )? )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 73 or LA7_0 == 105) :
                alt7 = 1
            if alt7 == 1:
                # SelectExpr.g:87:14: I C T ( I O N A R Y )?
                pass 
                self.mI()
                self.mC()
                self.mT()
                # SelectExpr.g:87:20: ( I O N A R Y )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 73 or LA6_0 == 105) :
                    alt6 = 1
                if alt6 == 1:
                    # SelectExpr.g:87:21: I O N A R Y
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

            # SelectExpr.g:89:9: ( ( ( '\\r' )? '\\n' ) )
            # SelectExpr.g:89:11: ( ( '\\r' )? '\\n' )
            pass 
            # SelectExpr.g:89:11: ( ( '\\r' )? '\\n' )
            # SelectExpr.g:89:12: ( '\\r' )? '\\n'
            pass 
            # SelectExpr.g:89:12: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # SelectExpr.g:89:12: '\\r'
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

            # SelectExpr.g:90:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # SelectExpr.g:90:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # SelectExpr.g:90:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((9 <= LA9_0 <= 10) or LA9_0 == 13 or LA9_0 == 32) :
                    alt9 = 1


                if alt9 == 1:
                    # SelectExpr.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1
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

            # SelectExpr.g:92:9: ( '/*' ( . )* '*/' )
            # SelectExpr.g:92:11: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # SelectExpr.g:92:16: ( . )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 42) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == 47) :
                        alt10 = 2
                    elif ((0 <= LA10_1 <= 46) or (48 <= LA10_1 <= 65535)) :
                        alt10 = 1


                elif ((0 <= LA10_0 <= 41) or (43 <= LA10_0 <= 65535)) :
                    alt10 = 1


                if alt10 == 1:
                    # SelectExpr.g:92:16: .
                    pass 
                    self.matchAny()


                else:
                    break #loop10
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

            # SelectExpr.g:93:14: ( '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # SelectExpr.g:93:16: '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # SelectExpr.g:93:20: (~ ( '\\n' | '\\r' ) )*
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                    alt11 = 1


                if alt11 == 1:
                    # SelectExpr.g:93:20: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop11
            # SelectExpr.g:93:34: ( '\\r' )?
            alt12 = 2
            LA12_0 = self.input.LA(1)

            if (LA12_0 == 13) :
                alt12 = 1
            if alt12 == 1:
                # SelectExpr.g:93:34: '\\r'
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

            # SelectExpr.g:95:9: ( DQ (~ ( DQ ) )* DQ | SQ (~ ( SQ ) )* SQ )
            alt15 = 2
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 34) :
                alt15 = 1
            elif (LA15_0 == 39) :
                alt15 = 2
            else:
                nvae = NoViableAltException("", 15, 0, self.input)

                raise nvae

            if alt15 == 1:
                # SelectExpr.g:95:11: DQ (~ ( DQ ) )* DQ
                pass 
                self.mDQ()
                # SelectExpr.g:95:14: (~ ( DQ ) )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((0 <= LA13_0 <= 33) or (35 <= LA13_0 <= 65535)) :
                        alt13 = 1


                    if alt13 == 1:
                        # SelectExpr.g:95:15: ~ ( DQ )
                        pass 
                        if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop13
                self.mDQ()


            elif alt15 == 2:
                # SelectExpr.g:95:28: SQ (~ ( SQ ) )* SQ
                pass 
                self.mSQ()
                # SelectExpr.g:95:31: (~ ( SQ ) )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((0 <= LA14_0 <= 38) or (40 <= LA14_0 <= 65535)) :
                        alt14 = 1


                    if alt14 == 1:
                        # SelectExpr.g:95:32: ~ ( SQ )
                        pass 
                        if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop14
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

            # SelectExpr.g:96:9: ( ( DIGIT )+ )
            # SelectExpr.g:96:11: ( DIGIT )+
            pass 
            # SelectExpr.g:96:11: ( DIGIT )+
            cnt16 = 0
            while True: #loop16
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((48 <= LA16_0 <= 57)) :
                    alt16 = 1


                if alt16 == 1:
                    # SelectExpr.g:96:11: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt16 >= 1:
                        break #loop16

                    eee = EarlyExitException(16, self.input)
                    raise eee

                cnt16 += 1



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

            # SelectExpr.g:97:8: ( ( DIGIT )* DOT ( DIGIT )* )
            # SelectExpr.g:97:10: ( DIGIT )* DOT ( DIGIT )*
            pass 
            # SelectExpr.g:97:10: ( DIGIT )*
            while True: #loop17
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((48 <= LA17_0 <= 57)) :
                    alt17 = 1


                if alt17 == 1:
                    # SelectExpr.g:97:10: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop17
            self.mDOT()
            # SelectExpr.g:97:21: ( DIGIT )*
            while True: #loop18
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((48 <= LA18_0 <= 57)) :
                    alt18 = 1


                if alt18 == 1:
                    # SelectExpr.g:97:21: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop18



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

            # SelectExpr.g:98:7: ( ( 'T' | 't' ) ( ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )? )
            # SelectExpr.g:98:9: ( 'T' | 't' ) ( ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )?
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SelectExpr.g:98:19: ( ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )?
            alt19 = 2
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 82 or LA19_0 == 114) :
                alt19 = 1
            if alt19 == 1:
                # SelectExpr.g:98:20: ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' )
                pass 
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

            # SelectExpr.g:99:8: ( ( 'F' | 'f' ) ( ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )? )
            # SelectExpr.g:99:10: ( 'F' | 'f' ) ( ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )?
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SelectExpr.g:99:20: ( ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )?
            alt20 = 2
            LA20_0 = self.input.LA(1)

            if (LA20_0 == 65 or LA20_0 == 97) :
                alt20 = 1
            if alt20 == 1:
                # SelectExpr.g:99:21: ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' )
                pass 
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

            # SelectExpr.g:101:8: ( ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )* )
            # SelectExpr.g:101:10: ( CHARACTER | SPECIAL ) ( DIGIT | CHARACTER | SPECIAL )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # SelectExpr.g:101:32: ( DIGIT | CHARACTER | SPECIAL )*
            while True: #loop21
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((48 <= LA21_0 <= 57) or (65 <= LA21_0 <= 90) or LA21_0 == 95 or (97 <= LA21_0 <= 122)) :
                    alt21 = 1


                if alt21 == 1:
                    # SelectExpr.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop21



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PHRASE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # SelectExpr.g:103:20: ( '0' .. '9' )
            # SelectExpr.g:103:22: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "CHARACTER"
    def mCHARACTER(self, ):

        try:
            # SelectExpr.g:104:20: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # SelectExpr.g:104:22: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # SelectExpr.g:105:20: ( '_' )
            # SelectExpr.g:105:22: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "SPECIAL"



    # $ANTLR start "A"
    def mA(self, ):

        try:
            # SelectExpr.g:107:12: ( ( 'A' | 'a' ) )
            # SelectExpr.g:107:14: ( 'A' | 'a' )
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
            # SelectExpr.g:107:12: ( ( 'N' | 'n' ) )
            # SelectExpr.g:107:14: ( 'N' | 'n' )
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
            # SelectExpr.g:108:12: ( ( 'B' | 'b' ) )
            # SelectExpr.g:108:14: ( 'B' | 'b' )
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
            # SelectExpr.g:108:12: ( ( 'O' | 'o' ) )
            # SelectExpr.g:108:14: ( 'O' | 'o' )
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
            # SelectExpr.g:109:12: ( ( 'C' | 'c' ) )
            # SelectExpr.g:109:14: ( 'C' | 'c' )
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
            # SelectExpr.g:109:12: ( ( 'P' | 'p' ) )
            # SelectExpr.g:109:14: ( 'P' | 'p' )
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
            # SelectExpr.g:110:12: ( ( 'D' | 'd' ) )
            # SelectExpr.g:110:14: ( 'D' | 'd' )
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
            # SelectExpr.g:110:12: ( ( 'Q' | 'q' ) )
            # SelectExpr.g:110:14: ( 'Q' | 'q' )
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
            # SelectExpr.g:111:12: ( ( 'E' | 'e' ) )
            # SelectExpr.g:111:14: ( 'E' | 'e' )
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
            # SelectExpr.g:111:12: ( ( 'R' | 'r' ) )
            # SelectExpr.g:111:14: ( 'R' | 'r' )
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
            # SelectExpr.g:112:12: ( ( 'F' | 'f' ) )
            # SelectExpr.g:112:14: ( 'F' | 'f' )
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
            # SelectExpr.g:112:12: ( ( 'S' | 's' ) )
            # SelectExpr.g:112:14: ( 'S' | 's' )
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
            # SelectExpr.g:113:12: ( ( 'G' | 'g' ) )
            # SelectExpr.g:113:14: ( 'G' | 'g' )
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
            # SelectExpr.g:113:12: ( ( 'T' | 't' ) )
            # SelectExpr.g:113:14: ( 'T' | 't' )
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
            # SelectExpr.g:114:12: ( ( 'H' | 'h' ) )
            # SelectExpr.g:114:14: ( 'H' | 'h' )
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
            # SelectExpr.g:114:12: ( ( 'U' | 'u' ) )
            # SelectExpr.g:114:14: ( 'U' | 'u' )
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
            # SelectExpr.g:115:12: ( ( 'I' | 'i' ) )
            # SelectExpr.g:115:14: ( 'I' | 'i' )
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
            # SelectExpr.g:115:12: ( ( 'V' | 'v' ) )
            # SelectExpr.g:115:14: ( 'V' | 'v' )
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
            # SelectExpr.g:116:12: ( ( 'J' | 'j' ) )
            # SelectExpr.g:116:14: ( 'J' | 'j' )
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
            # SelectExpr.g:116:12: ( ( 'W' | 'w' ) )
            # SelectExpr.g:116:14: ( 'W' | 'w' )
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
            # SelectExpr.g:117:12: ( ( 'K' | 'k' ) )
            # SelectExpr.g:117:14: ( 'K' | 'k' )
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
            # SelectExpr.g:117:12: ( ( 'X' | 'x' ) )
            # SelectExpr.g:117:14: ( 'X' | 'x' )
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
            # SelectExpr.g:118:12: ( ( 'L' | 'l' ) )
            # SelectExpr.g:118:14: ( 'L' | 'l' )
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
            # SelectExpr.g:118:12: ( ( 'Y' | 'y' ) )
            # SelectExpr.g:118:14: ( 'Y' | 'y' )
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
            # SelectExpr.g:119:12: ( ( 'M' | 'm' ) )
            # SelectExpr.g:119:14: ( 'M' | 'm' )
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
            # SelectExpr.g:119:12: ( ( 'Z' | 'z' ) )
            # SelectExpr.g:119:14: ( 'Z' | 'z' )
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
        # SelectExpr.g:1:8: ( T__94 | T__95 | DOT | SEP | END | COLON | AND | XOR | OR | NOT | IN | ASSIGN | EQ | NE | LE | GE | LT | GT | ADD | SUB | MUL | DIV | MOD | POW | SQ | DQ | LIST_BEGIN | LIST_END | AGE_BEGIN | AGE_END | SELECT | FROM | WHERE | ORDER | GROUP | HAVING | BY | AS | THIS | TIME | ASC | DESC | AS_LIST | AS_VALUE | AS_DICT | NEWLINE | WS | COMMENT | LINE_COMMENT | STRING | INTEGER | FLOAT | TRUE | FALSE | PHRASE )
        alt22 = 55
        alt22 = self.dfa22.predict(self.input)
        if alt22 == 1:
            # SelectExpr.g:1:10: T__94
            pass 
            self.mT__94()


        elif alt22 == 2:
            # SelectExpr.g:1:16: T__95
            pass 
            self.mT__95()


        elif alt22 == 3:
            # SelectExpr.g:1:22: DOT
            pass 
            self.mDOT()


        elif alt22 == 4:
            # SelectExpr.g:1:26: SEP
            pass 
            self.mSEP()


        elif alt22 == 5:
            # SelectExpr.g:1:30: END
            pass 
            self.mEND()


        elif alt22 == 6:
            # SelectExpr.g:1:34: COLON
            pass 
            self.mCOLON()


        elif alt22 == 7:
            # SelectExpr.g:1:40: AND
            pass 
            self.mAND()


        elif alt22 == 8:
            # SelectExpr.g:1:44: XOR
            pass 
            self.mXOR()


        elif alt22 == 9:
            # SelectExpr.g:1:48: OR
            pass 
            self.mOR()


        elif alt22 == 10:
            # SelectExpr.g:1:51: NOT
            pass 
            self.mNOT()


        elif alt22 == 11:
            # SelectExpr.g:1:55: IN
            pass 
            self.mIN()


        elif alt22 == 12:
            # SelectExpr.g:1:58: ASSIGN
            pass 
            self.mASSIGN()


        elif alt22 == 13:
            # SelectExpr.g:1:65: EQ
            pass 
            self.mEQ()


        elif alt22 == 14:
            # SelectExpr.g:1:68: NE
            pass 
            self.mNE()


        elif alt22 == 15:
            # SelectExpr.g:1:71: LE
            pass 
            self.mLE()


        elif alt22 == 16:
            # SelectExpr.g:1:74: GE
            pass 
            self.mGE()


        elif alt22 == 17:
            # SelectExpr.g:1:77: LT
            pass 
            self.mLT()


        elif alt22 == 18:
            # SelectExpr.g:1:80: GT
            pass 
            self.mGT()


        elif alt22 == 19:
            # SelectExpr.g:1:83: ADD
            pass 
            self.mADD()


        elif alt22 == 20:
            # SelectExpr.g:1:87: SUB
            pass 
            self.mSUB()


        elif alt22 == 21:
            # SelectExpr.g:1:91: MUL
            pass 
            self.mMUL()


        elif alt22 == 22:
            # SelectExpr.g:1:95: DIV
            pass 
            self.mDIV()


        elif alt22 == 23:
            # SelectExpr.g:1:99: MOD
            pass 
            self.mMOD()


        elif alt22 == 24:
            # SelectExpr.g:1:103: POW
            pass 
            self.mPOW()


        elif alt22 == 25:
            # SelectExpr.g:1:107: SQ
            pass 
            self.mSQ()


        elif alt22 == 26:
            # SelectExpr.g:1:110: DQ
            pass 
            self.mDQ()


        elif alt22 == 27:
            # SelectExpr.g:1:113: LIST_BEGIN
            pass 
            self.mLIST_BEGIN()


        elif alt22 == 28:
            # SelectExpr.g:1:124: LIST_END
            pass 
            self.mLIST_END()


        elif alt22 == 29:
            # SelectExpr.g:1:133: AGE_BEGIN
            pass 
            self.mAGE_BEGIN()


        elif alt22 == 30:
            # SelectExpr.g:1:143: AGE_END
            pass 
            self.mAGE_END()


        elif alt22 == 31:
            # SelectExpr.g:1:151: SELECT
            pass 
            self.mSELECT()


        elif alt22 == 32:
            # SelectExpr.g:1:158: FROM
            pass 
            self.mFROM()


        elif alt22 == 33:
            # SelectExpr.g:1:163: WHERE
            pass 
            self.mWHERE()


        elif alt22 == 34:
            # SelectExpr.g:1:169: ORDER
            pass 
            self.mORDER()


        elif alt22 == 35:
            # SelectExpr.g:1:175: GROUP
            pass 
            self.mGROUP()


        elif alt22 == 36:
            # SelectExpr.g:1:181: HAVING
            pass 
            self.mHAVING()


        elif alt22 == 37:
            # SelectExpr.g:1:188: BY
            pass 
            self.mBY()


        elif alt22 == 38:
            # SelectExpr.g:1:191: AS
            pass 
            self.mAS()


        elif alt22 == 39:
            # SelectExpr.g:1:194: THIS
            pass 
            self.mTHIS()


        elif alt22 == 40:
            # SelectExpr.g:1:199: TIME
            pass 
            self.mTIME()


        elif alt22 == 41:
            # SelectExpr.g:1:204: ASC
            pass 
            self.mASC()


        elif alt22 == 42:
            # SelectExpr.g:1:208: DESC
            pass 
            self.mDESC()


        elif alt22 == 43:
            # SelectExpr.g:1:213: AS_LIST
            pass 
            self.mAS_LIST()


        elif alt22 == 44:
            # SelectExpr.g:1:221: AS_VALUE
            pass 
            self.mAS_VALUE()


        elif alt22 == 45:
            # SelectExpr.g:1:230: AS_DICT
            pass 
            self.mAS_DICT()


        elif alt22 == 46:
            # SelectExpr.g:1:238: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt22 == 47:
            # SelectExpr.g:1:246: WS
            pass 
            self.mWS()


        elif alt22 == 48:
            # SelectExpr.g:1:249: COMMENT
            pass 
            self.mCOMMENT()


        elif alt22 == 49:
            # SelectExpr.g:1:257: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt22 == 50:
            # SelectExpr.g:1:270: STRING
            pass 
            self.mSTRING()


        elif alt22 == 51:
            # SelectExpr.g:1:277: INTEGER
            pass 
            self.mINTEGER()


        elif alt22 == 52:
            # SelectExpr.g:1:285: FLOAT
            pass 
            self.mFLOAT()


        elif alt22 == 53:
            # SelectExpr.g:1:291: TRUE
            pass 
            self.mTRUE()


        elif alt22 == 54:
            # SelectExpr.g:1:296: FALSE
            pass 
            self.mFALSE()


        elif alt22 == 55:
            # SelectExpr.g:1:302: PHRASE
            pass 
            self.mPHRASE()







    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\3\uffff\1\54\3\uffff\5\53\1\65\1\uffff\1\67\1\71\3\uffff\1\73"
        u"\2\uffff\1\74\1\76\4\uffff\1\53\1\101\4\53\1\107\1\113\1\117\1"
        u"\121\1\50\1\122\2\uffff\1\123\3\uffff\1\53\1\125\1\53\1\130\1\53"
        u"\1\133\13\uffff\2\53\1\uffff\4\53\1\142\1\uffff\3\53\1\uffff\3"
        u"\53\1\uffff\1\53\3\uffff\1\152\1\uffff\1\153\1\155\1\uffff\1\53"
        u"\1\157\1\uffff\6\53\1\uffff\6\53\1\121\2\uffff\1\53\1\uffff\1\53"
        u"\1\uffff\2\53\1\u0081\3\53\1\u0085\1\107\1\u0086\1\113\1\u0088"
        u"\1\117\2\53\1\u008c\1\53\1\101\1\uffff\1\u008e\1\u008f\1\53\2\uffff"
        u"\1\53\1\uffff\1\53\1\121\1\53\1\uffff\1\u0094\2\uffff\1\u0095\3"
        u"\53\2\uffff\5\53\1\153\2\53\1\113\1\u0088"
        )

    DFA22_eof = DFA.unpack(
        u"\u00a0\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\11\2\uffff\1\60\3\uffff\1\116\1\117\1\122\1\117\1\116\1\75\1"
        u"\uffff\2\75\3\uffff\1\52\2\uffff\2\0\4\uffff\1\105\1\60\1\110\1"
        u"\122\1\101\1\131\4\60\1\12\1\11\2\uffff\1\56\3\uffff\1\104\1\60"
        u"\1\122\1\60\1\124\1\60\13\uffff\2\114\1\uffff\1\117\1\105\1\117"
        u"\1\126\1\60\1\uffff\1\115\1\125\1\111\1\uffff\1\103\2\123\1\uffff"
        u"\1\114\3\uffff\1\60\1\uffff\2\60\1\uffff\1\105\1\60\1\uffff\1\105"
        u"\1\123\1\115\1\122\1\125\1\111\1\uffff\2\105\1\123\1\124\1\103"
        u"\1\124\1\60\2\uffff\1\116\1\uffff\1\122\1\uffff\1\103\1\105\1\60"
        u"\1\105\1\120\1\116\6\60\1\105\1\104\1\60\1\124\1\60\1\uffff\2\60"
        u"\1\107\2\uffff\1\117\1\uffff\1\116\1\60\1\111\1\uffff\1\60\2\uffff"
        u"\1\60\1\116\1\104\1\116\2\uffff\1\101\1\111\1\107\1\122\1\116\1"
        u"\60\1\131\1\107\2\60"
        )

    DFA22_max = DFA.unpack(
        u"\1\175\2\uffff\1\71\3\uffff\1\163\1\157\1\162\1\157\1\156\1\75"
        u"\1\uffff\2\75\3\uffff\1\52\2\uffff\2\uffff\4\uffff\1\145\1\172"
        u"\1\150\1\162\1\141\1\171\4\172\1\12\1\40\2\uffff\1\71\3\uffff\1"
        u"\144\1\172\1\162\1\172\1\164\1\172\13\uffff\2\154\1\uffff\1\157"
        u"\1\145\1\157\1\166\1\172\1\uffff\1\155\1\165\1\151\1\uffff\1\143"
        u"\2\163\1\uffff\1\154\3\uffff\1\172\1\uffff\2\172\1\uffff\1\145"
        u"\1\172\1\uffff\1\145\1\163\1\155\1\162\1\165\1\151\1\uffff\2\145"
        u"\1\163\1\164\1\143\1\164\1\172\2\uffff\1\156\1\uffff\1\162\1\uffff"
        u"\1\143\1\145\1\172\1\145\1\160\1\156\6\172\1\145\1\144\1\172\1"
        u"\164\1\172\1\uffff\2\172\1\147\2\uffff\1\157\1\uffff\1\156\1\172"
        u"\1\151\1\uffff\1\172\2\uffff\1\172\1\156\1\144\1\156\2\uffff\1"
        u"\141\1\151\1\147\1\162\1\156\1\172\1\171\1\147\2\172"
        )

    DFA22_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\uffff\1\4\1\5\1\6\6\uffff\1\16\2\uffff\1\23"
        u"\1\24\1\25\1\uffff\1\27\1\30\2\uffff\1\33\1\34\1\35\1\36\14\uffff"
        u"\1\57\1\61\1\uffff\1\67\1\3\1\64\6\uffff\1\15\1\14\1\17\1\21\1"
        u"\20\1\22\1\60\1\26\1\31\1\62\1\32\2\uffff\1\66\5\uffff\1\65\3\uffff"
        u"\1\55\3\uffff\1\53\1\uffff\1\54\1\56\1\63\1\uffff\1\46\2\uffff"
        u"\1\11\2\uffff\1\13\6\uffff\1\45\7\uffff\1\7\1\51\1\uffff\1\10\1"
        u"\uffff\1\12\21\uffff\1\40\3\uffff\1\50\1\47\1\uffff\1\52\3\uffff"
        u"\1\42\1\uffff\1\41\1\43\4\uffff\1\37\1\44\12\uffff"
        )

    DFA22_special = DFA.unpack(
        u"\26\uffff\1\0\1\1\u0088\uffff"
        )

            
    DFA22_transition = [
        DFA.unpack(u"\1\50\1\47\2\uffff\1\46\22\uffff\1\50\1\15\1\27\1\51"
        u"\1\uffff\1\24\1\uffff\1\26\1\1\1\2\1\22\1\20\1\4\1\21\1\3\1\23"
        u"\12\52\1\6\1\5\1\16\1\14\1\17\2\uffff\1\7\1\41\1\53\1\43\1\53\1"
        u"\35\1\37\1\40\1\13\2\53\1\44\1\53\1\12\1\11\3\53\1\34\1\42\1\53"
        u"\1\45\1\36\1\10\2\53\1\30\1\uffff\1\31\1\25\1\53\1\uffff\1\7\1"
        u"\41\1\53\1\43\1\53\1\35\1\37\1\40\1\13\2\53\1\44\1\53\1\12\1\11"
        u"\3\53\1\34\1\42\1\53\1\45\1\36\1\10\2\53\1\32\1\uffff\1\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\55"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56\4\uffff\1\57\32\uffff\1\56\4\uffff\1\57"),
        DFA.unpack(u"\1\60\37\uffff\1\60"),
        DFA.unpack(u"\1\61\37\uffff\1\61"),
        DFA.unpack(u"\1\62\37\uffff\1\62"),
        DFA.unpack(u"\1\63\37\uffff\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\0\75"),
        DFA.unpack(u"\0\75"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\77\37\uffff\1\77"),
        DFA.unpack(u"\12\53\7\uffff\1\100\20\53\1\102\10\53\4\uffff\1\53"
        u"\1\uffff\1\100\20\53\1\102\10\53"),
        DFA.unpack(u"\1\103\37\uffff\1\103"),
        DFA.unpack(u"\1\104\37\uffff\1\104"),
        DFA.unpack(u"\1\105\37\uffff\1\105"),
        DFA.unpack(u"\1\106\37\uffff\1\106"),
        DFA.unpack(u"\12\53\7\uffff\7\53\1\112\1\110\10\53\1\111\10\53\4"
        u"\uffff\1\53\1\uffff\7\53\1\112\1\110\10\53\1\111\10\53"),
        DFA.unpack(u"\12\53\7\uffff\4\53\1\115\3\53\1\114\21\53\4\uffff"
        u"\1\53\1\uffff\4\53\1\115\3\53\1\114\21\53"),
        DFA.unpack(u"\12\53\7\uffff\10\53\1\116\21\53\4\uffff\1\53\1\uffff"
        u"\10\53\1\116\21\53"),
        DFA.unpack(u"\12\53\7\uffff\1\120\31\53\4\uffff\1\53\1\uffff\1\120"
        u"\31\53"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\2\50\2\uffff\1\50\22\uffff\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\1\uffff\12\52"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\124\37\uffff\1\124"),
        DFA.unpack(u"\12\53\7\uffff\2\53\1\126\27\53\4\uffff\1\53\1\uffff"
        u"\2\53\1\126\27\53"),
        DFA.unpack(u"\1\127\37\uffff\1\127"),
        DFA.unpack(u"\12\53\7\uffff\3\53\1\131\26\53\4\uffff\1\53\1\uffff"
        u"\3\53\1\131\26\53"),
        DFA.unpack(u"\1\132\37\uffff\1\132"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
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
        DFA.unpack(u"\1\134\37\uffff\1\134"),
        DFA.unpack(u"\1\135\37\uffff\1\135"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\136\37\uffff\1\136"),
        DFA.unpack(u"\1\137\37\uffff\1\137"),
        DFA.unpack(u"\1\140\37\uffff\1\140"),
        DFA.unpack(u"\1\141\37\uffff\1\141"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143\37\uffff\1\143"),
        DFA.unpack(u"\1\144\37\uffff\1\144"),
        DFA.unpack(u"\1\145\37\uffff\1\145"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\146\37\uffff\1\146"),
        DFA.unpack(u"\1\147\37\uffff\1\147"),
        DFA.unpack(u"\1\150\37\uffff\1\150"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\151\37\uffff\1\151"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\4\53\1\154\25\53\4\uffff\1\53\1\uffff"
        u"\4\53\1\154\25\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\156\37\uffff\1\156"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\160\37\uffff\1\160"),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u"\1\162\37\uffff\1\162"),
        DFA.unpack(u"\1\163\37\uffff\1\163"),
        DFA.unpack(u"\1\164\37\uffff\1\164"),
        DFA.unpack(u"\1\165\37\uffff\1\165"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\166\37\uffff\1\166"),
        DFA.unpack(u"\1\167\37\uffff\1\167"),
        DFA.unpack(u"\1\170\37\uffff\1\170"),
        DFA.unpack(u"\1\171\37\uffff\1\171"),
        DFA.unpack(u"\1\172\37\uffff\1\172"),
        DFA.unpack(u"\1\173\37\uffff\1\173"),
        DFA.unpack(u"\12\53\7\uffff\24\53\1\174\5\53\4\uffff\1\53\1\uffff"
        u"\24\53\1\174\5\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\175\37\uffff\1\175"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\176\37\uffff\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\177\37\uffff\1\177"),
        DFA.unpack(u"\1\u0080\37\uffff\1\u0080"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u0082\37\uffff\1\u0082"),
        DFA.unpack(u"\1\u0083\37\uffff\1\u0083"),
        DFA.unpack(u"\1\u0084\37\uffff\1\u0084"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\10\53\1\u0087\21\53\4\uffff\1\53\1\uffff"
        u"\10\53\1\u0087\21\53"),
        DFA.unpack(u"\12\53\7\uffff\4\53\1\u0089\25\53\4\uffff\1\53\1\uffff"
        u"\4\53\1\u0089\25\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u008a\37\uffff\1\u008a"),
        DFA.unpack(u"\1\u008b\37\uffff\1\u008b"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u008d\37\uffff\1\u008d"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u0090\37\uffff\1\u0090"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0091\37\uffff\1\u0091"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0092\37\uffff\1\u0092"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u0093\37\uffff\1\u0093"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u0096\37\uffff\1\u0096"),
        DFA.unpack(u"\1\u0097\37\uffff\1\u0097"),
        DFA.unpack(u"\1\u0098\37\uffff\1\u0098"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0099\37\uffff\1\u0099"),
        DFA.unpack(u"\1\u009a\37\uffff\1\u009a"),
        DFA.unpack(u"\1\u009b\37\uffff\1\u009b"),
        DFA.unpack(u"\1\u009c\37\uffff\1\u009c"),
        DFA.unpack(u"\1\u009d\37\uffff\1\u009d"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\1\u009e\37\uffff\1\u009e"),
        DFA.unpack(u"\1\u009f\37\uffff\1\u009f"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53"),
        DFA.unpack(u"\12\53\7\uffff\32\53\4\uffff\1\53\1\uffff\32\53")
    ]

    # class definition for DFA #22

    class DFA22(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA22_22 = input.LA(1)

                s = -1
                if ((0 <= LA22_22 <= 65535)):
                    s = 61

                else:
                    s = 60

                if s >= 0:
                    return s
            elif s == 1: 
                LA22_23 = input.LA(1)

                s = -1
                if ((0 <= LA22_23 <= 65535)):
                    s = 61

                else:
                    s = 62

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 22, _s, input)
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
