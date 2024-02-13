x = int(input("Type a number from 2 to 100 -> "))


match x:
    case 5:
        print("You found to first number of 5 there are.")
    case 20:
        print("You found the second number of 5.")
    case 25:
        print("You found the thrid number of 5.")
    case 55:
        print("You found the fourth number of 5.")
    case 99:
        print("You found the last number of 5 there are.")
    case _:
        print("It isn't a number for win")

match x:
    case 5 | 10 | 15:
        print("It's a number multiply of 5")
    case 2 | 4 | 6 | 8 | 10:
        print("It's a number of multiply 2")
    case _:
        print("It's a number, what number is? I'm not know")

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
'''

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(x, x * 3), Point(x * 3, x)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

def fib(n):
    '''Print a Fibonacci series up to n.'''
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

fib(13000)
# To do the fibonacci serie but now give me the position and program return the number in it position.
# def fib0(n):
