from turtle import Turtle
from bullet import Bullet

PLAYERSPEED = 15
class Player(Turtle):
    def __init__(self):
        super().__init__()
        # player.shape("player.gif")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        # define bullet state
        # ready - ready to fire
        # fire - bullet is firing
        self.bulletstate = "ready"

    # Move the player left and right
    def move_left(self):
        x = self.xcor()
        x -= PLAYERSPEED
        if x < -280:
            x = -280
        self.setx(x)


    def move_right(self):
        x = self.xcor()
        x += PLAYERSPEED
        if x > 280:
            x = 280
        self.setx(x)

    def fire_bullet(self):
        if self.bulletstate == "ready":
            self.bulletstate = "fire"
            # Move the bullet to the just above the player
            x = self.xcor()
            y = self.ycor() + 10
            Bullet.setposition(x, y)
            Bullet.showturtle()