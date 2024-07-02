x = {"Muthu","Mani","Region"}
y=str(x)
print(y)
print(type(y))

x = {1,2,3,4,5}
print(type(x))
z=dict.fromkeys(x,0)
print(z)

x = [1,2,3,4,5,1,2]
print(type(x))
y=set(x)
print(y)

x={"a":100, "b" : 200, "c" : 300}
y=x.get("a")+x.get("b") + x.get("c")
print(y)

x={"a":100, "b" : 200, "c" : 300}
print(len(x))

x="Python is great and Java is also great"
y=list(x)
print(type(x))
z=set(y)
print(z)

x={"a":100, "b" : 200, "c" : 300,"d" : 150, "e" : 210}
y=sorted(x.items(), key= lambda x:x[1])
print(y)

#nested dictionary value change
#x={
#    {"name":"Car" , "Model" : 2.0 , "Year" : 2011 },
#    {"name":"bike" , "Model" : 1.0 , "Year" : 2021 },
#    {"name":"EV" , "Model" : 2.0 , "Year" : 2024 }
#}

x= {"a":100, "b" : 200, "c" : 300}
y= {"d" : 150, "e" : 210}
def merge(x,y):
    return (x.update(y))
print(merge(x,y))
print(x)

y={"name":"Car","Model": 2.0, "Year": 2011}
for key,value in y.items():
    print(key,value)

# new
x={"a":100, "b" : 200, "c" : 300,"d" : 150, "e" : 210}
print(max(x.values()))
print(min(x.values()))

x={"a":100, "b" : 200, "c" : 300,"d" : 150, "e" : 210}
y= list(x.items())
print(y)

l= 10
w=5
print("Area of rectangle is ", l*w)

y=[1,2,3,4,5,6,7,8,9,10]
print(sum(y))


x=123021456789
count=0
temp=x
for i in str(x):
    temp = temp//10
    count+=1
    print(count)


def add(a,b):
    total=a+b
    return total
a=10
b=10
total=add(a,b)
print("The total of a & b is ", total)

def count():
    return()
x=12345678910111
temp=x
ct=0
for i in str(x):
    temp=temp//10
    ct+=1
    print(ct)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


