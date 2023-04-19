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
        print("bullet initialized")

    def resetBullet(self, player, collision=False):
    # Check to see if the bullet has gone to the top

        # optional keyword argument so we can use this as a reset bullet state
        if self.ycor() > 275 or (collision==True):
            self.hideturtle()
            self.sety(player.ycor() - 50)
            player.ready_state()
            # bulletstate = "ready"


    def bulletFire(self, player):
    # # Move the bullet
        if player.bulletstate == "fire":
            # print("bulletfire moving")
            y = self.ycor()
            y += BULLETSPEED
            self.sety(y)
            self.resetBullet(player)

