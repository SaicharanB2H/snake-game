#Now i am going to create a small snake game with the help of turtle module
#first we need to import the required modules 
import turtle,time,random

delay = 0.1
#default score 
score = 0
high_score = 0

#setting up the screen 
window = turtle.Screen()
window.title("Snake Game by Charan")
window.bgcolor('black')
window.setup(height=600,width=600)
window.tracer(0)

#creating the snake head 
head = turtle.Turtle()
head.color('green')
head.speed(0)
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#snake food 
food = turtle.Turtle()
food.color('red')
food.speed(0)
food.shape('circle')
food.penup()
food.goto(0,100)

#creating a snake body
segments  = []

#creating scores for the game
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0  Highscore : 0", align="center", font=('Courier',24,'normal'))


#Functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

#keyboard binding 
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')



#main game loop
while True:
    window.update()
    #making the collisions with the border
    if head.xcor() <-290 or head.xcor()>290  or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        #Hiding the segments from the screen
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        score = 0
        pen.clear()
        pen.write("Score : {}  High Score : {} ".format(score,high_score),align='center',font=('Courier',24,'normal'))

    
    if head.distance(food) < 20 :
        #moving the food to random position on the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #adding new body or segment to the snake 
        #when it takes the food
        new_segment  = turtle.Turtle()
        new_segment.shape('square')
        new_segment.speed(0)
        new_segment.color('red')
        new_segment.penup()
        segments.append(new_segment)

        #adding the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {}  High Score : {} ".format(score,high_score),align='center',font=('Courier',24,'normal'))

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment to 0 where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move()

    #checking self body collisions 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
        #Hiding the segments from the screen
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score = 0
        pen.clear()
        pen.write("Score : {}  High Score : {} ".format(score,high_score),align='center',font=('Courier',24,'normal'))



    time.sleep(delay)
    
    



window.mainloop()