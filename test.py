'''
    CS 5001
    SPRING 2020
    Project
    Yiqian Deng

    test.py


there is a turtle prompt out when running this test.py file
Please don't close the turtle directly, just press 2 enter to skip these 2
prompt input.
Please please wait until the picture draw done to close the turtle!
I did few graph test on this prompt turtle. Thanks!
'''
import unittest
import os

from functions import *
from game import Game
from board import Board
from player import Player


# test class
class PlayerTest(unittest.TestCase):
    def test__init(self):
        p = Player("p1", 'Navy', 5, 'computer')
        self.assertEqual(p.name, "p1")
        self.assertEqual(p.color, "Navy")
        self.assertEqual(p.in_data, 5)
        self.assertEqual(p.identity, 'computer')
        


class BoardTest(unittest.TestCase):
    def test__init(self):
        b = Board(O, (3, 4))
        self.assertEqual(b.bg_color, 'Orange')
        self.assertEqual(b.dimension, (3, 4))


    # there is a turtle prompt out when running this test_draw_board function
    # just press 2 enter to skip these 2 prompt input
    # don't close the turtle directly, please wait until the picture draw done
    def test_draw_board(self):
        b = Board(O)
        b.draw_board()
        self.assertEqual(b.dimension, (6, 7))
        self.assertEqual(b.height, 6)
        self.assertEqual(b.wide, 7)
        self.assertEqual(b.adjust_height, 252)
        self.assertEqual(b.adjust_wide, 294)



class GameTest(unittest.TestCase):
    def test__init(self):
        g = Game(SCOREFILE)
        self.assertEqual(g.scorefile, SCOREFILE)
        self.assertEqual(g.ply_1.name, 'Red')
        self.assertEqual(g.ply_1.color, R)
        self.assertEqual(g.ply_1.in_data, 1)
        self.assertEqual(g.ply_2.name, 'Yellow')
        self.assertEqual(g.ply_2.color, Y)
        self.assertEqual(g.ply_2.in_data, 2)
        self.assertEqual(g.round, 0)
        
        # test all below attribute equal to None 
        self.assertEqual(g.column, None)
        self.assertEqual(g.row, None)
        self.assertEqual(g.winner, None)
        self.assertEqual(g.first, None)
        self.assertEqual(g.last, None)
        self.assertEqual(g.curr_player, None)
        self.assertEqual(g.board, None)
        self.assertEqual(g.signal_light, None)
        self.assertEqual(g.signal_text, None)
        self.assertEqual(g.info_box, None)
        self.assertEqual(g.piece, None)
        self.assertEqual(g.data, None)
        self.assertEqual(g.score, None)
        self.assertEqual(g.y_remove, None)
        self.assertEqual(g.y_insert, None)
        self.assertEqual(g.unit_x, None)


    def test_draw_sign(self):
        g = Game(SCOREFILE)
        p = Player("p1", 'Navy', 5, 'computer')
        # test after draw_sign function run,
        # following 3 objects not equal None
        g.draw_sign(p)
        self.assertNotEqual(g.signal_light, None)
        self.assertNotEqual(g.signal_text, None)
        self.assertNotEqual(g.info_box, None)

    
    def test_score_init(self):
        g = Game(SCOREFILE)
        g.score_init()
        self.assertEqual(g.score, [['Red', 0],['Yellow', 0]])
        


# test function
def who_turn_test():
    results = []
    for i in range(10):
         results.append(who_turn())
    is_pass = True
    for i in results:
        if i == True or i == False:
            return True
        else:
            return False




def main():
    
    if who_turn_test() == True:
        print('who_turn() ... pass')
    else:
        print('who_turn() ... test fail')

    unittest.main(verbosity = 3)

    
    
main()
