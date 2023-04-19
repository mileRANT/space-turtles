from turtle import Turtle

FONT = ("Courier", 36, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR = "white"

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.header()


    def border(self):
        # Draw border
        self.color(COLOR)
        self.setposition(-300, -300)
        self.pendown()
        self.pensize(3)
        for side in range(4):
            self.fd(600)
            self.lt(90)
        self.hideturtle()
        self.penup()

    def header(self):
        self.clear()
        self.border()
        # self.goto(x=0, y=-150)
        self.goto(x=0, y=335)
        self.write('Turtle Invader', align=ALIGNMENT, font=FONT)
        # self.goto(x=0, y=-150)
        # # self.goto(x=0, y=-180)
        # self.write('Press Space PAUSE/RESUME Game',
        #            align=ALIGNMENT, font=('Calibri', 14, 'normal'))

    def gameOver(self):
        self.goto(x=0, y=-150)
        # self.goto(x=0, y=-180)
        self.write('GAME OVER',
                   align=ALIGNMENT, font=('Calibri', 14, 'normal'))