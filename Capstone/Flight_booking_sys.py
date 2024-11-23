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
    
    def login(self):
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
        self.password = password
    
    def add_flight(self, flights):
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

    admin = Admin(password="admin123")
    while True:
        print("\n1. Register\n2. Login\n3. Admin Login\n4. Exit.")
main()