
from distutils.core import setup
setup(
  name = 'EasyGameTools',         # How you named your package folder (MyLib)
  packages = ['EasyGameTools'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GPL-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Makes creating games and handling data much easier',   # Give a short description about your library
  author = 'Arun Dutta-Plummer',                   # Type in your name
  author_email = 'arunjai12456@gmail.com',      # Type in your E-Mail
  url = 'https://ajtechcity.com',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AJTechCity/EasyGameTools/archive/refs/tags/v0.0.1-alpha.tar.gz',    # I explain this later on
  keywords = ['Data Handling', 'Data', 'Encrypted'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cryptography'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL-3.0 License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)