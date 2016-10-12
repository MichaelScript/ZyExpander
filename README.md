# Nested Zip File Expander for Blackboard & Zybook
Zybooks stores students in a bunch of nested zips and it can be hard to work with. ZyExpander seeks to fix that problem by taking a nested zip file from Zybooks and organizing it into a better folder structure. This is pretty old, and the code isn't as nice as I'd like but it gets the job done.

```

Example of ZyBook's native class storage structure:

Lab1.zip
├── Student1_First_Last.zip
│   ├── ==> lab1a.java   
│	└── ==> lab1b.java
│  
└── Student2_First_Last.zip
    └── ==> lab1a.java
    ... 


```


#### Difficulties
 1. Nested zips are annoying because even after they're expanded they remain in the directory, not only that but having to expand nested compressed files can get tedious.
 2. The actual programs get put in outer directory rather than in a folder. They all retain the same file name and this makes differentiating between students hard.
 3. This challenge gets even more difficult when a student only turns in a portion of the assignment as it isn't easy to see who did the whole assignment.

#### Solution
We can **speed up and organize** this process using ZyExpander. No more duplicate file names or expanding nested zips, simply run ZyExpander all of the lab zip files and you're good to go! Zybooks *creates a backup* of the original lab zip file, and puts program files in a directory corresponding to the student's name. You can even specify a common output directory so you can organize students however you see fit whether it be by class, assignment, or assignment type, that way you don't have to sift through different directories for each assignment. ZyExpander speeds up your workflow and organizes your ZyBooks students.

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
