class Dog:

    species = "Canis familiaris"  

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"


    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)  

# Accessing attributes
print(dog1.bark())         # Buddy is 3 years old.
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris
