from setuptools import find_packages,setup
from typing import List


E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this will install the requirements.txt
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        
        if E_DOT in requirements:
            requirements=requirements.remove(E_DOT)
        return requirements
        
    
    
    

setup(
name='Student-Performance-Indicator',
version='0.0.1',
author='Sidharth',
author_email='siniya2003@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)