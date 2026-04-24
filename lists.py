"""
# list are written with square brackets []

"""

my_list =[10,20,30,40,50]
print(my_list)

# lists can contain different data types

mixed_list =[1,"apple",3.5,True]
print(mixed_list)

# acces by their INDEX number
# Index always starts at 0

fruits = ["apple","banana","cherry"]
print(fruits[0])
print(fruits[2])

# you can also use a negative indexes to count from the end

print(fruits[-1])

#  modifying list items

fruits[1]= "mango"
print(fruits)

# adding items

fruits.append("orange")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

# removing items
fruits.remove("cherry")
print(fruits)

fruits.pop()
print(fruits)

# looping through a list

for fruit in fruits:
    print(fruit)
# check if item exist

if "mango"in fruits:
    print("yes, mango is in our list")
# list length 
print(len(fruits))


fav_movies = ["Shrek","clockwork orange","Stepbrothers"]
print(fav_movies)
fav_movies[1]="Talledega Nights"
print(fav_movies)
fav_movies.remove("Stepbrothers")
print(len(fruits))



# home work
new_list = ["spoon","fork","knife"]
print(new_list),
print(new_list[0])

new_list[2]="spork"
print (new_list)
new_list.remove("spoon")
print(new_list)
print(len(new_list))