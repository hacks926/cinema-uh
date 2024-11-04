import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

class InvalidSeatNumberError(Exception):
    pass

class Ticket:
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def display_info(self):
        return f"Movie: {self.movie_title}, Seat: {self.seat_number}, Price: ${self.price}"

class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, discount=0):
        super().__init__(movie_title, seat_number, price=100)  # Set fixed price for standard tickets
        self.discount = discount

    def display_info(self):
        info = super().display_info()
        if self.discount > 0:
            info += f", Discount: {self.discount}%"
        return info

class VIPticket(Ticket):
    def __init__(self, movie_title, seat_number, lounge_access=True, complimentary_drinks=2):
        super().__init__(movie_title, seat_number, price=250)  # Set fixed price for VIP tickets
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def display_info(self):
        info = super().display_info()
        info += f", Lounge Access: {'Yes' if self.lounge_access else 'No'}, Complimentary Drinks: {self.complimentary_drinks}"
        return info

class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            if not (1 <= ticket.seat_number <= 100):
                raise InvalidSeatNumberError(f"Seat number {ticket.seat_number} is out of the valid range (1-100).")
            self.tickets.append(ticket)
        except InvalidSeatNumberError as e:
            logging.error(e)
            print("Error: Invalid seat number.")
        except Exception as e:
            logging.exception("An error occurred while adding the ticket.")
            print("An error occurred while creating the ticket:", e)

    def display_all_tickets(self):
        if self.tickets:
            print("\nSummary of all tickets:")
            for ticket in self.tickets:
                print(ticket.display_info())
        else:
            print("No tickets available.")

def create_ticket():
    try:
        movie_title = input("Enter the movie title: ")
        seat_number = int(input("Enter the seat number (1-100): "))
        ticket_type = input("Select ticket type (Standard/VIP): ").strip().lower()

        if ticket_type == "standard":
            discount = int(input("Enter discount on the ticket (if any, otherwise enter 0): "))
            return StandardTicket(movie_title, seat_number, discount)
        elif ticket_type == "vip":
            lounge_access = input("Lounge access? (Yes/No): ").strip().lower() == "yes"
            complimentary_drinks = int(input("Number of complimentary drinks: "))
            return VIPticket(movie_title, seat_number, lounge_access, complimentary_drinks)
        else:
            print("Invalid ticket type. Please try again.")
            return None
    except ValueError:
        print("Input error. Please make sure the data is entered correctly.")
        return None

cinema = Cinema()

while True:
    action = input("Choose an action: (1 - Add ticket, 2 - Show all tickets, 3 - Exit): ").strip()

    if action == "1":
        ticket = create_ticket()
        if ticket:
            cinema.add_ticket(ticket)
    elif action == "2":
        cinema.display_all_tickets()
    elif action == "3":
        cinema.display_all_tickets()
        print("Program exited.")
        break
    else:
        print("Invalid choice. Please try again.")
