import turtle
import random
import time

delay = 0.1  # Speed of the snake
sc = 0  # Score card
hs = 0  # High score, initially 0
bodies = [] 

# Creating Screen
s = turtle.Screen()  # Object created
s.title("Snake Game")
s.bgcolor("#2F4F4F")
s.setup(width=800, height=800)  # Increased resolution

# Creating a Head
head = turtle.Turtle()  # Object name turtle of class Turtle
head.speed(0)
head.shape("circle")  # Changed to circle for the head
head.color("#00FF00")  # Bright green color for the head
head.fillcolor("#006400")  # Dark green inner color for the head
head.penup()
head.goto(0, 0)  # Starting point of the snake
head.direction = "stop"

# Creating food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")  # Shape of the food
food.color("orange")  # Color of the food
food.fillcolor("red")  # Inner color of the food
food.penup()  # Lift the pen, no drawing
food.goto(random.randint(-390, 390), random.randint(-390, 390))  # Random initial position

# Creating Score Board
sb = turtle.Turtle()
sb.penup()  # Lift the pen, no drawing
sb.ht()
sb.goto(-350, 350)
sb.write("Score : 0  |  Highest Score : 0")  # Initial text

# Creating Functions for moving in all directions

def moveUp():
    if head.direction != "down":  # Check to avoid moving in opposite direction
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"  # Stop the snake

# Move the snake based on direction
def move():
    if head.direction == "up":
        y = head.ycor()  # Getting y-coordinate
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()  # Getting x-coordinate
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event Handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Main game loop
while True:  # Moving snake infinitely
    s.update()  # Update the screen

    # Checking collision of snake with the border
    if head.xcor() > 390:
        head.setx(-390)

    if head.xcor() < -390:
        head.setx(390)

    if head.ycor() > 390:
        head.sety(-390)

    if head.ycor() < -390:
        head.sety(390)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-390, 390)  # x-coordinate of food after collision
        y = random.randint(-390, 390)  # y-coordinate of food after collision
        food.goto(x, y)

        # Increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")  # Circle shape for the body
        body.color("yellow")  # Color of the body
        bodies.append(body)  # Append body in list

        sc += 10  # Increase the score
        delay -= 0.001  # Increase the speed of snake

        if sc > hs:
            hs = sc  # Update high score

        sb.clear()
        sb.write("Score : {}  |  Highest Score : {}".format(sc, hs))

    # Move Snake Body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision of snake with itself
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hiding bodies
            for body in bodies:
                body.ht()

            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score : {}  |  Highest Score : {}".format(sc, hs))

    time.sleep(delay)

s.mainloop()
