import turtle



window = turtle.Screen()
window.title("FRUIT NINJA")
window.bgcolor("brown")
window.setup(width=800, height=600)



user = turtle.Turtle()
user.shape("circle")
user.color("grey")
user.speed(0)
user.penup()
user.setposition(0, -250)
user.setheading(90)

userspeed = 8


def move_left():
    x = user.xcor()
    x -= userspeed
    if x < -380:
        x = -380
    user.setx(x)

def move_right():
    x = user.xcor()
    x += userspeed
    if x > 380:
        x = 380
    user.setx(x)

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

bomb = turtle.Turtle()
bomb.shape("circle")
bomb.color("black")
bomb.speed(0)
bomb.penup()
bomb.setposition(0, 300)

while True:
    y = bomb.ycor()
    y -= 3
    bomb.sety(y)
    
    if y < -300:
        bomb.goto(0,300)


window.mainloop()