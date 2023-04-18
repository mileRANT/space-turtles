from turtle import Turtle
import random
import math

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color("RED")
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.setposition(x, y)

    # For collision between enemy and bullet
    def isCollision_enemy_bullet(self, other):
        distance = math.sqrt(
            math.pow(self.xcor() - other.xcor(), 2) + math.pow(self.ycor() - other.ycor(), 2)
        )
        if distance < 25:
            return True
        else:
            return False

    # For collision between enemy and player
    def isCollision_enemy_player(self, other):
        distance = math.sqrt(
            math.pow(self.xcor() - other.xcor(), 2) + math.pow(self.ycor() - other.ycor(), 2)
        )
        if distance < 30:
            return True
        else:
            return False

    def move(self, enemySpeed):
        # Move the enemy
        x = self.xcor()
        x += enemySpeed
        self.setx(x)

