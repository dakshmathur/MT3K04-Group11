import tkinter as tk
import serial
import threading
import time

# Global variables to store serial data
data1 = [1,7,5,2,7,7,2,4,6,2,6,9,0,1,7,5,2,7,7,2,4,6,2,6,9,0]
data2 = [1,7,5,5,2,7,6,2,6,9,0,1,7,7,2,4,6,2,6,9,0,2,7,7,2,4]

# Function to read data from serial port
def read_serial_data(serial_port, baud_rate):
    global data1, data2
    ser = serial.Serial(serial_port, baud_rate)
    while True:
        if ser.inWaiting() > 0:
            line = ser.readline().decode('utf-8').rstrip()
            # Assuming data is comma-separated: value1,value2
            values = line.split(',')
            if len(values) == 2:
                data1.append(float(values[0]))
                data2.append(float(values[1]))
                # Keep only the latest N data points
                data1 = data1[-100:]
                data2 = data2[-100:]

# Function to draw axes and labels for each graph
def draw_axes(canvas, y_offset, label, color):
    width = canvas.winfo_width()
    height = canvas.winfo_height() // 2  # Divide canvas for two graphs

    # Drawing axes
    canvas.create_line(50, height - 50 + y_offset, width - 10, height - 50 + y_offset, tag="graph")  # X-axis
    canvas.create_line(50, 10 + y_offset, 50, height - 50 + y_offset, tag="graph")  # Y-axis

    # Adding labels and legends
    canvas.create_text(25, height - 85 + y_offset, text="Voltage", angle=90, tag="graph")
    canvas.create_text(width - 80, height - 15 + y_offset, text="Time (ms)", tag="graph")
    canvas.create_text(100, 20 + y_offset, text=label, fill=color, tag="graph")

# Function to draw the graph
def draw_graph(canvas, data, color, y_offset, label):
    draw_axes(canvas, y_offset, label, color)  # Draw axes and labels
    width = canvas.winfo_width()
    height = canvas.winfo_height() // 2  # Divide canvas for two graphs
    max_data = max(data, default=1)  # Avoid division by zero
    points = [
        (50 + i * (width - 60) / len(data), height - 50 - (data_point * (height - 100) / max_data) + y_offset)
        for i, data_point in enumerate(data)
    ]
    for i in range(len(points) - 1):
        canvas.create_line(points[i] + points[i+1], fill=color, tags="graph")

# Function to update the canvas
def update_canvas(canvas):
    while True:
        canvas.delete("graph")  # Clear previous graph
        draw_graph(canvas, data1, "blue", 0, "Atrial")
        draw_graph(canvas, data2, "red", canvas.winfo_height() // 2, "Ventricular")
        time.sleep(0.1)  # Adjust the refresh rate as needed

# Function to create the main window and start the threads
def main():
    root = tk.Tk()
    root.title("ECG Graphs")

    canvas = tk.Canvas(root, width=600, height=800)  # Adjust height for two graphs
    canvas.pack(fill=tk.BOTH, expand=True)

    # Serial communication parameters
    serial_port = 'COM8'  # Change to your port
    baud_rate = 115200    # Change to your baud rate

    # Start the serial reading thread
    serial_thread = threading.Thread(target=read_serial_data, args=(serial_port, baud_rate))
    serial_thread.daemon = True
    serial_thread.start()

    # Start the canvas updating thread
    canvas_thread = threading.Thread(target=update_canvas, args=(canvas,))
    canvas_thread.daemon = True
    canvas_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()