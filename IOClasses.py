#----------------------------------------------------------------#
# Title: IOClasses.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# James Crockett, 2021-Dec-11, Created file
#----------------------------------------------------------------#


if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class FileIO:
    """Processes data to and from file:
        
        properties:
            
        methods:
            save_inventory(file_name, lst_Inventory): -> None
            load_inventory(file_name): -> (a list of CD objects)
            
    """
    # TODO (failed to figure this out on my own in lab9B)  Data is to be saved in two csv files: One for the CD / Album info (uses csv format). 
    # TODO (failed to figure this out on my own in lab9B) One for track info (needs to include for each row a reference to the CD / Album it is linked to (uses csv format).

    @staticmethod
    def save_inventory(file_name: str, lst_Inventory: list) -> None:
        """
        
        
        Args:
            file_name (str): name of file that holds the data.
            lst_Inventory (list): list of CD objects.
            
        Returns:
            None.
            
        """
        try:
            with open(file_name, 'w+') as file: # w+ used to create file if it doesn't exist
                for disc in lst_Inventory:
                    file.write(disc.get_record()) 
        
        
        
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
            
    @staticmethod
    def load_inventory(file_name: str) -> list:
        """
        
        
        Args:
            file_name (str): name of file that holds the data.
        Returns:
            list: list of CD objects.
            
        """
        objFile = open(file_name, 'a+') #creates text file if it doesn't exist
        objFile.close()
        
        lst_Inventory = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory
    
    
class ScreenIO:
    """Handling Input / Output"""
    
    @staticmethod
    def print_menu():
        """Display a menu of choices to the user
        
        Args:
            None.
            
        Returns:
            None.
        """
        
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[e] ---not working--- Edit CD Album tracks \n[s] Save Inventory to file\n[x] Exit\n')
    
    
# TODO (failed, spent too much time on other parts of lab9B) Add a menu item to select a CD / Album and offer a sub menu
# TODO (failed, spent too much time on other parts of lab9B) Sub menu needs to allow adding, deleting and displaying of track info and exit back to main menu

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        
        Args:
            None.
            
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, e, s or x
            
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'e', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, e, s or x]: ').lower().strip()
            print() # Add extra space for layout
            return choice
    
    @staticmethod
    def print_CDmenu():
        """Display a menu of choices to the user

        Args:
            None.
            
        Returns:
            None.
        """
        
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[e] Edit CD Album tracks\n[s] Save Inventory to file\n[x] Exit\n')
        
    @staticmethod
    def CDmenu_choice():
        """Gets user input for CD Sub Menu
        
        Args:
            None.
            
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, e, s or x
            
        """
        print('cd submenu')
        # choice = ' '
        # while choice not in ['l', 'a', 'i', 'e', 's', 'x']:
        #     choice = input('Which operation would you like to perform? [l, a, i, e, s or x]: ').lower().strip()
        #     print() # Add extra space for layout
        #     return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        
        
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            None.
            
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
        
    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory
            
        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.
            
        """

        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist