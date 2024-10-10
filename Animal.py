class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return f"{self.name} is {self.age} years old."

class Dog(Animal):
    species = "Canis familiaries"

    def bark(self):
        return f"{self.name} says woof!"
    

class Cat(Animal):
    species = "Cat Species"

    def meow(self):
        return f"{self.name} says meow!"

# Creating a Cat instance
cat1 = Cat("cat1", 2)
print(f"age={cat1.age}")

print(cat1.meow())         
print(cat1.get_age())      
print(cat1.species)       

# Creating a Dog instance
dog1 = Dog("dog1", 2)
print(f"age={dog1.age}")

print(dog1.bark())         # dog1 says woof!
print(dog1.get_age())      # dog1 is 2 years old.
print(dog1.species)        # Canis familiaries
