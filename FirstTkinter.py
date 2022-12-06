import tkinter as tk
from tkinter import ttk # for native design

root = tk.Tk() # root as main window

root.title("Greetings") # title of window

root.columnconfigure(0, weight=1) # assigning weight

user_name = tk.StringVar() # username for input by user

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0)) # frame for input
input_frame.grid(row=0, column=0, sticky="EW") # grid for positioning

input_frame.columnconfigure(0,weight=1) 
input_frame.columnconfigure(1,weight=1)

name_label = ttk.Label(input_frame, text="Greetings", padding=(30,10)) # Text
name_label.grid(row=0, column=0, padx=(0,10), sticky="EW")  # grid for positioning

name_entry = ttk.Entry(input_frame,width=15, textvariable=user_name) # User input 
name_entry.grid(row=0, column=1, sticky="EW") # grid for positioning
name_entry.focus() # focus is for input selection as windows open

button_frame = ttk.Frame(root, padding=(20, 10)) # frame for button
button_frame.grid(sticky="EW", row=1, column=0) # grid for positioning

button_frame.columnconfigure(0,weight=1) 
button_frame.columnconfigure(1,weight=1)


greet_btn = ttk.Button(button_frame, text="Greet", command=greet) #button for greet, greet command is function name to be called
greet_btn.grid(row=1, column=0, sticky="EW")

quit_btn = ttk.Button(button_frame, text="Quit", command=root.destroy) #button for quit, root.destroy remove the screen
quit_btn.grid(row=1, column=1, sticky="EW")

root.mainloop() # loops the screen and python event loops start