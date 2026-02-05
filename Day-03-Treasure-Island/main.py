print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = (input("There are two paths , which you wanna go? (left or right): ")).lower()
if choice_1 == "left":
    print("You have came across a river.")
    choice_2 = (input("Do you want to wait or swim the river? (swim or wait): ")).lower()
    if choice_2=="wait":
        print("\n You were rescued by a boat!")
        print("\n After crossing the river, you came across three doors.")
        choice_3=(input("which door are you going to go through?(Red, Blue or Yellow): ")).lower()
        if choice_3=="yellow":
            print("\n Hurray , You found the treasure. \nYou Won the game !!!!")
        elif choice_3=="red":
            print("\n You got burned by fire. \nGame Over!!")
        elif choice_3 == "blue":
            print("\n You got eaten by beasts. \nGame Over!!")
    else:
        print("\n You were killed by crocodiles. \nGame Over !!!")
else :
    print("\n You fall into a pit. \nGame Over !!!")