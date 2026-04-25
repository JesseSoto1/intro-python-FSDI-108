# tuples are immutable. cant change them
# written in parenthesis

my_tuple = ("apple","banana","cherry")
print(my_tuple)

# check if an item exist

if "banana" in my_tuple:
    print("Yes banbana is in tuple")

# length of tuple
print(len(my_tuple))

# single item tuple
# you must add a comma at the end or python wont recognize the tuple.

single = ("kiwi"),

print(type(single)) #with comma (tuple)


# nested tuples
tuple1 = ("a","b","c")
tuple2 = ("1","2","3")
combine =(tuple1, tuple2)
print(combine)


# travel bag

travel_bag = ("shirt","pantaloons","shoes","socks","underroos")
print(travel_bag[1])
print(travel_bag[3])
if "shoes" in travel_bag:
    print("You are ready to walk")

essentials = ("phone","charger","airpods")

final_bag = (travel_bag, essentials) 
print(final_bag)
print(len(final_bag))
print(final_bag[-1])

