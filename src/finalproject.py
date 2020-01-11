import turtle
import random


window = turtle.Screen()
window.title("FRUIT NINJA")
window.bgcolor("brown")
window.setup(width=800, height=600)
window.tracer(0)


user = turtle.Turtle()
user.shape("circle")
user.color("grey")
user.speed(0)
user.penup()
user.setposition(0, -250)
user.setheading(90)

userspeed = 15


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

bombs = []

for _ in range(15):
    bomb = turtle.Turtle()
    bomb.shape("circle")
    bomb.color("black")
    bomb.speed(0)
    bomb.penup()
    bomb.setposition(50, 300)
    bomb.speed = random.randint(3,5)
    bombs.append(bomb)

fruits = []

for _ in range(20):
    fruit = turtle.Turtle()
    fruit.shape("circle")
    fruit.color("orange")
    fruit.speed(0)
    fruit.penup()
    fruit.setposition(-50, 300)
    fruit.speed = random.randint(2,4)
    fruits.append(fruit)

while True:
 
    window.update()

    for bomb in bombs:
        y = bomb.ycor()
        y -= bomb.speed
        bomb.sety(y)
        
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)
    
        if bomb.distance(user) < 20:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)
    
    for fruit in fruits:
        y = fruit.ycor()
        y -= fruit.speed
        fruit.sety(y)
        
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)
    
        if fruit.distance(user) < 20:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)


window.mainloop()