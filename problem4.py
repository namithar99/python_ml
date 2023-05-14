

order = {}
for _ in range(int(input("enter the list:"))):
    item, space, price = input("enter the item name and space:").rpartition(" ")
    order[item] = order.get(item, 0) + int(price) # if there is no items then the value is zero i.e. orginal price is
                                                    #zero added with the price of the item
print("total items")
for item, price in order.items():
    print(item,price)









