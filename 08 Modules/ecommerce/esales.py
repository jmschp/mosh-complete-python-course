print("Sales initialized", __name__)

def calc_tax():
    print("Tax")


def calc_shipping():
    print("Shipping")


if __name__ == "__main__": # With this sentence we can use this file as a script. The code we write in the if statmente it will not be executed when we import this module to another module.
    print("Sales initialized")
    calc_tax()
    calc_shipping()