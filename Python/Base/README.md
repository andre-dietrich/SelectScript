# SelectScript_Base

This is the SelectScript base, which offers only a language stub. It can be
used and extended to generate any kind of interface to any other discrete
simulation environment.

Currently available interfaces are:

1. SelectScript_ODE
2. SelectScript_OpenRAVE

Check their implementation, to see, how simple it is to derive a new dialect.

## Installation

then via Python setuptools:
```
$ sudo python setup.py build
$ sudo python setup.py install
```
## Simplified Grammar

```
##############################################################################
# a script is a set of statements, each statement is closed with a semicolon #
<SCRIPT> ::= (<STMT> ";" | <COMMENT>)+                                       #
##############################################################################
# a statement can be either ...                                              #
<STMT>   ::= <EXPR>                            # an expression,              #
           | <ASSIGN>                          # a variable assignment,      #
           | <SELECT>                          # a select query,             #
           | <FUNC>                            # or a function call          #
##############################################################################
# dynamically typed variable assignments, with two types of variables:       #
<ASSIGN> ::= <Id> "=" <STMT>                   # standard                    #
           | <Id> "{" <Float> "}" "=" <STMT>   # with age                    #
##############################################################################
# allowed expression (identifiers are used as variable or function names)    #
<EXPR>   ::= <Id>                              # identifier (eg, Ax43_4)     #
           | (<Id>".")?"this"                  # pointer                     #
           | <Id> "{" <Float> "}"              # variable with time horizon  #
           | "[" <PARAMS>? "]"                 # defintion of a list         #
           | <Id> "[" <EXPR> "]"               # slice operator for lists    #
           | <EXPR> <bOp> <EXPR>               # binary operators            #
           | <uOp> <EXPR>                      # unary operators             #
           | "(" <EXPR> ")"                    # parenthesis                 #
           ##################################### literals:                   #
           | <Bool>                            # T(rue), F(alse), 0, 1       #
           | <Int> | <Float>                   # ... -1, 0, 1, 2 ... | 3.12  #
           | <String>                          # "enclosed by quotations"    #
##############################################################################
# function call with and name and arbitrary parameters                       #
<FUNC>   ::= <Id> "("<PARAMS> ")"              # identifier(p1, p2, ...)     #
##############################################################################
# list of parameters, applied by functions or additional AS representations  #
<PARAMS> ::=  <STMT> ( "," <STMT> )*                                         #
##############################################################################
# querying with the possibility for specialized return values, which is      #
# defined by the final keyword "AS" ...                                      #
<SELECT> ::= "SELECT" (<Id>|<FUNC>) (","(<Id>|<FUNC>))*                      #
             "FROM" <PARAMS>+                                                #                    
           ( "WHERE" <EXPR> )?                                               #
                                               # elements to enable hierar-  # 
           (  ("START" "WITH" <PARAMS>+)?      # chical and recursive que-   #
               "CONNECT" "BY" <X_OP> <PARAMS>+ # ries, with start-, recurse- #
               "STOP" "WITH" <EXPR>  )?        # and stop-conditions ...     #
           ( "GROUP" "BY" (<Id>|<FUNC>)                                      #
                          (","(<Id>|<FUNC>))*  )?                            #
           ( "ORDER" "BY" (<Id>|<FUNC>)     ("ASC"|"DESC")?                  #
                          (","(<Id>|<FUNC>) ("ASC"|"DESC")?)* )?             #
           ( "AS" ( "val"                      # only the first value        #
                  | "list"                     # array representation        #
                  | "dict"                     # default representation      #
                  | <Id> ("("<PARAMS>")")? )?  # enabling user extensions    #
##############################################################################
# standard Boolean and arithmetic operators                                  #
<bOp>    ::= "+" | "*" | "==" | "<" | "<=" | "%" | "OR" | "AND" |            #
             "-" | "/" | "!=" | ">" | ">=" | "^" | "IN" | "XOR"              #
<uOp>    ::= "-" | "NOT"                                                     #
##############################################################################
# additional options that can speedup a recursive query                      #
<X_OP>   ::= ("NO" "CYCLE")?       # prevents cycles                         #
             "UNIQUE"?             # allows only unique select results       #
             ("MEMORIZE" <Int>)?   # generates a graph with a certain length #
             ("MAXIMUM" <Int>)     # stops after <Int> results               #
##############################################################################
additional helpers, that can be placed everywere, see the examples           #
"IF" "(" expr,                     # evaluates to true or false              #
         <STMT> (","<STMT>)* ";"   # then ... couple of statements           #
         <STMT> (","<STMT>)* ")"   # else ... couple of statements           #
                                   # last statement defines the return value #
                                                                             #
# print out arbirtray log information with this inline function, the last    #
# statement is also the return value                                         #
"print" "(" <STMT> (","<STMT>)* ")"                                          #
                                                                             #
# evaluate a piece of code                                                   #
"eval" "(" "SelectScript-commands as strings" ")"                            #
##############################################################################
<COMMENT>::= "/*" * "*/"                      # internal or multi line       #
           | "#" * <EOL>                      # line comment (until newline) #
```

## Examples

See the examples in the example folder, that shows how different problems can
be solved with SelectScript, even without an underlying simulation environment.

## Contact

If you change the code, improve this project, fix bugs, or just have comments,
feel free to contact me...

| André Dietrich |                                           |
| -------------- | ----------------------------------------- |
| web:           | http://eos.cs.ovgu.de/crew/dietrich/      |
| eMail:         | dietrich@ivs.cs.uni-magdeburg.de          |
