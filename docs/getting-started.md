# Getting Started

## Clone the repository

```zsh
git clone git@github.com:ByAnthony/nztunnellers.git
```

## Setting up

### Server side

```zsh
// From repository root
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Client side

```zsh
// From repository root
cd client
npm install
```

*Note: delete `node-modules` package and `package-lock.json` if necessary and re-run `npm install`.*

### Pre-commit

```zsh
// From repository root
pre-commit install
```
