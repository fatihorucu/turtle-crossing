from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("blank")
        self.penup()
        self.setposition(-200, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.reset()
        self.penup()
        self.setposition(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game over", align="center", font=FONT)
