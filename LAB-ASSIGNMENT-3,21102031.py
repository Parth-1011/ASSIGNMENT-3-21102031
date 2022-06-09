#first question
print("Solving Q1:")
a=int(input("Enter your first number"))
b=bin(a)
print(b)

#second question
print("Solving Q2:")
a=int(input("enter a number:"))
print("+,-,x,/,exp")
n=input()
b=int(input("enter another number:"))
if n=="+":
    print(a+b)
elif n=="-":
    print(a-b)
elif n=="x":
    print(a*b)
elif n=="/":
    print(a/b)
elif n=="exp":
    print(a**b)
else:
    print("please enter a valid operation")

#third question
print("Solving Q3:")
import math
print('a.Value of (3+4)(5):',((3+4)*5))
n=int(input("Enter value of n: "))
print("b.Value of n(n-1)/2:",(n*(n-1))/2)
r=int(input("Enter the value of r: ",))
print("c.Value of 4πr²:",(4*(math.pi)*(r**2)))
r=int(input("Value of r: ",))
a=float(input("Value of Alpha in radians: "))
b=float(input("Value of Beta in radians: "))
print("d. Value of √(r(cos(α))²+r(sin(β))²)",math.sqrt(((r)*(math.cos(math.radians(a)))**2)+((r)*(math.sin(math.radians(b)))**2)))
x1=float(input("Value of x1:"))
x2=float(input("Value of x2:"))
y1=float(input("Value of y1:"))
y2=float(input("Value of y2:"))
print("e.Value of (y2-y1)/(x2-x1):",(y2-y1)/(x2-x1))

#fourth question
print("Solving Q4:")
for i in range(5):
    print(i,end=" ")
print()
for i in range(3,10):
    print(i,end=" ")
print()
for i in range(4,13,3):
    print(i,end=" ")
print()
for i in range(15,5,-2):
    print(i,end=" ")
print()
for i in range(5,3):
    print(i,end=" ")

#fifth question
print("Solving Q5:")
a=int(input("enter the number of oxygen atoms:"))
b=int(input("enter the number of carbon atoms:"))
c=int(input("enter the number of hydrogen atoms:"))
oxygen_weight=a*15.9994
carbon_weight=b*12.01007
hydrogen_weight=c*1.00794
print("total weight of compound is:",oxygen_weight+carbon_weight+hydrogen_weight)
