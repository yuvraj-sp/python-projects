from tkinter import *

FONT=("Arial", 12)
window = Tk()
window.title("KM to MILES Converter")
window.minsize(width=400, height=200)
window.config(bg="lightblue")

km_input=Entry(font=FONT)
km_input.focus()
km_input.bind("<Return>", lambda event: convert())
km_input.grid(row=0,column=1, padx=10, pady=10)

km_label=Label(text="Km",font=FONT)
km_label.grid(row=0,column=2, padx=10, pady=10)

my_label=Label(text="is equal to",font=FONT)
my_label.grid(row=1,column=0, padx=10, pady=10)

miles_output=Label(text="")
miles_output.grid(row=1,column=1, padx=10, pady=10)

miles=Label(text="Miles",font=FONT)
miles.grid(row=1,column=2, padx=10, pady=10)

def convert():
    try:
        value=float(km_input.get())/1.609
        miles_output.config(text=round(value,2),font=FONT,fg="green")
    except ValueError :
        miles_output.config(text="Enter valid number",fg="red")

button=Button(text="Convert",command=convert ,font=FONT )
button.grid(row=2,column=1, padx=10, pady=10)

def reset():
    km_input.delete(0, END)
    miles_output.config(text="")
    km_input.focus()

reset_button = Button(text="Reset", command=reset, font=FONT)
reset_button.grid(row=2, column=2, padx=10, pady=10)

window.mainloop()
