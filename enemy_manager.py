from turtle import Turtle
from enemy import Enemy
import random



class EnemyManager():
    def __init__(self):
        # Choose a number of enemies
        self.number_of_enemies = 10
        # Create an empty list of enemies
        self.all_enemies = []
        self.ENEMYSPEED = 5
        self.create_enemy()


    def create_enemy(self):
        # Add enemies to the list
        for i in range(self.number_of_enemies):
            # create the enemy
            self.all_enemies.append(Enemy())

        # for enemy in self.all_enemies:
            # enemy.color("Red")
            # enemy.shape("invader.gif")
            # enemy.penup()
            # enemy.speed(0)
            # x = random.randint(-200, 200)
            # y = random.randint(100, 250)
            # enemy.setposition(x, y)
    def move_all_enemies(self):
        for enemy in self.all_enemies:
            # move all enemies regular movement
            enemy.move(self.ENEMYSPEED)

            # Move the enemy back and down
            if (enemy.xcor() > 270) or (enemy.xcor() < -270):
                # Move all enemies down
                for e in self.all_enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                    if e.ycor() < -285: # and Game_Over == False:
                        e.hideturtle()
                        # missed_enemies += 1
                        # if missed_enemies == 5:
                        #     Game_Over = True
                        # x = random.randint(-200, 200)
                        # y = random.randint(100, 250)
                        # e.setposition(x, y)
                        # e.showturtle()
                # Change enemy direction
                self.ENEMYSPEED *= -1

            # if enemy.xcor() < -270:
            #     # Move all enemies down
            #     for e in enemies:
            #         y = e.ycor()
            #         y -= 40
            #         e.sety(y)
            #         if e.ycor() < -285 and Game_Over == False:
            #             e.hideturtle()
            #             missed_enemies += 1
            #             if missed_enemies == 5:
            #                 Game_Over = True
            #             x = random.randint(-200, 200)
            #             y = random.randint(100, 250)
            #             e.setposition(x, y)
            #             e.showturtle()
            #     # Change enemy direction
            #     self.ENEMYSPEED *= -1