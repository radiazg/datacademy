import os

def board(tries, lower_range, upper_range, value):
    clear = lambda: os.system('cls')
    clear()
    print('RANGE GAME')
    print('----------------------------')
    if tries > 0:
        print(f'Lower Range {lower_range}')
        print(f'Upper Range {upper_range}')
        print('----------------------------')
        print(f'Your number is {value}')
        print(f'# of tries is {tries}')


def run():
    tries = 0
    lower_range = 0
    upper_range = 0
    value = 0
    while True:
        board(tries, lower_range, upper_range, value)
        try:
            if tries == 0:
                lower_range = int(input('Enter the # lower range: '))
                upper_range = int(input('Enter the # upper range: '))
            value = int(input('Enter your number: '))

            if value >= lower_range and value <= upper_range:
                tries += 1
                board(tries, lower_range, upper_range, value)
                break
            else:
                tries += 1
                board(tries, lower_range, upper_range, value)

        except ValueError:
            print('You should enter a number')

if __name__ == "__main__":
    run()