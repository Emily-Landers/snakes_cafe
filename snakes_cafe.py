
welcome_msg = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(welcome_msg)

cust_quest = """
***********************************
** What would you like to order? **
***********************************
"""

def order():
    print('order running')
    print(cust_quest)
    currentOrder = True
    custOrder = {}
    while currentOrder:
        answer = input("> ")
        if answer == "quit":
            currentOrder = False
    else:
       if answer in custOrder.keys():
           custOrder[answer] += 1
       else:
            custOrder[answer] = 1
            num = custOrder[answer]
            if num == 1:
                orders = "order"
            else: 
                orders = "orders"
            orderMsg = f"{num} {orders} of {answer} have been added to your meal"
            print(orderMsg)

order()        
            



