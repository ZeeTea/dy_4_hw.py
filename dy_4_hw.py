#Turn the shopping cart program from yesterday into an object-oriented program

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    def __init__(self):
        self.items = {}
    
    def show(self):
        print(self.items)
        
    def add(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
            
    def delete(self, item):
        if item in self.items:
            self.items.pop(item)
        else:
            print(f"{item} not found in cart.")
  
shopping_cart = Cart()

while True:
    consumer = input("Do you want to Show, Add, Delete or Quit? ").lower()
    if consumer == "show":
        shopping_cart.show()
    elif consumer == "add":
        item = input("What item would you like to add? ")
        shopping_cart.add(item)
    elif consumer == "delete":
        item = input("What item would you like to delete? ")
        shopping_cart.delete(item)
    elif consumer == "quit":
        print("Exiting Shopping Cart.")
        break
    else:
        print("Invalid input. Please try again.")

print("Final shopping cart:")
shopping_cart.show()

#Exercise 2 - Write a Python class which has two methods get_String 
#and print_String. get_String accept a string from the user and print_String print the string in upper case

class StringPrinter:
    def __init__(self):
        self.string = ""
    
    def get_String(self):
        self.string = input("Enter a string: ")
        
    def print_String(self):
        print(self.string.upper())

string_printer = StringPrinter()
string_printer.get_String()
string_printer.print_String()