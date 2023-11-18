import re
from settings import PASSWORD_RULES, MAX_USER_COUNT, DATABASE_DIR
from tkinter import messagebox
import database as db

# Make it an absolute filepath everytime
import os
runningDirectory = os.path.dirname(os.path.abspath(__file__)) #pull working directory

def is_valid(username, password):
    if db.get_num_users() < MAX_USER_COUNT:
        error_message = ""
        if not username:
            error_message += "Username empty.\n"
        if not password:
            error_message += "Password empty.\n"
        if len(password) < PASSWORD_RULES['min_length']:
            error_message += "Password must be at least 6 characters long.\n"
        if not re.search(PASSWORD_RULES['special_chars'], password):
            error_message += "Password must contain at least one special character.\n"
        if not re.search(PASSWORD_RULES['number_range'], password):
            error_message += "Password must contain at least one digit.\n"
        if not re.search(PASSWORD_RULES['upper_case'], password):
            error_message += "Password must contain at least one uppercase letter.\n"
        if is_existing_user(username):
            error_message = "User already exists.\n"

        if len(error_message) > 0:
            messagebox.showerror("Error", error_message)
            return False
        else:
            return True
    else:
        messagebox.showerror("Error", "Maximum number of users reached.")
        return False

# Is the user an existing user?
def is_existing_user(username):
    for i in range (db.get_num_users()):
        if db.get_username(i) == username:
            return True
    return False
    
# Login the user
def login(username, password):

    # Validate the credentials
    def validate_credentials(username, password):
        num_users = db.get_num_users()
        for i in range(num_users):
            return db.get_username(i) == username and db.get_password(i) == password

    # Check if the credentials are valid
    if validate_credentials(username, password):
        messagebox.showinfo("Success", "User logged in successfully!")
        return True
    else:
        messagebox.showerror("Error", "Invalid entry.")
        return False

# Register the user
def register(username, password):
    if db.create_user(username, password):
        messagebox.showinfo("Success", "User registered successfully, please login.")