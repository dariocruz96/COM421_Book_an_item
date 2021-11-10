class Item:
    def __init__(self, customerName, itemType, itemDescription):
        self.customerName = customerName
        self.itemType = itemType
        self.itemDescription = itemDescription


class ListOfItems:
    def __init__(self):
        self.listOfItems = [] * 100

    def addItem(self, item):
        self.listOfItems.append(item)

    def __str__(self):
        for item in self.listOfItems:
            print(f"{item.customerName}, {item.itemType}, {item.itemDescription}")
        return ""


listOfItems = ListOfItems()
item1 = Item("Dario", "Rock", "123")
item2 = Item("Tiago", "Rock", "123")
listOfItems.addItem(item1)
listOfItems.addItem(item2)
print(listOfItems)