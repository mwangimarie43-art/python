# import mymodule

# result=mymodule.addtwonumbers(5,10)
# print(result)

import oop
#importing student class
#create a new student object
student3=oop.Student("John","Doe",23,"Physics")
print(student3)
#import what i need

from functions import add_numbers
sum_result=add_numbers(15,25)
#import mathematical functions from math module
import math
print(math.sqrt(16))  #4.0
import datetime

print(datetime.datetime.now())
print(datetime.datetime.today()) 
from datetime import date
print(date.today())  #2024-06-10
import os
print(os.getcwd())  #current working directory
