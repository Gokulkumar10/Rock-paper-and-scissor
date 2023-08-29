import random


def winner(bot, player):
    if bot == player:
        print('Match drawn')
        return
    if bot == 'rock':
        if player == 'paper':
            print('You Win')
            return True
        else:
            print('You Loose')
            return False
    elif bot == 'paper':
        if player == 'scissor':
            print('You won')
            return True
        else:
            print('You loose')
            return False
    elif bot == 'scissor':
        if player == 'paper':
            print('You loose')
            return False
        else:
            print('You won')
            return True


ch = ['rock', 'paper', 'scissor']
print('***Start the game by enter a valid option. Press any expected key to exit***')
print('The options are,\nr -> rock\np -> paper\ns -> scissor')
no_of_games = w = l = d = 0

while True:
    no_of_games += 1
    print(f'\nGame: {no_of_games}')
    bot = random.choice(ch)
    print(f'bot: {bot}')
    player = input('Enter the choice: ')
    for i in ch:
        if i[0] == player:
            player = i
    if len(player) == 1:
        break
    print(f'*****{bot} v/s {player}******')
    if winner(bot, player):
        w += 1
    else:
        l += 1
    print('-'*15)

d = no_of_games - (w + l)
print('-'*15)
print(f'No of games played: {no_of_games - 1}')
print(f'Games Won: {w}')
print(f'Games Loose: {l - 1}')
print(f'Drawn: {d}')
print('-'*15)