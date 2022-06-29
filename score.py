from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.l_player_score=0
        self.r_player_score = 0
        self.hideturtle()
        self.penup()
        self.color('green')
        self.score(None)

    def score(self,side):
        if side=='r':
            self.l_player_score+=1
        elif side=='l':
            self.r_player_score+=1
        else:
            self.l_player_score = 0
            self.r_player_score = 0

        self.clear()
        self.goto(0, 300)
        self.write('Score:', False, 'center', ("Arial", 15, "normal"))
        self.goto(-25, 250)
        self.write(self.l_player_score, False, 'center', ("Arial", 20, "normal"))
        self.goto(25, 250)
        self.write(self.r_player_score, False, 'center', ("Arial", 20, "normal"))

