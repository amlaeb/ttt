
class board:

    def __init__(self):
        self.squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    


    def update_square(self, player):
    #to run after each player has played
        row, column = player.move
        self.squares[row][column] = player.number

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

    def announce_winner(self, player_1, player_2):
        if player_1.winner == 1:
            print("{} has won the game!".format(player_1.name))
        elif player_2.winner == 1:
            print("{} has won the game!".format(player_2.name))

    def reset(self):
        self.squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


