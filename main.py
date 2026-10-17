from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
GREEN= "#00FF00"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter =[random.choice(letters) for _ in range(random.randint(8,10))]
    password_number =[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbol =[random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0,password)
    pyperclip.copy(password)


    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_name = web_input.get()
    e_mail_name = email_input.get()
    key = pass_input.get()

    if len(web_name) == 0 or len(key)==0 :
        messagebox.showinfo(title="Oops",message="PLease make sure you have entered all deatils")
    else:

        is_ok = messagebox.askokcancel(title=web_name , message=f"These are the details entered : \n Email: {e_mail_name} \n Password: {key} \n Is it ok to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{web_name} | {e_mail_name} | {key} \n")
                web_input.delete(0,END)
                pass_input.delete(0,END)
                saved=Label(text="Password Saved.",fg=GREEN)
                saved.grid(row=5,column=1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canva=Canvas(width=200 , height=200)
image=PhotoImage(file="logo.png")
canva.create_image(100,100,image=image)
canva.grid(row=0,column=1)

website=Label(text="Website :" )
website.grid(row=1,column=0)

web_input=Entry(width=39)
web_input.grid(row=1,column=1 , columnspan=2)
web_input.focus()

email=Label(text="Email/Username :" )
email.grid(row=2,column=0)

email_input=Entry(width=39)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"abc@gmail.com")

password_label=Label(text="Password :")
password_label.grid(row=3,column=0)

pass_input=Entry(width=21)
pass_input.grid(row=3,column=1)

generate_button=Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()