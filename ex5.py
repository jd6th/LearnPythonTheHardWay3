my_name = "Joy Dalud"
my_age = 33 #not a lie
my_height = 54 #inches
my_weight = 120 #lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall.")
print(f"She's {my_weight} pounds heavy.")
print("Actually that's not heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

#This line is tricky, to get it exactly right
total = my_age + my_height + my_weight

print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

my_height_cm = round(my_height*2.54,1)
print(f"Her height in centimeters: {my_height_cm} cm")

my_weight_kg = round(my_weight * (1/2.2),2)
print(f"Her weight in kilograms: {my_weight_kg} kg")
