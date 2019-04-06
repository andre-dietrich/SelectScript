import SelectScript
import SelectScript.Interpreter

ss = SelectScript.Interpreter()

problem = """# if is like in functional programming, and the last statement within
# the then or else-part defines the return value... every part is segregated
# with a semi-colon
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
# result: 0.5
####################################################################################
####################################################################################
problem = """# the opposite way ...
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
# result: 2.0
####################################################################################
####################################################################################

problem = """# print is a little helper function that can be placed for logging purposes
# everywhere within a script ... the last statement defines the returning value
print("what", "shall", [1,2,3], "I", "print", False);
"""
bytecode = SelectScript.compile(problem)
print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
result = ss.eval(bytecode)
print
print "result:", result
# what shall [1, 2, 3] I print False
#
# result: False
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

problem = """# why ifs? counting the positive and negative combinations within WHERE ...
# that do not affect the result of the query ...
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
"""

bytecode = SelectScript.compile(problem)
result  = ss.eval(bytecode)

print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
print "1. results:", result[0]
print "positive results:", ss.callVariable("positive")
print "negative results:", ss.callVariable("negative")
# 1. results: {'a': 'red', 'c': 'blue', 'b': 'green', 'e': 'green', 'd': 'yellow'}
# positive results: 48
# negative results: 976
####################################################################################
####################################################################################
problem = """# logging all results by applying print(..., ..., ...), the last parameter is
# always the return value
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
# log: 1 red red red red red False
# log: 2 red red red red green False
# log: 3 red red red red blue False
# log: 4 red red red red yellow False
# log: 5 red red red green red False
# log: 6 red red red green green False
# log: 7 red red red green blue False
# log: 8 red red red green yellow False
# log: 9 red red red blue red False
# log: 10 red red red blue green False
# log: 11 red red red blue blue False
# ...
# log: 1024 yellow yellow yellow yellow yellow False
####################################################################################
####################################################################################
problem = """# combining if and print to log only results where "a" is of red color, note that
# the else part is not alway required ...
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
                print(a.this,   b.this,   c.this,   d.this,   e.this)), True)
AS dict;
"""
print "----------------------------------------------------------------------------"
print problem
print "----------------------------------------------------------------------------"
bytecode = SelectScript.compile(problem)
result  = ss.eval(bytecode)
# red green blue yellow green
# red green blue yellow blue
# red green yellow blue green
# red green yellow blue yellow
# red blue green yellow green
# red blue green yellow blue
# red blue yellow green blue
# red blue yellow green yellow
# red yellow green blue green
# red yellow green blue yellow
# red yellow blue green blue
# red yellow blue green yellow
####################################################################################
####################################################################################