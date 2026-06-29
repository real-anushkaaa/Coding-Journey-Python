"""
Python Decorators Practice

Question:
Create a decorator login_required that checks whether a user is logged in. If logged in, 
execute the function; 
otherwise, print 'Access Denied'. 
Apply it to view_profile().
"""

# Write your solution below.

def login_required(func):
    def wrapper():
        is_logged_in = True
        if is_logged_in:
            func()
        
        else:
            print("Access Denied")
    return wrapper

@login_required
def view_profile():
    print("welcome!!!!")

view_profile()