from turtle import Turtle
BULLETSPEED = 30
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        # Creat the player's bullet
        self.color("white")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()


