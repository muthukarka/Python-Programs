
#1.	Check if a number is divisible by 2,3,4
x = int(input("Enter a number:"))
if x %2 == 0:
    print('Divisible by 2')
elif x %3 == 0:
    print('Divisible by 3')
elif x %4 == 0:
    print('Divisible by 4')
else:
    print('Not divisible by 2,3,4')

#2.	Print Grade based on marks

#Write a program to find the given number is odd or even
x = int(input("Enter a number:"))
if x %2 == 0:
    print('It is even')
elif x %3 == 0:
    print('It is odd')
else:
    print('It is not ever or odd')

#write the program about the fizzbuzz
x = int(input("Enter a number:"))
if x %3 == 0 and x % 5 ==0:
    print('FizzBuzz')
elif (x %5 == 0):
    print('Buzz')
elif x %3 == 0:
    print('Fizz')
else:
    print('It is not fizzbuzz')

#Loops
#1.	Get a number input and print all the values from 1 to the number
x= int(input("Enter a number"))
i=1
while i < 100:
  print(i)
  i += 1

#2 Set a number input and print all the values from 1 to the number but skip values that are divisible by 10 - using continue
i = int(input("Enter a number"))
while i < 100:
  print(i)
  if i % 10 ==0:
    break
  i += 1

#5.	Get a number input and print all the values from 1 to the number but exit the loop if i > 90
i = int(input("Enter a number"))
while i < 100:
  i += 1
  if i == 90:
    continue
  print(i)

#7.	Get a number input and print sum of all the number from 1 to the number
i = int(input("enter anum"))
sum = 0
while i <= 100:
    sum += i
    i += 1
    print(sum)

#For loop to print number from 1…n , n is the user input
x= int(input("Enter a number"))
for i in range(x,100):
    i+=1
    if i==77:
        continue
    print(i)

#12 For loop to sum numbers from 1…n
x= int(input("Enter a number"))
sum=0
for i in range(x,100):
    sum+=x
    i+=sum
    print(i)

#1.	Print the following pattern using loops
#1
#2 2
#3 3 3
#4 4 4 4
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

#1.	Reverse the words in the given string program
x="Muthumani"[::-1]
print(x)

#Python program to print even length words in a string
def my_function(x):
  return x[::-1]
x = my_function("I am muthumanikandan")
print(x)

x = 'Muthumanikandan'
even_characters = []
odd_characters = []

for i in range(len(x)):
    if i % 2 == 0:
        even_characters.append(x[i])
    else:
        odd_characters.append(x[i])
print('Odd characters: {}'.format(odd_characters))
print('Even characters: {}'.format(even_characters))

#6.	Python program to check if a string has at least one letter and one number
x = 'Muthumanikandan1506'
print(x.isalnum())
x = 'Muthumanikandan1'
print(x.isalpha())

#9.	Remove All Duplicates from a Given String in Python
x = ["Car","Bike","Bus","Flight","Boat","Bike"]
print(type(x))
y= set(x)
print(y)

#1.	Find the size of a tuple in bytes
x=("Abc","Muthu","Kk","123",456)
print(type(x))
y=len(x)
z=bytes(y)
print(z)

#Python program to create a list of tuples from given list having number and its cube in each tuple
#Input: list = [1, 2, 3]
#Output: [(1, 1), (2, 8), (3, 27)]

x=[1,2,3]
y=tuple(x)
print(y)
z1=y[0]**3,y[1]**3,y[2]**3
print(z1)
result = tuple(zip(y,z1))
print(result)

#3.	Adding Tuple to List and vice – versa
x=(1,2,3,4)
y=["a","b","c","d"]
z=list(x)
print(type(z))
re=z+y
print(re)

#5.	Python – Sum of tuple elements
x = (1, 2, 3, 4, 5, 6, 7, 8)
y = list(x)
i = 0
for value in y:
    i += value
print(i)

#7.	Update each element in tuple list
#The original list :[(1, 3, 4), (2, 4, 6), (3, 8, 1)]
#Expected output - [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
x=[(1,3,4),(2,4,6),(3,8,1)]
y=list(x[0])
print(y)
z1= y[0]+4,y[1]+4,y[2]+4
t2=list(x[1])
t3=list(x[2])
z2=t2[0]+4,t2[1]+4,t2[2]+4
z3=t3[0]+4,t3[2]+4,t3[2]+4
print(tuple(z1),tuple(z2),tuple(z3))
print([z1,z2,z3])

#6.	Multiply Adjacent elements
#The original tuple : (1, 5, 7, 8, 10)
#Expected tuple after multiplication : (5, 35, 56, 80)
x=(1,5,7,8,10)
y=list(x)
z1=y[0]*y[1],y[1]*y[2],y[2]*y[3],y[3]*y[4]
print(tuple(z1))

#1.	Iterate over a set in Python
m= {"Muthu","Mani","Bro","Raj","Loser"}
for x in m:
    print(x)

#3.	Min and Max elements in a Set
n={1,2,3,4,5,6,7,8,9}
o=list(n)
z=min(o),max(o)
print(z)

#4.	Python program to find common elements in three lists using sets
p= {"Muthu","Mani","Bro","Raj","Loser"}
q={"Muthu","Mani","Bro",}
r={"Muthu","Mani"}
s=p.intersection(q,r)
print(s)

#Input : ar1 = [1, 5, 10, 20, 40, 80]
#ar2 = [6, 7, 20, 80, 100]
#ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#Output : [80, 20]
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
r1=set(ar1)
r2=set(ar2)
r3=set(ar3)
r4= r1.intersection(r2,r3)
print(r4)

#5.	Difference between two lists
#list1 = [10, 15, 20, 25, 30, 35, 40]
#list2 = [25, 40, 35]
#Output: [10, 15, 20, 30]
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
list3=set(list1)
list4=set(list2)
list5 = list3.difference(list4)
print(list5)

#9.	Python program to convert Set into Tuple and Tuple into Set
m={"Muthu","Mani","Bro","Raj","Loser"}
n=tuple(m)
print("Tuple",n)
x=set(n)
print("set",x)

#
x={ "Muthu", "Mani" , "Region"}
y= str(x)
print(y)








