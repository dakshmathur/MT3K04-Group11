import tkinter as tk
import user as usr
#from PIL import ImageTk, Image

# Import the enum class for states
from enum import Enum

# Constant variables for the modes and parameters of the pacemaker
MODES = ['AOO', 'AAI', 'VOO', 'VVI']
PARAMETERS = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Ventricular Amplitude", "Atrial Pulse Width", "Ventricular Pulse Width", "VRP", "ARP"]
PARAMS = [[1, 1, 1, 0, 1, 0, 0, 0], #AOO - 0
          [1, 1, 1, 0, 1, 0, 0, 1], #AAI - 1
          [1, 1, 0, 1, 0, 1, 0, 0], #VOO - 2
          [1, 1, 0, 1, 0, 1, 1, 0]]  #VVI - 3

# State variables
connected = False
new_device = False
current_user_data = None

# Use the enum to define the states
class States(Enum):
    WELCOME = 0
    DASHBOARD = 1

# Tkinter setup
window = tk.Tk()
window.title("Pacemaker Device Controller-Monitor")
window.geometry("750x550")

frame = tk.Frame(window)
frame.pack(pady=5)

frame2 = tk.Frame(window)
frame2.pack(pady=5)

'''
def render_backround():
    backroundImg = ImageTk.PhotoImage(file = "BackroundPossible.jpg")
    canvas = tk.Canvas(window, width=700, height=3500)
    canvas.pack(fill = "both", expand=True)
    canvas.create_image(0,0,image=backroundImg,anchor='nw')
    def resize_image(e):
        global image, resized, image2
        image = Image.open("BackroundPossible.jpg")
        resized = image.resize((e.width, e.height), Image.LANCZOS)
        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0,0,image=image2,anchor='nw')
    window.bind("<Configure>", resize_image)
'''
    
# Define the current state
current_state = tk.StringVar()

# Define the welcome frame
def welcome_state():

    def get_credentials():
        return entry_username.get(), entry_password.get()

    # Login the user
    def login_user():   
        username, password = get_credentials()
        if usr.login(username, password):

            # Cache the current user as a global variable
            set_current_user(username)

            # Change the state to dashboard
            change_state(States.DASHBOARD)

    # Register the user
    def register_user():
        username, password = get_credentials()

        # Check if the user credentials are valid
        if usr.is_valid(username, password):
            usr.register(username, password)

            # Clear the username and password fields for login
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)

    # User and password labels and entry boxes
    label_username = tk.Label(frame, text="Username:")
    entry_username = tk.Entry(frame)

    label_password = tk.Label(frame, text="Password:")
    entry_password = tk.Entry(frame, show="*")

    # Login and register buttons
    button_login = tk.Button(frame, text="Login", command=login_user)
    button_register = tk.Button(frame, text="Register", command=register_user)

    # Pack the login and register widgets
    label_username.pack()
    entry_username.pack()

    label_password.pack()
    entry_password.pack()

    button_login.pack()
    button_register.pack()

def set_current_user(username):
    global current_user_data
    current_user_data = usr.get_user(username)

# Define the clear entire window
def clear_frame(fr):
    for widget in fr.winfo_children():
        widget.forget()

# Define the dashboard state 
def dashboard_state():
    # Connected to device label
    if connected:
        label_connected = tk.Label(frame, text="Communicating with Device", bg="green", fg="white")
    elif not connected:
        label_connected = tk.Label(frame, text="Not Communicating with Device", bg="red", fg="white")
    label_connected.pack(pady=5)

    # New device label
    if new_device:
        label_new_device = tk.Label(frame, text="New Device", bg="green", fg="white")
    elif not new_device:
        label_new_device = tk.Label(frame, text="Not a New Device", bg="red", fg="white")
    label_new_device.pack(pady=5)

    def update_parameters():
        for widget in frame2.winfo_children():
            widget.forget()

        usr.save_current_mode(current_user_data[0], mode.get())

        # Get the current mode
        j = MODES.index(mode.get())

        # Get the csv data offset for the current mode in the database
        k = 1 if (j > 1) else 2 if (j > 2) else 0
        l = 0

        entry_values = []

        # Create the parameter labels and entry boxes for the current mode 
        for i in range(len(PARAMETERS)):
            if PARAMS[j][i]:
                label_parameter = tk.Label(frame2, text=PARAMETERS[i])

                entry_value = tk.StringVar()
                entry = tk.Entry(frame2, textvariable=entry_value)
                entry.insert(0, current_user_data[j*4+3+k+l])

                label_parameter.pack()
                entry.pack()

                l += 1

                entry_values.append(entry_value)

        # Submit button
        button_submit = tk.Button(frame2, text="Submit", command=lambda: submit_parameters(entry_values))
        button_submit.pack()

    # Submit the parameters
    def submit_parameters(values_list):

        # Update the values
        updated_values = [val.get() for val in values_list]

        # Check if the values are valid
        if (usr.is_valid_parameters(updated_values, mode.get())):

            # Update the parameters in the database
            usr.save_current_parameters(current_user_data[0], MODES.index(mode.get()), updated_values)

    # Mode select
    mode = tk.StringVar(frame)
    mode_options = MODES
    mode.set(usr.get_current_mode(current_user_data[0]))
    mode_menu = tk.OptionMenu(frame, mode, *mode_options)
    button_mode = tk.Button(frame, text="Set Mode", command=update_parameters)

    mode_menu.pack(pady=5)
    button_mode.pack(pady=5)

    # Render the parameters
    update_parameters()

    # Logout button
    button_logout = tk.Button(frame, text="Logout", command=lambda: change_state(States.WELCOME))
    button_logout.pack(pady=5)

# Define changing states
def change_state(new_state):

    # Set the current state
    current_state.set(new_state)

    # Clear the window
    clear_frame(frame)
    clear_frame(frame2)
    
    # Render the new state
    if new_state == States.WELCOME:
        global current_user_data
        current_user_data = None
        welcome_state()
    elif new_state == States.DASHBOARD:
        dashboard_state()
    
    # Render the background
    #render_backround()

# Set the initial state
change_state(States.WELCOME)

# Start the main Tkinter process
window.mainloop()