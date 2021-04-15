# 2048 Game Language
### CS F363 Compiler Construction, Sem II 2020-21

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<p float="left">
  <img src="https://img.shields.io/badge/Sly-0.4-008fff.svg" height="30"/>
  <img src="https://img.shields.io/badge/python->=3.6-008fff.svg" height="30"/>
</p>


### Dependencies
```bash
pip install sly==0.4
```

### Introduction
The task is to make a parser-translator (that mean a complete syntax-directed translation scheme) for a game programming language. The game elements, its lexicon, and grammatical demands of its programming language are given. It is a 2048-game family.

 Here, variations on the original 2048 game are to be also provided for. The variations are:

- Allowing subtraction, multiplication and division in addition to the plain doubling operation at tile mergers.
- The operations:
    - **Moves**: Add/Subtract/Multiply/Divide Left/Right/Up/Down
    - **Assignment**: Assign ≪ value ≫ to ≪ x ≫,≪ y ≫
    - **Var** ≪ varname ≫ is ≪ x ≫,≪ y ≫
    - **Query**: Value in ≪ x ≫,≪ y ≫
- Remaining token types will be identifiers, numbers, and punctuation symbols ⟨,.?⟩. Com- mands must end with a full-stop. Co-ordinates must be separated by a comma, and optional whitespace.

### Assumption/Interpretations


### Handled Errors

### Instructions To Run
Running in debug mode

```bash
python test.py
```

For redirecting stderr to a file.

```bash
python test.py 2>err.txt
```

### Running with specifications

```python
import sys
from game import Board
from lexer import Lexer2048
from parser import Parser2048

board = Board(size=(4, 4))
lexer, parser = Lexer2048(), Parser2048(fmap=board.fmap)
print("Welcome to the 2048 Gaming Language, Below is the Board. Happy Coding!")

while True:
    try:
        inp = input("2048 >>>")
        command = lexer.err(inp)
        out = parser.parse(lexer.tokenize(command))
        board.eout()

    except EOFError:
        exit()

    except Exception as E:
        print(str(E))
        print("-1", file=sys.stderr)
```
