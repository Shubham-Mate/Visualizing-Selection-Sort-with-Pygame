# Visualizing Selection Sort with Pygame

## Demo
![Selection Sort](https://i.makeagif.com/media/2-28-2021/hyOAD7.gif)

[Youtube Video](https://www.youtube.com/watch?v=i-w4dDObyNY "Youtube Video")

## How to run
Run the GUI.py file

Press 'S' to sort the list

Press 'R' to generate a new list

It is recommended that the amount of numbers generated should not be more than 1000

## Commits
#### Initial Commit
Added file main.py

#### Second Commit
Added file sort.py

Changes:
- File Name Changed from main.py to sort.py
- Changed to an Object Oriented approach

#### Third Commit
Added file GUI.py

Changes:
- Added GUI with Tkinter at the beginning to take input from the User for range of number generation and amount of numbers to be generated
- Added Ability to Pause/Continue the Sort

#### Fourth Commit
Made changes to sort.py

Changes:
- Implemented proper selection sort. Previous version had an algorithm similiar to selection sort but not selection sort
- Selection sort can be seen with different coloring
- created a function which draws the bars for the values instead of directly drawing them in the mainloop

- Added Comments

#### Fifth Commit
Changes in sort.py and GUI.py

Changes:
- Changed the GUI to only take amount of numbers as input
- Instead of generating a random list with the input, a list is generated from the input given and is shuffled
- Made it so that the input in GUI can only be an integer
- Fixed issue where the highest value is not fitted properly to the window height
