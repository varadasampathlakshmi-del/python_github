#Week-7
#Lab-4-task-5(lambda for dictionary sorting value)
#Sampath lakshmi


items = {
    "Pen": 15,
    "Book": 50,
    "Pencil": 10,
    "Bag": 700,
    "Eraser": 5
}
sorted_items = sorted(items.items(), key=lambda item: item[1])
print("Items from cheapest to most expensive:")
for item, price in sorted_items:
    print(item, ":", price)



#output:
#Items from cheapest to most expensive:
#Eraser : 5
#Pencil : 10
#Pen : 15
#Book : 50
#Bag : 700
