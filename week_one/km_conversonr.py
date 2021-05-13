def km_mile_converter(option_choise, value):
    if option_choise == 1:
        ml = value / 1.609344
        print(f'{value} km has {ml} miles')
    elif option_choise == 2:
        km = value * 1.609344
        print(f'{value} miles has {km} km')
    else:
        pass


def run():
    print('KM - MILES  C O N V E R T E R')
    print('----------------------------')
    print('')
    print('What do you want to convert?')
    print('1️⃣ Km to Miles')
    print('2️⃣ Mile to Km')
    try:
        option_choise = int(input('Enter the number option: '))
        if option_choise > 0 and option_choise < 3:
            value = float(input('Enter the value: '))
            km_mile_converter(option_choise, value)
        print('')
    except ValueError:
        print('You should enter a number')

if __name__ == "__main__":
    run()