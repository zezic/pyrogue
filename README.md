![PyRogue](https://raw.github.com/zezic/pyrogue/master/logo.svg?sanitize=true)

PyRogue is a rogue-like game made to learn Python with a team of beginner programmers.

## Prerequisites

You will need at least Python 3.6 and [Pipenv](https://docs.pipenv.org/en/latest/) installed in your system to run PyRogue.

## Clone, Prepare & Run

```bash
git clone git@github.com:zezic/pyrogue.git
cd pyrogue
pipenv install
pipenv run uvicorn --reload app:app
```

After that you should be able to navigate to http://localhost:8000 and see an empty dungeon map. Walk with WASD or arrow keys.
