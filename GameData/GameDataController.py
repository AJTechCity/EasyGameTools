from json import loads, dumps
from os.path import exists
from cryptography.fernet import Fernet
import GameData.Exceptions as Exceptions


class GameDataController(object):
    """
        A Class used to manipulate data stored as JSON.
        This Class will be specialised for storage of GameData
        
        Example:
        controller = GameDataController("data.gdcdfile")
    """

    def __init__(self, file_location: str):
        """
            Intialises the GameDataController object
            Call it by:
                controller = GameDataController(path_to_file)
        """

        #Initialise all variables
        self.__file_location = file_location
        self.__file = self.__get_file(self.__file_location)
        self.__key = self.__load_fernet_key()
        self.__fernet = Fernet(self.__key)
        self.__data = self.__load_file_data_as_dict()

        #Add multiple names to each function
        self.add_variable = self.create_variable

    #PRIVATE FUNCTIONS#
    def __get_file(self, file_location: str, mode:str = "rb"):
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        file = None
        if exists(file_location):
            file = open(file_location, mode)
        else:
            create = open(file_location, "xb") #Create the file
            create.write(b"{}")
            create.close()
            file = open(file_location, mode)
        return file

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

    def __load_file_data_as_dict(self)->dict:
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        out = None
        try:
            out = self.__file.read().decode()
            if len(out) == 0:
                self.__file.write(b"{}")
                out = self.__load_file_data_as_dict()
        except:
            out = self.__file.read()
            if len(out) == 0:
                self.__file.close()
                self.__file = self.__get_file(file_location=self.__file_location, mode="wb")
                self.__file.write(b"{}")
                self.__file.close()
                self.__file = self.__get_file(file_location=self.__file_location)
                out = self.__load_file_data_as_dict()
        return loads(out)
    
    def __load_file_data_as_bytes(self)->bytes:
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        out = None
        try:
            out = self.__file.read().encode()
        except:
            out = self.__file.read()
        return out
    
    def __encrypt(self, data: bytes)->bytes:
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        return self.__fernet.encrypt(data)
    
    def __decrypt(self, data:bytes)->bytes:
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        return self.__fernet.decrypt(data)

    def __save(self):
        """
            PRIVATE FUNCTION
            If you call this function, it may damage the file contents and has fatal effects on your data
        """
        write_data = str(self.__data).encode()
        self.__file.close()
        self.__file = open(self.__file_location, "wb")
        self.__file.write(write_data)
        self.__file.close()
        self.__file = open(self.__file_location, "rb")

    #PUBLIC FUNCTIONS#
    def create_variable(self, name, value):
        """
            Creates a variable in your game data
            Call it by:
                controller.create_variable(name,value)
        """
        if name in self.__data: #If it already exists, raise an error
            raise IndexError(f"Variable with name '{name}' already exists in Game Data")
        else: #If it doesn't exist, create it
            self.__data[name] = value
        self.__save()

    def get_variable(self, name):
        """
            Returns the value of the variable you specify if it is in Game Data
            Call it by:
                value = controller.get_variable(name)
        """
        if name in self.__data: #If the variable exists, return it
            return self.__data[name]
        else: #If the variable doesn't exist, raise an error
            raise IndexError(f"Variable with name '{name}' does not exist in Game Data")
    
    def update_variable(self, name, value):
        """
            Updates an already created variable in the Game Data
            Call it by:
                controller.update_variable(name, value)
        """
        if name in self.__data:
            self.__data[name] = value
        else:
            raise IndexError(f"Variable with name '{name}' does not exist in Game Data")
        self.__save()
    
    def delete_variable(self, name, ignore_warning =  False):
        """
            Deletes a previously created variable in the Game Data
            Call it by:
                controller.delete_variable(name)

            You can ignore our warning message by adding a second parameter and setting it to True
        """
        if not name in self.__data and not ignore_warning:
            print(f"\033[2;34;41m Variable with name '{name}' does not exist in Game Data.\nThis doesn't raise an error but it is not recommended to do this\033[0m")
        self.__data.pop(name, None)
        self.__save()
    
    def view_all_variables(self):
        print(self.__data)