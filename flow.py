import board
import player

b = board.board()
t = player.player(1, 'Tommaso')
l = player.player(2, 'Lea')

print('\nPlayer creation')
print(t.name, t.number, t.starting, t.priority)
print(l.name, l.number, l.starting, l.priority)

b.game_init(t, l)

print('\nGame init')
print(t.name, t.number, t.starting, t.priority)
print(l.name, l.number, l.starting, l.priority)

b.round_init(t,l)
player_with_priority = t if t.priority == True else l

print('\nRound init')
print(t.name, t.number, t.starting, t.priority)
print(l.name, l.number, l.starting, l.priority)
print('Player with priority is {}'.format(player_with_priority.name))

while b.winner == 0:
    for i in range(9):
        player_with_priority.make_move(i)
        b.update_square(player_with_priority)
        b.check_winner(t, l)
        player_with_priority = t if t.priority == True else l

b.announce_winner(t, l)
print(b.squares)
b.reset(t, l)


