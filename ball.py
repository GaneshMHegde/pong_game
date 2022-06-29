from  turtle import Turtle
import  random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.fast=0.25
        self.penup()
        self.goto((0,0))

    def serve(self):
        self.fast=0.25
        self.goto(0,0)
        direction = random.randint(0, 60)
        side=random.choice([1,-1])
        player=random.choice([0,180])
        direction*=side
        direction+=player
        self.setheading(direction)

    def bounce(self):
        self.forward(self.fast)
        if self.xcor()>=400:
            direction = self.heading() + 180
            self.setheading(direction)
            return False
        elif self.xcor()<-400:
            direction = self.heading() + 180
            self.setheading(direction)
            return False

        if self.ycor() >= 300:
            direction = self.heading() + 90
            self.setheading(direction)

        elif self.ycor() < -300:
            direction = self.heading() + -90
            self.setheading(direction)

    def het(self):
        direction=self.heading()+90
        self.setheading(direction)
        self.fast+=0.1

    def side(self):
        if self.xcor()>=400:
            return 'r'
        elif self.xcor()<-400:
            return 'l'


