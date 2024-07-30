import turtle

class Asad_s_Turtle(turtle.Turtle):
    def __init__(self, shape,color,size):
        super().__init__(shape)
        self.color(color)
        self.shapesize(size,size)
        self.penup()


import random
size = 1
at = Asad_s_Turtle('square', 'green', size)
ua = Asad_s_Turtle('turtle','blue',size)
at.goto(-400,-200)
ua.goto(-400,200)



while(True):
    at.forward(random.randint(1,10))
    ua.forward(random.randint(1,10))

    if at.xcor() > 400:
        turtle.write('Asad won')
        at.goto(-400,at.ycor())
    if ua.xcor() > 400:
        turtle.write('Umer won')
        ua.goto(-400,ua.ycor())

    
    # somwhole jab eyeh end per pohanch jaen stop


turtle.mainloop()