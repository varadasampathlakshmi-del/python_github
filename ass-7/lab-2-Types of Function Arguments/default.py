#Week-7
#Lab-2-task-2(default arguments)
#Sampath lakshmi

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    total = price + tax
    final_price = total - discount
    return final_price
print("Only price:", calculate_price(1000))
print("Price and custom tax:", calculate_price(1000, 10))
print("All arguments:", calculate_price(1000, 10, 100))


#output:
#Only price: 1180.0
#Price and custom tax: 1100.0
#All arguments: 1000.0
