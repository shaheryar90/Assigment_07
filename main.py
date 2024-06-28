# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400


list = [100, 200, 300, 400]

for(i, value) in enumerate(list):
    print(f"{i} {value}")

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop
    

list1 = ['a', 'b', 'c', 'd']    
list2 = ['e', 'b', 'g', 'd', 'f', 'h'] 



combined=list1 +list2
result={}


for item in combined:
    if item not in result:
        result[item]=1
    else:
        result[item] +=1
print("Result===>",result)    



# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"
x = 2783
counter = 0

while x > 0:
    counter += 1
    x //= 10  # Floor division by 10 to remove the last digit

print("Total number of digits:", counter)



# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”
while True:
    user_input = input("Enter a value (enter '0' to stop): ")
    if user_input == "0":
        break
    print("You entered:", user_input)



# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list
    
numbers = []
counter = 0

while counter < 5:
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)
    counter += 1

total_sum = sum(numbers)

print("List of numbers:", numbers)
print("Sum of all values:", total_sum)

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
while True:
    name = input("Enter a name (type 'END' to stop): ")
    if name == "END":
        break
    print("You entered:", name)

print("I am done.")
# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"
l1 = [11, 33, 50]
result = ""

for number in l1:
    result += str(number)

print(result)


# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

words = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']

for word in words:
    if len(word) > 5:
        print(word)



# functions

# Write a program to create a function that takes two arguments, name and age. print them inside function.
def print_name_and_age(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

# Example usage:
print_name_and_age("Alice", 30)

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print(f"Employee Name: {name}")
    print(f"Salary: {salary}")

# Example usage:
show_employee("John", 5000)  # Providing both name and salary
show_employee("Jane")        # Providing only name, salary will default to 9000
# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]
def create_list(a, b, c, d):
    return [a, b, c, d]

# Given variables
a = 4
b = 8
c = 10
d = 12

# Calling the function with given variables
result_list = create_list(a, b, c, d)
print(result_list)
# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.
def km_to_miles(kilometers):
    # Conversion factor: 1 kilometer = 0.621371 miles
    miles = kilometers * 0.621371
    return miles

# Example usage:
kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles")
# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.
def is_divisible_by_11(num):
    return num % 11 == 0

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.
def get_highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
highest_number = get_highest(10, 20)
print(highest_number) 


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.

def fuel_cost(distance, fuel_per_liter=280):
    cost = distance * fuel_per_liter
    return cost

distance_traveled = 100
cost_of_fuel = fuel_cost(distance_traveled)
print(f"The cost of fuel for {distance_traveled} km is Rs. {cost_of_fuel}")


# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false
def is_valid_email(email):
   
    if '@' not in email or email.index('@') == 0:
        return False

    if email.count('@') != 1:
        return False
    

    local_part, domain_part = email.rsplit('@', 1)
    

    if '.' not in domain_part or domain_part.index('.') == 0:
        return False
    

    if domain_part[-1] == '.':
        return False

    if len(email) > 256:
        return False
    

    if not email[0].isalnum():
        return False

    return True



"""
Take a variable store i.e
Store = {“name”: “my store”, “inventory”: [], “orders”: []}

Add 5 items in the inventory using a function “add_item”
id, name, price and quantity

Take user input unless it says “done”
Display user updated inventory items every time
Ask user to type id of the item to purchase or type “done” to checkout
Each time only 1 quantity will by subtracted from the item

Functions: add_item_in_inventory, add_item_in_basket(), checkout()
On checkout, print “{quantity} {item} sold in {store}”
"""


# Initialize the store data structure
Store = {"name": "my store", "inventory": [], "orders": []}

# Function to add an item to the inventory
def add_item_in_inventory(id, name, price, quantity):
    item = {"id": id, "name": name, "price": price, "quantity": quantity}
    Store["inventory"].append(item)

# Function to add an item to the basket (order)
def add_item_in_basket(item_id):
    for item in Store["inventory"]:
        if item["id"] == item_id:
            if item["quantity"] > 0:
                item["quantity"] -= 1
                Store["orders"].append(item["name"])
                return True
            else:
                print(f"Sorry, {item['name']} is out of stock.")
                return False
    print("Invalid item ID.")
    return False

# Function to checkout and print the order details
def checkout():
    total_items_sold = len(Store["orders"])
    for item_name in set(Store["orders"]):  # Using set to count each item once
        quantity_sold = Store["orders"].count(item_name)
        print(f"{quantity_sold} {item_name} sold in {Store['name']}")
    Store["orders"] = []  # Clear the orders after checkout

# Adding initial items to the inventory
def add_initial_items():
    add_item_in_inventory(1, "Book", 100, 5)
    add_item_in_inventory(2, "Pen", 10, 10)
    add_item_in_inventory(3, "Notebook", 50, 3)
    add_item_in_inventory(4, "Pencil", 5, 15)
    add_item_in_inventory(5, "Eraser", 3, 20)

# Main program
if __name__ == "__main__":
    add_initial_items()
    print("Welcome to", Store["name"])
    print("Initial Inventory:")
    for item in Store["inventory"]:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: Rs. {item['price']}, Quantity: {item['quantity']}")
    
    while True:
        print("\nChoose an option:")
        print("1. Add item to basket")
        print("2. Checkout")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = int(input("Enter the ID of the item to purchase or type 'done' to go back: "))
            if item_id == "done":
                continue
            add_item_in_basket(item_id)
            print("Updated Inventory:")
            for item in Store["inventory"]:
                print(f"ID: {item['id']}, Name: {item['name']}, Price: Rs. {item['price']}, Quantity: {item['quantity']}")

        elif choice == "2":
            checkout()
            break

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
