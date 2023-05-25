import math

# Creating a class to represent tables of diners at a restaurant
class Table:

    def __init__(self, num_people):
        self.num_people = num_people
        self.bill = []
    
    
# Method that accepts an item, price and quantity 
    def order(self, item: str, price: int, quantity: int = 1):
        change_qty = False      # Control statement
# Using for loop to iterate through Objects 'bill' list and check for matching 'item' and 'price'
        for order_info in self.bill:
            if order_info["item"] == item and order_info["price"] == price:
                order_info["quantity"] += quantity      # Increase qty if match found
                change_qty = True
        if change_qty != True:      # If match not found and adding order to the 'bill' list
            self.bill.append({"item": item, "price": price, "quantity": quantity})
            

# Subtracts the quantity from the item in the 'bill' with the matching item and price
    def remove(self, item: str, price: int, quantity: int = 1):
# Using for loop to iterate through Objects 'bill' list and check for matching 'item' and 'price'
        for order_info in self.bill:
            if order_info["item"] == item and order_info["price"] == price:
# If match found and qty to remove is higher than qty in the 'bill' return False
                if order_info["quantity"] < quantity:
                    return False
# If match found and qty is equal to qty in the 'bill' remove order from 'bill'
                elif order_info["quantity"] == quantity:
                    self.bill.remove(order_info)
                    return True
                else:
                    order_info["quantity"] -= quantity
                    return True
            else:
                return False


# Returns the total cost for the table based on the prices and quantities in the bill
    def get_subtotal(self):
        sum = 0
        for order_info in self.bill:
            sum += order_info["price"] * order_info["quantity"]
        return sum
    

# Accepts a service charge percentage in the form of a decimal  
    def get_total(self, default: float = 0.10):
        subtotal = self.get_subtotal()
        serv_charge =  default * subtotal
        total = subtotal + serv_charge
# Using formatting to display results
        return {"Sub Total": f"£{subtotal:.2f}", "Service Charge": f"£{serv_charge:.2f}", 
                "Total": f"£{total:.2f}"}
    

# Returns the the subtotal cost of the bill divided by the number of diners 
    def split_bill(self):
        return round(self.get_subtotal() / self.num_people, 2)
