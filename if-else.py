"""
if condition:
-code block that runs when the condition is true
elif(else-if):
-code block runs if the first condition is false
-and this condition only works if its true
else:
-code block runs if none of the above conditions are true.
"""

x = 15

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
elif x >= 5:
    print("x equals 5")
else:
    print("x is not a positive number")

    # short had if statements
    if x > 5: print("x is greater than 5")

# shorthand if-else statements
print("Even") if x % 2 == 0 else print("Odd")


# nested IF statements
if x > 0:
    if x <20:
        print("x is positive number less than 20")


        # combining conditions
        age = 18

        if age >=18 and age <= 21:
            print("you are between 18 and 21")




temp = int(input("PLease enter todays temperature in Fahrenheit"))
if temp >= 86:
    print("Its hot outside")
elif temp >= 68:
    print("The weather is nice")
elif temp >= 50 and temp <68:
    print("its a bit chilly")
else:
    print("Its cold")
# jacket = 59
# if temp > 59: True
#     print("Get a jacket")
# else: False
#     print("No jacket")