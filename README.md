# Habit tracker app
## by Henny Purwadi

- created with python39
- database with sqlite3
- simple main loop for Main Page

## Features
> Two period to choose : Daily or Weekly.
> User can create new, edit, delete, or analyse history.

## License
Free for personal use. 
Please put my name in Credits.

## Installation
pip install -i https://test.pypi.org/simple/ habit-tracker12345

## Link(pypi)
https://test.pypi.org/project/habit-tracker12345/

## Link(github)
https://github.com/hennypurwadi/habit_tracker12345

## To test, from command prompt type
python -m pytest test_habit_tracker12345.py

## How To Use
In the beginning there is one question appear: USE PREDEFINED HABITS? Y/N :  
User is free to choose between start from scratch or usepredefined habits as examples.
User can choose between daily or weekly habits.
If user checkoff the task before the due date, Streak will be added by 1, as well as Max_Streak.
Streak will be increasing if user checkoff the task within period between Start_Date and Due_Date.
If user didn't checkoff within period, Streak will be reset to zero, but Max_Streak still remain the same, and Break will be added by 1.
If Streak > Max_Streak, then Max_Streak will be changed become = Streak.
User can 

