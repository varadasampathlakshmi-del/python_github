#Week-7
#Lab-2-task-5(combining all argument types)
#Sampath lakshmi


def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Ordered Items:")
    for item in items:
        print("-", item)
    print("Discount:", discount)
    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").title(), ":", value)
order_summary(
    "Chinnu",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=700,
    delivery_address="Mumbai",
    gift_wrap=True
)


#output:
#Customer: Chinnu
#Ordered Items:
#- Laptop
#- Mouse
#- Keyboard
#Discount: 700
#Extra Information:
#Delivery Address : Mumbai
#Gift Wrap : True

