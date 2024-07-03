#Write a  Python program to create a lambda function that adds 15 to a given number passed
x=[23]
y=[15]
o1= map(lambda x,y:x+y , x,y )
print(list(o1))

#Write a  Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number
x=[23]
o2= map(lambda x :x*2 , x )
print(list(o2))

#Write a Python program to sort a list of tuples using Lambda
x=(1,3,2,4,3,5,8,4,6,9,8)
o3= sorted(x)
print(o3)
#sorting the list of tuples
y=[('English',88),('science',48), ('Maths',55),('Social',35), ('Tamil',77),('AI',48)]
o4=sorted(y)
y.sort(key=lambda x:x[1])
print(o4)
print(y)

#Write a  Python program to sort a list of dictionaries using Lambda.
#Original list of dictionaries :
ab=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

