name = 'Zed A. Shaw'
age = 35 # Yeah, right!
height = 74 # Inches
weight = 180 # Pounds (lbs)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

lbs = 0.45359237  # lbs to kg
inches = 2.54  # cm to inches

height_in_cm = round(height * inches)
weight_in_kg = round(weight * lbs)

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} cm tall.")
print(f"He's {weight_in_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_in_cm + weight_in_kg
print(f"If I add {age}, {height_in_cm}, and {weight_in_kg} I get {total}.")
