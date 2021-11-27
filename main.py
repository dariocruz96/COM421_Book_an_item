class Item:
    # Creates an item structure with costumer name, item type and item description
    def __init__(self, customerName, itemType, itemDescription, serialNumber):
        self.customerName = customerName
        self.itemType = itemType
        self.itemDescription = itemDescription
        self.serialNumber = serialNumber

    # Returns readable content
    def __str__(self):
        return f"{self.customerName} {self.itemType} {self.itemDescription} {self.serialNumber}"


class ListOfItems:
    # Creates our list
    def __init__(self):
        self.listOfItems = []

    # Adds an item to our list
    def addItem(self, item):
        self.listOfItems.append(item)

    def popItem(self, serialNumber):
        for element in self.listOfItems:
            # Looks for a entry with the same serial number
            if int(element.serialNumber) == serialNumber:
                self.listOfItems.remove(element)
                return element

    # Searches for an item using costumer name
    def searchItemByName(self, customerName):
        temp = []
        # Looks for every entry in our list
        for element in self.listOfItems:
            # Looks for a entry with the same costumer name
            if element.customerName.lower() == customerName.lower():
                temp.append((element.customerName, element.itemType, element.itemDescription, element.serialNumber))
        if len(temp) == 0:
            print("This customer name doesn't exist.")
        return temp

    # Searches for an item using costumer name
    def searchItemBySerial(self, serialNumber):
        temp = []
        # Looks for every entry in our list
        for element in self.listOfItems:
            # Looks for a entry with the same costumer name
            if element.serialNumber == serialNumber:
                temp.append((element.customerName, element.itemType, element.itemDescription, element.serialNumber))
        if len(temp) == 0:
            print("This serial number doesn't exist.")
        return temp

    # Displays all items booked for repair, sorted by customer name
    def sortItem(self):
        # Used insertion sort
        for i in range(0, len(self.listOfItems) - 1):
            for j in range(0, len(self.listOfItems) - i - 1):
                # If the name is alphabetical "smaller" then the following name, it will switch the names
                # position
                if self.listOfItems[j].customerName > self.listOfItems[j + 1].customerName:
                    tempVar = self.listOfItems[j]
                    self.listOfItems[j] = self.listOfItems[j + 1]
                    self.listOfItems[j + 1] = tempVar
        return "\n".join(str(item) for item in self.listOfItems)

    # Calculate Hash
    def serialNumber(self, name):
        count = 0
        hashCode = 0
        for ch in name:
            hashCode += (ord(ch) - 96) * (31 ** count)
            count += 1
        # This will reduce the size of the serial number, but will limit it
        hashCode = hashCode % 2000
        while True:
            temp = 0
            for x in self.listOfItems:
                if x.serialNumber == str(hashCode):
                    hashCode += 1
                else:
                    temp += 1
            if temp == len(self.listOfItems):
                break

        return hashCode

    def tableDesign(self):
        cn = "Customer Name"
        it = "Item Type"
        ides = "Item Description"
        sc = "Serial Code"
        bar = "|"
        for j in range(222):
            print("-", end="")
        print("")
        print(f"|{cn:>22}{it:>50}{ides:>91}{bar:>38}\t {sc:<16}|")
        for i in self.listOfItems:
            for j in range(222):
                print("-", end="")
            print("")
            print(f"|\t{i.customerName:<35}|\t{i.itemType:<50}|\t{i.itemDescription:<105}|\t{i.serialNumber:<17}|")
        for j in range(222):
            print("-", end="")

    # Returns readable content
    def __str__(self):
        return "\n".join(str(item) for item in self.listOfItems)


class Queue:

    def __init__(self, capacity=10):
        self.front = 0
        self.back = 0
        self.queueSize = 0
        self.data = [None] * capacity
        self.capacity = capacity

    def add(self, item):
        self.data[self.back] = item
        self.back += 1
        # wrap around the index
        if self.back == self.capacity:
            self.back = 0
        # increase queue size by 1
        self.queueSize += 1

    def remove(self):
        temp = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        # wrap around the index
        if self.front == self.capacity:
            self.front = 0
        self.queueSize -= 1
        return temp

    def size(self):
        return self.queueSize

    def __str__(self):
        return self.data.__str__()


def menu():
    print("Welcome to Solent Computer Repairs!\n"
          "How can I help you today?")
    # Creates our list
    listOfItems = ListOfItems()
    enquiries = Queue()
    firstLoop = 0
    # Runs the menu until user presses "x" and exits the program
    while True:
        print("\n1 - Book item")
        print("2 - Search item by serial number")
        print("3 - Show items sorted by customer name")
        print("4 - Search item by customer name")
        print("5 - Delete item")
        print("6 - Enquiries")

        print("x - Exit Application\n")
        choice = input()
        if choice:
            # Book an item
            if choice == "1":
                if firstLoop == 0:
                    item1 = Item("Tiago", "Macbook", "Macbook pro 15.1 2016", "12341")
                    item2 = Item("Andre", "Laptop", "Asus ROG gtx 1060", "123124")
                    item3 = Item("Dario", "Desktop", "MSI GLA Combat", "123123")
                    item4 = Item("Filipe", "Laptop", "Alienware", "12313")
                    item5 = Item("Dario", "Desktop", "Rog MXO", "12412313")
                    # Adds items to our list
                    listOfItems.addItem(item1)
                    listOfItems.addItem(item2)
                    listOfItems.addItem(item3)
                    listOfItems.addItem(item4)
                    listOfItems.addItem(item5)
                    firstLoop += 1
                    print("BOOKING AN ITEM\n\n---Information Required---\n")
                while True:
                    customer_name = input("Customer name:\n")
                    if customer_name == "":
                        print("Please provide a customer name!")
                    else:
                        break
                serial = listOfItems.serialNumber(customer_name)
                item_type = input("Item type:\n")
                item_description = input("Item description:\n")
                item_temp = Item(f"{customer_name}", f"{item_type}", f"{item_description}", f"{serial}")
                listOfItems.addItem(item_temp)

                print(f"\n\nItem added successfully!\t --- SERIAL NUMBER : {serial} ---")

            # Search an item by serial number
            elif choice == "2":
                tempList = ListOfItems()
                serialNumber = input("Please provide the serial number associated to the item belongs:\n")
                foundItem = listOfItems.searchItemBySerial(serialNumber)
                print("Found Item:")
                for customer in foundItem:
                    item = Item(f"{customer[0]}", f"{customer[1]}", f"{customer[2]}", f"{customer[3]}")
                    tempList.addItem(item)
                tempList.tableDesign()

            # Display all items booked for repair, sorted by customer name
            elif choice == "3":
                listOfItems.sortItem()
                listOfItems.tableDesign()

            # Search an item by costumer name
            elif choice == "4":
                tempList = ListOfItems()
                customer_name = input("Please provide the customer name:\n")
                foundItem = listOfItems.searchItemByName(customer_name)
                print("Found Item:")
                for customer in foundItem:
                    item = Item(f"{customer[0]}", f"{customer[1]}", f"{customer[2]}", f"{customer[3]}")
                    tempList.addItem(item)
                tempList.tableDesign()

            # Delete an item after being repaired
            elif choice == "5":
                tempList = ListOfItems()
                print("Item already repaired:")
                serial = int(input("Serial Number: "))
                item = listOfItems.popItem(serial)
                tempList.addItem(item)
                tempList.tableDesign()
                print("\nThe item will now be deleted from database...\nDone!")


            elif choice == "6":
                while True:
                    print("\n1 - Client")
                    print("2 - Staff")
                    print("x - Exit Application\n")
                    choice = input()
                    if choice:
                        # Client
                        if choice == "1":
                            enquiry = input("Please leave your enquiry for staff to answer:\n")
                            enquiries.add(enquiry)
                        # Staff
                        elif choice == "2":
                            if enquiries.queueSize == 0:
                                print("You don't have new enquiries on hold!")
                            else:
                                while enquiries.queueSize > 0:
                                    print(f"You got {enquiries.queueSize} enquiries on hold!")
                                    print(enquiries.remove())
                                    input("Your reply:\n")
                                print("You have answered all the enquiries!")

                        elif choice == "x":
                            break

            elif choice == "0":
                listOfItems.tableDesign()

            # Exit program
            elif choice == "x":
                break


# Runs program when running in main
if __name__ == "__main__":
    # Loads the GUI
    menu()
