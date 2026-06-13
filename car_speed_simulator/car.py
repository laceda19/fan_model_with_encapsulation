class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed
    def get_make(self):
        return self.__make
    def get_year_model(self):
        return self.__year_model
    def display_information(self):
        print("Year Model:", self.__year_model)
        print("Make:", self.__make)
        print("Current Speed:", self.__speed)