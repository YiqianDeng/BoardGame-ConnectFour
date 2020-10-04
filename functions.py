'''
    CS 5001
    SPRING 2020
    PROJECT
    YIQIAN DENG

    functions.py
'''
import turtle
import random

# CONSTANT
UNIT_1 = 35
UNIT_2 = 7
UNIT_3 = 20
W = 'White'
R = 'Red'
Y = 'Yellow'
B = 'Blue'
BB = 'Black'
O = 'Orange'
D = (6, 7)
INIT_X = -200
INIT_Y = 150
TEXT_X = -330
TEXT_Y = 60
DISPLAY_X = -300
DISPLAY_Y = 120
END_X = -150
END_Y = 0
SCORE_Y = 250
INFO_Y = 200
ANGLE = 90
CIRCLE = 'circle'
TRIANGLE = 'triangle'
CLASSIC = 'classic'
SIZE = 1.5
SCOREFILE = "score.txt"


# FUNCTIONS
def create_turtle(x, y, shape):
    ''' Function: create_turtle
        Parameters: x(int), y(int), shape(a string)
        Return: an turtle object
        Does: create each turtle object in board
    '''
    c = turtle.Turtle()
    c.up()
    c.hideturtle()
    c.setposition(x, y)

    c.shape(shape)
    if shape == CIRCLE:
        c.shapesize(SIZE, SIZE)
        c.color(W)    
    elif shape == TRIANGLE:
        c.right(ANGLE)
        c.color(BB)
    elif shape == CLASSIC:
        c.shapesize(SIZE, SIZE)
        c.left(ANGLE)
        c.color(O)
    c.showturtle()

    return c
    
    
def who_turn():
    ''' Function: who_turn
        Parameter: none
        Return: boolean value
        Does: randomly return True or False to decide which player go first
    '''
    if random.randint(0, 1) == 0:
        return True
    else:
        return False







    
