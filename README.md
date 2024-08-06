# Fyle Backend Challenge

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below
3. The following commands are for linux platform. If you are using Windows, You can either use WSL or Docker. Check installation steps for docker below these.

### Installation Steps for Linux Environment:
```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

### Installation Steps Using Docker:
1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install

```
docker-compose build
```
### Reset DB

```
docker-compose run web bash reset.sh
```
### Start Server

```
docker-compose up
```
### Run Tests

```
docker-compose run web pytest -vvv -s tests/
```

### Get Coverage Report

```
docker-compose run web pytest --cov
```