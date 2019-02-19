import os
import pathlib

# define the path
# provided the script is placed in downloads and would be run from downloads
currentDirectory = pathlib.Path('.')

# define the pattern
currentPattern = "VEVO*.pdf"

for currentFile in currentDirectory.glob(currentPattern):
    print(currentFile)
