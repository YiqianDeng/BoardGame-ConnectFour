'''
    CS 5001
    SPRING 2020
    PROJECT
    YIQIAN DENG

    driver.py
'''
from game import Game
from functions import *

def main():
    # create a game object, pass scorefile as parameter
    game = Game(SCOREFILE)

    # call play method of game to start it
    game.play()

main()
