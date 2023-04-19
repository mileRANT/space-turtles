from turtle import Turtle
from bullet import Bullet

class Player(Turtle):
    def __init__(self):
        super().__init__()
        # player.shape("player.gif")
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.playerspeed = 15
        # define bullet state
        # ready - ready to fire
        # fire - bullet is firing
        self.bulletstate = "ready"
        self.bullet = Bullet()

    # Move the player left and right
    def move_left(self):
        x = self.xcor()
        x -= self.playerspeed
        if x < -280:
            x = -280
        self.setx(x)


    def move_right(self):
        x = self.xcor()
        x += self.playerspeed
        if x > 280:
            x = 280
        self.setx(x)

    def fire_bullet(self):
        if self.bulletstate == "ready":
            self.bulletstate = "fire"
            # print (self.bulletstate)
            # Move the bullet to the just above the player
            x = self.xcor()
            y = self.ycor() + 10
            self.bullet.setposition(x, y)
            self.bullet.showturtle()

    def ready_state(self):
        self.bulletstate = "ready"
