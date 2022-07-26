from setuptools import setup, find_packages
from typing import List


# declaring variables for setup
project_name = "insurance-premium-predictor"
version = "0.0.1"
author = "Vyankatesh Bhimrathi"
description = "The aim of this project is to predict premium of insurance."
packages = ["insurance"]
requirement_file_name = 'requirements.txt'

def get_requirements_list()->List[str]: # List[str] it shows what the function returns when it is triggered 
    """
    This function is going to return list which contain name of libraries mentioned 
    in the requirements.txt file
    """
    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines()


setup(
name = project_name,
version = version,
author = author,
description = description,
packages = find_packages(),
install_requires = get_requirements_list(), # to install external packages like sklearn, pandas etc
)

# find packages will find all local packages(folder) whereever there __init__ file and try to install
# -e . is also do the same thing as find packages function if you use this method we must need setup.py file