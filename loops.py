#a for loop is a control structure that lets you repeat a block of code foe=r each item in a sequence.
#  always initialized\ with for variable in sequence:
                                    # code block runs for each item in sequence


fruits = ["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)


print("----------------------------------------------------------------------------------")

for letter in "Leopoldo":
    print(letter)

print("----------------------------------------------------------------------------------")

# range()generates a sequence of numbers

for x in range(5):
    print(x)

print("----------------------------------------------------------------------------------")

# start and end range

for x in range(2, 6):
    print(x)

print("----------------------------------------------------------------------------------")

# using step

for x in range(0, 10, 2):  # step just skips
    print(x)


# mini challenge

# num = int(input("Enter a number: "))

# for i in range(1, 11):

#     print(f"{num} x {i} = {num * i}")

print("----------------------------------------------------------------------------------")
# while loops

# a while loop repeats a block of code as long the condition is True
# be careful if the condition never becomes False, youll get an Infinite loop!!!!
#  code block runs as long as condition is true

count = 1
while count <= 5:
    print("Count is: ", count)
    count += 1 #you can use break to stop the loop

number = 0

while True:
    print(number)
    number += 1
    if number == 3:
        break

print("----------------------------------------------------------------------------------")

# continue to skip an interation

count = 0
while count < 5:
    count += 1 
    if count == 3:
        continue
    print(count)
print("----------------------------------------------------------------------------------")
# else with while

count = 1
while count < 3:
    print(count)
    count+=1
else:
    print("loop is finished")

# password checker

password = ""

while password != "Secret123":
    password = input("Enter password: ")
    if password != "Secret123":
        print ("Wrong! try again")

print("access granted")

