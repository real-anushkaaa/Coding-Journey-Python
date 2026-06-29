"""
Python multilevel Inheritance Practice

Question:
Create Animal → Dog → Puppy.
"""

# Write your solution below.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name,breed)
        self.age = age

p1 = Puppy("sweety","jerman shephard",20)

print(p1.name)
print(p1.breed)
print(p1.age)