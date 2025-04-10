from setuptools import find_packages, setup
from typing import List


HPYE_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    """
    this function will return the list of requirements

    """
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HPYE_E_DOT in requirements:
            requirements.remove(HPYE_E_DOT)
    return requirements

        

setup(
name='mlproject',
verision='0.0.1',
author='santhankumar',
author_email='kumarsanthan32@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')

)
