# here I'll explain to pip what to do

# from setuptools import setup

# setup(name="toto", description="My first package",
#       packages=["toto"], scripts=["scripts/toto-blabla"])

from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='toto',
      description="package description",
      packages=find_packages(),
      install_requires=requirements)
