#Week-7
# Lab-7-Task-5: (Acess-control Decorator)
#Sampath Lakshmi

from functools import wraps
is_logged_in = True
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login.")
    return wrapper
@require_login
def dashboard():
    print("Welcome to the dashboard!")
is_logged_in = True
dashboard()
is_logged_in = False
dashboard()

#output:
#Welcome to the dashboard!
#Access denied. Please login.


