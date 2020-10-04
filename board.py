'''
    CS 5001
    SPRING 2020
    PROJECT
    YIQIAN DENG

    board.py
'''
import turtle
from functions import *

class Board:
    ''' Class: Board
        Attributes: bg_color(string), dimension(tuple), height(int), wide(int),
                    adjust_height(int), adjust_wide(int),
                    screen(turtle object)
        Methods: constructor, draw_board
    '''

    def __init__(self, bg_color = B, dimension = D):
        '''
        constuctor -- create an Board object
        Parameters: dimension(tuple), bg_color(string)
        '''
        self.dimension = dimension
        self.bg_color = bg_color


    def draw_board(self):
        '''
            Method -- draw the board's background
            Parameter: current object
        '''
        # screen setup
        self.screen = turtle.Screen()

        # ask input dimension and opponent type, default (6, 7)
        while True:
            height = self.screen.textinput\
                     ('Rows', "Enter number of rows or press enter set 6 as default.")
            wide = self.screen.textinput\
                   ('Columns', "Enter number of column or press enter set 7 as default")
            if height == '' and wide == '':
                break
            else:
                try:
                    height = int(height)
                    wide = int(wide)
                    break
                except ValueError:
                    print("Invalid input, please enter integers")
        if height != '' and wide != '':
            self.dimension = (height, wide)
    
        # calculate wide and height of the board
        self.height, self.wide = self.dimension
        self.adjust_height = self.height * UNIT_1 + self.height * UNIT_2
        self.adjust_wide = self.wide * UNIT_1 + self.wide * UNIT_2
        
        # draw board's background
        bg = turtle.Turtle()
        bg.hideturtle()
        bg.up()
        bg.goto(INIT_X, INIT_Y)

        bg.color(self.bg_color)
        bg.begin_fill()

        bg.forward(self.adjust_wide)
        bg.right(ANGLE)
        bg.forward(self.adjust_height)
        bg.right(ANGLE)
        bg.forward(self.adjust_wide)
        bg.right(ANGLE)
        bg.forward(self.adjust_height)

        bg.end_fill()



            
