def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

def calculate_bill_without_tax(item_cost, quantity, discount=0):
    total = (item_cost * quantity) - discount
    return total