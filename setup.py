# this code will automatically install requirements.txt when we 
# run pip .. -r requirements.txt
from setuptools import find_packages , setup


HYPHEN_DOT_E = '-e .'
# used to connect the requirements file to setup.py

def get_requirements(filename : str) -> list:
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [line.replace('\n' , '') for line in requirements]


    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
    
    return requirements
    


setup(
    name='mlproject',
    version='0.0.1',
    author_email='dhruv999ddrr@gmail.com',
    author='Dhruv Sharma',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)