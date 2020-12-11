import numpy as np


class board:

    def __init__(self):
        self.squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    
        self.board_state = []
        self.list_of_states = []

    def game_init(self, player_1, player_2):
    #to run at the start of the first round of the session
        coin = np.random.random()
        if coin < 0.5:
            player_1.starting = True
        else:
            player_2.starting = True
        self.winner = 0

    def round_init(self, player_1, player_2):
    #to run at the beginning of every round
        for p in (player_1, player_2):
            if p.starting == True:
                p.priority = True

    def update_square(self, player):
    #to run after each player has played
        row, column = player.move
        self.squares[row][column] = player.number   
        self.write_board_state()

    def check_winner(self, player_1, player_2):    
    #to run after updating the square 
        for i in (0, 1, 2):     
            #check the rows
            if self.squares[i][0] == self.squares[i][1] == self.squares[i][2]:
                if self.squares[i][0] == player_1.number:
                    player_1.winner = 1
                elif self.squares[i][0] == player_2.number:
                    player_2.winner = 1
                elif self.squares[i][0] == 0:
                    pass
            #check columns
            elif self.squares[0][i] == self.squares[1][i] == self.squares[2][i]:
                if self.squares[0][i] == player_1.number:
                    player_1.winner = 1
                elif self.squares[0][i] == player_2.number:
                    player_2.winner = 1
                elif self.squares[0][i] == 0:
                    pass                   
            else:
                pass
        #check diagonal 1
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2]:
            if self.squares[1][1] == player_1.number:
                player_1.winner = 1
            elif self.squares[1][1] == player_2.number:
                player_2.winner = 1
            elif self.squares[1][1] == 0:
                pass
        #check diagonal 2
        elif self.squares[0][2] == self.squares[1][1] == self.squares[2][0]:
            if self.squares[1][1] == player_1.number:
                player_1.winner = 1
            elif self.squares[1][1] == player_2.number:
                player_2.winner = 1
            elif self.squares[1][1] == 0:
                pass
        if player_1.winner == 1 or player_2.winner == 1:
            player_1.priority = False 
            player_2.priority = False 
            player_1.starting = not player_1.starting
            player_2.starting = not player_2.starting
        else:
            player_1.priority = not player_1.priority
            player_2.priority = not player_2.priority
        if player_1.winner == 1:
            self.winner = player_1.number
        elif player_2.winner == 1:
            self.winner = player_2.number

    def announce_winner(self, player_1, player_2):
        if player_1.winner == 1:
            print("{} has won the game!".format(player_1.name))
        elif player_2.winner == 1:
            print("{} has won the game!".format(player_2.name))

    def reset(self, player_1, player_2):
        self.squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        player_1.reset()
        player_2.reset()
        self.winner = 0
        self.list_of_states = []

    def get_playable_moves(self):
        playable_moves = [] 
        for j in (0, 1, 2):
            for i in (0, 1, 2):
                if self.squares[i][j] == 0:
                    playable_moves.append(3 * j + i)
        return playable_moves


    def write_board_state(self):
        for j in (0, 1, 2):
            for i in (0, 1, 2):
                self.board_state.append(self.squares[i][j])
        self.list_of_states.append(self.board_state)
        return self.board_state

