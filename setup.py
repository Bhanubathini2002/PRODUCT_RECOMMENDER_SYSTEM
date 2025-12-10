from setuptools import setup,find_packages


with open("requirements.txt") as f:
    requirements= f.read().splitlines()

setup(
    name= "Flipkart recommenter",
    version = "0.1",
    author= "BHANUPRAKASH",
    packages= find_packages(),
    install_requires = requirements,
)
