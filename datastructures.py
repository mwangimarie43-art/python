#LIST
#list are ordered collection of items
#list are changeable(mutable)
#list allow duplicate values
#list are defined using square brackets []
my_list=[23,45,"Mary",True,2.678,"Brian"]
print(my_list)
my_list.append("Shiro")                   #append() adds item to the end of the list
print(my_list)
print(len(my_list))
my_list.pop(2)
print(my_list)
my_list.insert(4,"Phill")
print(my_list)
new_list=["Apples","books",567,"Age"]
print(new_list)
my_list.extend(new_list)
print(my_list)
for x in my_list:
    print(x)
my_list.remove(23)
print(my_list)
del my_list[3]
print(my_list)



#Tuples
my_tupple=("Sherry","Shanny","Whitney","Phill")
print(my_tupple)
print(type(my_tupple))




