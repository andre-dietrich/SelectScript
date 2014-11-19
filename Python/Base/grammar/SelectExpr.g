grammar SelectExpr;

options {
	language=Python;
	output=AST;
	ASTLabelType=CommonTree;
	backtrack=true;
}

tokens {
	FCT;

	VAR;
	VAL;
	LIST;
    
	POS;
	NEG;
    
	AGE;
    
	STMT_SELECT;
}


@header{
import antlr3
import antlr3.tree
from SelectExprLexer import SelectExprLexer
}

/*------------------------------------------------------------------
 * LEXER RULES
 *------------------------------------------------------------------*/

DOT 	: '.';
SEP 	: ',';
END 	: ';';
COLON 	: ':';

AND 	: A N D ;
XOR 	: X O R ;
OR  	: O R   ;
NOT 	: N O T ;
IN  	: I N   ;

ASSIGN	:  '=' ;

EQ	: '==' ;
NE	: '!=' ;
LE	: '<=' ;
GE	: '>=' ;
LT	:  '<' ;
GT	:  '>' ;

ADD 	: '+' ;
SUB 	: '-' ;
MUL 	: '*' ;
DIV 	: '/' ;
MOD 	: '%' ;
POW 	: '^' ;

SQ 	: '\'';
DQ 	: '\"';

LIST_BEGIN : '[' ;
LIST_END   : ']' ;

AGE_BEGIN : '{' ;
AGE_END   : '}' ;

SELECT : S E L E C T ;
FROM   : F R O M ;
WHERE  : W H E R E ;
ORDER  : O R D E R ;
GROUP  : G R O U P ;
HAVING : H A V I N G ;
BY     : B Y ;
AS     : A S ;

THIS   : T H I S ;
TIME   : T I M E ;

CONNECT: C O N N E C T ;
START  : S T A R T ;
STOP   : S T O P ;
WITH   : W I T H ;


ASC    : A S C (E N D I N G)? ;
DESC   : D E S C (E N D I N G)? ;

AS_LIST : L I S T ;
AS_VALUE: V A L (U E)? ;
AS_DICT	: D I C T (I O N A R Y)? ;

NEWLINE	: ('\r'? '\n') {self.skip()};
WS	: (' '|'\t'|'\n'|'\r')+ {self.skip()} ;

COMMENT : '/*' .* '*/' {$channel=HIDDEN;} ;
LINE_COMMENT : '#' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;} ;

STRING 	: DQ (~(DQ))* DQ | SQ (~(SQ))* SQ ;
INTEGER : DIGIT+ ;
FLOAT 	: DIGIT* DOT DIGIT* ;
TRUE 	: ('T'|'t') ('R'|'r') ('U'|'u') ('E'|'e');
FALSE 	: ('F'|'f') ('A'|'a') ('L'|'l') ('S'|'s') ('E'|'e');

PHRASE : (CHARACTER | SPECIAL) (DIGIT | CHARACTER | SPECIAL)* ;

fragment DIGIT     : '0'..'9' ;
fragment CHARACTER : ('a'..'z' | 'A'..'Z') ;
fragment SPECIAL   : '_';

fragment A : ('A'|'a') ; fragment N : ('N'|'n') ;
fragment B : ('B'|'b') ; fragment O : ('O'|'o') ;
fragment C : ('C'|'c') ; fragment P : ('P'|'p') ;
fragment D : ('D'|'d') ; fragment Q : ('Q'|'q') ;
fragment E : ('E'|'e') ; fragment R : ('R'|'r') ;
fragment F : ('F'|'f') ; fragment S : ('S'|'s') ;
fragment G : ('G'|'g') ; fragment T : ('T'|'t') ;
fragment H : ('H'|'h') ; fragment U : ('U'|'u') ;
fragment I : ('I'|'i') ; fragment V : ('V'|'v') ;
fragment J : ('J'|'j') ; fragment W : ('W'|'w') ;
fragment K : ('K'|'k') ; fragment X : ('X'|'x') ;
fragment L : ('L'|'l') ; fragment Y : ('Y'|'y') ;
fragment M : ('M'|'m') ; fragment Z : ('Z'|'z') ;

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

eval : prog //{ print $prog.tree.toStringTree()}
;

prog : statement+
;

statement : statement_select END!
	| expr END!
	| END!
;

statement_select :
	select_ from_ (where_)? ((start_)? connect_ stop_)? (group_ (having_)?)? (order_)? (as_)? ->  ^(STMT_SELECT select_ from_ (where_)? (group_ (having_)?)? (order_)? (as_)? ((start_)? connect_ stop_)?) 
;

select_	: SELECT^ (MUL! | ((PHRASE | function | this_) (SEP! (PHRASE | function | this_) )* ))
;

from_ : FROM^ expr (SEP! expr)*
;

where_ : WHERE^ expr
;

start_ : START^ WITH! expr (SEP! expr)*
;

connect_ : CONNECT^ BY! expr (SEP! expr)*
;

stop_ : STOP^ WITH! expr
;

group_ : GROUP^ BY! ( PHRASE | function ) (SEP! ( PHRASE | function ) )*
;

having_ : HAVING^ expr
;

order_ : ORDER^ BY! ( PHRASE direction_ | function direction_ ) (SEP! ( PHRASE direction_ | function direction_ ) )* 
;

direction_ : (ASC | DESC)?
;

as_ : AS^ ( AS_LIST | AS_VALUE | AS_DICT | PHRASE ('('! parameter? ')'!)? )
;

expr : assign_expr 
	| logic_expr
;

assign_expr : PHRASE (age)? ASSIGN expr -> ^(ASSIGN PHRASE expr (age)?);

logic_expr : logic_or ;
logic_or  : logic_xor (OR^  logic_xor)* ;
logic_xor : logic_and (XOR^ logic_and)* ;
logic_and : logic_not (AND^ logic_not)* ;
logic_not : (NOT^)? compare_expr ;

compare_expr : compare_in ;
compare_in : compare_eq (IN^ atom)* ;
compare_eq : compare_ne (EQ^ compare_ne)* ;
compare_ne : compare_ge (NE^ compare_ge)* ;
compare_ge : compare_gt (GE^ compare_gt)* ;
compare_gt : compare_le (GT^ compare_le)* ;
compare_le : compare_lt (LE^ compare_lt)* ;
compare_lt : arithmetic_expr (LT^ arithmetic_expr)* ;

arithmetic_expr : arithmetic_sub_add ;
arithmetic_sub_add : arithmetic_mul_div_mod ((SUB^|ADD^) arithmetic_mul_div_mod)* ;
arithmetic_mul_div_mod : arithmetic_pow ((MUL^ | DIV^ | MOD^) arithmetic_pow)* ;
arithmetic_pow : arithmetic_unary (POW^ arithmetic_unary)* ;
arithmetic_unary :
	SUB atom -> ^(NEG atom)
	|  ADD atom -> ^(POS atom)
	|  atom
;

atom 
	: value
	| variable
	| function
	| '('! expr ')'!
	| statement_select
;

function : PHRASE '(' parameter? ')' -> ^(FCT PHRASE parameter?)
;

parameter : expr (SEP! expr)*
;

variable : PHRASE (age)? -> ^(VAR PHRASE (age)?)
;

age : AGE_BEGIN expr? AGE_END -> ^(AGE expr?)
;

value : STRING 	-> ^(VAL STRING)
	| FLOAT 	-> ^(VAL FLOAT)
	| INTEGER	-> ^(VAL INTEGER)
	| TRUE		-> ^(VAL TRUE)
	| FALSE		-> ^(VAL FALSE)
	| this_
	| list_ 
;

this_ : (PHRASE DOT)? THIS  -> ^(THIS PHRASE?) 
;

list_ :  LIST_BEGIN ( expr? (SEP expr)* ) LIST_END -> ^(LIST expr*)
;