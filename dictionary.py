#dictionaries-used to store data in a key:value pairs
#dictionaries are changeable(mutable)
#dictionaries do not allow duplicates   
student={
    "name":"Phill",
    "age":22,
    "course":"Culinary arts",
    "gender":"male",
    "location":"Juja"
}
print(student)
print(type(student))
#accessing a value
print(student["name"])  #Phill
print(student["gender"])
#updating a value
student["location"]="Nairobi"
print(student)
#accessing all keys
print(student.keys())
#accessing all values
print(student.values())
#accesing key:value
print(student.items())
#looping through a dictionary
for x,y in student.items():
    print(x,":",y)