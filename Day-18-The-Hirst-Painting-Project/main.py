from turtle import  Screen
import turtle as t
import random
tiny = t.Turtle()


tiny.shape("turtle")
tiny.color("blue")


directions = [0,90,180,270]
tiny.speed("fastest")

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

head = 0
for _ in range(0,255):
    tiny.color(random_color())
    tiny.circle(radius=100)
    tiny.setheading(head)
    head+=5






my_screen = Screen()
my_screen.exitonclick()

