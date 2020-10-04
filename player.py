'''
    CS 5001
    SPRING 2020
    PROJECT
    YIQIAN DENG

    player.py
'''

class  Player:
    ''' Class: Player
        Attributes: name(string), color(string), in_data(int), identity(string)
        Methods: constructor
    '''
    
    def __init__(self, name, color, in_data, identity = 'human'):
        '''
            Constructor -- creat a new player object
            Parameters:
                self --- current object
                name --- the name of this player
                color --- which color player belong to, red or yellow.
                identity --- this player is computer or human
        '''
        self.name = name
        self.color = color
        self.in_data = in_data
        self.identity = identity


        






        
