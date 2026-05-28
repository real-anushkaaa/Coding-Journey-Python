"""
Question:
Traverse a nested dictionary.
"""

# Write your code here

students = {
    "student1": {"name": "Rahul", "age": 20},
    "student2": {"name": "Aman", "age": 21}
}

for key, value in students.items():
    print(key)
    
    for k, v in value.items():
        print(k, ":", v)