from json import loads, dumps
from os.path import exists
from cryptography.fernet import Fernet


class GameDataController(object):
    """
        A Class used to manipulate data stored as JSON
        
        Example:
        controller = GameDataController("data.gdcdfile")
    """

    def __init__(self, file_location: str):
        """
            Intialises the GameDataController object
            Call it with GameDataController() and pass the string location of the file with the extension
        """

        #Initialise all variables
        self.__file_location = file_location
        self.__key = None
        self.__fernet = None
        self.__data = None
        self.__file = __get_file(self.__file_location)

    def __get_file(self, file_location: str):
        file = None
        if exists(file_location):
            file = open(file_location, "rb")
        else:
            create = open(file_location, "x") #Create the file
            create.close()
            file = open(file_location, "rb")
        return file
