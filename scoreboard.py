from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.write(f"{self.l_score} :SCORE: {self.r_score}", align="center", font=("Courier", 25, "bold"))


    def increase_left(self):
        self.l_score +=1
        self.clear()
        self.write(f"{self.l_score} :SCORE: {self.r_score}", align="center", font=("Courier", 25, "bold"))

    def increase_right(self):
        self.r_score +=1
        self.clear()
        self.write(f"{self.l_score} :SCORE: {self.r_score}", align="center", font=("Courier", 25, "bold"))

    
    def end_game(self):
        self.goto(0, 0)
        if self.r_score > self.l_score:
            self.write("Game Over, Player 2 Wins", align="center", font=("Courier", 25, "bold"))
        else:
            self.write("Game Over, Player 1 Wins", align="center", font=("Courier", 25, "bold"))
