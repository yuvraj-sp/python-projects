import turtle as t 
import pandas

screen=t.Screen()
screen.setup(width=800, height=900)
screen.title("Indian States Game")
image="blank_states.gif"
screen.addshape(image)  

t.shape(image)

# def get_mouse_click_cor(x,y):
#     print(x,y)

# t.onscreenclick(get_mouse_click_cor)
# t.mainloop()

data=pandas.read_csv("28_states.csv")
all_states = data.state.to_list()

guessed_states=[]

while len(guessed_states) < 28 :
    answer_state=screen.textinput(title= f"{len(guessed_states)} /28" , prompt="State's name ?").title()
    
    if answer_state == "Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states :
                missing_states.append(state)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states :
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            a=t.Turtle()
            a.hideturtle()
            a.penup()
            state_data = data[data.state == answer_state]
            a.goto(state_data.x.item() , state_data.y.item())
            a.write(answer_state)
        
        
