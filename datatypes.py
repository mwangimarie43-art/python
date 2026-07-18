#data types
#data types tells python what kind of value we are working with
#string
import array as arr
import numpy as np

school="JKUAT"
location="Kenya"
print(type(school))    #string
print(type(location))  #string

#numbers ...int,floaat,complex
#integer-stores whole numbers
year_established=1997   #integer
students=20000          #integer
print(type(year_established))
print(type(students))
#float-stores decimal numbers
pi=3.14                  #float
w=65.5                  #float
print(type(pi))
print(type(w))

#complex-stores numbers with an imaginary part j
a=2 + 3j
b=5 + 4j
print(type(a))
print(type(b))

#boolean-stores True or False values
is_open=True    #boolean
is_closed=False #boolean
print(type(is_open))        
print(type(is_closed))


#identity operator
age1=234
age2=12
print(age1 is age2)
print(age1 is not age2)


#ARRAYS
my_arr=arr.array('i',[34,2,4,67,87,56])
print(my_arr)
print(my_arr.index(2))
print(type(my_arr))
my_arr.append(23)
print(my_arr)
my_arr.insert(2,134)
print(my_arr)
my_arr.remove(4)
print(my_arr)
my_arr.pop()
print(my_arr)
my_arr.reverse()
print(my_arr)

for x in my_arr:
    print(x)

my_array=arr.array('i',[2,3,1,24,12])
print(my_array)
my_arr.extend(my_array)
print(my_arr)
my_string=arr.array()
