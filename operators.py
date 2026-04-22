# # Arithmetic operators
# # math operations
# x = 1
# y = 2
# res = 0

# res = x + y  
# print(res)

# assingment operators- used to ssign values to variables

x = 5
x += 5
x -= 3
x *= 3
x /= 3

print(x)         #+=, all operators have to be before the + sign

#comparison operators
# used to compare two values- same as the if else statements

#  == (equal to), !=(not equal), <>(less/greater than), <= >=

# logical operators- used to combine conditional statements
# used with True/False value like conditions
# and -> both must be true
# not -> flips True to False(vice versa) 

x = 10
y = 10
z = 3

print(x == y and y == z) # False, because both conditions are NoT true
print (x == y or y == z)
print(not x == y) #False, bacause x == y  are the same

# Identity operators - used to compare the objects, not if they are equal
# but if theyre actually the same object with the same memory location
#is -> checks if two things are the exact same obejct in memory
# is not -> checks if theyre are not the same

x = 3
y = 3
print(x is y)
print(x is not y)

# memebership operators - used to test if a sequence is presented in an object
# in -> checks is something exist inside a sequence(list,string, etc)
# not in -> checks if something is not inside

x = [1,2,3,4,5]# this is a list
print (4 in x)
print(9 not in x)