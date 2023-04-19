# importing turtle, math and random python modules
import turtle
import math
import random
from scoreboard import Scoreboard
from player import Player
from bullet import Bullet
from enemy import Enemy
from enemy_manager import EnemyManager
from ui import UI

# Set up the game window screen
window = turtle.Screen()
window.bgcolor("green")
window.title("Space Invaders - Turtles")
# window.bgpic("background.gif")

# Register the shape
# turtle.register_shape("invader.gif")
# turtle.register_shape("player.gif")

# scoreboard
scoreboard = Scoreboard(lives=3)
# player
player = Player()
# bullet = Bullet()
ui = UI()
#enemies
enemy_manager = EnemyManager()


# Create keyboard bindings
turtle.listen()
turtle.onkey(key='Left', fun=player.move_left)
turtle.onkey(key='Right', fun=player.move_right)
turtle.onkey(key='space', fun=player.fire_bullet)

# Main game loop
Game_Over = False
missed_enemies = 0
while True:

    enemy_manager.move_all_enemies()
    player.bullet.bulletFire(player)
    for enemy in enemy_manager.all_enemies:
        # Game logic for collisions
        # 1. Enemy x Bullet collision
        if enemy.isCollision_enemy_bullet(player.bullet):
            # Reset bullet
            player.bullet.resetBullet(player, collision=True)   #reset the bullet which will hide the bullet and change player bullet state
            # Reset the enemy
            enemy.enemyReset()
            #increase score
            scoreboard.increase_score()
        # 2. Enemy x Player collision
        if enemy.isCollision_enemy_player(player):
            Game_Over = True
        if enemy.ycor() < -285:  # and Game_Over == False:
            Game_Over = True
        if Game_Over == True:
            player.hideturtle()
            for e in enemy_manager.all_enemies:
                e.hideturtle()
                break

turtle.done