from json import loads, dumps
from os.path import exists
from cryptography.fernet import Fernet
import GameData.Exceptions as Exceptions


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
        self.__key = self.__load_fernet_key()
        self.__fernet = Fernet(self.__key)
        self.__data = None
        self.__file = self.__get_file(self.__file_location)

    def __load_fernet_key(self)->bytes:
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        
        if exists("egtgdcek.k3y"):
            f = open("egtgdcek.k3y", "rb")
            key = f.read()
            if type(key) != bytes:
                key = None
                raise Exceptions.FatalError("Fatal Error: Key could not be resolved")
            return key
        else:
            f = open("egtgdcek.k3y", "xb")
            key = Fernet.generate_key()
            f.write(key)
            f.close()
            return self.__load_fernet_key()
            
            

    def __get_file(self, file_location: str):
        file = None
        if exists(file_location):
            file = open(file_location, "rb")
        else:
            create = open(file_location, "xb") #Create the file
            create.close()
            file = open(file_location, "rb")
        return file
    
    def __load_file_data_as_str(self)->str:
        out = None
        try:
            out = self.__file.read().decode()
        except:
            out = self.__file.read()
        return out
    
    def __load_file_data_as_bytes(self)->bytes:
        out = None
        try:
            out = self.__file.read().encode()
        except:
            out = self.__file.read()
        return out
    
    def __encrypt(self, data: bytes)->bytes:
        return self.__fernet.encrypt()
