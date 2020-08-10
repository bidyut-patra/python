def main():    
    print("Hello, World");

f=0
print(f)

f="Text"
print(f)

print("Check numbers " + str(123))

# Even though the variable name (f) is same outside and inside the following method but there
# value outside & inside are different therefore they are treated as individual variable

def testMethod1():
    f="inside the test method1"
    print(f)

# The variable name (f) is same outside and inside the following method but
# notice the variable is now marked with 'global' keyword which implies that
# there will be only one copy of the variable.

def testMethod2():
    global f
    f="inside the test method2"
    print(f)    

testMethod1()
print(f)

testMethod2()
print(f)

testMethod1()
print(f)

# Undefining the variable
del f

def testMethod2():
    print("Test method 2")

# The following call just prints the text from the method inside
testMethod2()

# The following prints statement first calls the method which prints the 
# text from the method inside and then prints return value of the method 
# by the print method
print(testMethod2())

# The following print statement prints the location of the method and treated as object
print(testMethod2)

# Function with arguments
def testMethod2(arg1, arg2):
    print(arg1, " ", arg2)

# Function returning value
def cube(x):
    return x * x * x

# Function with default value
def findSquareArea(side, unit = "cm"):
    result=side*side
    return "Area Of Square with side length " + str(side) + " " + unit + " = " + str(result) + " " + unit + "^2"

testMethod2(10, 12)
print(cube(9))

print(findSquareArea(10))

# Function with variable number of arguments
def addNumbers(*args):
    result=0
    for n in args:
        result = result + n
    return result

print(addNumbers(10, 20, 23, 45, 56))

##########################
# CONDITIONAL STRUCTURES #
##########################

x, y = 200, 200

# if, elif, else condition example and also the variable defined 
# inside the if / elif / else is accessible outside the scope

if (x < y):
    cResult = "x is less than y"
elif (x > y):
    cResult = "x is greater than y"
else:
    cResult = "x is equal to y"

print(cResult)

# ternary equivalent in python

cResult = "x is less than y" if (x < y) else "x is greater or equal to y"
print(cResult)

#################
# Various Loops #
#################

print("For Loop")
# There is no index for an array in python
# Generally iterators are used to loop through an array
for n in range(5, 10):
    print(n)

print("For Loop with enumeration")
for i, n in enumerate(range(5, 10)):
    print(i,n)

print("While Loop")
x = 0
while (x < 10):
    print(x)
    x = x + 1

# tuple or list : tuple is immutable whereas list is mutable
il = (1, 4, 7, 3, 8)
for i in il:
    print("i = {}".format(i))
arr = [1, 4, 7, 3, 8] 
arr[4] = 32
for i in arr:
    print("i = {}".format(i))

# dictionary
d = { 'x': 12, 'y': 56 }
d['z'] = 43
for k, v in d.items():
    print("k = {}, v = {}".format(k, v))

# data types
t = 56
print(f'The value is {t:>09}')
print(f'The value type is {type(t)}')
b = 5 < 6
print(f'The value is {b:>09}')
print(f'The value type is {type(b)}')
n = None
print(f'The value type is {type(n)}')
