from turtle import Screen
from  peddle import Right_player, Left_player
from  outline import Outline
from  ball import Ball
from score import Score


def end_the_game():
    return False

screen=Screen()
screen.screensize(canvwidth=800,canvheight=600,bg='black')
screen.title('pong')
screen.tracer(0)

outline=Outline()
outline.net()
score=Score()
ball=Ball()
ball.serve()
r_p=Right_player()
r_p.create_player()
l_p=Left_player()
l_p.create_player()

play=True
side=None

game_is_on=True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(r_p.move_up,'Up')
    screen.onkey(r_p.move_down,'Down')
    screen.onkey(l_p.move_up,'w')
    screen.onkey(l_p.move_down,'s')
    if play==False:
        ball.serve()
        score.score(side)
    play=ball.bounce()
    side=ball.side()


    if ball.xcor() > 340 and ball.distance(r_p.right_p[2]) < 55:
        ball.het()

    if ball.xcor() < -340 and ball.distance(l_p.left_p[2]) < 55:
        ball.het()

screen.exitonclick()

