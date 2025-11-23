#1.arithmetic operators +,-,*,/,%,**
# +
a=20
b=10
c=3
print(f"The sum of {a} and {b} is {a+b}")
# -
print(f"The difference of {a} and {b} is {a-b}")
# * 
print(f"The product of {a} and {b} is {a*b}")
# / - division
print(f"The division of {a} by {b} is {a/b}")
# % modulus-returns the remainder of a division
print(f"The modulus of {a} and {b} is {a%b}")
print(f"The modulus of {a} and {c} is {a%c}")
# ** exponentiation-returns the power of a number
print(f"{a} raised to the power of {b} is {a**b}")
print(f"{b} raised to the power of {c} is {b**c}")
print(4**4)
# // floor division-returns the integer part of a division
print(f"The floor division of {a} by {b} is {a//b}")
print(f"The floor division of {a} by {c} is {a//c}")

#2.comparison operators ==, !=, >, <, >=, <=
# >-grater than
print(f"is {a} greater than {b}?, {a>b}")  #True
print(b > a)  #False
# <-less than
print(f"is {a} less than {b}?, {a<b}")     #False   
#== equal to
print(f"is {a} equal to {b}?, {a==b}")     #False
#>= greater than or equal to
print(f"is {a} greater than or equal to {b}?, {a>=b}") #True
#<= less than or equal to  
print(f"is {a} less than or equal to {b}?, {a<=b}")    #False
#!= not equal to        
print(f"is {a} not equal to {b}?, {a!=b}")   #True  

#3.assignment operators =, +=, -=, *=, /=, %=, **=, //= .....used to assign values to variables
x=15
print(x)
x += 3   #x=x+3
print(x)  #18
#-=
x -= 2   #x=x-2
print(x)  #16
#*=
x *= 2   #x=x*2
print(x)  #32
# /=            
x /= 4   #x=x/4
print(x)  #8.0
# %=
x %= 3   #x=x%3
print(x)  #2.0
# **=
x **= 3  #x=x**3
print(x)  #8.0
# //=
x //= 2  #x=x//2
print(x)  #4.0

#4.logical operators and, or, not
# and-returns True if both statements are true
p=50
q=30
print(f"is {p} greater than {q} and {q} less than {p}?, {p>q and q<p}")  #True
print(f"is {p} greater than {q} and {q} greater than {p}?, {p>q and q>p}")  #False
# or-returns True if one of the statements is true
print(f"is {p} greater than {q} or {q} greater than {p}?, {p>q or q>p}")#True
#not-reverses the result, returns False if the result is true
print(f"not {p} greater than {q} is {not(p>q)}")  #False
print(f"not {q} greater than {p} is {not(q>p)}")  #True 
#5.identity operators is, is not
# is-returns True if both variables are the same object
m=["apple", "banana"]
n=m
print(f"are m and n the same object?, {m is n}")  #True
o=["apple", "banana"]
print(f"are m and o the same object?, {m is o}")  #False
# is not-returns True if both variables are not the same object
print(f"are m and o not the same object?, {m is not o}")  #True
print(f"are m and n not the same object?, {m is not n}")  #False
