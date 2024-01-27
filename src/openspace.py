from src.table import Table
import pandas as pd 



number_of_places_by_table = 4

class OpenSpace():
    """
    class defining the Openspace, made up of tables and seats where people will be assigned 
    """
    def __init__(self, number_of_tables : int = 6):
        self.tables =  [Table(True, number_of_places_by_table) for i in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        """assigns people to seats from an empty room"""
        for i in range(self.number_of_tables):
            for j in range(number_of_places_by_table):
                num_elem = ( i * number_of_places_by_table ) + j
                self.tables[i].assign_seat(names[num_elem])



    
    def display(self, in_filename : str=""):
        """"display a panda view of tables scheduling"""
        list_numtable = []
        list_numseat = []
        list_occupants = []
        
        for i in range(self.number_of_tables):
            for j in range(number_of_places_by_table):
                if self.tables[i].Seats[j].free == False:
                        list_numtable.append(i+1)
                        list_numseat.append(j+1)
                        list_occupants.append([self.tables[i].Seats[j].occupant])
        
        print("... Tables occupancy...")
        df = pd.DataFrame(list(zip(list_numtable, list_numseat, list_occupants)), columns=["Table", "Seat", "Name"])
        
     
        for i in range(6):          # = number of table
            print("\n", df[(i*4):(i*4)+4].to_string(index=False))        # +4 = number of seats   

      
        if in_filename != "":
            in_filename += ".xlsx" 
            df.to_excel(in_filename, index=False)
        return df
        
    
    def store(self, in_filename : str="export_excel"):
        """"save a panda view of table scheduling in xlsx File"""
        self.display(in_filename)
        print("\n...File recorded..." * 3)

                


