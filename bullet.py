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

    def check_readyState(self, player):
    # Check to see if the bullet has gone to the top
        print("check player state: " & player.bulletstate)
        if self.ycor() > 275:
            self.hideturtle()
            player.ready_state()
            # bulletstate = "ready"


    def bulletFire(self, player):
    # # Move the bullet
        if player.bulletstate == "fire":
            print("bulletfire moving")
            y = self.ycor()
            y += BULLETSPEED
            self.sety(y)
            self.check_readyState(player)

