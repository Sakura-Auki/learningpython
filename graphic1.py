import turtle
import random 

rosi=turtle.Turtle()
rosi.shape("turtle")
rosi.pensize(5)
def haus():
    rosi.pencolor(random.choice(("red","pink","green","blue","yellow","purple","black")))
    rosi.fillcolor(random.choice(("red","pink","green","blue","yellow","purple","black")))
    rosi.pensize(random.randint(1,10))
    rosi.begin_fill()
    rosi.forward(150)
    rosi.left(90)
    rosi.forward(100)
    rosi.left(45)
    rosi.forward(75)
    rosi.left(75)
    rosi.forward(100)
    rosi.left(60)
    rosi.forward(105)
    rosi.left(90)
    rosi.end_fill()

for a in range (100):

    rosi.penup()
    x=random.randint(-300,200)
    y=random.randint(-200,300)
    rosi.goto(x,y)
    rosi.pendown()
    rosi.setheading(0)
    haus()
    
    

#haus()
turtle.exitonclick()
