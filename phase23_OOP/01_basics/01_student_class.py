# Question:
# Create a class Student with attributes name and age. Create an object and display the values.

class Student:
    def personal_info(self,name,age):
        self.name= name
        self.age= age

    def display(self):
        print(f"my name is {self.name} and my age is {self.age} ")

s1 = Student()
s1.personal_info('anushka',20)
print(s1)

s1.display()
