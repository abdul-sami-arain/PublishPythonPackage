# Steps to publish Python package on PyPl.org: #
* Make a directory(folder) for package setup and other files (ie. package2) <br/>
* Make another folder in your recent created directory with the name of your package (ie. StatisticVibes) <br/>
* Make files of license.txt , readme.txt and setup.py within package folder (parent folder) <br/>
* Make file named <yourfileName>.py within package folder (child folder / StatisticVibes) <br/>
* Write your whole code of library in <yourfileName>.py file <br/>
* In setup.py write the below code <> <br/>
```
from setuptools import setup

setup (name="StatisticVibes",
version="0.1",
description="this is a package",
long_description="this is a very very long description",
author = "Abdul Sami",
packages = ["StatisticVibes"],
install_packages = []
)
```
* In the package folder install the following using cmd:<br/>
``` 
pip install wheel 
``` 
``` 
python setup.py bdist_wheel 
``` 
``` 
python setup.py sdist bdist_wheel 
``` 
* After this there will be two folders automatically created in the package folder. <br/>
* After every change in the python file must run the following command: <br/>
``` 
python setup.py sdist bdist_wheel 
``` 
* Setup an account on  https://pypi.org/
* For publishing the package on pypi run the following command
```
pip install twine
```
```
twine upload dist/*
```
Then enter username and password of pypi account
* Package has been uploaded

