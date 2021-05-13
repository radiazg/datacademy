def sphere_volume(r):
    volume = (4 / 3) * 3.14159 * (r ** 3)
    print(f'The sphere volume is {volume}')


def cube_volume(s):
    volume = s ** 3
    print(f'The cube volume is {volume}')


def cylinder_volume(br, h):
    volume = h * 3.14159 * (br ** 2)
    print(f'The cylinder volume is {volume}')


def run():
    print('V O L U M E')
    print('----------------------------')
    print('')
    print('calculate volume for:')
    print('1️⃣ Sphere')
    print('2️⃣ Cube')
    print('3️⃣ Cylinder')
    print('')

    try:
        option_choise = int(input('Enter the option: '))
        if option_choise == 1:
            r = int(input('Enter the sphere radius: '))
            sphere_volume(r)
        elif option_choise == 2:
            s = int(input('Enter the sube side: '))
            cube_volume(s)
        elif option_choise == 3:
            br = int(input('Enter the cylinder base radius: '))
            h = int(input('Enter the cylinder height: '))
            cylinder_volume(br, h)
        else:
            print('Enter a valid option')
        
    except ValueError:
        print('You should enter a number')

if __name__ == "__main__":
    run()