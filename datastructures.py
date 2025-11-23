#list are ordered collection of items
#list are changeable(mutable)
#list allow duplicate values
#list are defined using square brackets []
fruits=["passion","mangoes","guava","orange","banana","apple","watermelon"]
print(fruits)
#accessing items in a list using index
print(fruits[0])  #passion
print(fruits[4])
#changing list items
fruits[2]="kiwi"
print(fruits)

#looping through a list
for x in fruits:
    print(x)
#list methods append(),insert(),remove(),pop(),clear(),sort(),reverse(),copy()
#append()-used to add an item to the end of the list
fruits.append("grapes")
print(fruits)
#sort()-sorts in alphabetical order
fruits.sort()
print(fruits)
#insert()-used to add an item at a specified index
fruits.insert(0,"pear")
print(fruits)
#remove()-used to remove a specified item
fruits.remove("banana")
print(fruits)