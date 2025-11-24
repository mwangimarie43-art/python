# try...except-used when handlng errors in python
#try-tests the code that might cause an error
#except-handles the error
try:
    x=10
    print(x/0)
except ZeroDivisionError:
    print("you can't divide a number by zero")