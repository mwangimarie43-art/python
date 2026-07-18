# try...except-used when handlng errors in python
#try-tests the code that might cause an error
#except-handles the error
try:
    x=int(input("Enter Number:"))
    print(x/0)
except ZeroDivisionError:
    print("you can't divide a number by zero")
finally:
   print("The try except is finished")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")





