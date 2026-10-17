from tkinter import *
import pandas
import random
import winsound

FRONTGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("questions_to_remenber.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("questions.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
 

def next_card():
    global current_card , flip_timmer
    window.after_cancel(flip_timmer)

    if len(to_learn) == 0: 
        canva.itemconfig(card_title, text="Congratulations!", fill="black")
        canva.itemconfig(card_word, text="All Questions learned!", fill="black")
        canva.itemconfig(card_background, image=card_front)
        return

    current_card = random.choice(to_learn)

    canva.itemconfig(card_title,text="Question" , fill="black")
    canva.itemconfig(card_word,text=current_card["Question"] , fill="black")
    canva.itemconfig(card_background, image=card_front)

    flip_timmer = window.after(3000,func=flip_card)


def flip_card():
    winsound.Beep(500, 400)
    canva.itemconfig(card_title , text="Answer" , fill="white")
    canva.itemconfig(card_word, text=current_card["Answer"] , fill="white")
    canva.itemconfig(card_background, image=card_back )

def is_know():
    winsound.Beep(1200, 400)
    to_learn.remove(current_card) 

    progress_label.config(text=f"Questions left: {len(to_learn)}") 

    data=pandas.DataFrame(to_learn)
    data.to_csv("questions_to_remenber.csv", index=False)
    #did this because we dont want to reset everything after we re-launch the program
    next_card()

def reset_progress():
    global to_learn
    original_data = pandas.read_csv("questions.csv")
    to_learn = original_data.to_dict(orient="records")
    progress_label.config(text=f"Questions left: {len(to_learn)}")
    next_card()

def wrong_answer():
    winsound.Beep(400, 400) 
    next_card()
# -----------------------------UI----------------------------
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=FRONTGROUND_COLOR)

flip_timmer = window.after(3000,func=flip_card)

canva=Canvas(width=800 , height=526)
card_front=PhotoImage(file="card_front.png")
card_back=PhotoImage(file="card_back.png")
card_background = canva.create_image(400,263,image=card_front)
card_title = canva.create_text(400, 150, text="", font=("Arial", 28, "italic"), width=650)
card_word = canva.create_text(400, 263, text="", font=("Arial", 32, "bold"), width=650)
canva.config(bg=FRONTGROUND_COLOR , highlightthickness=0)
canva.grid(row=0,column=0,columnspan=2)

correct_button_img = PhotoImage(file="right.png")
correct_button = Button(image=correct_button_img,command=is_know, highlightthickness=0)
correct_button.grid(row=1,column=1)

wrong_button_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_img,command=wrong_answer, highlightthickness=0)
wrong_button.grid(row=1,column=0)

progress_label = Label(text=f"Questions left: {len(to_learn)}", bg=FRONTGROUND_COLOR, font=("Arial", 14))
progress_label.grid(row=2, column=0, columnspan=2)

reset_button_img = PhotoImage(file="reset.png")  
reset_button = Button(image=reset_button_img, command=reset_progress, highlightthickness=0)
reset_button.grid(row=3, column=0, columnspan=2)

next_card()

window.mainloop()
