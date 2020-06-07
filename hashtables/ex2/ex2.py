#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create a new dict to store all of the flights, and create a new
    # list of None types to later store the reconstructed itinerary
    flights = dict()
    itinerary = [None] * length

    # using the flight tickets, add each flight to the flights dict
    # with its source as its key and its destination as its value
    for ticket in tickets:
        flights[ticket.source] = ticket.destination

    # start at the first flight, which has a key (source) of NONE
    current_flight = flights['NONE']

    # traverse each element in itinerary and overwrite it w/ the current flight
    # then update the current_flight variable and continue the loop
    for i in range(length):
        itinerary[i] = current_flight        
        current_flight = flights[current_flight]

    # return the reconstructed itinerary
    return itinerary
