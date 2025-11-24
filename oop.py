#oop-object oriented programming
#class- a blueprint for creating objects
class person:
    def __init__(self, name, age):  #constructor method
        self.name = name
        self.age = age
    #method to display all info
    def displayinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

# create an object
myobject=person("Alice", 30)
#dot notation
print(myobject.name)  #Alice
print(myobject.age)   #30
#calling the displayinfo method
myobject.displayinfo()  #Name: Alice, Age: 30
person2=person("phill",22)
person2.displayinfo()  #Name: phill, Age: 22


#another class
class Student:
    def __init__(self,fname,lname,age,course):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
    #method returns a readable string
    def __str__(self):
        return f"Student Name: {self.fname} {self.lname}, Age: {self.age}, Course: {self.course}"
    #method that returns full name
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def studentemail(self):
        return f"{self.lname.lower()}.{self.fname.lower()}@gmail.com"

#creating an object-instance in a class
student1=Student("Mary","Mwangi",20,"Computer Science")
print(student1)  
student2=Student("Phill","Muchiri",25,"Mathematics")
print(student2)
#calling fullname method
print(student1.fullname())  #Mary Mwangi    
print(student2.fullname())  #John Doe
print(student1.studentemail())
print(student2.studentemail())

