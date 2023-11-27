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
    frame = tk.Frame(canvas, bg='#414347')
    frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='center')


    # Create a frame which will contain the scrollbar and the canvas
    frame2 = tk.Frame(canvas, bg= '#F0F0F0')
    
    # Create a canvas inside frame2 for scrolling
    canvas_frame2 = tk.Canvas(frame2,bg='#F0F0F0')
    canvas_frame2.pack(side="left", fill="both", expand=True)
    canvas_frame2.pack_forget()

    # Create a scrollbar and set its command to the canvas' yview
    scrollbar = tk.Scrollbar(frame2, orient="vertical", command=canvas_frame2.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas to work with the scrollbar
    canvas_frame2.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas for your widgets
    scrollable_frame = tk.Frame(canvas_frame2,bg='#F0F0F0')

    # Add the scrollable_frame to the canvas
    canvas_frame2.create_window((0, 0),window=scrollable_frame, anchor='n')


    # This function updates the scrollable region of the canvas
    def onFrameConfigure(event):
        canvas_frame2.configure(scrollregion=canvas_frame2.bbox("all"))

    # Bind the configuration function to the scrollable_frame
    scrollable_frame.bind("<Configure>", onFrameConfigure)

    # Place frame2 with the canvas and scrollbar in the window
    frame2.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='center')
    frame2.place_forget()

    # Return canvas, frame, and the new scrollable_frame inside canvas_frame2
    return canvas, frame, frame2, canvas_frame2, scrollable_frame