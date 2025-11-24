#inheritance
#parent class
class Animal:
    def __init__(self, name,breed,age):
        self.name = name
        self.breed = breed
        self.age=age



    def move(self):
        print("Animal is moving")
    def speak(self):
        print("Animal makes a sound")
#child class will inherit from parent class
class Dog(Animal):
    #speak overrides the animal speak method
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Bird(Animal):
    def speak(self):
        print("Bird chirps")
    def move(self):
        print("Bird flies")
#inheriting attributes name from parent class
#creating a dog object
dog1=Dog("Buddy", "Labrador",4)
mycat=Cat("Whiskers","Siamese",3)
mybird=Bird("Tweety","Canary",2)
print(dog1.name)  #Buddy
print(dog1.breed)
print(dog1.speak()) #Animal is moving
mycat.speak()  #Cat meows
mybird.move()  #Bird flies
mycat.move()  #Animal is moving
