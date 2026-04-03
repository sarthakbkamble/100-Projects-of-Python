import turtle, pandas

cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/new/100-Projects-of-Python/Day-25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data_of_50_states = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/50_states.csv")
all_states= data_of_50_states.state.to_list()

all_states.append
correct_states=[]

data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/50_states.csv")


while len(correct_states)<51:
    answer_state = (screen.textinput(title=f"{len(correct_states)}/50 Correct States", prompt="What's the another state's name?")).title()

    if answer_state == "Exit":
        missing_states= []
        for state in all_states:
            if state not in correct_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("C:/new/100-Projects-of-Python/Day-25/States_to_learn.csv")
        
        break

    for state in data.state:
        if answer_state == state:
            ans_correct_row =  data[data["state"]==answer_state]
            if answer_state == ans_correct_row.state.values[0]:
                correct_states.append(answer_state)
                cursor.goto(ans_correct_row.x.values[0],ans_correct_row.y.values[0])
                cursor.write(arg=answer_state,font=("Arial", 8, "bold"))
    


