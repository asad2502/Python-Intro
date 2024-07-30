import turtle
import random




class EnemyTurtle(turtle.Turtle):
    def __init__(self,colors = ['red', 'green', 'blue', 'yellow', 'black']):
        super().__init__()
        self.colors = colors
        self.color (random.choice(self.colors))
        self.shape('turtle')
        self.penup()
        
    def catchy_behaviour(self):
        pass



class GoodTurtle(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color ('red')
        self.shape ('turtle')
        self.penup()


    def Up(self):
        self.setheading(90)
        self.forward(10)

    def Down(self):
        self.setheading(270)
        self.forward(10)

    def control_turtle(self):
        turtle.listen()
        turtle.onkey(self.Up,'Up')
        turtle.onkey(self.Down,'Down')
        turtle.onkey(self.Right,'Right')
        turtle.onkey(self.Left,'Left')

    def Right(self):
        self.setheading(0)
        self.forward(10)

    def Left(self):
        self.setheading(180)
        self.forward(10)