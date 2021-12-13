#----------------------------------------------------------------#
# Title: DataClasses.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# James Crockett, 2021-Dec-11, Created file
# James Crockett, 2021-Dec-11, Added TrackInfo class from Lab08_E.py
#----------------------------------------------------------------#


# CD class:
# [Done] The attributes need to be extended to store the tracks
# [-] A method to add tracks
# [-] A method to delete tracks
# [-] A method to sort tracks by position
# [-] A method to display album data including tracks
# [-] A method to print track info for saving


if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

class CD:
    """Stores data about a CD:

        properties:
            cd_id: (int) with CD ID
            cd_title: (string) with the title of the CD
            cd_artist: (string) with the artist of the CD
            cd_track: (string) with track info of CD
        methods:
            get_record() -> (str):

    """
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        # -- Attributes -- #
        # DONE The attributes need to be extended to store the tracks
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            #self.__cd_track = str(cd_track)
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be an Integer.')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be a String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be a String!')
            
    @property
    def cd_track(self):
        return self.__cd_track

    @cd_track.setter
    def cd_track(self, value):
        try:
            self.__cd_track = str(value)
        except Exception:
            raise Exception('Track needs to be a String!')
    #TODone Add Code to the CD class

    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{}(by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)


class Track():
    """Stores track details for CDs:

        properties:
            trk_position: (int) with track position for CD.
            trk_title: (string) with track title for CD.
            trk_length: (string) with track length for CD.
        methods:
            None.

    """
    # -- Fields -- #
    position = int()
    title = ''
    length = ''
    # -- Constructor -- #
    def __init__(self, p, t, l):
    #    -- Attributes -- #
        self.__trk_position = p
        self.__trk_title = t
        self.__trk_length = l
    # -- Properties -- #
    @property
    def trk_position(self):
        return self.__trk_position
    
    @trk_position.setter
    def trk_position(self,value):
        if type(value) is str:
            raise Exception('position must be an integer.')
        else:
            self.__trk_position = value
    
    @property
    def trk_title(self):
        return self.__trk_title
    
    @trk_title.setter
    def trk_title(self,value):
        if type(value) is int:
            raise Exception('title must a string value.')
        else:
            self.__trk_title = value
    
    @property
    def trk_length(self):
        return self.__trk_length
    
    @trk_length.setter
    def trk_length(self,value):
        if type(value) is int:
            raise Exception('length must be a string.')
        else:
            self.__trk_length = value
    
    # -- Methods -- #
    @staticmethod
    def __str__(self):
        """Returns: track details as formatted string"""
        return '{:>2}\t{}(length: {})'.format(self.trk_position, self.trk_title, self.trk_length)

    def get_track(self):
        """Returns: CD track formatted for saving to file"""
        return '{},{},{}\n'.format(self.trk_position, self.trk_title, self.trk_length)
