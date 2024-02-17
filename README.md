# Flask boilerplate, design patterns and good practices playground

## Setup pyenv
```
pyenv local 3.11
sudo apt-get install pipx || python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry
```

## Poetry init
```
sudo apt-get install libpq-dev
poetry config virtualenvs.in-project true
poetry install --no-root
```

## Start services
```
docker compose up -d
```

## Database
```
flask db init
flask db upgrade
```
#
