import setuptools
setuptools.setup(
     name='EasyGameTools',  
     version='0.1.3',
     license="GPL-3.0",
     author="Arun Dutta-Plummer",
     author_email="arunjai12456@gmail.com",
     description="Makes developing games and handling data easy",
     long_description="Makes developing games and handling data easy. The controllers use the CRUD options and there is a controller that stores the data as plain text with no encryption (PlainTextGameDataController) and there is one that stores each key, value with encrpytion and a unique key (GameDataController)",
     url="https://ajtechcity.com",
     packages=setuptools.find_packages(where="src"),
     package_dir={"":"src"},
     install_requires=[
       "cryptography"
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )