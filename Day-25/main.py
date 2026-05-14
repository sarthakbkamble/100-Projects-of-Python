import turtle, pandas

# 1. Cursor Setup
# Initialize a hidden turtle to act as a pen for writing state names on the map
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

# 2. Screen Setup
# Load the blank map image as a background shape for the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/new/100-Projects-of-Python/Day-25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# 3. Data Loading
# Load the CSV containing state names and their corresponding map coordinates
data_of_50_states = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/50_states.csv")
all_states= data_of_50_states.state.to_list()

all_states.append  # Reference to append method (kept as-is)
correct_states=[]

data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/50_states.csv")

# 4. Main Game Loop
# Continue prompting the player until they find all states or choose to exit
while len(correct_states)<51:
    # Pop up a text input dialog and convert the response to Title Case
    answer_state = (screen.textinput(title=f"{len(correct_states)}/50 Correct States", prompt="What's the another state's name?")).title()

    # Handle manual exit trigger
    if answer_state == "Exit":
        # Identify which states were missed using list comprehension
        missing_states= [state for state in all_states if state not in correct_states]
        
        # Save the list of missing states to a new CSV for study sessions
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("C:/new/100-Projects-of-Python/Day-25/States_to_learn.csv")
        
        break

    # Check the user's input against the list of state names
    for state in data.state:
        if answer_state == state:
            # Extract the row corresponding to the correct state
            ans_correct_row =  data[data["state"]==answer_state]
            if answer_state == ans_correct_row.state.values[0]:
                correct_states.append(answer_state)
                # Send the writing cursor to the state's map coordinates and write its name
                cursor.goto(ans_correct_row.x.values[0],ans_correct_row.y.values[0])
                cursor.write(arg=answer_state,font=("Arial", 8, "bold"))