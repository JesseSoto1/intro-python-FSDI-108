print('Hello World from Python!')
print(2)
print(5+3)
print(True)

#  this is a comment


"""

eveything inside here is a comment

"""

# Creatr a variable
name = "Jesse"
age = 40
print(name)

print("My name is: " + name + " and I am " + str(age) + " years old ")

name = " Jesse "
age = 40
middle_name = ""
last_name = " Soto "
found = False
print(" My name is: " + name + middle_name + last_name + " my age is: " + str(age))

# f-strings
print(f" my name is: {name}{middle_name}{last_name} my age is: {age}")
# to call variables wrap in {}
#  no need for converting woth str()

name = "Joe"
age = 20
place = "forest"
action = "camping"
temp = 75 
temp_type = "Farhenheit"
print("A man named" + name + "he was" + str(age) + "years old, he loved" + action+ "in the" + place + " only because the temperature was" + str(temp) + "Degrees" + temp_type)

print(f" A man named {name} he was {age} years old, he loved {action} in the {place} only because the temperature was {temp} Degrees {temp_type}")



# type_functions
print(type(name))
print(type(age))
print(type(True))

# casting (Changing data types
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)

# input function its a user input function. returns the input as strings
# user_name = input("Enter your name:")
# print(f"Hello, {user_name}")

# # input()always returns a string
# print(type(input("Enter your age")))


# new_age = int(input("Enter your age"))
# print(age + new_age)

slice = int(input("Enter slices"))
people = int(input("Enter how many persons"))
total = slice / people
print(f"The total slices per person is {total}")