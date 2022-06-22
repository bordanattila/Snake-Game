from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as prev_high_score:
            self.high_score = int(prev_high_score.read())
        self.hideturtle()
        self.goto(0, 270)
        self.color("yellow")
        self.display_score()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            prev_score = open("data.txt", mode="w")
            prev_score.write(f"{self.high_score}")
            prev_score.close()
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", False, align=ALIGNMENT, font=FONT)