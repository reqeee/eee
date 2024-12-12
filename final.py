class Event:
    def __init__(self, id, title, date, location, seats):
        self.id = id
        self.title = title
        self.date = date
        self.location = location
        self.seats = seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            return True
        return False

    def cancel_booking(self):
        if self.booked_seats > 0:
            self.booked_seats -= 1
            return True
        return False


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def register(self):
        pass  # логика регистрации

    def login(self):
        pass  # логика авторизации


class Booking:
    def __init__(self, id, user, event):
        self.id = id
        self.user = user
        self.event = event

    def confirm_booking(self):
        if self.event.book_seat():
            return True
        return False

    def get_booking_details(self):
        return {
            "user": self.user.name,
            "event": self.event.title,
            "date": self.event.date
        }
