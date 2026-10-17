from tkinter import *
from tkinter.ttk import Combobox

FONT = ("Arial", 12)
window = Tk()
window.title("Unit Converter")
window.minsize(width=400, height=250)
window.config(bg="lightblue")

conversions = {
    "KM to Miles": {"factor": 0.621371,"input":"km", "output": "miles"},
    "Feet to CM": {"factor": 30.48,"input":"ft", "output": "cm"},
    "Meters to CM": {"factor": 100,"input":"m","output": "cm"},
    "KG to Pounds": {"factor": 2.20462262,"input":"kg", "output": "lbs"}
}

conversion_label = Label(text="Convert :",font=FONT,bg="lightblue")
conversion_label.grid(row=0,column=0)

conversion_type = Combobox(window, values=["KM to Miles", "Feet to CM", "Meters to CM", "KG to Pounds"], font=FONT)
conversion_type.current(0) 
conversion_type.bind("<<ComboboxSelected>>",lambda event: input_field.focus()) 
conversion_type.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

input_label = Label(text="Enter value:", font=FONT ,bg="lightblue")
input_label.grid(row=1, column=0, padx=10, pady=10)

input_field = Entry(font=FONT)
input_field.focus()
input_field.bind("<Return>", lambda event: convert())
input_field.grid(row=1, column=1, padx=10, pady=10)

output_label = Label(text="", font=FONT)
output_label.grid(row=2, column=1, padx=10, pady=10)

def convert():
    try:
        value = float(input_field.get())
        conv_type = conversion_type.get()
        factor = conversions[conv_type]["factor"]
        result = round(value * factor, 2)
        output_label.config(text=f"{value} {conversions[conv_type]['input']} = {result} {conversions[conv_type]['output']}", fg="green", font=FONT)
    except ValueError:
        output_label.config(text="Enter valid number", fg="red")

convert_button = Button(text="Convert", command=convert, font=FONT)
convert_button.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
