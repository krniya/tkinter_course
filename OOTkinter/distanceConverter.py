
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
        self.frames = dict()
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        feetToMeterFrame = FeetToMeter(container, self)
        feetToMeterFrame.grid(row=0, column=0, sticky="NSEW")

        meterToFeetFrame = MeterToFeet(container, self)
        meterToFeetFrame.grid(row=0, column=0, sticky="NSEW")

        self.frames[FeetToMeter] = feetToMeterFrame
        self.frames[MeterToFeet] = meterToFeetFrame

        self.show_frame(MeterToFeet)
        
    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MeterToFeet(ttk.Frame):
    def __init__(self, container, controller,  **kwargs):
        super().__init__(container, **kwargs)
        self.meters_values = tk.StringVar()
        self.feet_value = tk.StringVar()
        meter_label = ttk.Label(self, text="Meters:")
        meter_input = ttk.Entry(self, width=10, textvariable=self.meters_values, font=("Arial", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, text="Feet show here", textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page = ttk.Button(self, text="Swich FeetToMeter", command= lambda: controller.show_frame(FeetToMeter))

        meter_label.grid(column=0, row=0, sticky="W")
        meter_input.grid(column=1, row=0, sticky="EW")
        meter_input.focus()
        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page.grid(column=0, row=3, columnspan=2, sticky="EW")

        # Updating padding
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            meters = float(self.meters_values.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

class FeetToMeter(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.meters_values = tk.StringVar()
        self.feet_value = tk.StringVar()
        feet_label = ttk.Label(self, text="Feets:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Arial", 15))
        meter_label = ttk.Label(self, text="Meter:")
        meter_display = ttk.Label(self, text="meter show here", textvariable=self.meters_values)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page = ttk.Button(self, text="Swich MeterToFeet", command= lambda: controller.show_frame(MeterToFeet))

        feet_label.grid(column=0, row=0, sticky="W")
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus()
        meter_label.grid(column=0, row=1, sticky="W")
        meter_display.grid(column=1, row=1, sticky="EW")
        switch_page.grid(column=0, row=3, columnspan=2, sticky="EW")
        
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        # Updating padding
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meter = feet / 3.28084
            self.meters_values.set(f"{meter:.3f}")
        except ValueError:
            pass

 
root = DistanceConverter()
font.nametofont("TkDefaultFont").configure(size=15)
root.columnconfigure(0, weight=1)

root.mainloop()