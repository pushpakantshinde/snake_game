from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
# HISTORY_DATA = open("data.txt", mode="r+")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as history_data:
            self.highest_score = int(history_data.read())
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.update_scoreboard()
        self.score = 0
        with open("data.txt", mode="w") as history_data:
            history_data.write(f"{self.highest_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)
