#import required libraries 
import tkinter as tk                                                    #Import tkinter for GUI Construction
import user as usr                                                      #Import user to store user date and parameters
import validate_param as vp                                             #Import validate_param to validate parameters
from settings import States, DATABASE_DIR, RATE_SMOOTHING_OPTIONS       #Import settings for parameters
from PIL import ImageTk, Image                                          #Import PIL for dynamic image resizing
from enum import Enum                                                   #Import the enum class for states
import os                                                               #Import os for the absolute file math
import database as db                                                   #Import database module for database management

import wmi                                              #Import Windows Management Instrumentation for checking windows usb connections
import io                                               #Import input output
from contextlib import redirect_stdout                  #Import redirect_stdout 
import re                                               #Import regex
import sqlite3                                          #Import sqlite3 for database management

# Global state variables
connected = False                                       #Checks if the device is connected
new_device = False                                      #Checks if a new device is connected
logout_button_pressed = False                           #checks if the logout button is pressed

current_user_id = None                                  #Stores the current user data

##CHECK IF BOARD IS CONNECTED
#Initialize a WMI connection
c = wmi.WMI()

# Initialize a variable to store the output
captured_output = io.StringIO()

# Redirect the standard output to the captured_output variable
with redirect_stdout(captured_output):
    for item in c.Win32_PhysicalMedia():
        print(item)
    for drive in c.Win32_DiskDrive():
        print(drive)
    for disk in c.Win32_LogicalDisk():
        print(disk)

# Get the captured output as a string
output_text = captured_output.getvalue()

# Define the regular expression pattern to match the serial number string
pattern = r'\b[0-9A-Fa-f]{8}&\d&\d{12}\b'

# Search for the pattern in the text
match = re.search(pattern, output_text)

# save output to variable
global extracted_string
extracted_string = ""

# Check if a match was found and extract the desired string
if match:
    extracted_string = match.group(0)

# If connected, change connected variable
if "SEGGER" in output_text:
    connected = True
else:
    connected = False

# Make local files an absolute filepath everytime
runningDirectory = os.path.dirname(os.path.abspath(__file__))           #Pull current working directory
filenameBGFINAL = os.path.join(runningDirectory, 'backroundfinal.jpg')  #Append backroundfinal.jpg

#Setup the master window using tkinter
window = tk.Tk()
window.title("Pacemaker Device Controller-Monitor")
window.geometry("750x450")

#Setup the database for storing data
connector = sqlite3.connect(DATABASE_DIR)
cursor = connector.cursor()

#This function creates the database if it does not exist
try:
    db.createDB()
except:
    print("Database already exists")
    pass

#This function renders the backround for the master window
def render_backround():

    #create a canvas that fills the window
    canvas = tk.Canvas(window)
    canvas.pack(fill="both", expand=True)
    
    #This function dynamically changes the size of the canvas and frame according to the screen size
    def resize_image(event):

        # Get the current window size
        new_width = event.width
        new_height = event.height
        
        # Load the background image and resize it to fit the window
        image = Image.open(filenameBGFINAL)
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
    
    #Create frames used for login/displaying parameter values
    frame = tk.Frame(canvas, bg='#20202A')
    frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='center')
    frame2 = tk.Frame(bg="white")
    frame2.place(in_=frame, anchor='center', relx = .5, rely= .5)
    
    #return values
    return canvas, frame, frame2 

#call function to render frames and canvas
canvas, frame, frame2 = render_backround()

# Define the current staSte
current_state = tk.StringVar()

# Define the current state
current_state = tk.StringVar()

#This function define the welcome frame
def welcome_state():
    
    #This function returns the username and password entered
    def get_credentials():
        return entry_username.get(), entry_password.get()

    #This function logs the user in if the credentials appear in the user file
    def login_user():

        # Get the username and password
        username, password = get_credentials()

        if usr.login(username, password):

            #destroy the old widgets in frame 1
            for widget in frame.winfo_children():
                widget.destroy()

            #place frame 2 which contains parameter values
            frame2.place(in_=frame, anchor='center', relx = .5, rely= .5)
            
            # Cache the current user as a global variable
            global current_user_id
            current_user_id = db.get_user_id(username)

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
    label_version = tk.Label(frame, text="Version 0.1.2\tMcMaster University", bg='#20202A', fg='white')
    label_version.place(relx=0.5, rely=0.95, anchor='center')

# This function deines the dashboard state 
def dashboard_state():

    # Connected/not connected device label
    if connected:
        serial_number = extracted_string
        label_connected = tk.Label(frame, text=f"Communicating with Device, SN: {serial_number}", bg="green", fg="white")
    elif not connected:
        label_connected = tk.Label(frame, text="Not Communicating with Device", bg="red", fg="white")

    # Place label in frame
    label_connected.place(relx=0.5, rely=0.05, anchor='center')

    # New/old device label
    if new_device:
        label_new_device = tk.Label(frame, text="New Device", bg="green", fg="white")
    elif not new_device:
        label_new_device = tk.Label(frame, text="Not a New Device", bg="red", fg="white")

    # Place label in frame
    label_new_device.place(relx=0.5, rely=0.15, anchor='center')

    # Submit the parameters
    def submit_parameters(entry_values):

        # Update the values
        updated_values = {key: val.get() for key, val in entry_values.items()}

        # Check if the values are valid
        if (vp.is_valid_parameters(updated_values, mode.get())):
            db.update_mode_parameters(current_user_id, mode.get(), updated_values)

    # This function updates the parameters
    def update_parameters():
        for widget in frame2.winfo_children():
            widget.forget()

        # Update the database with the new mode
        db.update_mode(current_user_id, mode.get().lower())

        entry_values = {}

        # Create the parameter labels and entry boxes for the current mode
        mode_parameters = db.get_mode_parameters(current_user_id)

        for key in mode_parameters:
            label_parameter = tk.Label(frame2, text=key)          

            # Check if the parameter is 'Rate Smoothing' for dropdown
            if key == "Rate Smoothing":
                rate_smoothing_var = tk.StringVar(frame2)
                rate_smoothing_var.set(mode_parameters[key])  # set the default value
                entry = tk.OptionMenu(frame2, rate_smoothing_var, *RATE_SMOOTHING_OPTIONS)
                entry_values[key] = rate_smoothing_var
            else:
                entry_value = tk.StringVar()
                entry = tk.Entry(frame2, textvariable=entry_value)
                entry.insert(0, mode_parameters[key])
                entry_values[key] = entry_value

            label_parameter.pack()
            entry.pack()

        # Submit button
        button_submit = tk.Button(frame2, text="Submit", command=lambda: submit_parameters(entry_values))
        button_submit.pack()

    #This function checks if the logout button is pressed
    def check_button():
        #decale logout_button_pressed as a global variable
        global logout_button_pressed

        #if logout button is True set to False
        if logout_button_pressed:
            logout_button_pressed = False
        
        #if logout button is False set it to True, clear/hide frames, and return to welcome screen
        if not logout_button_pressed:
            logout_button_pressed = True
            for widget in frame.winfo_children():
                    widget.destroy()
            frame2.place_forget()
            change_state(States.WELCOME)

    # Mode select
    mode = tk.StringVar(frame)
    mode_options = db.get_all_modes()
    mode.set(db.get_mode(current_user_id).upper())
    mode_menu = tk.OptionMenu(frame, mode, *mode_options)
    button_mode = tk.Button(frame, text="Set Mode", command=update_parameters)

    # Place the mode and menu
    mode_menu.place(relx=0.25, rely=0.25, anchor='center')
    button_mode.place(relx=0.75, rely=0.25, anchor='center')

    # Render the parameters
    update_parameters()

    # Logout button if logout button is pressed welcome screen is shown
    button_logout = tk.Button(frame, text="Logout", command=lambda: check_button())
    button_logout.place(relx=0.75, rely=0.4, anchor='center')

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