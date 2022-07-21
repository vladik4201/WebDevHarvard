class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_some_passenger(self, name):
        if not self.available_seating():
            return False
        self.passengers.append(name)
        return True
        #adds someone new to the passengers list

    def available_seating (self):
        return self.capacity - len(self.passengers)

flight = Flight(12)

individual = ["Greg", "Travis", "Henry", "Micheal", "Fiona"]

for person in individual:
    success = flight.add_some_passenger(individual)

    if success:
        print(f'Added a {individual} to the flight')
    else:
        print(f'There aren\'t any available seats for {individual}')
        

#__innit__ creates a new flight 
#add_some_passenger that adds a new passenger to that fight 
#available_seating that tells us how many open seats there are
