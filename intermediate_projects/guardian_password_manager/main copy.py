from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
import json

GREEN= "#25A325"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project that i did earlier
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
    web_name = web_input.get().lower()
    e_mail_name = email_input.get()
    key = pass_input.get()
    new_data={
        web_name:{
            "email":e_mail_name,
            "password":key,
        }
    }


    if len(web_name) == 0 or len(e_mail_name) == 0 or len(key) == 0:
        messagebox.showinfo(title="Oops",message="PLease make sure you have entered all details")

    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
             # updating the old data with new data
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)

        finally:
            web_input.delete(0,END)
            pass_input.delete(0,END)
            saved=Label(text="Password Saved.",fg=GREEN)
            saved.grid(row=5,column=1)
            window.after(2000, saved.grid_remove)

# ---------------------- Searching the password ---------------------- #
        
def search():
    web_name=web_input.get().lower()
    try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)

    except FileNotFoundError:
           messagebox.showinfo(title="Error" , message="No Data File Found")
    
    else:
        if web_name in data:
            e_mail=data[web_name]["email"]
            key=data[web_name]["password"]
            pyperclip.copy(key)
            messagebox.showinfo(title=web_name,message=f" Email : {e_mail} \n Password: {key} ")
        else:
            messagebox.showerror(title="Error",message=f"No details for website: {web_name} exists.")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canva=Canvas(width=200 , height=200)
image=PhotoImage(file="newlogo.png")
canva.create_image(100,100,image=image)
canva.grid(row=0,column=1)

website=Label(text="Website :" )
website.grid(row=1,column=0)

web_input=Entry(width=21)
web_input.grid(row=1,column=1 )
web_input.focus()

email=Label(text="Email/Username :" )
email.grid(row=2,column=0)

email_input=Entry(width=43)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"yuvraj@gmail.com")

password_label=Label(text="Password :")
password_label.grid(row=3,column=0)

pass_input=Entry(width=21)
pass_input.grid(row=3,column=1)

generate_button=Button(text="Generate Password",width=18 , command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=18 ,command=search )
search_button.grid(row=1,column=2 ,columnspan=1)



window.mainloop()
