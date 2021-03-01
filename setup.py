from setuptools import find_packages
from setuptools import setup

dependencies = [
    "Click",
    "netmiko",
    "pytest"

]

setup(
    name="ShadowFramework",
    version='1.0',
    description="Python CLI to act as a toolkit of cybersecurity and networking professionals.", 
    author="Nicolas Janis",
    packages=find_packages(),
    install_requires=dependencies, 
    entry_points={"console_scripts": ["shadow=shadow.__main__:shadow"]}
)