from turtle import Turtle

FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open(file="highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score : {self.score} High Score : {self.highscore}", False, align='center', font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file="\\Users\\USER\\Desktop\\highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
