'''
    CS 5001
    SPRING 2020
    PROJECT
    YIQIAN DENG

    game.py
'''
from player import *
from board import *
from functions import *
import turtle
from time import sleep

class Game:
    ''' Class: Game
        Attributes: ply_1 (player object), ply_2 (player object), winner (player object),
                    first (player object), last (player object), curr_player (player object),
                    board (board object),
                    signal_light (turtle object), signal_text (turtle object),
                    info_box (turtle object), piece (nested list of turtle object),
                    data (nested list of integer), score (nested list), scorefile (string),
                    column (integer), row (integer), round (integer),
                    y_remove (float), y_insert (float), unit_x (int)
        Methods: constructor, draw_piece, draw_button, draw_sign, print_info, display_signal,
                place_piece, draw_score, end_game, ai_generate, click_button, check_result,
                score_init, update_score, play
    '''

    def __init__(self, scorefile):
        '''
            Constructor -- create a new game
            Parameters: self(current object), dimensions(tuple), is_human(bool)
        '''
        # create 2 player object
        self.ply_1 = Player('Red', R, 1)
        self.ply_2 = Player('Yellow', Y, 2)

        self.scorefile = scorefile
        self.round = 0

        # variable hold play's input row coordinate (integers)
        self.column = None
        self.row = None

        # hold objects of game
        self.winner = None
        self.first = None
        self.last = None
        self.curr_player = None
        self.board = None
        self.signal_light = None
        self.signal_text = None
        self.info_box = None

        # hold data of game (lists)
        self.piece = None
        self.data = None
        self.score = None

        # hold draw board and pieces values
        self.y_remove = None
        self.y_insert = None
        self.unit_x = None


    # methods for graph
    def draw_piece(self):
        '''
            Methods: draw piece holder on board
            Parameters: self(current object)
        '''
        # calculate the x, y coordinate of initial piece place
        init_x = INIT_X + (self.board.adjust_wide / self.board.wide / 2)
        init_y = INIT_Y - (self.board.adjust_height / self.board.height / 2)
        # calculate the distance between eache piece
        unit_x = self.board.adjust_wide / self.board.wide
        unit_y = self.board.adjust_height / self.board.height

        # init empty lists to hold each piece object and data use later
        self.pieces = []
        self.data = []

        # iterate each position and create piece holder
        for i in range(self.board.height):
            self.pieces.append([])
            self.data.append([])
            y = init_y - i * unit_y
            for j in range(self.board.wide):
                x = init_x + j * unit_x
                c = create_turtle(x, y, CIRCLE)
                self.pieces[i].append(c)
                self.data[i].append(0)


    def draw_button(self):
        '''
            Methods: draw each insert and remove button of every colomn
            Parameter: self(current object)
        '''
        # calculate the y-coordinate of remove and insert buttons
        self.y_remove = INIT_Y - UNIT_2 - self.board.height * \
                   (self.board.adjust_height / self.board.height)
        self.y_insert = INIT_Y + \
                        (self.board.adjust_height / self.board.height / 2)

        # calculate the first x-coordinate and
        # distance to next coordinate of remove and insert buttons
        init_x = INIT_X + (self.board.adjust_wide / self.board.wide / 2)
        self.unit_x = self.board.adjust_wide / self.board.wide

        # init a list as button holder
        buttons = [[],[]]
        # place each button in their position
        for i in range(2):
            for j in range(self.board.wide):
                if i == 1:
                    x = init_x + j * self.unit_x
                    t = create_turtle(x, self.y_remove, CLASSIC)
                    t.onclick(self.click_button)
                    buttons.append(t)
                elif i == 0:
                    x = init_x + j * self.unit_x
                    t = create_turtle(x, self.y_insert, TRIANGLE)
                    t.onclick(self.click_button)
                    buttons.append(t)


    def draw_sign(self, player):
        '''
            Methods --- create a turtle objects to indicate signal light and text
            Parameters: self(current object), player(player object)
        '''
        # initiate turtle objects: signal_light, signal_text, and info_box
        self.signal_light = turtle.Turtle()
        self.signal_text = turtle.Turtle()
        self.info_box = turtle.Turtle()

        # set initial signal_light
        self.signal_light.up()
        self.signal_light.hideturtle()
        self.signal_light.setposition(DISPLAY_X, DISPLAY_Y)
        self.signal_light.shape(CIRCLE)
        self.signal_light.shapesize(SIZE,SIZE)
        self.signal_light.color(player.color)
        self.signal_light.showturtle()

        # set initial signal_text
        self.signal_text.hideturtle()
        self.signal_text.up()
        self.signal_text.setposition(TEXT_X, TEXT_Y)
        self.signal_text.color(BB)
        self.signal_text.write("{}:({}) \n current turn".format(player.name, \
                        player.identity), font = ('Arial', 14, 'normal', 'bold'))

        # set initial Info box
        self.info_box.hideturtle()
        self.info_box.up()
        self.info_box.setposition(INIT_X, INFO_Y)
        self.info_box.color(R)


    def print_info(self, info):
        '''
            Method --- show information on screen
            Parameters: self(current object), info(string)
        '''
        # clear previous info
        self.info_box.clear()
        # write new info
        self.info_box.write(info, font = ('Arial', 18, 'normal', 'bold'))


    def display_signal(self, player):
        '''
            Methods --- display signal light on screen
            Parameters: self(current object), player(player object)
        '''
        # toggles signal_light to indicate who's next turn
        self.signal_light.color(player.color)
        self.signal_light.showturtle()
        self.signal_text.clear()
        self.signal_text.write("{}:({}) \n current turn".format(player.name, \
                            player.identity), font = ('Arial', 14, 'normal', 'bold'))


    def place_piece(self, row, col, color, data_idx):
        '''
            Method --- place each piece on board.
            Parameters: row and col are integers which indicate the position
                        of piece will place. color is a string, and data_idx
                        is an integer.
        '''
        self.pieces[row][col].color(color)
        self.data[row][col] = data_idx
        

    def draw_score(self):
        '''
            Method --- display scores on screen
            Parameter: current object
        '''
        # convert current score into string
        text = ''
        for i in range(len(self.score)):
            for j in self.score[i]:
                text += str(j) + ' '
            text += '   '

        # display score on screen        
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        pen.setposition(END_X, SCORE_Y)
        pen.color(B)
        pen.write(text, font = ('Arial', 18, 'normal', 'bold'))


    def draw_end_page(self):
        '''
            Method --- when game done, erase all draws, write the winner
                        on screen, and update score
            Parameter: self(current object)
        '''
        # wait 1 second to show result
        sleep(1)
        
        # cleaar screen
        self.board.screen.clear()
    
        # set background to black
        self.board.screen.bgcolor(BB)

        # write game result on screen
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        pen.color(W)
        pen.setposition(END_X, END_Y)
        
        if self.winner == None:
            text = "No Winner!"
        else:
            text = self.winner.name + ' win!'
        pen.write(text, font = ('Arial', 50, 'normal', 'bold'))
        

    def end_game(self):
        '''
            Method --- when game done, update score
            Parameter: self(current object)
        '''

        # update score
        self.update_score()

        print("Done")



    




    # methods without graph
    def ai_generate(self, data, player, strategy = 'random'):
        '''
            Method --- generate the position where the computer's next pliece placed.
            Parameter: self(current object), data(nested list), player(player object),
                        strategy(string)
            Return: x, y coordinate(int)
        '''
        # this stretegy always place piece in most left column
        if strategy == 'basic':
            for y in range(self.board.wide):
                if data[0][y] != 0:
                    self.print_info("This column is full. Computer will pick another")
                else:
                # locate the row
                    for x in range(self.board.height - 1, -1, -1):
                        if data[x][y] == 0:
                            return x, y

        # this stretegy random pick a empty position to place
        if strategy == 'random':
            y = random.randint(0, self.board.wide-1)
            while self.data[0][y] != 0:
                y = random.randint(0, self.board.wide-1)
            for x in range(self.board.height - 1, -1, -1):
                if data[x][y] == 0:
                    return x, y
                

    def click_button(self, x, y):
        '''
            Methods --- The main logic of how game play, deal with human vs human
                        and human  vs computer
            Parameter: x and y are both integers, and they are the coordinate of
                        mouse click on screen.
        '''
        # set current player
        # set next player for next turn indicator
        if self.round % 2 == 0:
            curr_player = self.first
            next_player = self.last
        else:
            curr_player = self.last
            next_player = self.first
        curr_player_done = False
        self.info_box.clear()
        
        # calculate the col-coordinate of piece that need to change color
        # locate the column
        picked_col = int((x - INIT_X) // self.unit_x)
            
        # if click on top button
        # place piece
        if self.y_insert - UNIT_2 <= y <= self.y_insert + UNIT_2:
            if self.data[0][picked_col] != 0:
                curr_player_done = False
                self.print_info("This column is full.Pick another")
            else:
            # locate the row
                for i in range(self.board.height - 1, -1, -1):
                    if self.data[i][picked_col] == 0:
                        picked_row = i
                        # place a piece
                        #self.pieces[self.row][self.column].color(self.curr_player.color)
                        #self.data[self.row][self.column] = self.curr_player.in_data
                        self.place_piece(picked_row, picked_col, \
                                         curr_player.color, curr_player.in_data)
                        curr_player_done = True
                        self.round += 1
                        # indicate who's turn
                        self.display_signal(next_player)
                        break
            
                if self.check_result(curr_player) == True:
                    self.draw_end_page()
                    self.end_game()
        # if clicked on botton buttons
        # remove opponent piece if possible
        # otherwise no change
        elif self.y_remove - UNIT_3 <= y <= self.y_remove + UNIT_3:
            for i in range(self.board.height):
                if self.data[i][picked_col] != 0:
                    if self.data[i][picked_col] != curr_player.in_data:
                        picked_row = i
                        # remove a piece
                        self.place_piece(picked_row, picked_col, W, 0)
                        self.round += 1
                        # indicate who's turn
                        curr_player_done = True
                        self.display_signal(next_player)
                        break
                    else:
                        curr_player_done = False
                        self.print_info("Error! You can't remove youself's piece")
                        break

        # if next step is computer's turn, set next turn
        if curr_player_done and next_player.identity == 'computer':
            self.info_box.clear()
            # computer think for 1 second
            sleep(1)
            if self.round % 2 == 0:
                curr_player = self.first
                next_player = self.last
            else:
                curr_player = self.last
                next_player = self.first

            # place piece for computer
            ai_row, ai_col = self.ai_generate(self.data, curr_player, 'random')
            self.place_piece(ai_row, ai_col, curr_player.color, \
                             curr_player.in_data)
            self.round += 1
            self.display_signal(next_player)
            if self.check_result(curr_player) == True:
                self.draw_end_page()
                self.end_game()
            

    
        
        


    def check_result(self, curr_player):
        '''
            Methods: check_result
            Parameters: self(current object)
            Does: 1. create an visit list to track which element has been loop
                    through.
                  2. iterate each element of data, if the element match current
                     player, check the rows, columns, and diagonol of
                     this element
                  3. check if the board full or not
            Return: return True (boolean) indicate the game is end,
                    and return nothing if the game not end
        '''
        # init list to record visit
        visit = []
        for i in range(self.board.height):
            visit.append([])
            for j in range(self.board.wide):
                visit[i].append(False)

        # loop through data list and check anyone win
        for i in range(self.board.height):
            for j in range(self.board.wide):
                if curr_player.in_data == self.data[i][j] and \
                   visit[i][j] == False:

                    # check row
                    combo = 1
                    for k in range(1, 4, 1):
                        # check bound
                        if j + k >= self.board.wide:
                            break
                        # check value
                        elif curr_player.in_data != self.data[i][j + k]:
                            break
                        else:
                            combo += 1
                    if combo == 4:
                        self.winner = curr_player
                        return True

                    # check column
                    combo = 1
                    for l in range(1, 4, 1):
                        # check bound
                        if i + l >= self.board.height:
                            break
                        # check value
                        elif curr_player.in_data != self.data[i + l][j]:
                            break
                        else:
                            combo += 1
                    if combo == 4:
                        self.winner = curr_player
                        return True

                    # check diagonol_right_side
                    combo = 1
                    for m in range(1, 4, 1):
                        # check bound
                        if i + m >= self.board.height or \
                           j + m >= self.board.wide:
                            break
                        # check value
                        elif curr_player.in_data != self.data[i + m][j + m]:
                            break
                        else:
                            combo += 1
                    if combo == 4:
                        self.winner = curr_player
                        return True

                    # check diagonol_left_side
                    combo = 1
                    for n in range(1, 4, 1):
                        # check bound
                        if i + n >= self.board.height or \
                           j - n >= self.board.height:
                            break
                        elif curr_player.in_data != self.data[i + n][j - n]:
                            break
                        else:
                            combo += 1
                    if combo == 4:
                        self.winner = curr_player
                        return True
                
                visit[i][j] = True

        # check the board is full
        full = self.board.height * self.board.wide
        count = 0
        for i in range(self.board.height):
            for j in range(self.board.wide):
                if self.data[i][j] != 0:
                    count += 1
        if count == full:
            self.winner = None
            self.print_info('Gameover! The board is full, but no one win the game.')
            print('Gameover! The board is full, but no one win the game.')
            return True
        





    # methods that deal with files
    def score_init(self):
        '''
            Method --- initiate score in the beginning of game
            Parameter: current object
        '''
        self.score = []
        try:
            with open(self.scorefile, 'r') as infile:
                lines = infile.readlines()
                for line in lines:
                    lst = line.split()
                    self.score.append(lst)
        except OSError:
            self.score = [['Red', 0],['Yellow', 0]]
                

    def update_score(self):
        '''
            Method --- calculate new score, and write it in scorefile.
            Parameter: current object
        '''
        # update self.score
        if self.winner != None:
            if self.score[0][0] == self.winner.name:
                self.score[0][1] = int(self.score[0][1]) + 1
            elif self.score[1][0] == self.winner.name:
                self.score[1][1] = int(self.score[1][1]) + 1

        # write new score in scorefile
        score = self.score[0][0] + ' ' + str(self.score[0][1]) + '\n' + \
                self.score[1][0] + ' ' +str(self.score[1][1])
        try:
            with open(self.scorefile, 'w') as outfile:
                outfile.write(score)
        except:
            self.print_info("Unable to save score")
            print("Unable to save score")


    

    # start game
    def play(self):
        '''
            Method --- begin play, the main logic of game.
            Parameter: current object
        '''
        # draw board
        self.board = Board()
        self.board.draw_board()
        self.draw_piece()
        self.draw_button()

        # draw score
        self.score_init()
        self.draw_score()
        
        # ask input, dimensions, pvp or pvc
        while True:
            identity = self.board.screen.textinput('human or computer', \
                "Do you want your opponent to be human or computer?").lower()
            if identity == 'computer' or identity == 'human':
                break
        self.ply_2.identity = identity
                
        
        # decide which player go first
        if who_turn() == True:
            self.first = self.ply_1
            self.last = self.ply_2
        else:
            self.first = self.ply_2
            self.last = self.ply_1
        
        # draw the first turn indicator on screen
        self.draw_sign(self.first)
        
        # start playing the game
        print('starting game')
        # if computer go first, do the first step
        if self.first.identity == 'computer':
            # computer think for 1 second befor place pieces
            sleep(1)
            x, y = self.ai_generate(self.data, self.first, 'random')
            self.place_piece(x, y, self.first.color, self.first.in_data)
            self.round += 1
            self.display_signal(self.last)
        self.board.screen.mainloop()
            
        
        
        


        









        
