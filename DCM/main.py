import tkinter as tk
import user as usr
from settings import MODES, PARAMETERS, PARAMS, States
from PIL import ImageTk, Image

# Import the enum class for states
from enum import Enum

# Global state variables
connected = False
new_device = False
current_user_data = None

# Tkinter setup
window = tk.Tk()
window.title("Pacemaker Device Controller-Monitor")
window.geometry("750x450")

def render_backround():
    canvas = tk.Canvas(window)
    canvas.pack(fill="both", expand=True)
    
    def resize_image(event):
        # Get the current window size
        new_width = event.width
        new_height = event.height
        
        # Load the background image and resize it to fit the window
        image = Image.open("backroundFinal.jpg")
        image = image.resize((new_width, new_height), Image.LANCZOS)  # Use ANTIALIAS for better image quality
        img = ImageTk.PhotoImage(image)
        
        # Update the canvas size to match the window size
        canvas.config(width=new_width, height=new_height)
        
        # Update the image on the canvas
        canvas.create_image(0, 0, image=img, anchor="nw")
        
        # Keep a reference to the image to prevent it from being garbage collected
        canvas.img = img
    
    # Bind the resize_image function to the <Configure> event
    canvas.bind("<Configure>", resize_image)
    
    # Initially, display the image at the canvas size
    canvas.event_generate("<Configure>")
    
    frame = tk.Frame(canvas, bg='#20202A')
    frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='center')
    
    frame2 = tk.Frame(bg="white")
    frame2.place(in_=frame, anchor='center', relx = .5, rely= .5)
    
    return canvas, frame, frame2 

canvas, frame, frame2 = render_backround()


# Define the current staSte
current_state = tk.StringVar()

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

            for widget in frame.winfo_children():
                widget.destroy()
            
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
    label_username = tk.Label(frame, text="Username:", bg='#20202A', fg='white')
    entry_username = tk.Entry(frame)

    label_password = tk.Label(frame, text="Password:", bg='#20202A', fg='white')
    entry_password = tk.Entry(frame, show="*")

    # Login and register buttons
    button_login = tk.Button(frame, text="Login", command=login_user, bg="white", fg="black")
    button_register = tk.Button(frame, text="Register", command=register_user, bg="white", fg="black")

    # Pack the login and register widgets
    label_username.place(relx=0.5, rely=0.2, anchor='center')
    entry_username.place(relx=0.5, rely=0.3, anchor='center')

    label_password.place(relx=0.5, rely=0.4, anchor='center')
    entry_password.place(relx=0.5, rely=0.5, anchor='center')

    button_login.place(relx=0.42, rely=0.65, anchor='center')
    button_register.place(relx=0.58, rely=0.65, anchor='center')

    # Version num/instatution
    label_version = tk.Label(frame, text="Version 0.1.0\tMcMaster University", bg='#20202A', fg='white')
    label_version.place(relx=0.5, rely=0.95, anchor='center')



# Define the dashboard state 
def dashboard_state():
    # Connected to device label
    if connected:
        label_connected = tk.Label(frame, text="Communicating with Device, SN: [Serial Number]", bg="green", fg="white")
    elif not connected:
        label_connected = tk.Label(frame, text="Not Communicating with Device", bg="red", fg="white")

    label_connected.place(relx=0.5, rely=0.05, anchor='center')

    # New device label
    if new_device:
        label_new_device = tk.Label(frame, text="New Device", bg="green", fg="white")
    elif not new_device:
        label_new_device = tk.Label(frame, text="Not a New Device", bg="red", fg="white")
    label_new_device.place(relx=0.5, rely=0.1, anchor='center')

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

    mode_menu.place(relx=0.25, rely=0.25, anchor='center')
    button_mode.place(relx=0.75, rely=0.25, anchor='center')

    # Render the parameters
    update_parameters()

    # Logout button
    button_logout = tk.Button(frame, text="Logout", command=lambda: change_state(States.WELCOME))
    button_logout.place(relx=0.75, rely=0.4, anchor='center')


# Set the current user data
def set_current_user(username):
    global current_user_data
    current_user_data = usr.get_user(username)

# Define the clear entire window
def clear_frame(fr):
    for widget in fr.winfo_children():
        widget.forget()

# Define changing states
def change_state(new_state):

    # Set the current state
    current_state.set(new_state)

    # Clear the window
    clear_frame(frame)
    clear_frame(frame2)

    
    # Render the new state
    if new_state == States.WELCOME:

        # Clear the current user data on logout
        global current_user_data
        current_user_data = None

        # Render the welcome screen
        welcome_state()

    elif new_state == States.DASHBOARD:

        # Render the dashboard
        dashboard_state()
    
    # Render the background
    #render_backround()

# Set the initial state
change_state(States.WELCOME)

# Start the main Tkinter process
window.mainloop()