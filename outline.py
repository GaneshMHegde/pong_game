from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color('yellow')
        self.goto(395,290)
        self.setheading(270)
        self.pendown()
        self.forward(590)
        self.setheading(180)
        self.forward(790)
        self.setheading(90)
        self.forward(590)
        self.setheading(0)
        self.forward(790)
        self.penup()

    def net(self):
        self.goto(0,300)
        self.setheading(270)
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
