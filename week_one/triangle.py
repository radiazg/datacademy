# Calculate the triangle's area
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    a = ((s * (s - a) * (s - b) * (s - c))) ** 0.5
    
    return a


# Determines the triangles' type
def triangle_type(a, b, c):
    if a == b and b == c:
        type_name = 'Equilateral'
    elif a != b and b != c and a != c:
        type_name = 'Scalene'
    else:
        type_name = 'Isosceles'
    
    return type_name


def run():
    print('T R I A N G L E     A R E A')
    print('----------------------------')
    print('')
    try:
        b = float(input('Enter the base value: '))
        a = float(input('Enter the A side value: '))
        c = float(input('Enter the B side value: '))
        area = triangle_area(a, b, c)
        type_name = triangle_type(a, b, c)
        print('')
        print(f'The triangle is {type_name} and its area is {area}')
    except ValueError:
        print('You should enter a number')

if __name__ == "__main__":
    run()