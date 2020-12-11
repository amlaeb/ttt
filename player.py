#pytorch libraries
import torch
import torch.nn as nn
import torch.optim as optim

#my libraries
import learn
import board

#python libraries
import math
import random



class player:

    def __init__(self, player_number, player_name, player_behaviour):
        self.name = player_name
        self.number = player_number #either 1 or 2
        self.starting = False  #whether the player is starting this turn
        self.priority = False   #whether the player has to play or not 
        self.winner = 0     #when this variable is 1, the player wins
        self.behaviour = player_behaviour #default behaviour, either 'random' or 'learner'
        self.n_features = 10
        self.list_of_moves = []
        self.reward = 0

        self.net = learn.net(self.n_features)
        self.lr = 0.1   #the optimiser learning rate
        self.momentum = 0.9 #the optimiser momentum
        self.loss_fn = nn.MSELoss(reduction = 'mean')
        self.optimiser = optim.SGD(self.net.parameters(), lr = self.lr, momentum = self.momentum)
        self.epsilon = 0.9      #epsilon-greedy parameter
        self.alpha = 0.05       #epsilon-greedy decay rate
        self.gamma = 0.1        #Q-learning rate
        


    def reset(self):
        self.winner = 0
        self.priority = 0
        self.list_of_moves = []
        #add other important things to reset AFTER EACH GAME


    def epsilon_greedy(self):
        if np.random.random() > self.epsilon:   #exploit
            self.behaviour = 'learner'
        else:   #explore
            self.behaviour = 'random'

    
    def play(self):
        if self.behaviour == 'random':
            self.random_play()
        elif self.behaviour == 'learner':
            self.learner_play()
        else:
            print('Can\'t figure out the play, check the behaviour')


    def random_play(self, board):
        self.playable_moves = board.get_playable_moves()
        self.play_id = random.choice(self.playable_moves)  
        self.make_move()


    def learner_play(self, board):
        '''
        feed every available state-action pair to the NNET and 
        play the move that has the highest Q-value (with torch.no_grad())
        '''
        pass



    def make_move(self):
        j = math.floor((self.play_id) / 3)
        i = self.play_id - 3 * j 
        self.move = (i, j)
        self.list_of_moves.append(self.play_id) #for the backtrack learn

    def create_state_action_pair(self, board):
        for state in board.list_of_states: 



    def training_step(self, board):
        discounted_reward = self.reward

                features = self.create_features_vector(state, action)
                Q_value = self.net(features)
                loss = self.loss_fn(Q_value, discounted reward)
                self.optimiser.zero_grad()
                self.optimiser.step()



        
    def create_features_vector(self, state_array, action):
        for state in state_array:
            features.append(state)
        features.append(action)
        return features

