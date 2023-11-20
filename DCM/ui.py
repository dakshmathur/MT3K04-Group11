import tkinter as tk
from PIL import ImageTk, Image
from settings import BACKGROUND_IMAGE_DIR

#This function renders the backround for the master window
def render_backround(window):

    #create a canvas that fills the window
    canvas = tk.Canvas(window)
    canvas.pack(fill="both", expand=True)
    
    #This function dynamically changes the size of the canvas and frame according to the screen size
    def resize_image(event):

        # Get the current window size
        new_width = event.width
        new_height = event.height
        
        # Load the background image and resize it to fit the window
        image = Image.open(BACKGROUND_IMAGE_DIR)
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