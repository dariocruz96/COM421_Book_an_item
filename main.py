class Item:
    # Creates an item structure with costumer name, item type and item description
    def __init__(self, customerName, itemType, itemDescription):
        self.customerName = customerName
        self.itemType = itemType
        self.itemDescription = itemDescription

    # Returns readable content
    def __str__(self):
        return f"{self.customerName} {self.itemType} {self.itemDescription}"


class ListOfItems:
    # Creates our list
    def __init__(self):
        self.listOfItems = []

    # Adds an item to our list
    def addItem(self, item):
        self.listOfItems.append(item)

    def popItem(self, customerName):
        for element in self.listOfItems:
            # Looks for a entry with the same costumer name
            if element.customerName == customerName:
                temp = element
                self.listOfItems.remove(element)
                return temp

    # Searches for an item using costumer name
    def searchItem(self, customerName):
        temp = []
        count = 0
        # Looks for every entry in our list
        for element in self.listOfItems:
            # Looks for a entry with the same costumer name
            if element.customerName == customerName:
                temp.append((element.customerName, element.itemType, element.itemDescription))
                count += 1
        if count == 0:
            print("This customer name doesn't exist.")
        return temp

    # Displays all items booked for repair, sorted by customer name
    def sortItem(self):
        # Used insertion sort
        for i in range(0, len(self.listOfItems) - 1):
            for j in range(0, len(self.listOfItems) - i - 1):
                # If the name is alphabetical "smaller" then the following name, it will switch the names
                # position
                if self.listOfItems[j].customerName > self.listOfItems[j+1].customerName:
                    tempVar = self.listOfItems[j]
                    self.listOfItems[j] = self.listOfItems[j + 1]
                    self.listOfItems[j + 1] = tempVar
        return "\n".join(str(item) for item in self.listOfItems)

    # Returns readable content
    def __str__(self):
        return "\n".join(str(item) for item in self.listOfItems)


def menu():
    # Creates our list
    listOfItems = ListOfItems()
    # Runs the menu until user presses "x" and exits the program
    while True:
        print("\n1 - Book item")
        print("2 - Search item")
        print("3 - Sort by customer name")
        print("4 - Search item by costumer name")
        print("5 - Delete item")

        print("x - Exit Application\n")
        choice = input()
        if choice:
            # Book an item
            if choice == "1":
                item1 = Item("Tiago", "Macbook", "Macbook pro 15.1 2016")
                item2 = Item("Andre", "Laptop", "Asus ROG gtx 1060")
                item3 = Item("Dario", "Desktop", "MSI GLA Combat")
                item4 = Item("Filipe", "Laptop", "Alienware")
                item5 = Item("Dario", "Desktop", "Rog MXO")
                # Adds items to our list
                listOfItems.addItem(item1)
                listOfItems.addItem(item2)
                listOfItems.addItem(item3)
                listOfItems.addItem(item4)
                listOfItems.addItem(item5)
                print("Item added successfully!")

            # Search an item
            elif choice == "2":
                foundItem = listOfItems.searchItem("Dario")
                print("Found Item:")
                for costumer in foundItem:
                    print(f"{costumer[0]} {costumer[1]} {costumer[2]}")

            # Display all items booked for repair, sorted by customer name
            elif choice == "3":
                print(listOfItems.sortItem())

            # Search an item by costumer name
            elif choice == "4":
                foundItem = listOfItems.searchItem("Dario")
                print("Found Item:")
                for costumer in foundItem:
                    print(f"{costumer[0]} {costumer[1]} {costumer[2]}")

            # Delete an item after being repaired
            elif choice == "5":
                print("After repairing:")
                print(listOfItems.popItem("Dario"))
                print("The item will now be deleted from database...\nDone!")

            # Exit program
            elif choice == "x":
                break


# Runs program when running in main
if __name__ == "__main__":
    # Loads the GUI
    menu()
