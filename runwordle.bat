@echo off
if exist wordle.py goto openwordle
if not exist wordle.py goto wordlenotexsist

:openwordle
py wordle.py
pause


:wordlenotexsist
echo wordle.py does not exsist
pause