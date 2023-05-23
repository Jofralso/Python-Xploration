'''
Example 1: Employee Database
Problem: Create an employee database where you can store employee information such as name, age, department, and salary. Implement functions to add new employees, retrieve employee details, update employee information, and remove employees from the database.

Solution:
'''

def add_employee(database, emp_id, name, age, department, salary):
    employee = (name, age, department, salary)
    database[emp_id] = employee

def get_employee(database, emp_id):
    if emp_id in database:
        return database[emp_id]
    else:
        return None

def update_employee(database, emp_id, name=None, age=None, department=None, salary=None):
    if emp_id in database:
        employee = database[emp_id]
        name = name if name is not None else employee[0]
        age = age if age is not None else employee[1]
        department = department if department is not None else employee[2]
        salary = salary if salary is not None else employee[3]
        database[emp_id] = (name, age, department, salary)

def remove_employee(database, emp_id):
    if emp_id in database:
        del database[emp_id]
        
'''
Explanation:

We represent each employee as a tuple containing their name, age, department, and salary.
The add_employee function adds a new employee to the database dictionary. The employee is stored with their unique emp_id.
The get_employee function retrieves the details of an employee based on their emp_id. It returns the employee tuple or None if the employee is not found.
The update_employee function updates the information of an existing employee in the database. Any field that is not provided remains unchanged.
The remove_employee function removes an employee from the database based on their emp_id.
Usage:
'''

employee_db = {}

# Add employees
add_employee(employee_db, 1, "John Doe", 30, "Sales", 50000)
add_employee(employee_db, 2, "Jane Smith", 35, "Marketing", 60000)

# Get employee details
employee1 = get_employee(employee_db, 1)
print(employee1)  # Output: ('John Doe', 30, 'Sales', 50000)

# Update employee details
update_employee(employee_db, 2, name="Jane Johnson", salary=65000)
employee2 = get_employee(employee_db, 2)
print(employee2)  # Output: ('Jane Johnson', 35, 'Marketing', 65000)

# Remove employee
remove_employee(employee_db, 1)

'''
Example 2: Book Inventory
Problem: Create a book inventory system where you can keep track of book titles, authors, genres, and quantities available. Implement functions to add books, search for books by title or author, update book details, and remove books from the inventory.

Solution:
'''
def add_book(inventory, title, author, genre, quantity):
    book = {"title": title, "author": author, "genre": genre, "quantity": quantity}
    inventory[title] = book

def search_by_title(inventory, title):
    if title in inventory:
        return inventory[title]
    else:
        return None

def search_by_author(inventory, author):
    matching_books = []
    for book in inventory.values():
        if book["author"] == author:
            matching_books.append(book)
    return matching_books

def update_book(inventory, title, author=None, genre=None, quantity=None):
    if title in inventory:
        book = inventory[title]
        book["author"] = author if author is not None else book["author"]
        book["genre"] = genre if genre is not None else book["genre"]
        book["quantity"] = quantity if quantity is not None else book["quantity"]

def remove_book(inventory, title):
    if title in inventory:
        del inventory[title]
'''
Explanation:

Each book in the inventory is represented as a dictionary with keys for title, author, genre, and quantity.
The add_book function adds a new book to the inventory dictionary. The book is stored with its title as the key.
The search_by_title function retrieves the details of a book based on its title. It returns the book dictionary or None if the book is not found.
The search_by_author function searches for books by a given author. It returns a list of books (dictionaries) matching the author.
The update_book function updates the details of an existing book in the inventory. Any field that is not provided remains unchanged.
The remove_book function removes a book from the inventory based on its title.
Usage:
'''

book_inventory = {}

# Add books
add_book(book_inventory, "1984", "George Orwell", "Dystopian", 10)
add_book(book_inventory, "To Kill a Mockingbird", "Harper Lee", "Classic", 5)
add_book(book_inventory, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 8)

# Search books
book1 = search_by_title(book_inventory, "1984")
print(book1)  # Output: {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'quantity': 10}

books_by_author = search_by_author(book_inventory, "Harper Lee")
print(books_by_author)  # Output: [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Classic', 'quantity': 5}]

# Update book
update_book(book_inventory, "The Great Gatsby", genre="Literary Fiction", quantity=6)
book2 = search_by_title(book_inventory, "The Great Gatsby")
print(book2)  # Output: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Literary Fiction', 'quantity': 6}

# Remove book
remove_book(book_inventory, "1984")

'''
Example 3: Flight Scheduler
Problem: Implement a flight scheduler system that stores flight information such as airline, origin, destination, and departure time. Allow users to add new flights, search for flights by origin or destination, update flight details, and cancel flights.

Solution:
'''
def add_flight(scheduler, flight_number, airline, origin, destination, departure_time):
    flight = {"flight_number": flight_number, "airline": airline, "origin": origin, "destination": destination, "departure_time": departure_time}
    scheduler[flight_number] = flight

def search_by_origin(scheduler, origin):
    matching_flights = []
    for flight in scheduler.values():
        if flight["origin"] == origin:
            matching_flights.append(flight)
    return matching_flights

def search_by_destination(scheduler, destination):
    matching_flights = []
    for flight in scheduler.values():
        if flight["destination"] == destination:
            matching_flights.append(flight)
    return matching_flights

def update_flight(scheduler, flight_number, airline=None, origin=None, destination=None, departure_time=None):
    if flight_number in scheduler:
        flight = scheduler[flight_number]
        flight["airline"] = airline if airline is not None else flight["airline"]
        flight["origin"] = origin if origin is not None else flight["origin"]
        flight["destination"] = destination if destination is not None else flight["destination"]
        flight["departure_time"] = departure_time if departure_time is not None else flight["departure_time"]

def cancel_flight(scheduler, flight_number):
    if flight_number in scheduler:
        del scheduler[flight_number]
'''
Explanation:

Each flight is represented as a dictionary with keys for flight number, airline, origin, destination, and departure time.
The add_flight function adds a new flight to the scheduler dictionary. The flight is stored with its flight number as the key.
The search_by_origin function searches for flights based on the given origin and returns a list of matching flights.
The search_by_destination function searches for flights based on the given destination and returns a list of matching flights.
The update_flight function updates the details of an existing flight in the scheduler. Any field that is not provided remains unchanged.
The cancel_flight function cancels a flight by removing it from the scheduler based on its flight number.
Usage:
'''

flight_scheduler = {}

# Add flights
add_flight(flight_scheduler, "ABC123", "Airline A", "New York", "Los Angeles", "09:00")
add_flight(flight_scheduler, "DEF456", "Airline B", "Chicago", "Denver", "12:30")
add_flight(flight_scheduler, "GHI789", "Airline C", "London", "Paris", "15:45")

# Search flights
flights_from_ny = search_by_origin(flight_scheduler, "New York")
print(flights_from_ny)  # Output: [{'flight_number': 'ABC123', 'airline': 'Airline A', 'origin': 'New York', 'destination': 'Los Angeles', 'departure_time': '09:00'}]

flights_to_denver = search_by_destination(flight_scheduler, "Denver")
print(flights_to_denver)  # Output: [{'flight_number': 'DEF456', 'airline': 'Airline B', 'origin': 'Chicago', 'destination': 'Denver', 'departure_time': '12:30'}]

# Update flight
update_flight(flight_scheduler, "GHI789", departure_time="16:00")
flight = flight_scheduler["GHI789"]
print(flight)  # Output: {'flight_number': 'GHI789', 'airline': 'Airline C', 'origin': 'London', 'destination': 'Paris', 'departure_time': '16:00'}

# Cancel flight
cancel_flight(flight_scheduler, "ABC123")





