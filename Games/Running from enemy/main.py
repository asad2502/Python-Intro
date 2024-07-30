import turtle
from myturtle import GoodTurtle, EnemyTurtle

g = GoodTurtle()
g.control_turtle()

e = EnemyTurtle()

while(True):
    g.forward(1)


turtle.mainloop()