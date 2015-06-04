import SelectScript
import SelectScript.Interpreter

ss = SelectScript.Interpreter()

problem = """
b = IF ( 2<3;
         a=1., 2.; # then
         a=2., 1.);# else
a/b;
"""
bytecode = SelectScript.compile(problem)
print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
print "result:", ss.eval(bytecode)

####################################################################################
####################################################################################
problem = """
b = IF ( 2>3;
         a=1., 2.; # then
         a=2., 1.);# else
a/b;
"""

bytecode = SelectScript.compile(problem)
print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
print "result:", ss.eval(bytecode)

####################################################################################
####################################################################################

problem = """print("what", "shall", [1,2,3], "I", "print", False);"""

bytecode = SelectScript.compile(problem)
print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
result = ss.eval(bytecode)
print
print "result:", result

####################################################################################
####################################################################################
# Map
# =============================
#  ______________________
# |     |                |
# |     |____________  b |
# |  a  |            |   |
# |     |      c     |   |
# |     |____________|___|
# |_____|                |
# |     |                |
# |  e  |        d       |
# |_____|________________|

problem = """# counting the positive and negative combinations within WHERE ...
positive   = 0;
negative   = 0;

colors     = ['red', 'green', 'blue', 'yellow'];

neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this], 
              [b.this, c.this], [b.this, d.this], [c.this, d.this], [d.this, e.this]];

SELECT a.this,   b.this,   c.this,   d.this,   e.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors                     
WHERE  IF( [] == SELECT this
                 FROM neighbours
                 WHERE this[0] == this[1]
                 AS list;
            positive = positive + 1, True;
            negative = negative + 1, False)
AS dict;

[positive, negative];"""

bytecode = SelectScript.compile(problem)
result  = ss.eval(bytecode)

print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
print "positive results:", result[0]
print "negative results:", result[1]

####################################################################################
####################################################################################
problem = """# logging all results by applying print(..., ..., ...), the last parameter is always the return value
counter    = 0;
colors     = ['red', 'green', 'blue', 'yellow'];

neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this], 
              [b.this, c.this], [b.this, d.this], [c.this, d.this], [d.this, e.this]];

SELECT a.this,   b.this,   c.this,   d.this,   e.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors                     
WHERE  print("log:",
             counter=counter+1,
             a.this,   b.this,   c.this,   d.this,   e.this,
             
             [] == SELECT this
                   FROM neighbours
                   WHERE this[0] == this[1]
                   AS list)
AS dict;"""

print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
bytecode = SelectScript.compile(problem)
result  = ss.eval(bytecode)


####################################################################################
####################################################################################
problem = """# combining if and print to log only results where a is of red color
colors     = ['red', 'green', 'blue', 'yellow'];

neighbours = [[a.this, b.this], [a.this, c.this], [a.this, d.this], [a.this, e.this], 
              [b.this, c.this], [b.this, d.this], [c.this, d.this], [d.this, e.this]];

SELECT a.this,   b.this,   c.this,   d.this,   e.this
FROM   a=colors, b=colors, c=colors, d=colors, e=colors                     
WHERE  IF( [] == SELECT this
                 FROM neighbours
                 WHERE this[0] == this[1]
                 AS list;
            IF( a.this == "red";
                print(a.this,   b.this,   c.this,   d.this,   e.this)),
            True;
            False)
AS dict;"""

print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
bytecode = SelectScript.compile(problem)
result  = ss.eval(bytecode)

####################################################################################
####################################################################################