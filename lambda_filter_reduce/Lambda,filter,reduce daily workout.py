import functools

n=[1,2,3,4,5,6,7,8,9,10]

o1= filter(lambda x: x%2 ==0 , n)
print(list(o1))
o2 = filter(lambda x: x%3 ==0 , n)
print(list(o2))

#2.	Write a Python program to square and cube every number in a given list of integers using Lambda.
n=[1,2,3,4,5,6,7,8,9,10]
o3= map(lambda x: x**2,n)
print(list(o3))
o4= map(lambda x: x**3,n)
print(list(o4))

#3.	Write a Python program to find if a given string starts with a given character using Lambda.
n=["Apple","America","India","Rajasthan","Arizona"]
o5= filter(lambda x:x[0] == "A" , n )
print(list(o5))

#6.	Write a Python program to check whether a given string is a number or not using Lambda.
p="12345678"
y=p.isnumeric()
print(y)

#8.	Write a Python program to create Fibonacci series up to n using Lambda
from functools import reduce
num=4
z= reduce(lambda x,y:x*y, range(1,num+1))
print("%d! = %d" % (num,z) )

#10.	Write a Python program to find the intersection of two given arrays using Lambda
p = [1,2,3,4,5]
q=[1,3,4,7,8]
z= filter(lambda x: x in p,q)
print(list(z))

#12.	Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
t=[1,-2,3,9,-4,-2]
t=sorted(t, key=lambda o: not abs(o) == o )
print(t)

lst = [1, -2, 10, -12, -4, -5, 9, 2]
lst = sorted(lst, key=lambda o: not abs(o) == o)
print(lst)

#13.	Write a Python program to count the even and odd numbers in a given array of integers using Lambda
t=[2,3,4,5,6,7,8,9,10,11]
odd= len(list(filter(lambda x:x%2 != 0, t)))
even= len(list(filter(lambda x:x%2 == 0, t)))
print("Odd count is",odd )
print("even count is", even )

#15.	Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
t1=[2,3,4,5,6,7,8]
le= filter(lambda x: x if len(x) ==6 else "false " , t1)
for x in t1:
    print(len)

#Write a Python program to add two given lists using map and lambda.
a=[1,2,3]
b=[4,5,6]
res=map(lambda x,y: x + y , a,b)
print(list(res))

#12.	Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
c=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
res= filter(lambda x:x%13 ==0 or x%19==0, c)
print(list(res))

#13.	Write a Python program to find palindromes in a given list of strings using Lambda
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
print(result)

#14.	Write a Python program to find all anagrams of a string in a given list of strings using Lambda.


#15.	Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
d=[2, 4, 6, 9, 11]
resu=list(map(lambda x: x*2, d))
print(resu)

#16.	Calculate the mean values of the elements from input list
d1=[2, 4, 6, 9, 11]
sum = reduce(lambda x,y:x+y , d1)
mean = sum/len(d1)
print(mean)

