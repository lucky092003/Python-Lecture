class Cat:

    species = "Panthera"  

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def mew(self):
        return f"{self.name} says mew"


    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Creating instances
cat1 = Cat("Buddy", 3) 
cat2 = Cat("Charlie", 5)

# Accessing attributes
print(cat1.mew())         
print(cat2.get_age())     
print(cat1.species)       
