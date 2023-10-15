import re
from tkinter import messagebox

def is_valid(username, password):
    if get_num_users() < 10:
        error_message = ""
        if not username:
            error_message += "Username empty.\n"
        if not password:
            error_message += "Password empty.\n"
        if len(password) < 6:
            error_message += "Password must be at least 6 characters long.\n"
        if not re.search(r'[!@#$%^&*()-_+=]', password):
            error_message += "Password must contain at least one special character.\n"
        if not re.search(r'[0-9]', password):
            error_message += "Password must contain at least one digit.\n"
        if not re.search(r'[A-Z]', password):
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
    with open("users.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        data = line.split(",")
        stored_username = data[0]
        if stored_username == username:
            return True
    return False

# Get the number of users in the file   
def get_num_users():
    with open("users.csv", "r") as file:
        lines = file.readlines()
    return len(lines)
    
# Login the user
def login(username, password):

    # Validate the credentials
    def validate_credentials(username, password):

        # Read the file and check if the username and password match
        with open("users.csv", "r") as file:
                lines = file.readlines()
        for line in lines:
            data = line.split(",")
            stored_username = data[0]
            stored_password = data[1]
            if stored_username == username and stored_password == password:
                return True
        return False

    # Check if the credentials are valid
    if validate_credentials(username, password):
        messagebox.showinfo("Success", "User logged in successfully!")
        return True
    else:
        messagebox.showerror("Error", "Invalid entry.")
        return False

#aoo (lrl, url, aa, apw), aai (lrl, url, aa, apw, arp), voo (lrl, url, va, vpw), vvi (lrl, url, va, vpw, vrp)

# Register the user
def register(username, password):

    # Write the username and password to the file
    with open("users.csv", "a") as file:
        file.write(f"{username},{password},AOO,")
        file.write(f"60,120,3.5,0.4,")
        file.write(f"60,120,3.5,0.4,250,")
        file.write(f"60,120,3.5,0.4,")
        file.write(f"60,120,3.5,0.4,320\n")

    messagebox.showinfo("Success", "User registered successfully, please login.")

def get_current_mode(username):
    with open("users.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        data = line.split(",")
        stored_username = data[0]
        if stored_username == username:
            return data[2]
    return None

def save_current_mode(current_username, mode):
    with open("users.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        data = line.split(",")
        stored_username = data[0]
        if stored_username == current_username:
            data[2] = mode
            lines[lines.index(line)] = ",".join(data)
            break
    with open("users.csv", "w") as file:
        file.writelines(lines)

def get_user(username):
    with open("users.csv", "r") as file:
        lines = file.readlines()
    for line in lines:
        data = line.split(",")
        stored_username = data[0]
        if stored_username == username:
            return data
    return None