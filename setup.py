from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="mlops_jenkins_project",
    version="0.1.0",
    packages=find_packages(),
    author="Vivek Chandan",
    install_requires=requirements,
)    
