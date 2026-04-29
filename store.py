from catalog import catalog # import you catalog dictionary

cart = []# global variable empty list
# total = sum({prod["price"]}) in view_cart()

# header/helper functions
def print_header(text):
    print("----------------------------")
    print(text)
    print("----------------------------")

def menu():
    print("Menu")
    print(" 1. - View Catalog")
    print(" 2. - Search Product")
    print(" 3. - View Cart")
    # add more functions
    print(" 4. - Clear Cart")
    print(" Q. - QUIT")

# catalog and cart functions

def print_catalog():
    print_header("- Our catalog -")
    for prod in catalog:
        print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")

    # implementing adding product function
    answer = input("Enter ID to add (N to close): ")
    if answer.lower() =="n":
        return
    else:
        add_product_to_cart(answer)
        print("----------------------------")




def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)# add product to end of cart
            print(f"{prod["title"]} ADDED TO YOU CART. ")
            break#stop after finding the product

    if not found:
        print("**Error: Invalid ID")
        print("----------------------------")

def search_product():
    text = input("Search product title: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
            choice = input("Do you want to add this item to your cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
                break
    if not found:
        print("Sorry, this item doesnt exist.")
        print("----------------------------")

def view_cart():
    print_header("Your cart")
    if not cart:        #checking if cart is empty. NOT is boolean
        print("Your cart is empty")
    else:
        for prod in cart:
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}") 
        cart_total()


def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f" Your Total: ${total}")
        
def clear_cart():
    cart.clear
    print("Your Cart is empty.")


        






# main program loop


option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Awesome Blossoms")
    menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        clear_cart()
    elif option == "q" or option =="Q":
        print("Quit")
    else:
        print("** Error: Invalid option")
        print("----------------------------")