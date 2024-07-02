#Python Tuples
#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

#The tuple() Constructor
#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#o/p - ('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#o/p- ('orange', 'kiwi', 'melon')

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#o/p - Yes, 'apple' is in the fruits tuple

#Python - Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#o/p - ("apple", "kiwi", "cherry")

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#o/p - ('apple', 'banana', 'cherry', 'orange')

#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#Python - Unpack Tuples
#Packing a tuple:
fruits = ("apple", "banana", "cherry")
#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#o/p - apple
#banana
#cherry

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#o/p - apple
#banana
#['cherry', 'strawberry', 'raspberry']

#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#o/p - apple
#['mango', 'papaya', 'pineapple']
#cherry

#Python - Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#o/p - ('a', 'b', 'c', 1, 2, 3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#o/p - ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#Count() function
x=("Mut","Har","EEE","123","ari","axe")
y=x.count("Har")
print(y)
#Index function
x=("Mut","Har","EEE","123","ari","axe")
y=x.index("EEE")
print(y)

x=("Abc","Muthu","Kk","123",456)
print(type(x))
y=len(x)
z=bytes(y)
print(z)

x=[1,2,3]
y=tuple(x)
print(y)
z1=y[0]**3,y[1]**3,y[2]**3
print(z1)
result = tuple(zip(y,z1))
print(result)

x=(1,2,3,4)
y=["a","b","c","d"]
z=list(x)
print(type(z))
re=z+y
print(re)

x=[1,2,3,4]
y=("a","b","c","d")
z=tuple(x)
print(type(z))
res=y+z
print(res)

print(i)

x = (1, 2, 3, 4, 5, 6, 7, 8)
y = list(x)
i = 0
for value in y:
    i += value
print(i)

x=(1,5,7,8,10)
y=list(x)
z1=y[0]*y[1],y[1]*y[2],y[2]*y[3],y[3]*y[4]
print(tuple(z1))

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

myset={"Muthu","Mani", True,1,0,False}
print(myset)
print(len(myset))
for x in myset:
    print(x)
if "Mani" in myset:
    print("Yes True")

myset.add("Bro")
print(myset)

x={"Muthu","Mani","Bro","Raj"}
y={"Jen","Det",2,4,"Muthu","Mani"}
x.update(y)
z=x.union(y)
z1=x|y
print(x)
print("Union:",z)
print("Pipe" , z1)
m={"Muthu","Mani","Bro","Raj"}
n={"Jen","Det",2,4,"Muthu","Mani"}
o=m.intersection(n)
print("Inter",o)
p=m&n
print("&", p)

m= {"Muthu","Mani","Bro","Raj","Loser"}
for x in m:
    print(x)

n={1,2,3,4,5,6,7,8,9}
o=list(n)
z=min(o),max(o)
print(z)

p= {"Muthu","Mani","Bro","Raj","Loser"}
q={"Muthu","Mani","Bro",}
r={"Muthu","Mani"}
s=p.intersection(q,r)
print(s)
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
r1=set(ar1)
r2=set(ar2)
r3=set(ar3)
r4= r1.intersection(r2,r3)
print(r4)

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
list3=set(list1)
list4=set(list2)
list5 = list3.difference(list4)
print(list5)

m={"Muthu","Mani","Bro","Raj","Loser"}
n=tuple(m)
print("Tuple",n)
x=set(n)
print("set",x)


