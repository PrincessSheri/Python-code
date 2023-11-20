#identation
if 5 > 2:
    print("Five is greater than two")
#variables
userage = 100
username= "shalom"
print(userage)
print(username)
#types of variables
myVariableName= "Camel Case shalom"
MyVariableName= "Pascal Case shalom"
my_variable_name= "Snake Case shalom"
print(myVariableName)
print(MyVariableName)
print(my_variable_name)
#print function
x = "My Name is Shalom, First of his Name, Ruler of Egypt, Leader of the universe"
print(x)

a = "John Snow"
b = "is"
c = "cool"
print (a,b,c)
digit = 5
print(digit)
print(type(digit))
#data types
digit2 = 1.5
print(digit2)
print(type(digit2))
#randomlibrary
digit3=2J
print(digit3)
print(type(digit3))
#random library
import random
print(random.randrange(1,100))

#casting
Y = int(1)
Z = int(1.5)
t = int("1")
print(type(Y))
print(type(Z))
print(type(t))
#float
b = float(1)
c = float(2.0)
d= float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#string
f = str(1)
g = str(1.0)
print(type(f))
print(type(g))

#strings
string1 = "i am the most funniest person in the entire world"
print(string1)
print(type(string1))

#concatetination
string2 = ("he is also a super hero - spiderman")
string3 = string1+string2
print(string3)

#python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("digit5 is more than digit4")
else:
    print("digit4 is less than digit5")

#arithmetic operators
#sum
h = 20
i = 30
j = h + i
print(j)

#substraction
k = i-h
print(k)

#multiplication
l = h*i
print(l)

#division
m = i/h
print(m)

#modules
n = i%h
print(n)

#list
thislist = ["Apple","Banana","Cherry","Mango","Avocado"]
print(thislist)

#Access list
print(thislist[0])

#Negative indexing
print(thislist[-1])

#Randeofindexes
print(thislist[1:4])

#whileloop
o = 1
while o < 6:
    print(o)
    o+=1

#breakstatement
p = 1
while p <6:
    print(p)
    if p==3:
      break
    p+=1

#else statement
q = 1
while q <6:
    print(q)
    q+=1
else:
     print("q is more than 1")

#forloops
cars = ["Toyota","Subaru","Tesla","Nissan","Marzda"]
for x in cars:
    print(x)

#funcutions
def myfuncution():
    print("this is a funcution")
myfuncution()

#INPUT
name = input ("what is your name:")
print("your name is:" +name)
