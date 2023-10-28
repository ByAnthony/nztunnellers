# New Zealand Tunnellers Web App: nztunnellers

[The New Zealand Tunnellers Web App](https://www.nztunnellers.com) is dedicated to a special military unit who fought in France during the First World War (1914-1918): the *New Zealand Tunnelling Company*. This company was formed at a time where the British Army struggled in their fights against the German miners beneath the no man's land. The Web App tells the [original story](https://www.nztunnellers.com/#history) of this special unit and shares the [men's war experience](https://www.nztunnellers.com/tunnellers/).

## Table of Contents

- [New Zealand Tunnellers Web App: nztunnellers](#new-zealand-tunnellers-web-app-nztunnellers)
  - [Table of Contents](#table-of-contents)
  - [Before Starting](#before-starting)
    - [Homebrew](#homebrew)
    - [pyenv](#pyenv)
    - [MySQL](#mysql)
  - [Getting Started](#getting-started)
    - [Clone the repository](#clone-the-repository)
    - [Setting up](#setting-up)
      - [Server side](#server-side)
      - [Client side](#client-side)
      - [Pre-commit](#pre-commit)
  - [Running the Web App](#running-the-web-app)

## Before Starting

Make sure you have the following installed:

### Homebrew

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
```

*Source: [Homebrew website](https://brew.sh/)*

### pyenv

```zsh
brew install pyenv
pyenv install 3.9.7
```

*Source: [pyenv GitHub repository](https://github.com/pyenv/pyenv)*

### MySQL

```zsh
brew install mysql
```

## Getting Started

### Clone the repository

```zsh
git clone git@github.com:ByAnthony/nztunnellers.git
```

### Setting up

#### Server side

```zsh
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

#### Client side

```zsh
cd client
npm install
```

*Note: delete `node-modules` package and `package-lock.json` if necessary and re-run `npm install`.*

#### Pre-commit

```zsh
pre-commit install
```

## Running the Web App

```zsh
// From repository root
// Open tab 1 in console
make run-server
// Open tab 2 in console
make run-client
```
