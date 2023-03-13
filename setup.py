from typing import List
from setuptools import find_packages, setup


def get_requirements(file_path:str) -> List[str]:
    #   this function will return a list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

setup(
    name='dasier',
    version='0.0.1',
    author='latioms',
    author_email='latioms@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
