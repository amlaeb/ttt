import board
import player

#initialise the board and the players
b = board.board()
learner = player.player(1, 'learner')
random = player.player(2, 'random')

#initialise the game
b.game_init(learner, random)

#initialise the round and set the player which currently has priority
b.round_init(learner, random)
player_with_priority = learner if learner.priority == True else random

#play the round until a winner is found
while b.winner == 0:
    player_with_priority.decide_move() #using ANN or random
    player_with_priority.make_move()
    b.update_square(player_with_priority)
    b.check_winner(random, learner)
    player_with_priority = learner if learner.priority == True else random

#once a winner is found, announce it and reset the board
b.announce_winner(learner, random)
b.reset(learner, random)

