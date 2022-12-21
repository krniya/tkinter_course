
import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from turtle import st
from windows import set_dpi_awareness

set_dpi_awareness() # dpi setting for windows


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Distance Coverter")
        frame = MeterToFeet(self, padding=(60, 30))
        frame.grid()
        self.bind("<Return>", frame.calculate_feet) 
        self.bind("<KP_Enter>", frame.calculate_feet) 

class MeterToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.meters_values = tk.StringVar()
        self.feet_value = tk.StringVar()
        meter_label = ttk.Label(self, text="Meters:")
        meter_input = ttk.Entry(self, width=10, textvariable=self.meters_values, font=("Arial", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, text="Feet show here", textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        meter_label.grid(column=0, row=0, sticky="W")
        meter_input.grid(column=1, row=0, sticky="EW")
        meter_input.focus()
        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        # Updating padding
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate_feet(self, *args):
        try:
            meters = float(self.meters_values.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

 
root = DistanceConverter()
font.nametofont("TkDefaultFont").configure(size=15)
root.columnconfigure(0, weight=1)

root.mainloop()