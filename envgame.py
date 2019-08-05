# setting up
import turtle
turtle.tracer(1,0)
options = []
healths = []
energys = []
environments = []
impact = []
turtle.screensize(2000,2000)

# creating the bars
health = turtle.Turtle()
health.speed(100)
health.hideturtle()
health.penup()
health.goto(-100, 350)
health.write("health: 75")
energy = turtle.Turtle()
energy.speed(100)
energy.hideturtle()
energy.penup()
energy.goto(0, 350)
energy.write("energy: 75")
environment = turtle.Turtle()
environment.speed(100)
environment.hideturtle()
environment.penup()
environment.goto(100, 350)
environment.write("environment: 75")

# creating the character
character = turtle.Turtle()
character.hideturtle()

# choice turtle
#turtle.register_shape("goodmorning.gif") 
choice = turtle.Turtle()
#choice.shape("good_morning.gif")
choice.hideturtle()
choice.penup()

# first choice
choice.stamp()
#choice.shape("goodmorning.png")
choice.stamp()
choice.goto(turtle.xcor(),100)
#choice.shape("wakeup")
choice.stamp()
options.append(choice.pos())
#choice.shape("snooze")
choice.goto(turtle.xcor(),-100)
choice.stamp()
options.append(choice.pos())

# choosing function
def choose():
    if character.ycor() >= 300:
            health.clear()
            energy.clear()
            environment.clear()
            health.goto(health.xcor(), character.ycor()+50)
            energy.goto(energy.xcor(), character.ycor()+50)
            environment.goto(environment.xcor(), character.ycor()+50)
            health.write("health: 75")
            energy.write("energy: 75")
            environment.write("environment: 75")
    if character.pos() in options[-2:]:
        if len(options) == 2: #get up
            #choice.shape("getup")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 3: #brush teeth
            #choice.shape("brushteeth")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 4: #shower for..
            #choice.shape("shower thing")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 5: #long / short
            #choice.shape("longshower")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("shortshower")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 7: #get dressed
            #choice.shape("clothes")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 8: #eat breakfast
            #choice.shape("breakfast")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 9: #ac
            #choice.shape("ac")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 10: #off or on
            #choice.shape("ac on")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("ac off")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 12: #get outside
            #choice.shape("outside")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 13: #order coffee in:
            #choice.shape("coffee")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 14: #single use/ reuseable
            #choice.shape("single use")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("reuseable (expensive)")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 16: #walk out:
            #choice.shape("walk")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 13: #get to work by:
            #choice.shape("transportation")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 14: #car / bikes
            #choice.shape("car")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("bikes")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 13: #enter office:
            #choice.shape("office")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 13: #wow, donuts!:
            #choice.shape("donuts")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 14: #eat / not
            #choice.shape("eat")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("no")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 16: #work:
            #choice.shape("work")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 17: #eat lunch at:
            #choice.shape("lunch")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 18: #order in / restaurant
            #choice.shape("restaurant")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("order in")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 20: #back to office:
            #choice.shape("office")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 21: #work:
            #choice.shape("work")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())

    
def up():
    character.goto(character.xcor(),character.ycor()+100)
    choose()

def down(): 
    character.goto(character.xcor(),character.ycor()-100)
    choose()

def right():
    character.goto(character.xcor()+100,character.ycor())
    health.clear()
    energy.clear()
    environment.clear()
    health.forward(100)
    energy.forward(100)
    environment.forward(100)
    health.write("health: 75")
    energy.write("energy: 75")
    environment.write("environment: 75")
    choose()

def left():
    character.goto(character.xcor()-100,character.ycor())
    health.clear()
    energy.clear()
    environment.clear()
    health.backward(100)
    energy.backward(100)
    environment.backward(100)
    health.write("health: 75")
    energy.write("energy: 75")
    environment.write("environment: 75")
    choose()


#listening
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(right,'Right')
turtle.onkeypress(left, 'Left')
turtle.listen()

def finish():
    if len(healths)>=80:
        print('you are super healthy!')
    elif len(healths)>=50:
        print('your health is struggling!')
    elif len(healths)>=10:
        print("")
    else:
        print('you healh suckes!')
        print('you are dying!!!!')
    if len(environments)>=80:
        print('what a green environment that U live in!!!')
    elif len(environments)>=50:
        print('this environment is okay...')
    elif len(environments)>=10:
        print('what a dirty environment!!!')
    if len(energys)>=80:
        print('what a great energy!!')
    elif len(energys)>=50:
        print('your energy is okay...')
    elif len(energys)>=10:
        print('OH your dead!!!')
        print('your energy is tooo low!!')
        

turtle.listen()
turtle.mainloop()

