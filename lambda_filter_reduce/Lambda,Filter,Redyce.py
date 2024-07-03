import functools
import operator

#Map , Reduce and Filter Operations in Python
#Syntax: map(fun, iterable)
# Function to return double of n
#Map' operation transforms one form of data into another
def muthu(n):
    return n*5
a=[1,2,3,4,5]
output=map(muthu,a)
print("Number is ", list(output))


# Usung map funtion Ex 1
fruits = ['apple', 'mango', 'orange', 'banana']
capital_fruits = []
for fruit in fruits:
    fruit_ = fruit.upper()
    capital_fruits.append(fruit_)
print(capital_fruits)

# Usung map funtion Ex 2
capital_fruits = map(str.upper, fruits)
print(list(capital_fruits))

#map function with lambda
n1=[1,2,3,4]
n2=[3,4,5,6]
n3=[5,6,7,8]
output=map(lambda x,y,z : x+y-z , n1,n2,n3)
print(list(output))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

m=["She is liar"]
t1=list(map(list,m))
print(t1)

#reduce(function,sequence)
#'Reduce' operation combines the elements of a list into a single result

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.mul, lis))

p=[1,2,3,4,5,6,7,8,9]
print("sum of number is " , end="")
print(functools.reduce(lambda x,y: x+y, p ))
print("max of num is  " , end="")
print(functools.reduce(lambda x,y: x if x>y else y, p))
print(functools.reduce(operator.add,p))
print(functools.reduce(operator.mul,p))

#filter
#filter(function, iterable(s))
#'Filter' operation selects a subset of items from a list based on a certain condition.

def starts_with_A(s):
    return s[0] == "A"

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruits)
print(type(filter_object))
print(list(filter_object))

#filter using lambda
output= filter(lambda s: s[0] == 'A', fruits)
print(list(output))

#filter using lambda to find grades
s=[30,40,50,60,70,80,90,95,75]
o1=filter(lambda x:x>50 , s)
print("Passed students" , list(o1))





