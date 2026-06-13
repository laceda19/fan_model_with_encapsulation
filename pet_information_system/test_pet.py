from pet import Pet

my_pet = Pet()
my_pet.display_information()
name = input("Enter pet name: ")
animal_type = input("Enter animal type: ")
age = int(input("Enter pet age: "))

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\nPet Information")
print("Name:", my_pet.get_name())
print("Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())