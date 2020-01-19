import turtle
import random

#set up window
window = turtle.Screen()
window.title("FRUIT NINJA")
window.bgcolor("brown")
window.bgpic("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/backround.gif")
window.setup(width=800, height=600)
window.tracer(0)

#set score and lives 
score = 0
lives = 3

#register bomb, strawberry, left facing katana, and right facing katana images
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/bomb.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/fruit.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
window.register_shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/right_katana.gif")


#create the user
user = turtle.Turtle()
user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
user.color("grey")
user.speed(0)
user.penup()
user.setposition(0, -250)
user.setheading(90)

#set user speed
userspeed = 15

#create a list of bombs
bombs = []

#add 15 bombs total
for _ in range(15):
    #create the bomb
    bomb = turtle.Turtle() 
    bomb.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/bomb.gif")
    bomb.color("black")
    bomb.speed(0)
    bomb.penup()
    bomb.setposition(50, 300)
    bomb.speed = random.randint(3,5)
    bombs.append(bomb)

#create a list of fruits
fruits = []

#add 20 fruits total
for _ in range(20):
    #create the fruit
    fruit = turtle.Turtle()
    fruit.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/fruit.gif")
    fruit.color("orange")
    fruit.speed(0)
    fruit.penup()
    fruit.setposition(-50, 300)
    fruit.speed = random.randint(2,4)
    fruits.append(fruit)

#create the scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.shape("circle")
scoreboard.color("white")
scoreboard.speed(0)
scoreboard.penup()
scoreboard.setposition(0, 260)
font = ("Arial", 25, "normal")
scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)

#create the game over message
lose = turtle.Turtle()
lose.hideturtle()
lose.shape("circle")
lose.color("white")
lose.speed(0)
lose.penup()
lose.setposition(0, 50)
font = ("Arial", 30, "bold")

#create main game loop
while lives > 0:
    
    #update the screen
    window.update()

    #move the user leftwards 
    def move_left():
        user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/left_katana.gif")
        x = user.xcor()
        x -= userspeed
        #create boundary checking
        if x < -380:
            x = -380
        user.setx(x)

    #move the user rightwards
    def move_right():
        user.shape("/Users/kevincavicchia/Documents/final-project-fruit-ninja/src/right_katana.gif")
        x = user.xcor()
        x += userspeed
        #create boundary checking
        if x > 380:
            x = 380
        user.setx(x)

    #create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    
    for bomb in bombs:
        #move the bombs
        y = bomb.ycor()
        y -= bomb.speed
        bomb.sety(y)
        
        #check if bombs are off screen and replace
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)

        #check for collision with user
        if bomb.distance(user) < 35:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bomb.goto(x,y)
            #decrease score and lives and print
            score -= 500
            lives -= 1
            scoreboard.clear()
            scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)
    
    for fruit in fruits:
        #move the fruits
        y = fruit.ycor()
        y -= fruit.speed
        fruit.sety(y)
        
        #check if fruits are off the screen and replace
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)
        
        #check for collsion with user
        if fruit.distance(user) < 35:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            fruit.goto(x,y)
            #increase score and print
            scoreboard.clear()
            score += 100
            scoreboard.write("Score: {}  Lives: {}".format(score,lives), align = "center", font = font)

#print the game over message when user loses
while lives == 0:
    lose.write("GAME OVER. YOU BRING SHAME TO NINJAS.".format(score), align = "center", font = font)

window.mainloop()