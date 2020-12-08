


class player:

    def __init__(self, player_number, player_name):
        self.name = player_name
        self.number = player_number #either 1 or 2
        self.starting = False  #whether the player is starting this turn
        self.priority = False   #whether the player has to play or not 
        self.winner = 0     #when this variable is 1, the player wins
        #add - check pytorch initialisation

    def make_move(self, cell_id):
    #better to use a cell ID, it will communicate better with the output
    #of the neural network
        if cell_id == 0:
            self.move =  (0, 0)
        if cell_id == 1:
            self.move =  (0, 1)
        if cell_id == 2:
            self.move =  (0, 2)
        if cell_id == 3:
            self.move =  (1, 0)
        if cell_id == 4:
            self.move =  (1, 1)
        if cell_id == 5:
            self.move =  (1, 2)
        if cell_id == 6:
            self.move =  (2, 0)
        if cell_id == 7:
            self.move =  (2, 1)
        if cell_id == 8:
            self.move =  (2, 2)

    def reset(self):
        self.winner = 0
        self.priority = 0
        #add other important things to reset AFTER EACH GAME
