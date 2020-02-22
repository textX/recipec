# RECIPEC

recipec, a recipe DSL + compiler in << 1000 LOC.
(Example for textx grammar + code generator)


## Features

Allows to define recipes. To plan days with recipes and compute a list of
ingredients + generate MD file with all the info.


## File types

See tests/demos

- recipes: use ingredients with units
- ingredients: define units (and aliases)
- plans: group recipes, are used to generate documents
- config: language dependent adaptations


## Test

    python -m venv venv
    source venv/bin/activate
    pip install -e .[test]
    pytest tests


## Install

    python setup.py install


## Usage

    cd tests/demos
    textx generate --target md bananentag.plan --overwrite
 
(see `textx --help`)
