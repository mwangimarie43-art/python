#functions-reusable block of code that performs a specific task
# 
'''def function_name(parameters):
      body of function
#calling the function
function_name()
    '''
def greet():
    print("Hello,Mary!")
#calling the function
greet()

#function with parameters
def greetings(fname,age):
    print(f"Hello am,{fname} and am {age} years old")
#calling the function with arguments
greetings("Phill",22)
greetings("Mary",20)
greetings(fname="Alice",age=25)  #keyword arguments
greetings(age=30,fname="Brian")  #keyword arguments
#a function tat calculates area of a rectangle
def area_of_rectangle(length,width):
    area=length*width
    print(f"The area of the rectangle  is {area}")
#calling the function
area_of_rectangle(5,3)
area_of_rectangle(45,20)
#function that calculates area of a circle
def area_of_circle(radius):
    pi=3.14
    area=pi*radius**2
    print(f"The area of a circle  is {area}")
area_of_circle(14)
area_of_circle(7)
area_of_circle(radius=28)
#function that determines if a number is even or odd(num%2==0 even,num%2!=0 odd )
def even_or_odd():
    num1=int(input("Enter a number:"))
    if num1%2==0:
        print(f"{num1} is an even number.")
    else:
        print(f"{num1} is an odd number.")
#call the function
even_or_odd()


#function that returns keyword
#return keyword can be used to exit a function or return a value
#function that adds two numbers and returns the sum
def add_numbers(a,b):
    sum=a+b
    return sum
#call the  function
#option1
result=add_numbers(12,23)
print(f"The sum is {result}")
#option2
add_numbers(34,56)
print(add_numbers(34,56)) #the return value is not stored or printed

#function that ask user for two numbers and print the average
def average_of_two_numbers():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    average=(num1+num2)/2
    return average
#call the function
avg=average_of_two_numbers()
print(f"The avarege is {avg}")


