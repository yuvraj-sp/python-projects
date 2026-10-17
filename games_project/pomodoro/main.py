from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
clock = None

def start_timer():
    start_button.config(state=DISABLED)
    global reps
    reps+=1
    session_label.config(text=f"Session: {reps}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer.config(text="Break" , fg=RED)
    
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break" , fg=PINK)

    else :
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

def reset_timer():
    if clock is not None: 
        window.after_cancel(clock)
    start_button.config(state=NORMAL)
    timer.config(text="Timer")
    canva.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")
    session_label.config(text="Session: 1")
    global reps
    reps=0

def count_down(count):

    count_min= math.floor(count/60)
    count_sec= count % 60

    if count_sec < 10 :
        count_sec = f"0{count_sec}"

    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count > 0 :
        global clock
        clock = window.after(1000, count_down , count-1)
    else:
        start_button.config(state=NORMAL)
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)

window= Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 ,bg=YELLOW)

canva=Canvas(width=200 , height=224 , bg=YELLOW ,highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tomato_img)
timer_text = canva.create_text(100,130,text="00:00" ,fill="white",font=(FONT_NAME,35,"bold"))
canva.grid(row=1,column=1)

start_button=Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=2)

timer=Label(text="Timer",fg=GREEN , bg=YELLOW,font=(FONT_NAME,30,"bold"))
timer.grid(row=0 , column= 1)

checkmark=Label(text="" , fg=GREEN , bg=YELLOW ,font=(FONT_NAME,15,"bold"))
checkmark.grid(row=3,column=1)

session_label = Label(text="Session: 1", fg="black", bg=YELLOW, font=(FONT_NAME, 12))
session_label.grid(row=4, column=1)


window.mainloop()
