# ShadowFramework

![Github License](https://img.shields.io/badge/license-MIT-green)


## Description
The Shadow Framework is a python based CLI Tool designed to help in Cybersecurity and Networking Tasks. 
Components include Cisco Configuration and CTF Tools with more to come. 

## Table of contents
- [**Getting Started**](#getting-started)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgements)

## Getting Started

### Install
The Shadow Framework in built using python. For this reason it is recomended that you use the latest version of python.
We also recomend that you install the Shadow Framework in a virtual enviroment for easy use and install.
**Note: A Docker container is also provided if you would like to install in docker.**
#### Linux
```console
sudo apt update

python3.9 -m venv env
source env/Scripts/activate.bat
pip setup.py install
```
#### Windows
```console
python3.9 -m venv env
source env/bin/activate
pip setup.py install
```

#### Docker
```console
cd docker
sudo docker build .
```

####Usage
```console
shadow [OPTIONS] COMMAND [ARGS]
```
Runing shadow will give you a list a runnable commands. 

## Contributing
If you would like to contribute to the Shadow Framework please visit the [CONTRIBUTING](CONTRIBUTING.md) page.

## License
This project is licensed under the [MIT License](LICENSE) 

## Acknowledgments
