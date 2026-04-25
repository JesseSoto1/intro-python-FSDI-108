#  a function is a block of code that only runs when its called
# we can pass data functions (parameters), and the can return data as a result

# use def to dfine function and then function name     def funtion_name(parameters):
                                                                # code block(indented)
                                                                # preform actions using parameters
                                                                # return values #optional

def my_function():
    print("This is my function")


# calling the function
my_function()


# function with parameters

def print_full_name(f_name, l_name):
    print(f"This name is: {f_name} {l_name}")

print_full_name("Jesse", "Soto")


# Functions that return values
# instead of just printing, function can send back data.

def get_full_name(f_name, l_name):
    return f"{f_name} {l_name}" #returns as txt

full_name = get_full_name("Jesse", "Soto")
print(full_name)

# functions with default parameters
# a default parameter means the function will use that value
# if no argument is provided when calling the function

def greet(name = "Student"):
    print(f"Hello, {name}! welcome to class")

# calling with no argument
greet()

# calling with argument
greet("Jesse")