#number_of_table = 6
number_of_places_by_table = 4

class Seat():
    """
    Class defining Seat 
    Seat will be assigned to tables and people will be assigned to these seats
    """
    def __init__(self, free : bool = True, occupant : int = None):
        """By default, our surface is empty"""
        self.free = True                            #indicates whether the chair is free
        self.occupant = occupant                    #name of the person sitting on the chair
        self.prioroccupant = []                     #list of previous occupants if there has been a change of location
    
    def set_occupant(self, name):
        """"assign someone a seat if it's free"""
        self.occupant = name
        self.prioroccupant.append(name)
        self.free = False
        #print(self.occupant)
        


    def remove_occupant(self, name):
        """removes someone from a seat and returns the name of the person occupying the seat before"""
        self.occupant = self.prioroccupant[-1]
        self.prioroccupant = self.prioroccupant[:-1]


class Table():
    """
    Class defining Table that will be assigned to openspaces
    """
    def __init__(self, free : bool=True, capacity : int=number_of_places_by_table):
        self.free = True                                                                    #True If (capacity - occupant) > 0
        self.capacity = capacity                                                            #Maximum Table Capacity
        self.occupant = 0
        self.Seats =  [Seat(True, "Name Occupant Seat") for i in range(self.capacity)]      #list of allocated Seat()  

    def has_free_spot(self):
        """"determine whether we can still seat people at the table"""
        if capacity_left(self) > 0:
            return_value = True
        else : 
            return_value = False
        return return_value
   
    def assign_seat(self, name):
        """places someone at the table in the first free seat, incrementing the number of occupants"""
        for i in range(self.capacity):
            if self.Seats[i].free == True:
                    self.Seats[i].set_occupant(name)
                    self.occupant += 1
                    break
            elif i == self.capacity:
                print("ERROR / Nore more place here")
    
    def capacity_left(self):
        """"return the number of free seats"""
        print("capacity left :", self.capacity - self.occupant)
        return self.capacity - self.occupant







