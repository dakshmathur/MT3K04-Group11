import tkinter as tk                                                    #Import tkinter for GUI Construction
from tkinter import messagebox
import user as usr                                                      #Import user to store user date and parameters
import validate_param as vp                                             #Import validate_param to validate parameters
import database as db                                                   #Import database module for database management
from settings import States, DATABASE_DIR, RATE_SMOOTHING_OPTIONS       #Import settings for parameters
from settings import PARAMETER_UNITS, ACTIVITY_THRESHOLD_OPTIONS
from settings import SER_COM_PORT, SER_BAUD_RATE
import ui as ui                                                         #Import ui for GUI construction
import egram as eg                                                      #Import egram for egram construction
import communication as cm                                            #Import communication for serial communication

import wmi                                              #Import Windows Management Instrumentation for checking windows usb connections
import io                                               #Import input output
from contextlib import redirect_stdout                  #Import redirect_stdout 
import re                                               #Import regex
import sqlite3                                          #Import sqlite3 for database management

# Global variables
connected = False                                       #Checks if the device is connected
new_device = False                                      #Checks if a new device is connected
logout_button_pressed = False                           #checks if the logout button is pressed
current_user_id = None                                  #Stores the current user data

sim_status = 0
send_recv = 0

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

#call function to render frames and canvas
canvas, frame, frame2, canvas_frame2, scrollable_frame = ui.render_backround(window)

# Define the current state of the application
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

            # #place frame 2 which contains parameter values
            frame2.place(relx=0.5, rely=0.55, relwidth=0.25, relheight=0.55, anchor='center')
            canvas_frame2.pack(side="left", fill="both", expand=True)
            
            # Cache the current user as a global variable
            global current_user_id
            current_user_id = db.get_user_id(username)

            # Change the state to dashboard
            change_state(States.DASHBOARD)

    # Register the user
    def register_user():
        username, password = get_credentials()

        # Check if the user credentials are valid
        if usr.is_valid_register(username, password):
            usr.register(username, password)

            # Clear the username and password fields for login
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)

    # User and password labels and entry boxes
    label_username = tk.Label(frame, text="Username", bg='#414347', fg='white', font='Helvetica 12 bold')
    entry_username = tk.Entry(frame)

    label_password = tk.Label(frame, text="Password", bg='#414347', fg='white', font='Helvetica 12 bold')
    entry_password = tk.Entry(frame, show="*")

    # Login and register buttonsn
    button_login = tk.Button(frame, text="  Login  ", command=login_user, bg="#212429", fg="white", font='Helvetica 10 bold')
    button_register = tk.Button(frame, text=" Register ", command=register_user, bg="#212429", fg="white", font='Helvetica 10 bold')

    # Pack the login and register widgets
    label_username.place(relx=0.5, rely=0.2, anchor='center')
    entry_username.place(relx=0.5, rely=0.3, anchor='center')

    label_password.place(relx=0.5, rely=0.4, anchor='center')
    entry_password.place(relx=0.5, rely=0.5, anchor='center')

    button_login.place(relx=0.42, rely=0.65, anchor='center')
    button_register.place(relx=0.58, rely=0.65, anchor='center')

    # Version num/instatution
    label_version = tk.Label(frame, text="Version 0.2.0\tMcMaster University", bg='#414347', fg='white', font='Helvetica 8')
    label_version.place(relx=0.5, rely=0.95, anchor='center')

# This function deines the dashboard state 
def dashboard_state():

    def configure_scrollable_frame(event):
        # You might want to subtract a little if you want the scrollbar to be inside the frame
        new_width = canvas_frame2.winfo_width() 
        scrollable_frame.config(width=new_width)
        # Make sure the canvas_frame2 scrollregion is updated to encompass the new size of scrollable_frame
        canvas_frame2.configure(scrollregion=canvas_frame2.bbox("all"))

    # Bind this function to the canvas_frame2 configuration event
    canvas_frame2.bind("<Configure>", configure_scrollable_frame)

    # Connected/not connected device label
    if connected:
        serial_number = extracted_string
        label_connected = tk.Label(frame, text=f"Communicating with Device, SN: {serial_number}", bg='#414347', fg="green", font='Helvetica 12 bold')
    elif not connected:
        label_connected = tk.Label(frame, text="Not Communicating with Device", bg='#414347', fg="red", font='Helvetica 12 bold')

    # Place label in frame
    label_connected.place(relx=0.5, rely=0.05, anchor='center')

    # New/old device label
    if new_device:
        label_new_device = tk.Label(frame, text="New Device", bg='#414347', fg="green", font='Helvetica 12 bold')
    elif not new_device:
        label_new_device = tk.Label(frame, text="Not a New Device", bg='#414347', fg="red", font='Helvetica 12 bold')

    # Place label in frame
    label_new_device.place(relx=0.5, rely=0.15, anchor='center')

    mode = tk.StringVar(frame)
    mode.set(db.get_mode(current_user_id).upper())

    pvarp_ext_enabled = tk.BooleanVar(value=False)
    dynamic_av_delay_enabled = tk.BooleanVar(value=False)
    atr_mode_enabled = tk.BooleanVar(value=False)
    hys_enabled = tk.BooleanVar(value=False)
    sensed_av_delay_enabled = tk.BooleanVar(value=False)
    
    if (mode.get() == "VDD" or mode.get() == "DDD" or mode.get() == "DOOR" or mode.get() == "DDDR"):
        pvarp_ext_enabled = tk.BooleanVar(value=db.lookup_parameter_value(current_user_id, mode.get(), "pvarp_extension"))
        dynamic_av_delay_enabled = tk.BooleanVar(value=db.lookup_parameter_value(current_user_id, mode.get(), "dynamic_av_delay"))
        atr_mode_enabled = tk.BooleanVar(value=db.lookup_parameter_value(current_user_id, mode.get(), "atr_fallback_mode"))

    if (mode.get() == "AAI" or mode.get() == "VVI" or mode.get() == "DDD" or mode.get() == "AAIR" or mode.get() == "VVIR" or mode.get() == "DDDR"):
        hys_enabled = tk.BooleanVar(value=db.lookup_parameter_value(current_user_id, mode.get(), "hysteresis"))
        
    if (mode.get() == "DDD" or mode.get() == "DDDR"):
         sensed_av_delay_enabled = tk.BooleanVar(value=db.lookup_parameter_value(current_user_id, mode.get(), "sensed_av_delay_offset"))


    # Submit the parameters
    def submit_parameters(entry_values):
        updated_values = {key: val.get() for key, val in entry_values.items()}

        if (mode.get() == "VDD" or mode.get() == "DDD"):
            if not pvarp_ext_enabled.get():
                updated_values["PVARP EXTENSION"] = 'Off'

            if not dynamic_av_delay_enabled.get():
                updated_values["DYNAMIC AV DELAY"] = 'Off'
            else: 
                updated_values["DYNAMIC AV DELAY"] = 'On'
            
            if not atr_mode_enabled.get():
                updated_values["ATR FALLBACK MODE"] = 'Off'
            else:
                updated_values["ATR FALLBACK MODE"] = 'On'  
    
        sim_status = 0
        send_recv = 0
        
        is_valid = vp.is_valid_parameters(updated_values, mode.get())
        if is_valid:
            db_ok = db.update_mode_parameters(current_user_id, mode.get(), updated_values)

            sent = cm.txSer(updated_values, mode.get(), sim_status, send_recv)
            recieved = cm.rxSer()
            txrx_ok = sent == recieved

            if db_ok and txrx_ok:
                messagebox.showinfo("Success", "Database Updated\n\nData sent successfully.\nData sent matched data recieved.")

    def update_parameters():

        def toggle_pvarp_ext():
            if pvarp_ext_enabled.get():
                entry_pvarp_ext.configure(state='normal')
            else:
                entry_pvarp_ext.configure(state='disabled')

        def toggle_hys():
            if hys_enabled.get():
                entry_hys.configure(state='normal')
            else:
                entry_hys.configure(state='disabled')

        def toggle_sensed_av_delay():
            if sensed_av_delay_enabled.get():
                entry_sensed_av_delay.configure(state='normal')
            else:
                entry_sensed_av_delay.configure(state='disabled')

        def toggle_dynamic_av_delay():
            if dynamic_av_delay_enabled.get():
                dynamic_av_delay_enabled.set(True)
            else:
                dynamic_av_delay_enabled.set(False)

        def toggle_atr_mode():
            if atr_mode_enabled.get():
                atr_mode_enabled.set(True)
            else:
                atr_mode_enabled.set(False)

        if (mode.get() == "VDD" or mode.get() == "DDD"):
            pvarp_ext_enabled.set(db.lookup_parameter_value(current_user_id, mode.get(), "pvarp_extension"))
            dynamic_av_delay_enabled.set(db.lookup_parameter_value(current_user_id, mode.get(), "dynamic_av_delay"))
            atr_mode_enabled.set(db.lookup_parameter_value(current_user_id, mode.get(), "atr_fallback_mode"))

        if (mode.get() == "AAI" or mode.get() == "VVI" or mode.get() == "DDD"):
            hys_enabled.set(db.lookup_parameter_value(current_user_id, mode.get(), "hysteresis"))

        if (mode.get() == "DDD"):
            sensed_av_delay_enabled.set(db.lookup_parameter_value(current_user_id, mode.get(), "sensed_av_delay_offset"))

        for widget in scrollable_frame.winfo_children():
            widget.forget()

        db.update_mode(current_user_id, mode.get().lower())

        entry_values = {}

        mode_parameters = db.get_mode_parameters(current_user_id)

        for parameter in mode_parameters:
            label = parameter + (' (' + PARAMETER_UNITS[db.upper_to_lower(parameter)] + ')') if PARAMETER_UNITS[db.upper_to_lower(parameter)] != '' else parameter
            label_parameter = tk.Label(scrollable_frame, text=label)
            label_parameter.pack()

            # Dropdownsn
            if parameter == "RATE SMOOTHING":
                rate_smoothing_var = tk.StringVar(scrollable_frame)
                rate_smoothing_var.set(mode_parameters[parameter])
                entry = tk.OptionMenu(scrollable_frame, rate_smoothing_var, *RATE_SMOOTHING_OPTIONS)
                entry_values[parameter] = rate_smoothing_var
            elif parameter == "ACTIVITY THRESHOLD":
                activity_threshold_var = tk.StringVar(scrollable_frame)
                activity_threshold_var.set(mode_parameters[parameter])
                entry = tk.OptionMenu(scrollable_frame,activity_threshold_var, *ACTIVITY_THRESHOLD_OPTIONS)
                entry_values[parameter] = activity_threshold_var

            # Checkboxes
            elif parameter == "DYNAMIC AV DELAY":
                checkbox_dynamic_av_delay = tk.Checkbutton(scrollable_frame, text="Enable", var=dynamic_av_delay_enabled, command=toggle_dynamic_av_delay)
                checkbox_dynamic_av_delay.pack()
                entry_values[parameter] = dynamic_av_delay_enabled
            elif parameter == "ATR FALLBACK MODE":
                checkbox_atr_mode = tk.Checkbutton(scrollable_frame, text="Enable", var=atr_mode_enabled, command=toggle_atr_mode)
                checkbox_atr_mode.pack()
                entry_values[parameter] = atr_mode_enabled

            # Checkboxes + Input Boxes
            elif parameter == "PVARP EXTENSION":
                entry_pvarp_ext = tk.Entry(scrollable_frame, textvariable=entry_values)
                entry_pvarp_ext.insert(0, mode_parameters[parameter])
                toggle_pvarp_ext()
                checkbox_pvarp_ext = tk.Checkbutton(scrollable_frame, text="Enable", var=pvarp_ext_enabled, command=toggle_pvarp_ext)
                checkbox_pvarp_ext.pack()
                entry_pvarp_ext.pack()
                entry_values[parameter] = entry_pvarp_ext
            elif parameter == "HYSTERESIS":
                entry_hys = tk.Entry(scrollable_frame, textvariable=entry_values)
                entry_hys.insert(0, mode_parameters[parameter])
                toggle_hys()
                checkbox_hys = tk.Checkbutton(scrollable_frame, text="Enable", var=hys_enabled, command=toggle_hys)
                checkbox_hys.pack()
                entry_hys.pack()
                entry_values[parameter] = entry_hys
            elif parameter == "SENSED AV DELAY OFFSET":
                entry_sensed_av_delay = tk.Entry(scrollable_frame, textvariable=entry_values)
                entry_sensed_av_delay.insert(0, mode_parameters[parameter]) 
                toggle_sensed_av_delay()
                checkbox_sensed_av_delay= tk.Checkbutton(scrollable_frame, text="Enable", var=sensed_av_delay_enabled , command=toggle_sensed_av_delay)
                checkbox_sensed_av_delay.pack()
                entry_sensed_av_delay.pack()
                entry_values[parameter] = entry_sensed_av_delay

            # Input Boxes
            else:
                entry_value = tk.StringVar()
                entry = tk.Entry(scrollable_frame, textvariable=entry_value)
                entry.insert(0, mode_parameters[parameter])
                entry_values[parameter] = entry_value

            entry.pack()

        button_submit = tk.Button(scrollable_frame, text="Submit", command=lambda: submit_parameters(entry_values))
        button_submit.pack()

    #This function checks if the logout button is pressed
    def check_button():
        global current_user_id
        current_user_id = None
    
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
            canvas_frame2.place_forget()
            change_state(States.WELCOME)

    # Place the mode and menu
    mode_options = db.get_all_modes()
    mode_menu = tk.OptionMenu(frame, mode, *mode_options)
    mode_menu.config(bg="#212429", fg="white", activebackground='#8f8b81', activeforeground="white", font='Helvetica 10 bold')
    mode_menu["menu"].config(bg="#212429", fg="white", activebackground='#8f8b81', activeforeground="white", font='Helvetica 10 bold')
    button_mode = tk.Button(frame, text="Set Mode", command=update_parameters,  bg="#212429", fg="white", font='Helvetica 10 bold')
    mode_menu.place(relx=0.20, rely=0.25, anchor='e')
    button_mode.place(relx=0.80, rely=0.25, anchor='w')

    # Render the parameters
    update_parameters()

    # Logout button if logout button is pressed welcome screen is shown
    button_logout = tk.Button(frame, text="Logout", command=lambda: check_button(),  bg="#212429", fg="white", font='Helvetica 10 bold')
    button_logout.place(relx=0.80, rely=0.35, anchor='w')

    # Egram buttom
    button_egram = tk.Button(frame, text="Egram", command=lambda: eg.main(),  bg="#212429", fg="white", font='Helvetica 10 bold')
    button_egram.place(relx=0.80, rely=0.44, anchor='w')

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
    clear_frame(scrollable_frame)
    
    # Render the new state
    if new_state == States.WELCOME:

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