#Functions
#Creating a Function
def my_function_1():
    print("Hello World")

my_function_1()

#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Arguments are often shortened to args in Python documentations.
#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If you try to call the function with 1 or 3 arguments, you will get an error:
#def my_function(fname, lname):
 # print(fname + " " + lname)

#my_function("Emil")

#Arbitrary Arguments, *args
#This way the function will receive a tuple of arguments, and can access the items accordingly:
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Arbitrary Arguments are often shortened to *args in Python documentations.
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
    print("The kid lname is " + kid["lname"])
my_function(fname = "emil", lname = "Mendy")

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
    print("I am from country" + country)
my_function("America")
my_function("Australia")
my_function("Norway")
my_function("Sweden")

#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
    for x in food:
        print(x)
fruits = ("Apple","Banana","Cherry")






def my_function(x, /):
  print(x)

my_function(3)
my_function(4)
my_function(5)
