import setuptools
setuptools.setup(
     name='EasyGameTools',  
     version='0.1.2',
     license="GPL-3.0",
     author="Arun Dutta-Plummer",
     author_email="arunjai12456@gmail.com",
     description="Makes developing games and handling data easy",
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