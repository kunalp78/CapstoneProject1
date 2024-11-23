"""
This module does flight booking
classes here:
 ...
"""


class User:
    """
    User Registration and Login:
        o	Users can register and log in with their credentials.
        o	Password validation and encryption can be added for security.
    """
    users = {}
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hash(password)
        self.booking = []
    
    @classmethod
    def register(cls):
        name = input("Enter the Name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username in cls.users:
            print("Username already esxists!!")
            return None
        cls.users[username] = User(name, username, password)
        print("User Registration Successfull!!")
        return cls.users[username]
    
# Soulution: We were hashing the hashed password instead of we should have hashed the password
# so line 39 should be  if username in User.users and User.users[username].password == hash(password):

    @staticmethod
    def login():
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username in User.users and hash(User.users[username].password) == password:
            print("Login Successfull!!")
            return User.users[username]
        print("Invalid useraname or password!!")
        return None
    

class Flight:
    """
    1. Flight Search:
        o	Users can search for available flights based on source, destination, and date.
    2.	Flight Booking:
        o	Users can select a flight and book tickets.
        o	Handle seat availability and pricing dynamically.
    """
    def __init__(self, flight_no, source, destination, date, seats, price):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.date = date
        self.seats = seats
        self.price = price
    
    def display_details(self):
        print(f"Flight No: {self.flight_no} | From: {self.source} | To: {self.destination} | "
              f"Date: {self.date} | Seat Available: {self.seats} | Price: {self.price}")


class Booking:
    """
    Booking History:
        o	Users can view their booking history.
        o	Provide options to cancel a booking.
    """
    def __init__(self, user, flight, seats_booked):
        self.user = user
        self.flight = flight
        self.seats_booked = seats_booked
    
    def display_booking(self):
        print(f"User: {self.user.username} | Price: {self.flight.price * self.seats_booked}$")
        

class Admin:
    """
    Admin Panel:
        o	Admins can add or update flights.
        o	View all bookings and user details
    """
    def __init__(self, password):
        self.password = hash(password)
    
    @staticmethod
    def add_flight(flights):
        flight_no = input("Enter the flight number: ")
        source = input("Enter the source: ")
        destination = input("Enter the destination: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        seats = input("Enter the seats: ")
        price = float(input("Enter the price of each seat: "))
        flight = Flight(flight_no, source, destination, date, seats, price)
        flights.append(flight)
        print("Flight is added successfully!!")


def main():
    """
    Main function logic
    """
    flights = []
    admin = Admin(password=input("Enter the Admin password: "))
    print("Main Menu!!")
    while True:
        print("\n1. Register\n2. Login\n3. Admin Login\n4. Exit.")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            User.register()
        elif choice == 2:
            user = User.login()
            if user:
                print("Getting in the User menu!!")
                while True:
                    print("\n1. Search Flight\n2. Book Flight\n3. View Bookings\n4. Logout")
                    user_choice = int(input("Enter your choice: "))
                    if user_choice == 1:
                        source = input("Enter the source: ")
                        destination = input("Enter the destination: ")
                        date = input("Enter data (YYYY-MM-DD): ")
                        available_flights = [f for f in flights if f.source == source and f.destination == destination and f.date == date]
                        if available_flights:
                            print("Available Flights:")
                            for f in available_flights:
                                f.display_details()
                        else:
                            print("No Flights available :(")
                    if user_choice == 2:
                        flight_no = input("Enter the flight number to book:")
                        for flight in flights:
                            if flight.filght_no == flight_no:
                                if flight.seats > 0:
                                    seats_to_book = int(input("Enter the seats you want to book: "))
                                    if seats_to_book <= flight.seats:
                                        flight.seats -= seats_to_book
                                        booking = Booking(user, flight, seats_to_book)
                                        user.booking.append(booking) # assignemt: create getter and setter for booking attribute
                                        print("Booking is successfull!!")
                                    else:
                                        print("Not enough seats available!!")
                                else:
                                    print("No seats available!!")
                            else:
                                print("Invalid Flight number!!")
                    elif user_choice == 3:
                        print("Your bookings: ")
                        for b in user.booking:
                            b.display_booking()
                    elif user_choice == 4:
                        print("Logging out!!")
                        break
                    else:
                        print("Invalid Choice!!")
        elif choice == 3:
            admin_password = input("Enter the admin password: ")
            if hash(admin_password) == admin.password:
                while True:
                    print("\n1. Add Flight\n2. View All Flights")
                    admin_choice = int(input("Enter you choice: "))
                    if admin_choice == 1:
                        admin.add_flight(flights)
                    elif admin_choice == 2:
                        for f in flights:
                            f.display_details()
                    else:
                        print("Invalid choice!!")
                        break
            else:
                print("Invalid admin password!")
        
        elif choice == 4:
            print("Thanks for using the Flight booking system!!")
            break
        else:
            print("Invalid choice. Enter Again!!\n\n")

main()