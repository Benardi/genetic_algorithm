[![Build Status](https://travis-ci.com/Benardi/genetic_algorithm.svg?branch=master)](https://travis-ci.com/Benardi/genetic_algorithm)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Genetic Algorithm

Genetic algorithm implementation in Python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To make use of this project you need both python3 and pip3.
Both are readily available in packages: 

```
sudo apt update
sudo apt install python3
sudo apt install python3-pip

```
**Optionally**: venv

### Installing

Clone and enter the directory using cd

```
git clone https://github.com/Benardi/genetic_algorithm

cd ToPresente
```

Use venv to keep dependencies tidy, but you may opt not to use it.
Create a new directory inside the project directory where will keep the dependencies as 'venv'.

```
python3 -m venv ./venv
```

Source the venv to activate it.

```
source venv/bin/activate
```

Use pip to install the requirements

```
pip3 install -r requirements.txt
```



# Running the tests

To execute tests simply run 

```
python3 setup.py test
``` 

or 

```
nosetests tests
``` 


## Authors

* **Benardi Nunes** - *Initial work* - [Benardi](https://github.com/Benardi)

See also the list of [contributors](https://github.com/Benardi/genetic_algorithm/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Kenneth Reitz** - Python project [example repo](https://github.com/kennethreitz/samplemod)
