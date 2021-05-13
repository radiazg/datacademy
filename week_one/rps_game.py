import os
import random

def rps_winner(player_option, cpu_option):
    player_winner = 1
    cpu_winner = 2
    tie = 3
    if player_option == 'rock':
        if cpu_option == 'scissors':
            return player_winner
        elif cpu_option == 'paper':
            return cpu_winner
        else:
            return tie
    elif player_option == 'paper':
        if cpu_option == 'scissors':
            return cpu_winner
        elif cpu_option == 'rock':
            return player_winner
        else:
            return tie
    else:
        if cpu_option == 'rock':
            return cpu_winner
        elif cpu_option == 'paper':
            return player_winner
        else:
            return tie


def board(tries, player_option, cpu_option, player_winners, cpu_winners):
    clear = lambda: os.system('cls')
    clear()
    print('🥌, 📄 AND ✂ GAME')
    print('----------------------------')
    print('Choice a option:')
    print('1️⃣ Rock 🥌')
    print('2️⃣ Paper 📄')
    print('3️⃣ Scissors ✂')
    print('')
    print('----------------------------')
    if tries > 0:
        print(f'# of games: {tries}')
        print('----------------------------')
        print(f'Your Choice is {player_option}')
        print(f'CPU Choice is {cpu_option}')
        print('----------------------------')
        print(f'You win {player_winners} of 3 rounds')
        print(f'CPU win {cpu_winners} of 3 rounds')


def run():
    options = ['rock', 'paper', 'scissors']
    tries = 0
    cpu_winners = 0
    player_winners = 0
    player_option = ''
    cpu_option = ''
    while True:
        board(tries, player_option, cpu_option, player_winners, cpu_winners)
        try:
            option_choise = int(input('Enter the number option: '))
            if option_choise > 0 and option_choise < 4:
                tries += 1
                player_option = options[option_choise-1]
                cpu_option = random.choice(options)
                winner = rps_winner(player_option, cpu_option)

                if winner == 1:
                    player_winners += 1
                elif winner == 2:
                    cpu_winners += 1
                
                if player_winners == 2:
                    board(tries, player_option, cpu_option, player_winners, cpu_winners)
                    print('')
                    print(f'😁 Congrats 😁 You WIN 🎉 the GAME')
                    break
                elif cpu_winners == 2:
                    board(tries, player_option, cpu_option, player_winners, cpu_winners)
                    print('')
                    print(f'💀 Sorry 😁 You LOST 💀 the GAME')
                    break

        except ValueError:
            print('You should enter a number')

if __name__ == "__main__":
    run()