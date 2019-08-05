# setting up
import turtle
options = []
turtle.screensize(2000,2000)

# creating the bars

# creating the character
character = turtle.Turtle()
character.hideturtle()

# choice turtle
###shapes import
choice = turtle.Turtle()
#choice.shape("good_morning.gif")
choice.hideturtle()
choice.penup()

# first choice
#choice.shape("wake_up")
choice.goto(turtle.xcor(),100)
choice.stamp()
#choice.shape("snooze")
choice.goto(turtle.xcor(),-100)
choice.stamp()

# choosing function
def choice():

def up():
    character.goto(character.xcor(),character.ycor()+100)
def down():
    character.goto(character.xcor(),character.ycor()-100)
def right():
    character.goto(character.xcor()+100,character.ycor())



turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(right,'Right')

turtle.listen()
turtle.mainloop()
