#----------------------------------------------------------------#
# Title: ProcessingClasses.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# James Crockett, 2021-Dec-11, Created file
#----------------------------------------------------------------#

if __name__ == '__main__':
    raise Exception('THis file is not meant to be ran by itself.')
    
import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info to CDinfo to the inventory table.
        
        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of CD Objects): 2D data structure (list of CD Objects) that holds the data during runtime.
            
        Returns:
            None.
            
        """
        
        cdId, title, artist = CDInfo
        cdId = int(cdId)
        row = DC.CD(cdId, title, artist)
        table.append(row)
        
# TODO Add processing of selecting a CD / Album

# TODO Add processing of adding a track
