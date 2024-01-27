import pandas as pd 
import os
from pathlib import Path
nb_participants = 24
    
def display_main_choice_screen():
    """"Display the options screen and return the chosen option """
    print("\n*********************************************************")
    print("*********************************************************")
    print("******** choose the data source         =    1      *****")
    print("******** (re)organize tables occupancy  =    2      *****")
    print("******** save tables occupancy          =    3      *****")
    print("*********************************************************")
    print("*********************************************************")
    return_value = input("\n                     What's your choice ? \n")
    return return_value

def display_data_source_screen():
    """"Ask to enter the path of the source file, 
        without input it will works with a default file.
        Used with an argument, the method saves to an xslx file            
    """
    print("...Change data source...\n")
    print("*********************************************************")
    print("*********************************************************")
    print("******** enter the full address                  ********")
    print("******** with the file name and extension        ********")
    print("******** ex.:    c:\path\\filename.xlsx           ********")
    print("*********************************************************")
    print("*********************************************************")
    user_input = Path(input("\n\n         Enter the path with filename: "))
 
    
    try:
    # load participants from the SourceFile
        dataframe1 = pd.read_excel(user_input)
        list_participants = list(dataframe1["Participants"])
  
    except Exception as err:
    # load participants from a Default SourceFile
        print("\n\n\n...Wrong Path, filename or extension...")
        print("...Working with default file : participants.xslx in the current directory...\n\n")
        user_input = os.getcwd() + "\participants.xlsx"
        dataframe1 = pd.read_excel(user_input)
        list_participants = list(dataframe1["Participants"])

    return list_participants