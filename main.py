"""
Created on Thu Jan 25 09:59:36 2024

@author: Cédric EL-Dib
"""

if __name__ == "__main__":
 
       

    import pandas as pd 
    import random
    import src.utils as utils
    import random
    from src.openspace import OpenSpace
    from src.table import Table
    nb_participants = 24
    nb_tables = 6
    
    
    #create the Openspace
    openSpace1 = OpenSpace(nb_tables)   
    #load the participants in the input file source
    list_occupant = random.sample(utils.display_data_source_screen(), nb_participants)
    #Organize participants around tables
    openSpace1.organize(list_occupant)
    while True:
        choice = utils.display_main_choice_screen()
        if choice == "1":
            #choose the SourceFile
            list_occupant = random.sample(utils.display_data_source_screen(), nb_participants)
        elif choice == "2":
            #randomize participants around tables and display the result
            list_occupant_randomized = random.sample(list_occupant, nb_participants)
            openSpace1.__init__()
            openSpace1.organize(list_occupant_randomized)
            openSpace1.display()        
        elif choice == "3":
            #Save plan proposed in a xlsx file
            recordname =input("Enter the record name file (without extension) :")
            if recordname == "":
                print("\n... Wrong Record name!!! ...\n")
            else:
               openSpace1.store(recordname)
        else :
            print("\n...Wrong Input... You can do it :-) ...Try again...")
            pass
