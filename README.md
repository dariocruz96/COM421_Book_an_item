# COM421_Book_an_item

1. A member of staff must be able to book an item for repair. They must provide, at the very least, a customer name, item type, and a description. (You may also ask the user for other information if you believe it is necessary, but I will leave it up to you to decide).

2. A member of staff must be able to search for a specific item sent in for repair by the customer (I will leave it up to you as to how you identify specific items).

3. A member of staff must be able to display all items booked for repair, sorted by customer name.

4. A member of staff must be able to search for an item by customer name. (It is possible that a customer might want more than one item repaired).

5. The member of staff must be able to delete a specific item (I will leave it up to you as to how you identify specific items). This would happen when the item has been repaired.

Task 6 (needs to be completed or mostly completed for a Grade B)

6.  The repair shop also offers a computing help service through its application. Using a different menu option within the same application, a customer should be able to make an enquiry about a computing topic, such as “my computer is running slow – what can I do about it?” or “which web browser would you recommend, and why?”, etc. 

The staff of the repair store should be able view and answer these enquiries using the same application, via a different menu option. In a real-world case, the staff would have to login to answer the enquiries, and the facility would operate online, but for this assignment, you do not need to implement login or online functionality. Just add the “answer enquiries” functionality as an option in the application.  Answering an enquiry should simply remove the enquiry from the collection of enquiries – you do not actually need to write code to send the answer back to the user. Enquiries must be answered in the order they come in (the first enquiry should be answered first)

Task 7 (needs to be at least partially completed for a Grade A)

7. Add routing functionality to the application. Using a further menu option, a user must be able to find a route between the railway station or bus station, and a specific branch of the repair shop (remember that there are four branches in and around the city centre). This route will pass  points of interest (POIs) along the way, such as pubs, restaurants, cafes and so on. 

Create an appropriate data structure and develop an appropriate algorithm to perform this routing, and integrate it into the application so that the user can enter an origin (railway or bus station) and destination (a specific branch of the repair shop), and the application will show them the route, by listing all the intermediate POIs along the way. 

It is not necessary to show the direction the user needs to walk – for example, a route listing all POIs along the way will be fine. For example, this output would be acceptable:

- Railway Station
- Park Cafe
- White Horse Pub
- Solent Computer Repairs, West Street Branch

You can ‘hard-code’ the data structure and add the points of interest to it within your code – it is not necessary for the user to enter the details of the points of interest.

Conditions

As this is a data structures and algorithms module, you must develop your own algorithms, and not use the algorithms provided with the programming language (so, for example, you cannot use a pre-written sort() function; you must select and code your own sorting algorithm). However you are allowed to use the language’s in-built data structures as long as you clearly justify your choice of data structures in your report.
