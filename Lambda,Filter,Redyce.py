import functools
import operator

#Map Reduce and Filter Operations in Python
#Syntax: map(fun, iterable)
# Function to return double of n

def double(n):
    return n * 2
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print("result ",list(result))
