from setuptools import find_packages, setup
from typing import List

MINUS_E_DOT = '-e .'
def get_requirements(filepath) -> List[str]:
    require=[]
    with open(filepath) as f:
        require = f.readlines()
        require = [req.replace("\n", "") for req in require]
        if MINUS_E_DOT in require:
            require.remove(MINUS_E_DOT)
    return require

setup(
    name='mlcode',
    version='0.1.0',
    author='Harry',
    author_email='palharihar1507@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)