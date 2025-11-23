# conditional statement
# if condition:
      #execute this block of code
x=34
if x>20:
    print(f"{x} is greater than 20")

"""if condition:
      # block of code to be executed if the condition is true
else:
      #execute this block of code if the condition is false"""
age=14
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

"""program that asks user to enter a number and
 then checks if the number is even or odd"""
#even%2==0
#odd%2!=0
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
#get user age and check if they are eligible to drive
#a program that propmts user to enter two numbers and displays the larger number



#elif statement-used to check multiple conditions
"""if condition1:
      block of code to be executed if condition1 is true
elif condition2:
     block of code to be executed if condition2 is true
elif condition3:
      block of code to be executed if condition3 is true
else:
      block of code to be executed if all conditions are false"""
x=3
if x>10:
    print(f"{x} is greater than 10")
elif x==20:
    print(f"{x} is equal to 20")
elif x<5:
    print(f"{x} is less than 5")
else :
    print("None of the conditions are true")

"""a program that asks user to enter their age and output
below 18 children
18-25 young adult
25-40 adult
40-100 mature adult
"""
#answer for above question
age=int(input("Enter your age: "))
if age<18:
    print("You are a child.")
elif age>=18 and age<=25:
    print("You are a young adult.")
elif age>=26 and age<=40:
    print("You are an adult.")
elif age>40 and age<=100:
    print("You are a mature adult.")
else:
    print("Invalid age entered.")

"""a program that prompts user for marks and prints the grade
A: 80-100   
B: 60-79
C: 40-59
D: 0-39
"""
# answer for above question
marks=int(input("Enter your marks: "))
if marks>=80 and marks<=100:
    print("Your grade is A.")
elif marks>=60 and marks<=79:
    print("Your grade is B.")
elif marks>=40 and marks<=59:
    print("Your grade is C.")
elif marks>=0 and marks<=39:
    print("Your grade is D.")
else:
    print("Invalid marks entered.")