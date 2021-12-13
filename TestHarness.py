#----------------------------------------------------------------#
# Title: TestHarness.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# James Crockett, 2021-Dec-11, Created file
#----------------------------------------------------------------#

import DataClasses as DC
import IOClasses as IO
strFileName1 = 'CDInventory.csv'
strFileName2 = 'CDInventory2.csv'
lstofCDs1 = []
lstofCDs2 = []

print('-------------------------------')
print('Testing CD class')
print('-------------------------------')
print(DC.CD.__doc__)
cd1 = DC.CD(1, 'meow meows', 'the cat')
cd2 = DC.CD(2, '80s', 'various')
cd3 = DC.CD(3, '90s', 'various')

cd4 = DC.CD(1, 'rock', 'various')
cd5 = DC.CD(2, 'jazz', 'various')
cd6 = DC.CD(3, 'holidays', 'various')
# cdr1 = DC.CD.__str__(cd1)
# cdr2 = DC.CD.__str__(cd2)
# cdr3 = DC.CD.__str__(cd3)
# print(cdr1, '\n')

lstofCDs1.append(cd1)
lstofCDs1.append(cd2)
lstofCDs1.append(cd3)
print(lstofCDs1)
lstofCDs2.append(cd4)
lstofCDs2.append(cd5)
lstofCDs2.append(cd6)

print()
print()
print('-------------------------------')
print('Testing FileIO class')
print('-------------------------------')
print()
# TEST save an object from file 1
IO.FileIO.save_inventory(strFileName1, lstofCDs1)
IO.FileIO.save_inventory(strFileName2, lstofCDs2)
# TEST load inventory from file 1 and file 2
lstFile1 = IO.FileIO.load_inventory(strFileName1)
lstFile2 = IO.FileIO.load_inventory(strFileName2)

# TEST load function and print objects from file 1
print(IO.FileIO.load_inventory(strFileName1))

# TEST saveFile.save_inventory(strFileName, lstofCDs)
print('\n')
print('-------------------------------')
print('Testing IO class')
print('-------------------------------')
# print menu
IO.ScreenIO.print_menu()

# TEST display menu choices
# IO.ScreenIO.menu_choice()

# TEST show inventory from file 1 and file 2
lstofCDs = lstFile1
print('File 1 Inventory')
Inventory1 = IO.ScreenIO.show_inventory(lstofCDs)
lstofCDs = lstFile2
print('File 2 Inventory')
Inventory2 = IO.ScreenIO.show_inventory(lstofCDs)

# print('\n')
# print('-------------------------------')
# print('Testing Track class')
# print('-------------------------------')
# TestTrack1 = TrkMod.Track(1, 'good times', '03:00')
# print(TestTrack1)