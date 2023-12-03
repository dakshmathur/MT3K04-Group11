import tkinter as tk
import serial
import threading
import time
import communication as cm 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


# values for graph
x_vals = []
y_vals = []
y_vals2 = []
start_time = 0
max_time_displayed = 8

def animate(i):
    global start_time
    x_vals.append(start_time)
    #last_two_values = cm.get_last_two_values()
    y_vals.append(random.randint(0,5))
    y_vals2.append(random.randint(0,5))
    start_time += 1

    while x_vals[-1] - x_vals[0] > max_time_displayed:
        x_vals.pop(0)
        y_vals.pop(0)
        y_vals2.pop(0)

    # Get all axes of figure
    ax1, ax2 = plt.gcf().get_axes()
    # Clear current data
    ax1.cla()
    ax2.cla()
    # Plot new data
    ax1.plot(x_vals, y_vals, 'tab:red')
    ax2.plot(x_vals, y_vals2, 'tab:blue')
    #limit x-axis
    ax1.set_xlim(max(start_time - max_time_displayed, 0), start_time)

    #lables
    ax1.set_title('Atrium')
    ax1.set_ylabel('Voltage (V)')
    ax2.set_title('Ventricle')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Voltage (V)')

def main():
    # GUI
    root = tk.Tk()
    root.title("Egram Graphs")
    # graph 1
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.get_tk_widget().grid(column=0, row=1)
    # Create two subplots in row 1 and column 1, 2
    plt.gcf().subplots(2, 1, sharex=True)
    ani = FuncAnimation(plt.gcf(), animate, interval=1000, blit=False)
    root.mainloop()

if __name__ == "__main__":
    main()