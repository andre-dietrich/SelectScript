// Define a grammar 
tree grammar SelectScript;

options {
	language=Python;
	tokenVocab=SelectExpr;
	ASTLabelType=CommonTree;
	backtrack=true;
}

@header{
import sys

import antlr3
import antlr3.tree

import operator

from SelectExprLexer import SelectExprLexer
from SelectExprParser import SelectExprParser
}

@members{

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
         'phrase':6, 'eval': 7 }
         
asTypes = {'dict' :'d', 'list' :'l', 'value':'v'}
			
def _fct(self, name, params):
	return [self.types['fct'], name, params]

def _var(self, var_name, age=0) :
	return [self.types['var'], var_name, age]

def _val(self, value) :
	return [self.types['val'], value]
	
def _list(self, l) :
	return [self.types['list'], l]
	
def _sel(self, s, f, w, g, h, o, a, rec) :
	return [self.types['sel'], s, f, w, g, h, o, a, rec]
	
def _this(self, name='') :
	return [self.types['this'], name]
	
def _phrase(self, name) :
	return [self.types['phrase'], name]
	
def _eval(self, string):
	return [self.types['eval'], string]
	
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
		S, F, W, G, H, O, A, R = prog[1:]
		
		S = [self.Simplify(expr) for expr in S]
		F = [self.Simplify(expr) for expr in F]
		W =  self.Simplify(W)
		G = [self.Simplify(expr) for expr in G]
		H = [self.Simplify(expr) for expr in H]
		if O != []:
			O = [[self.Simplify(expr[0]), expr[1]] for expr in O]
		A[1] = [self.Simplify(expr) for expr in A[1]]
		
		R[0] = [self.Simplify(expr) for expr in R[0]]
		R[1] = [self.Simplify(expr) for expr in R[1]]
		R[2] = [self.Simplify(expr) for expr in R[2]]
		
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
			
		if prog[8] != [[],[],[]]:
			print treE, "[ start with,",
			self.prettyPrint( prog[8][0], depth+2 )
			print treE, "[ connect by,",
			self.prettyPrint( prog[8][1], depth+2 )
			print treE, "[ stop with,",
			self.prettyPrint( prog[8][2], depth+2 )
	else:
		print ""
}	
	

@main {
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
			print code
			scene.prettyPrint(code)
			expr = ""
}


/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

eval returns [stmt_list]:
    p=prog {stmt_list = p}
;

prog returns [stmt_list]
@init{stmt_list = []}:
	(stmt=statement {stmt_list.append( stmt )})+ 
;

statement returns [stmt]: 
	s=statement_select 	{stmt = s}
	| e=expr 		{stmt = e}
;

statement_select returns [selection] 
@init{ s=[]; f=[]; w=[]; g=[]; h=[]; o=[]; a=[self.asTypes['dict'],[]]; rec_start=[]; rec_connect=[]; rec_stop=[]; }
@after{ selection = self._sel(s, f, w, g, h, o, a, [rec_start, rec_connect, rec_stop]); } 
:
	^(STMT_SELECT s=select_ f=from_ ( w=where_ )? ( g=group_ (h=having_)?)? ( o=order_ )? ( a=as_ )? ((rec_start=start_)? rec_connect=connect_ rec_stop=stop_ )? )
;

select_ returns [types]
@init{types = []} :
	^(SELECT 
		(
		type=PHRASE 	{ types.append( self._phrase (type.getText()) ); }
		| f= function 	{ types.append( f ); }
		| t= this_	{ types.append( t ); }
		)*
	)
;

from_ returns [env]
@init{ env=[]; }: 
	^(FROM (e=expr { env.append(e); })+)
;

as_ returns [rep] 
@init{ p=[]; }:
	^(AS AS_DICT)				{ rep= [ self.asTypes['dict'],  []]; }
	| ^(AS AS_LIST)				{ rep= [ self.asTypes['list'],  []]; }
	| ^(AS AS_VALUE)			{ rep= [ self.asTypes['value'], []]; } 
	| ^(AS v=PHRASE ( p=parameter )? )	{ rep= [ v.getText(),           p ]; } 
;

where_ returns [stack] :
	^(WHERE e=expr) { stack=e } 
;

start_ returns[with_]
@init{with_ = []} :
	^(START (e=expr { with_.append(e); })+ )
;

connect_ returns[by]
@init{by = []} :
	^(CONNECT (e=expr { by.append(e); })+ )
;

stop_ returns[with_]
@init{with_ = []} :
	^(STOP (e=expr { with_ = e; }) )
;

group_ returns [by]
@init{by = []} :
	^(GROUP 
		( type=PHRASE { by.append( self._phrase ( type.getText() ) ); }
		| f= function { by.append( f ); }
		)+
	)
;

having_ returns [stack] :
	^(HAVING e=expr) { stack=e } 
;

order_ returns [by]
@init{by = []} :
	^(ORDER 
		( 
		  type=PHRASE 	{ by.append( [ self._phrase ( type.getText()), dir ]); }
		| f= function dir=direction_ { by.append( [f, dir] ); }
		)+
	)
;

direction_ returns [dir]
@init{dir = 0} :
	( ASC  { dir=0; }
	| DESC { dir=1; }
	)?
;

expr returns [val] :
	a = assign_expr		{val = a;} 
	| l= logic_expr		{val = l;}
	| c= compare_expr	{val = c;}
	| a= arithmetic_expr	{val = a;}
	| a= atom		{val = a;}
;

age returns [a] 
@init{ a=self._val(0); }:
	^(AGE (t=expr { a=t; })?) 
;

assign_expr returns [stack]
@init{ a = self._val(0); }:
	^(ASSIGN v=PHRASE e=expr (a=age)?) { stack = self._fct( 'assign', [ self._val(v.getText()) , e, a]); }
;

logic_expr returns [stack] : 
	^(OR e1=expr e2=expr)	{ stack = self._fct('or',  [e1, e2]); }
	| ^(XOR e1=expr e2=expr){ stack = self._fct('xor', [e1, e2]); } 
	| ^(AND e1=expr e2=expr){ stack = self._fct('and', [e1, e2]); }
	| ^(NOT e=expr) 	{ stack = self._fct('not', [e] ); }
;

compare_expr returns [stack]: 
	^(IN e1=expr e2=expr)	{ stack = self._fct('in', [e2, e1]); }
	| ^(EQ e1=expr e2=expr)	{ stack = self._fct('eq', [e1, e2]); }
	| ^(NE e1=expr e2=expr) { stack = self._fct('ne', [e1, e2]); }
	| ^(GE e1=expr e2=expr)	{ stack = self._fct('ge', [e1, e2]); }
	| ^(GT e1=expr e2=expr)	{ stack = self._fct('gt', [e1, e2]); }
	| ^(LE e1=expr e2=expr)	{ stack = self._fct('le', [e1, e2]); }
	| ^(LT e1=expr e2=expr)	{ stack = self._fct('lt', [e1, e2]); }
;

arithmetic_expr returns [stack]: 
	^(MUL e1=expr e2=expr)	{ stack = self._fct('mul', [e1, e2]); }
	|^(DIV e1=expr e2=expr)	{ stack = self._fct('div', [e1, e2]); }
	|^(MOD e1=expr e2=expr)	{ stack = self._fct('mod', [e1, e2]); }
	|^(SUB e1=expr e2=expr)	{ stack = self._fct('sub', [e1, e2]); }
	|^(ADD e1=expr e2=expr)	{ stack = self._fct('add', [e1, e2]); }
	|^(POW e1=expr e2=expr)	{ stack = self._fct('pow', [e1, e2]); }
	|^(NEG e=expr)		{ stack = self._fct('neg', [e]); }
	|^(POS e=expr)		{ stack = self._fct('pos', [e]); }
;

atom returns [stack] :
	val = value			{stack = val}
	| var = variable		{stack = var}
	| fct = function		{stack = fct}
	| '(' e=expr ')'		{stack = e  }
	| s=statement_select		{stack = s  }
;

value returns [val] :
	  ^(VAL STRING	)	{val= self._val( $STRING.getText()[1:-1] ); }
	| ^(VAL INTEGER )	{val= self._val( int($INTEGER.getText()) ); }
	| ^(VAL FLOAT	)	{val= self._val( float($FLOAT.getText()) ); }
	| ^(VAL TRUE	)	{val= self._val( True  ); }
	| ^(VAL FALSE	)	{val= self._val( False ); }
	| t=this_		{val=t; }
	| l=list_		{val= self._list(l ) ; }
;

this_ returns [p]
@init { p=self._this(); }:
	^(THIS (PHRASE { p=self._this($PHRASE.getText()); })?)
;

list_ returns [l]
@init{ l = [] } :
	^(LIST ( e=expr { l.append(e); } )*)
;

variable returns [var]
@init{ a = self._val(0); }:
	^(VAR PHRASE (a=age)?) { var = self._var( $PHRASE.getText(), a ); }
;

function returns [stack] :
	^(FCT PHRASE params=parameter?)
	{ stack = self._fct( $PHRASE.getText(), params) if $PHRASE.getText()!= "eval" else self._eval(params[0]) ; }
;

parameter returns [stack]
@init{stack = []} :
	(e=expr {stack.append(e)})*
;
