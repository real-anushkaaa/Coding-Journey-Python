"""
Python Static Methods Practice

Question:
Create a class MathUtility. 
Create a static method find_max(a, b) that returns the larger number.
"""

# Write your solution below.

class MathUtility:
    
    @staticmethod
    def find_max(a,b):
        if a > b:
            return a
        
        else:
            return b
        
print(MathUtility.find_max(20,10))