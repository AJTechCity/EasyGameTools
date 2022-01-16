# EasyGameTools

# Easy Game Tools

How to install:

    >>>pip install --upgrade EasyGameTools
    

# Game Data

How to import into a program:

    >>> import GameData

## **PlainTextGameDataController() class**

 - ## **Importing:**
   
       >>> from GameData import PlainTextGameDataController
   
  - ## **Initialisation:**
   
   > You can pass the file_location parameter even if there isn't a file yet, the class will create it for you

***Function Name:***
-`PlainTextGameDataController()`
   
   ***Parameters:***
    - file_location (string) - Location of the file without the extension name
   
   ***Usage:***
   
       >>> controller = PlainTextGameDataController("file")
      

- ## **Creating/Adding a variable:**
>This function allows a variable with a value to be added to the data file
>An `IndexError` is raised if there is a value with this name already in the data file

***Function Names:***
-`add_variable()`
-`create_variable()`

***Parameters:***
-name (string) - The name of the variable to be created
-value (string) - The value to be stored under the variable name passed

***Usage:***

    >>> controller.add_variable("Test Name", "Test Value")
    
   or 
   
    >>> controller.create_variable("Test Name", "Test Value")
   
- ## **Reading/Getting a variable:**
>This function gets the value of a variable in the data file and returns it as a string
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`get_variable()`

***Parameters:***
-name (string) - The name of the variable to be read

***Usage:***

    >>> controller.get_variable("Test Name")
    
- ## **Updating a variable:**
>This function allows a variable to be updated in the data file
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`update_variable()`

***Parameters:***
-name (string) - The name of the variable to be updated
-value (string) - The value to be updated on the passed variable name

***Usage:***

    >>> controller.update_variable("Test Name", "Test Value Changed")

- ## **Deleting a variable:**
>This function allows a variable to be deleted in the data file
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`delete_variable()`

***Parameters:***
-name (string) - The name of the variable to be deleted

***Usage:***

    >>> controller.delete_variable("Test Name")


## **GameDataController() class**
>A class used to store data as JSON in a custom file with encryption to protect the data
>DO NOT DELETE THE `egdgcek.ajtck3y` FILE AS THIS CONTAINS THE KEY AND DATA WILL BE UNRECOVERABLE AFTER THIS

 - ## **Importing:**
   
       >>> from GameData import PlainTextGameDataController
   
  - ## **Initialisation:**
   
   > You can pass the file_location parameter even if there isn't a file yet, the class will create it for you

***Function Name:***
-`PlainTextGameDataController()`
   
   ***Parameters:***
    - file_location (string) - Location of the file without the extension name
   
   ***Usage:***
   
       >>> controller = PlainTextGameDataController("file")
      

- ## **Creating/Adding a variable:**
>This function allows a variable with a value to be added to the data file
>An `IndexError` is raised if there is a value with this name already in the data file

***Function Names:***
-`add_variable()`
-`create_variable()`

***Parameters:***
-name (string) - The name of the variable to be created
-value (string) - The value to be stored under the variable name passed

***Usage:***

    >>> controller.add_variable("Test Name", "Test Value")
    
   or 
   
    >>> controller.create_variable("Test Name", "Test Value")
   
- ## **Reading/Getting a variable:**
>This function gets the value of a variable in the data file and returns it as a string
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`get_variable()`

***Parameters:***
-name (string) - The name of the variable to be read

***Usage:***

    >>> controller.get_variable("Test Name")
    
- ## **Updating a variable:**
>This function allows a variable to be updated in the data file
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`update_variable()`

***Parameters:***
-name (string) - The name of the variable to be updated
-value (string) - The value to be updated on the passed variable name

***Usage:***

    >>> controller.update_variable("Test Name", "Test Value Changed")

- ## **Deleting a variable:**
>This function allows a variable to be deleted in the data file
>An `IndexError` is raised if there is not a value with the passed name in the data file

***Function Names:***
-`delete_variable()`

***Parameters:***
-name (string) - The name of the variable to be deleted

***Usage:***

    >>> controller.delete_variable("Test Name")