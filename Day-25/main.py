import turtle, pandas

cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/new/100-Projects-of-Python/Day-25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_states=0

data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/50_states.csv")

while correct_states<51:
    answer_state = (screen.textinput(title=f"{correct_states}/50 Correct States", prompt="What's the another state's name?")).title()
    for state in data.state:
        if answer_state == state:
            ans_correct_row =  data[data["state"]==answer_state]
            if answer_state == ans_correct_row.state.values[0]:
                cursor.goto(ans_correct_row.x.values[0],ans_correct_row.y.values[0])
                cursor.write(arg=answer_state,font=("Arial", 8, "bold"))
                correct_states+=1
    
screen.exitonclick()

