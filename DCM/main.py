import tkinter as tk
import user as usr
import mode as md
from PIL import ImageTk, Image

# Import the enum class for states
from enum import Enum

MODES = ['AOO', 'AAI', 'VOO', 'VVI']
PARAMETERS = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Ventricular Amplitude", "Atrial Pulse Width", "Ventricular Pulse Width", "VRP", "ARP"]
PARAMS = [[1, 1, 1, 0, 1, 0, 0, 0], #AOO - 0
          [1, 1, 1, 0, 1, 0, 0, 1], #AAI - 1
          [1, 1, 0, 1, 0, 1, 0, 0], #VOO - 2
          [1, 1, 0, 1, 0, 1, 1, 0]  #VVI - 3
]

# State variables
connected = False
new_device = False
current_user_data = None
current_username = ""

# Use the enum to define the states
class States(Enum):
    WELCOME = 0
    DASHBOARD = 1

# Tkinter setup
window = tk.Tk()
window.title("Pacemaker Device Controller-Monitor")
window.geometry("750x450")

frame = tk.Frame(window)
frame.pack(pady=5)

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
    
# Define the current state
current_state = tk.StringVar()

# Define the welcome frame
def welcome_state():

    def get_credentials():
        return entry_username.get(), entry_password.get()

    def login_user():   
        username, password = get_credentials()
        if usr.login(username, password):
            set_current_user(username)
            change_state(States.DASHBOARD)

    def register_user():
        username, password = get_credentials()
        if usr.is_valid(username, password):
            usr.register(username, password)
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

    global current_username
    current_username = username

# Define the clear window function
def clear_window():
    for widget in frame.winfo_children():
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
        usr.save_current_mode(current_username, mode.get())
        mode_number = 0
        if mode.get() == "AOO":
            mode_number = 0
        elif mode.get() == "AAI":
            mode_number = 1
        elif mode.get() == "VOO":
            mode_number = 2
        elif mode.get() == "VVI":
            mode_number = 3
            
        for i in range (0, 8):
            if PARAMS[mode_number][i] == 1:
                label = tk.Label(frame, text=PARAMETERS[i])
                label.pack(pady=5)

    # Mode select
    mode = tk.StringVar(frame)
    mode_options = MODES
    mode.set(usr.get_current_mode(current_username))
    mode_menu = tk.OptionMenu(frame, mode, *mode_options)
    button_mode = tk.Button(frame, text="Set Mode", command=update_parameters)

    mode_menu.pack(pady=5)
    button_mode.pack(pady=5)

    # Parameters
    update_parameters()

# Define changing states
def change_state(new_state):

    # Set the current state
    current_state.set(new_state)

    # Clear the window
    clear_window()
    
    if new_state == States.WELCOME:
        welcome_state()
    elif new_state == States.DASHBOARD:
        dashboard_state()
    
    # Render the background
    #render_backround()

# Set the initial state
change_state(States.WELCOME)

# Start the main Tkinter process
window.mainloop()