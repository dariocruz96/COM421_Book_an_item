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
        self.data = []

    # Option 1 - Adds an item to our list
    def addItem(self, item):
        self.data.append(item)

    # Option 2 - Searches for an item using serial number
    def searchItemsBySerial(self, serialNumber):
        temp = []
        # Looks for every entry in our list
        for element in self.data:
            # Looks for a entry with the same serial number
            if element.serialNumber == serialNumber:
                temp.append(element)
                break
        if len(temp) == 0:
            print("This serial number doesn't exist.")

        return temp

    #  Option 4 - Searches for an item using costumer name
    def searchItemByName(self, customerName):
        temp = []
        # Looks for every entry in our list
        for element in self.data:
            # Looks for a entry with the same costumer name
            if element.customerName.lower() == customerName.lower():
                temp.append(element)

        if len(temp) == 0:
            print("This customer name doesn't exist.")
            temp = "None"

        return temp

    # Option 5 - Deletes an item from our list and returns it after repair
    def deleteItem(self, serialNumber):
        for element in self.data:
            # Looks for a entry with the same serial number
            if int(element.serialNumber) == serialNumber:
                self.data.remove(element)
                return element

    # Calculate serial number using Hash
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
            for x in self.data:
                if x.serialNumber == str(hashCode):
                    hashCode += 1
                else:
                    temp += 1
            if temp == len(self.data):
                break

        return hashCode

    # Returns readable content
    def __str__(self):
        return self.data.__str__()


def tableDesign(listOfItems):
    cn = "Customer Name"
    it = "Item Type"
    ides = "Item Description"
    sc = "Serial Code"
    bar = "|"
    for j in range(222):
        print("-", end="")
    print("")
    print(f"|{cn:>22}{it:>50}{ides:>91}{bar:>38}\t {sc:<16}|")
    for i in listOfItems:
        for j in range(222):
            print("-", end="")
        print("")
        print(
            f"|\t{i.customerName:<35}|\t{i.itemType:<50}|\t{i.itemDescription:<105}|\t{i.serialNumber:<17}|")
    for j in range(222):
        print("-", end="")


# Option 3 - Displays all items booked for repair, sorted by customer name
def mergesort(data):
    sortedListA = []
    sortedListB = []
    if len(data) > 1:
        # mid of the array
        pivot = len(data) // 2
        # left side
        listA = data[:pivot]
        # right side
        listB = data[pivot:]
        sortedListA = mergesort(listA)
        sortedListB = mergesort(listB)
    elif len(data) == 1:
        return data
    sortedList = merge(sortedListA, sortedListB)
    return sortedList


def merge(listA, listB):
    # Set counterA to 0
    counterA = 0
    # Set counterB to 0
    counterB = 0
    sorted_list = []

    while counterA < len(listA) and counterB < len(listB):
        customerNameA = listA[counterA].customerName.lower()
        customerNameB = listB[counterB].customerName.lower()

        if customerNameA <= customerNameB:
            # Add listA[counterA] to sorted_list
            sorted_list.append(listA[counterA])
            # Increase counterA by 1
            counterA += 1

        elif customerNameB < customerNameA:
            # Add listB[counterB] to sorted_list
            sorted_list.append(listB[counterB])
            # Increase counterB by 1
            counterB += 1

        # At this point we will have added all elements from ONE of the two lists
        # to the output list but not the other
    while counterA < len(listA):
        sorted_list.append(listA[counterA])
        counterA += 1
    while counterB < len(listB):
        sorted_list.append(listB[counterB])
        counterB += 1

    return sorted_list


# Option 6 - Creates a queue to create and answer enquiries
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


# Option 7 - routing
'''
import sys
import heapq
from heapq import heappush, heappop

class Node:
  def __init__(self, name):
    self.data = (sys.maxsize, self)
    self.name = name
    self.parent = None
    self.edges = []
    self.used = False
    self.isOnOpenList = False # boolean specifiying whether the node
    # is on the open list, preventing us adding it twice

  # Add an edge to the list of edges from this node
  def add_edge(self, edge):
    self.edges.append(edge)


class Edge:
  def __init__(self, startNode, endNode, dist):
    self.startNode = startNode
    self.endNode = endNode
    self.dist = dist

class Graph:
  def add_edge(self, startNode, endNode, dist):
    # Create an edge using the two nodes n1 and n2
    # and the distance passed in
    edge1=Edge(startNode, endNode, dist)
    edge2=Edge(endNode, startNode, dist)
    n1 = Node(edge1)
    n2 = Node(edge2)
    #n1(edge1)
    #n2(edge2)
    print(n1)

  # Actually do the Dijkstra algorithm
  def dijkstra(self, start, end):
    cur_node = start
    open_list = []

    # start.data[0] = 0
    start.data = (0, start)
    heappush(open_list, start.data)

    while cur_node != end and len(open_list) > 0:
      hp = heappop(h)
    print(hp)
newedge = Graph()
print(newedge.add_edge("lisboa", "porto", 120))
new_edge = Graph
new_edge.add_edge("lisboa","porto", 120)
new_edge.add_edge("porto","coimbra", 120)
new_edge.add_edge("coimbra","olhao", 120)
new_edge.add_edge("olhao","tavira", 120)
new_edge.add_edge("tavira","castelo", 120)
new_edge.add_edge("castelo","braga", 120)
'''


# -------------Menu------------------#


def menu():
    print("Welcome to Solent Computer Repairs!\n"
          "How can I help you today?")

    # Creates our list
    listOfItems = ListOfItems()
    # Creates our enquiry queue
    enquiries = Queue()
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
                item_temp = Item(f"{customer_name}", f"{item_type}",
                                 f"{item_description}", f"{serial}")
                listOfItems.addItem(item_temp)

                print(
                    f"\n\nItem added successfully!\t --- SERIAL NUMBER : {serial} ---")

            # Search an item by serial number
            elif choice == "2":
                serialNumber = input(
                    "Please provide the serial number associated to the item belongs:\n")
                foundItems = listOfItems.searchItemsBySerial(serialNumber)
                if len(foundItems) != 0:
                    print("Found Items:")
                    tableDesign(foundItems)

            # Display all items booked for repair, sorted by customer name
            elif choice == "3":
                print("All items shown by customer name:")
                sortedList = mergesort(listOfItems.data)
                tableDesign(sortedList)

            # Search an item by costumer name
            elif choice == "4":
                customer_name = input("Please provide the customer name:\n")
                foundItems = listOfItems.searchItemByName(customer_name)
                if foundItems != "None":
                    print(f"Items booked in for repair by {customer_name}:")
                    tableDesign(foundItems)

            # Delete an item after being repaired
            elif choice == "5":
                print("Item already repaired:")
                serial = int(input("Serial Number: "))
                item = listOfItems.deleteItem(serial)
                tableDesign([item])
                print("\nThe item will now be deleted from database...\nDone!")

            # Enquiry menu
            elif choice == "6":
                while True:
                    print("\n1 - Client")
                    print("2 - Staff")
                    print("x - Back to main menu\n")
                    choice = input()
                    if choice:
                        # Client
                        if choice == "1":
                            enquiry = input(
                                "Please leave your enquiry for staff to answer:\n")
                            enquiries.add(enquiry)
                        # Staff
                        elif choice == "2":
                            if enquiries.queueSize == 0:
                                print("You don't have new enquiries on hold!")
                            else:
                                while enquiries.queueSize > 0:
                                    print(f"You got {enquiries.queueSize} enquiries on hold!\nEnquiry:")
                                    print(enquiries.remove())
                                    input("Your reply:\n")
                                print("You have answered all the enquiries!")

                        elif choice == "x":
                            break

            # Exit program
            elif choice == "x":
                break


# Runs program when running in main
if __name__ == "__main__":
    # Loads the GUI
    menu()
