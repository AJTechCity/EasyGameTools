from distutils.core import setup, find_packages
setup(
  name = 'EasyGameTools',
  packages = ['EasyGameTools'],
  version = '0.1',
  license='GPL-3.0',
  description = 'Makes creating games and handling data much easier',
  author = 'Arun Dutta-Plummer',
  author_email = 'arunjai12456@gmail.com',
  url = 'https://ajtechcity.com',
  download_url = 'https://github.com/AJTechCity/EasyGameTools/archive/refs/tags/v0.0.1-alpha.tar.gz',
  keywords = ['Data Handling', 'Data', 'Encrypted'],
  install_requires=[
          'cryptography'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL-3.0 License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  package_dir={"":"src"},
  packages=find_packages(where="src"),
)