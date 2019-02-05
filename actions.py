# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "MG"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print (store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store_name != store.name:
            return False
        else:
            return True

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print ("available stores are: ")
    print_stores
    print ("please, choose a store: ")
    while True:
        user_input = input()
        if user_input == "checkout":
            return False

        elif get_store(user_input):
            return get_store(user_input)
        else:
            print("No store with that name. Please try again")



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    print ("please feel free to chose anything than type exit to move on")
    while True:
        user_input = input
        if user_input == "exit" or user_input == "back":
            break
        for product in picked_store.products:
            if user_input == product.name:
                cart.add_to_cart(product)

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    while True:
        picked_store = pick_store()
        if picked_store == False:
            break
        else:
            pick_products(cart, picked_store)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
