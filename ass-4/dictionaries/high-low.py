#Week-4
#Part-C Dictionaries-C2(high-low)
#Sampath lakshmi

items = {
    "Pen": 20,
    "Notebook": 80,
    "Bag": 500,
    "Pencil": 10,
    "Bottle": 150
}

highest_item = max(items, key=items.get)
lowest_item = min(items, key=items.get)

print("Item with highest price:", highest_item, "-", items[highest_item])
print("Item with lowest price:", lowest_item, "-", items[lowest_item])
#output:-
#Item with highest price: Bag - 500
#Item with lowest price: Pencil - 10
