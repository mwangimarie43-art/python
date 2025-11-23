#for loop-used to iterrate over a sequence (list, tuple, string) 
#loopping overa string
"""for variable in sequence:
      #block of code to be executed for each item in the sequence"""
for x in "cursor":
    print(x)

#looping through a list
students=["Maart","Phill","Alice","Brian","Cate"]
for y in students:
    print(y)
#break statement can be used to terminate a loop
marks=[12,23,43,56,78,90,98]
for i in marks:
    print(i)
    if i==43:
        break
#loop through a range
for z in range(3,11):
    print(z)

#while loop-used to execute a block of code as long as a condition is true
"""while condition:
      #block of code to be executed as long as the condition is true"""
a=1
while(a<=5):
    print(a)
    a+=1   #Increment