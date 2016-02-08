# Zybooks-Scripts
Zybooks stores students in a bunch of nested zips and it can be hard to work with. ZyExpander seeks to fix that problem by taking a nested zip file from Zybooks and organizing it into a better folder structure.

# Usage
## Basic Usage
Simply run the file with your native python interpreter and supply a list of zipfiles to expand. Optionally you can specify an output directory to put the files into. By default ZyExpander will not overwrite any current directories that exist, but if you specify a directory that does not exist it will create it.

```

usage: Python ZyExpander.py [-h] [-o O] zips [zips ...]

Takes input zipfiles and expands them.

positional arguments:
  zips        zipfiles you want to process

optional arguments:
  -h, --help  show this help message and exit
  -o O        option to specify an output directory

```
## Installing as a command line tool
```
to do...
```