from turtle import Turtle


class Right_player:
    def __init__(self):
        self.right_p = []
        self.position=[(350,0), (350,-10), (350,-20), (350,-30), (350,-40), (350,-50)]
    def create_player(self):
        for i in range(6):
            rightp = Turtle()
            rightp.resizemode('user')
            rightp.shapesize(stretch_wid=0.5,stretch_len=0.5,outline=0.5)
            rightp.speed(0)
            rightp.penup()
            rightp.shape('square')
            rightp.color('blue')
            rightp.setheading(90)
            rightp.goto(self.position[i])
            self.right_p.append(rightp)
        self.move_up()
        self.move_up()

    def move_up(self):
        if self.right_p[0].ycor() <= 265:
            for segment in range(6):
                self.right_p[segment].forward(40)

    def move_down(self):
        if self.right_p[0].ycor() >= -220:
            for segment in range(6):
                self.right_p[segment].backward(40)



class Left_player:
    def __init__(self):
        self.left_p = []
        self.position = [(-350, 0), (-350, -10), (-350, -20), (-350, -30), (-350, -40), (-350,-50)]

    def create_player(self):
        for i in range(6):
            leftp = Turtle()
            leftp.resizemode('user')
            leftp.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.5)
            leftp.speed(0)
            leftp.penup()
            leftp.shape('square')
            leftp.color('red')
            leftp.setheading(90)
            leftp.goto(self.position[i])
            self.left_p.append(leftp)
        self.move_up()
        self.move_up()

    def move_up(self):
        if self.left_p[0].ycor()<=265:
            for segment in range(6):
                self.left_p[segment].forward(40)

    def move_down(self):
        if self.left_p[0].ycor() >= -220:
            for segment in range(6):
                self.left_p[segment].backward(40)
