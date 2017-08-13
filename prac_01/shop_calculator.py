""""
Shop Calculator
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.
The output should look something like
Number of items: 3
Price of item: 100
Price of item: 21.56
Price of item: 3
Total price for 3 items is $112.10
"""
# ask user how many items need adding up. user input must not be negative.
items_count = 0
valid_input = False
while not valid_input:
    try:
        items_count = int(input("Enter total number of items in basket: "))
        if items_count < 0:
            print("Total items can not be negative")
        else:
            valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
# initialise the item count and cost variables
item = 1
total_price = 0
# add up cost of each item
while item <= items_count:
    total_price = total_price + float(input("Price of item: "))
    item = item + 1
# check if 10% discount can be applied
if total_price > 100:
    total_price = total_price * 0.9
print("Total price for ", items_count, " items is ${:.2f}".format(total_price))