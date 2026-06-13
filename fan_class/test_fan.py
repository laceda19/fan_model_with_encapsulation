from fan import Fan

# First fan
fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

# Second fan
fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)
print("===== FAN 1 =====")
print("Speed:", fan1.get_speed())
print("Radius:", fan1.get_radius())
print("Color:", fan1.get_color())
print("On:", fan1.get_on())

print()

print("===== FAN 2 =====")
print("Speed:", fan2.get_speed())
print("Radius:", fan2.get_radius())
print("Color:", fan2.get_color())
print("On:", fan2.get_on())