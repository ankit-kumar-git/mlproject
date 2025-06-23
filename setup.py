# This file helps to build my complete ml project as package which can later be deployed on PyPi and can be used in other projects as well.

from setuptools import find_packages,setup
from typing import List



HYPHEN_E_DOT='-e .'  # this is added in requirements.txt so that it could automatically connect with setup.py but should not come as package. Therefore we ignore here


# This function will basically take file path and return a list(list of modules/packages in our case from requirements.txt file)
def get_requirements(file_path:str)->List[str]:
	requirements=[]
	with open(file_path) as file_obj:
		requirements=file_obj.readlines()
		requirements=[req.replace("\n","") for req in requirements] #to replace \n with space which got read by readlines()

		if HYPHEN_E_DOT in requirements:
			requirements.remove(HYPHEN_E_DOT)

	return requirements


setup(
name='mlproject',
version='0.0.1',
author='Ankit',
author_email='mail.ankitkumar14@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)