from setuptools import find_packages,setup
from typing import List

def get_requirement(file: str)-> List[str]:
    requirement=[]
    with open(file) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.strip() for req in requirement]

    if '-e .' in requirement:
        requirement.remove('-e .')
    return requirement


setup(
    name= "mlproject",
    version= '0.0.1',
    author= "Sonal",
    author_email= "sonalkuka14@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)