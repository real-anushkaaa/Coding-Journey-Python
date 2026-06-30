"""
Python Static Methods Practice

Question:
Create a class TemperatureConverter. 
Create a static method celsius_to_fahrenheit(celsius).
"""

# Write your solution below.

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
print(TemperatureConverter.celsius_to_fahrenheit(45))