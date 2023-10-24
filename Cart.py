from item import list_item                      # Importing the list of instantances of items to buy
import datetime                                 # Importing the time stamp for the items in the list
from os import system, name                     # importing what the operating system is to clear the terminal screen to keep it clean
from time import sleep                          # Importing the sleep method to stop the program to view the terminal before continuing

def clear():
    if name == 'nt':
        _ = system('cls')
    # Clear screen for mac and linux
    else:
     _ = system('clear')
    # Clear screen for Windows

# Creating the main cart class
class Cart():
    def __init__(self):
        self.cart_list = [] # Creates the list to store the items for the shopping cart
        self.timestamp = ""
      
    def add_item(self,data):
        self.timestamp = datetime.datetime.now()
        self.cart_list.append(list_item[data]) # takes the item from the item list and adds it to the shopping cart
    
    def viewCart(self):
        if self.cartEmpty(): # Used to determine if the list is empty
            print("Cart is empty\n")       # If list is empty then printing a message instead of an error
        else:  
          e = 1
          for x in self.cart_list:
              print(str(e)+":\n","Product:",x.name,"\n Price:", x.price, "\n Discription:",x.descript,"\n") # Prints out items in the shopping cart
              e += 1
          self.get_total() # Used to get total
        
    def cartEmpty(self):
        return len(cart.cart_list) == 0 # gets the length of the list to see if the list is empty
    
    def delete_item(self,data): # deleting the desire item from the shopping cart by using the index value
        if self.cartEmpty():
            print("Cart is empty\n")
        self.cart_list.pop(data)
    
    def clear_cart(self):   # uses the clear method to empty the entire shopping cart
        self.cart_list.clear()

    def get_total(self): # Used to calculate the total for the shopping cart
        total = 0
        for x in self.cart_list:
            total += x.price
        print("Total: $"+ str(total))
        print(self.timestamp)

clear()
i = True
cart = Cart() # creates the Object which creates the list for the shopping cart and allowing items to be added to it
while i == True: # Using a While loop to keep the program running
    print("Items to choose from")
    print("======================")
    for x in list_item: # Prints the list of Items from the items class that can be added to the shopping cart
        print(str(x.e)+":\n Product:",x.name,"\n Price:",x.price,"\n Discription:",x.descript)
    print("======================")
    print("Option 1: Add Item to Cart")
    print("Option 2: View Cart")
    print("Option 3: Remove Item from Cart")              # Providing an Option for what to do with the shopping cart
    print("Option 4: Clear your Cart")
    Options = int(input("what would you like to do?"))
    if Options == 1:
        option2 = int(input("What item would you like to add to your cart? *Type the Number* : ")) 
        opt = cart.add_item(option2-1)
    elif Options == 2:
        clear()
        cart.viewCart() 
        exit = input("Press enter to continue.") 
    elif Options == 3:
        clear()
        cart.viewCart()
        option3 = int(input("What item would you like to delete from your cart? *Type the Number* : "))
        opt = cart.delete_item(option3-1)
    elif Options == 4:
        cart.clear_cart()
    clear() # clearing the terminal screen to help keep things neater
