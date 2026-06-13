from car import Car

my_car = Car(2025, "Toyota")
print("Accelerating")

for count in range(5):
    my_car.accelerate()
    print("Current speed:", my_car.get_speed())
print("\nBraking")

for count in range(5):
    my_car.brake()
    print("Current speed:", my_car.get_speed())