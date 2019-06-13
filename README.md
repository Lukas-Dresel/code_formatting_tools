# code_formatting_tools
My tools to automate simple code formatting tasks for software repos

## Usage
E.g. for a python repo:
```
find . -name '*.py' | grep -v '.git' | python lengthchecker.py 80
find . -name '*.py' | grep -v '.git' | python lengthchecker.py 120
find . -name '*.py' | grep -v '.git' | python strip_trailing_spaces.py 
```
