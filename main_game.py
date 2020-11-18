from turtle import *                #this libraray will help us to build our snake its food and to move our snake
import random                       #this library is used to generate random numbers for random placements of food
from freegames import square,vector #this library is used to apply basic functions i.e square and vector for building game block and defing the particular vector directions


#----------------------game window-------------------------


setup(520,520,470,0)                #defing the setup co ordinate(size)
hideturtle()
tracer(False)

#------------------CREATING SNAKES FOOD--------------------

food = vector(0,0)
snake = [ vector(10,0)]             #snake is a list point victors
aim = vector(0,-10)


#-------------------THE MOVEMENT FUNCTION------------------
def change(x,y):                    #function creates aim based on the direction keys player will press
    aim.x = x
    aim.y = y

def inside(head):                   #to check weather the snake is inside of block or not
    return -200 < head.x < 190 and -200 <head.y<190

def move():
    head = snake[-1].copy()         #this creates the snakes head
    head.move(aim)                  #moves the head towards aim

    if head in snake or not inside(head):    #this creates red colour box indicating end of game
        square(head.x, head.y , 9 , 'red')
        update()
        return
    
    snake.append(head)

    if head == food:                #increases the snake length for food it eats everytime
        print('Snake : ', len(snake))
        food.x = random.randrange(-15,15)*10  #random placement of food
        food.y = random.randrange(-15,15)*10
    else:
        snake.pop(0)
    
    clear()

    for body in snake:
        square(body.x, body.y,9,'black')      #creates the snake body
    
    square(food.x, food.y, 9 ,'green')
    update()
    ontimer(move,100)



listen()                            #this is a turtle function that will listen to the keys pressed by user
onkey(lambda : change(10,0),'Right')#onclick function for right click
onkey(lambda : change(-10,0),'Left')#onclick function for left click
onkey(lambda : change(0,10),'Up')   #onclick function for up click
onkey(lambda : change(0,-10),'Down')#onclick function for down click
move()
done()