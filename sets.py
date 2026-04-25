# sets unordered, unindexed and have no duplicates
# written with {}

fruits = {"apple", "banana","cherry"}
print(fruits)

# no duplicates allowed

fruits = {"apple","banana","apple"}
print(fruits)

# check if item exist
print("banana" in fruits)

# adding items
fruits.update(["kiwi","mango"])
print(fruits)

# remove item
fruits.remove("kiwi")
print(fruits)

# sets operation
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2)) #combines both (no duplicates)
print(set1.intersection(set2)) #combines duplicates as new set
print(set1.difference(set2)) #whats only in set1


# party guest list

invited_friends = {"Alex","Sam","Leo","Nina"}
rsvped = {"nina","Sam","Jordan"}
print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))

invited_friends.update(["Bobby","Ricky"])
print(invited_friends)
invited_friends.remove("Leo")
print(rsvped)
if "Sam" in rsvped:
    print("Glad youre coming")
else:
    print("Too bad, maybe next time!")