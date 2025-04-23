from cProfile import label
import tkinter as tk
from tkinter import Button, messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import simpledialog
import os
import subprocess
import sys
import json
import time 
import random
import threading
import requests
import datetime
import re
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
import matplotlib.animation as animation
import numpy as np
from collections import deque




import sensors

config = {
    "bg":"#212935", # background hex color
    "text":"#ffffff", # text hex color
}




root = tk.Tk()
root.geometry("800x600")
root.title("Tonbridge F24+ GUI")
root.configure(bg=config["bg"])
root.resizable(False, False)

def NotImplementedYet(feature = "This Feature"):
    messagebox.showinfo("Not Implemented Yet", f"{feature} is not implemented yet")
    return f"{feature} is not implemented yet"

# creating menus at the top
menu = tk.Menu(root)
root.config(menu=menu)
# add new menus here
fileMenu = tk.Menu(menu, tearoff=0)
editMenu = tk.Menu(menu, tearoff=0)

# File Menu conf
menu.add_cascade(label="File", menu=fileMenu)

# File Menu items
fileMenu.add_command(label="Exit", command=root.quit)
# Edit menu conf
menu.add_cascade(label="Edit", menu=editMenu)

# Edit menu items
editMenu.add_command(label="Preferences", command=lambda: NotImplementedYet("Preferences"))

frame = tk.Frame(root, bg=config["bg"])
frame.pack()
text = tk.Label(frame, text="Tonbridge F24+ GUI", bg=config["bg"], fg=config["text"], font=("Arial", 24))
text.grid(row=0, column=0, padx=10, pady=10, sticky="w")

graphFrame = tk.Frame(root, bg=config["bg"])
graphFrame.pack()

data = deque(maxlen=50)
x_vals = deque(maxlen=50)
start_time = time.time()
ani = None  # to store the animation object
data2 = deque(maxlen=50)
x_vals2 = deque(maxlen=50)
start_time2 = time.time()
ani2 = None


def getData():
    """This function handles getting data from sensors"""
    # Simulate getting data from a sensor
    # In a real application, this would be replaced with actual sensor data retrieval code
    return random.randint(0, 100)
def getData2():


    return random.randint(0, 100)
def plot1():
    """Handles Starting Plotting"""
    global ani

    def init():
        axis1.set_xlim(0, 50)
        axis1.set_ylim(0, 100)
        line.set_data([], [])
        return line,

    def update(frame):
        data.append(getData())
        x_vals.append(time.time() - start_time)
        line.set_data(range(len(data)), list(data))
        axis1.set_xlim(max(0, len(data)-50), len(data))
        return line,

    axis1.cla()
    axis1.set_title("Live Data")
    axis1.set_xlabel("Sample Number")
    axis1.set_ylabel("Value")
    line, = axis1.plot([], [], lw=2)


    ani = animation.FuncAnimation(fig1, update, init_func=init, interval=500, blit=True)

    # Redraw canvas inside tkinter
    canvas1.draw()


def clear1():
    """Handles clearing the data"""
    global data, x_vals, ani
    data.clear()
    x_vals.clear()

    if ani:
        ani.event_source.stop()
        ani._stop()
        ani = None

    axis1.cla()
    axis1.set_title("Cleared Plot")
    canvas1.draw()

def plot2():

    """Handles Starting Plotting"""
    global ani2

    def init():
        axis2.set_xlim(0, 50)
        axis2.set_ylim(0, 100)
        line.set_data([], [])
        return line,

    def update(frame):
        data2.append(getData2())
        x_vals2.append(time.time() - start_time2)
        line.set_data(range(len(data2)), list(data2))
        axis2.set_xlim(max(0, len(data2)-50), len(data2))
        return line,

    axis2.cla()
    axis2.set_title("Live Data")
    axis2.set_xlabel("Sample Number")
    axis2.set_ylabel("Value")
    line, = axis2.plot([], [], lw=2)


    ani2 = animation.FuncAnimation(fig2, update, init_func=init, interval=500, blit=True)

    # Redraw canvas inside tkinter
    canvas2.draw()

def clear2():
    """Handles clearing the data"""
    global data, x_vals, ani2
    data2.clear()
    x_vals2.clear()

    if ani2:
        ani2.event_source.stop()
        ani2._stop()
        ani2 = None

    axis2.cla()
    axis2.set_title("Cleared Plot")
    canvas2.draw()
# graphing stuff
plot1button = tk.Button(frame, text="Start Plot", command=lambda: plot1())
plot1button.grid(row=1, column=0, padx=10, pady=10, sticky="w")
clearplot1 = tk.Button(frame, text="Clear Plot", command=lambda: clear1())
clearplot1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

plot2button = tk.Button(frame, text="Start Plot", command=lambda: plot2())
plot2button.grid(row=1, column=1, padx=10, pady=10,sticky="w")
clearplot2 = tk.Button(frame, text="Clear Plot", command=lambda: clear2())
clearplot2.grid(row=2, column=1, padx=10, pady=10, sticky="w")


graphFrame.columnconfigure(0, weight=1)
graphFrame.columnconfigure(1, weight=1)
graphFrame.rowconfigure(0, weight=1)

graph1 = tk.Frame(graphFrame, bg=config["bg"])
graph1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
fig1, axis1 = plt.subplots(figsize=(4,4))
canvas1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig1, master=graph1)
canvas1.get_tk_widget().pack()

graph2 = tk.Frame(graphFrame, bg=config["bg"])
graph2.grid(row=0, column=1, padx=10, pady=10, sticky="w")
fig2, axis2 = plt.subplots(figsize=(4,4))
canvas2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig2, master=graph2)
canvas2.get_tk_widget().pack()




root.mainloop()