class Fan:
    # Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):
        self.__speed = Fan.SLOW
        self.__on = False
        self.__radius = 5
        self.__color = "blue"