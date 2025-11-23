#input allow the user to enter the details on the keyboard
username=input("Please enter your name: ")
age=input("Please enter your age: ")

print(f"Hello, {username}! Welcome to the program.")
print(f"You are {age} years old.")
#print(type(age))
#ask the user to enter two numbers then display their sum
num1=input("Enter first number: ")
num2=input("Enter second number: ")
sum=int(num1)+int(num2)
print("the sum of" , num1+num2)     #The above code concatenates the two inputs as strings.
print("the sum is" ,sum)                            #This line correctly adds the two numbers after converting them to integers.www
#get the length and width of a rectangle and find the area and perimeter
length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
area=length*width
perimeter=(length+width)*2
print(f"The area of the rectangle is {area}")
print(f"The perimater of the rectangle is {perimeter}")
