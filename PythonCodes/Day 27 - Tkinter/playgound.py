print("playgound")
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
    return total

add(2,3,4,5,6,7,8,4,5,6 )


def calculator(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(2, add =3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model = "GT-R")
print(my_car.color)


