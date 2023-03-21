#class Ticket:
#
#    def __init__(self, flight, class_):
#        self.flight = flight
#        self.class_ = class_
#    
#    def print(self):
#        print(f"Я билетик на рейс {self.flight} в класс {self.class_}")

class Ticket:

    def __init__(self, flight, seat_class):
        self.flight = flight
        self.seat_class = seat_class
    
    def print(self):
        print(f"Я билетик на рейс {self.flight} в класс {self.seat_class}")


#ticket_1 = Ticket("SP-101", "econom")
#ticket_1.print()

#ticket_2 = Ticket("PD-320", "econom")
#ticket_2.print()
#ticket_2.class_ = "business"
#ticket_2.print()

ticket_1 = Ticket("PD-320", "econom")
ticket_2 = Ticket("SP-101", "econom")

#tickets = [ticket_1, ticket_2]

#for ticket in tickets:
#    ticket.print()

tickets = {"Туда": ticket_1, "Обратно": ticket_2}

tickets["Туда"].print()
tickets["Обратно"].print()
