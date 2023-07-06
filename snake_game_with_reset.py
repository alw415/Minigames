# Import the Turtle Graphics and random modules
import turtle
import random

#Define program constants
WIDTH = 1000
HEIGHT = 1000
DELAY = 100 #Milliseconds
FOOD_SIZE = 10 #constant size of food in pixels

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0),
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def snake_loop():
    stamper.clearstamps() #Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
    or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        #Add new head to snake body.
        snake.append(new_head)

        #Check for food collision
        if not food_collision():
            snake.pop(0) #Keep the snake the same length unless fed.
    
        #Draw snake for the first time, also grows the snake by one segment
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
    
        #Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        #Repeat action
        turtle.ontimer(snake_loop, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

#Generates random position for food
def get_random_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE) #x-coordinate between lower and upper bound
    y = random.randint(-HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE) #y-coordinate
    return (x,y)

#Calculating distance between two points
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1)**2 + (x2 - x1)**2)**0.5 #Pythagora's thoerem
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]] #Create snake as a list of coordinate pairs.
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    snake_loop()

#Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) #Sets dimensions
screen.title("Snake Gameeee")
screen.bgcolor("cyan")
screen.tracer(0) #Turn off automatic animation.

#Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

#Create your turtle
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.penup()

#Food objects
food = turtle.Turtle()
food.shape("circle")
food.color("purple")
food.shapesize(FOOD_SIZE / 20) #For pixel control
food.penup()

#Set animation in motion
reset()

#Finish nicely
turtle.done()