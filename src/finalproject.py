import turtle
import random


window = turtle.Screen()
window.title("FRUIT NINJA")
window.bgcolor("brown")
window.bgpic("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/backround.gif")
window.setup(width=800, height=600)
window.tracer(0)

score = 0
lives = 3

window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/bomb.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/fruit.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/right_katana.gif")



user = turtle.Turtle()
user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
user.color("grey")
user.speed(0)
user.penup()
user.setposition(0, -250)
user.setheading(90)

userspeed = 15


def move_left():
    user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
    x = user.xcor()
    x -= userspeed
    if x < -380:
        x = -380
    user.setx(x)

def move_right():
    user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/right_katana.gif")
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
    bomb.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/bomb.gif")
    bomb.color("black")
    bomb.speed(0)
    bomb.penup()
    bomb.setposition(50, 300)
    bomb.speed = random.randint(3,5)
    bombs.append(bomb)

fruits = []

for _ in range(20):
    fruit = turtle.Turtle()
    fruit.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/fruit.gif")
    fruit.color("orange")
    fruit.speed(0)
    fruit.penup()
    fruit.setposition(-50, 300)
    fruit.speed = random.randint(2,4)
    fruits.append(fruit)

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.shape("circle")
scoreboard.color("white")
scoreboard.speed(0)
scoreboard.penup()
scoreboard.setposition(0, 260)
font = ("Arial", 25, "normal")
scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)

lose = turtle.Turtle()
lose.hideturtle()
lose.shape("circle")
lose.color("white")
lose.speed(0)
lose.penup()
lose.setposition(0, 50)
font = ("Arial", 30, "bold")

while lives > 0:
 
    window.update()

    for bomb in bombs:
        y = bomb.ycor()
        y -= bomb.speed
        bomb.sety(y)
        
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)
    
        if bomb.distance(user) < 35:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)
            score -= 500
            lives -= 1
            scoreboard.clear()
            scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)
    
    for fruit in fruits:
        y = fruit.ycor()
        y -= fruit.speed
        fruit.sety(y)
        
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)
    
        if fruit.distance(user) < 35:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)
            scoreboard.clear()
            score += 100
            scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)

while lives == 0:
    lose.write("GAME OVER. YOU BRING SHAME TO NINJAS.".format(score), align = "center", font = font)

window.mainloop()