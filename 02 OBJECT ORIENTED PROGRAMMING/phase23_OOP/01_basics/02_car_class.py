# Question:
# Create a class Car with attributes brand and model.

class Car:
    def info(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"brand is {self.brand} and model is {self.model}")

c1 = Car()
c1.info("BMW","X5")
print(c1)

c1.display()