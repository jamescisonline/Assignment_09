#----------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 09 - Working with modules
# Change Log: (Who, When, What)
# James Crockett, 2021-Dec-11, Created file, added code from Assignment 8 to be refactored
# James Crockett, 2021-Dec-12, Wired up code for basic CD functions reflected from lab9A.
#                              I was unable to implement and get track logic to work propertly on my own,
#                              also failed to figure out the the logic for the other lab9B TODOs. Code 
#                              below is what I was able to do from Lab9A without looking at the solution PDF.
#----------------------------------------------------------------#

#import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

strFileName = 'CDInventory.csv'
lstOfCDObjects = []

# -- Main Body of Script -- #
# Done Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = IO.FileIO.load_inventory(strFileName)


while True:
    # Display menu to user
    IO.ScreenIO.print_menu()

    strChoice = IO.ScreenIO.menu_choice()

    # let user add data to the inventory
    if strChoice == 'a':
        #get user input and pass it to CD Class
        strID, strTitle, strArtist = IO.ScreenIO.get_CD_info()

        # Pass user input into an instance of the CD Class
        newCd = (strID, strTitle, strArtist)
        # append values from newCd instance to a table
        PC.DataProcessor.add_CD(newCd, lstOfCDObjects)

        continue  # start loop back at top
    
    if strChoice == 'i':
    #display current inventory
        IO.ScreenIO.show_inventory(lstOfCDObjects)

        continue  # start loop back at top
    
    if strChoice == 'e':
    #display current inventory
        IO.ScreenIO.CD_Submenu()

        continue  # start loop back at top
    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # save data to file
            IO.FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(strFileName)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            #IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # let user exit program
    if strChoice == 'x':
        break
        # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
        
