# Flask boilerplate, design patterns and good practices playground

# Debian/Ubuntu fresh install
## Python build  requirements
```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
## Setup pyenv
```
curl https://pyenv.run | bash
sudo apt-get install zlib1g-dev
pyenv install 3.11
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
