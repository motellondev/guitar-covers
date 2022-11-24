#!/bin/bash

# MAIN APP

if [ -d ./main/management/__pycache__ ];
then
rm -r ./main/management/__pycache__
fi

if [ -d ./main/__pycache__ ];
then
rm -r ./main/__pycache__
fi

if [ -d ./main/migrations/__pycache__ ];
then
rm -r ./main/migrations/__pycache__
fi

if [ -d ./main/management/commands/__pycache__ ];
then
rm -r ./main/management/commands/__pycache__
fi

if [ -f ./main/migrations/0001_initial.py ];
then
rm ./main/migrations/0001_initial.py
fi



# PROJECT FOLDER

if [ -d ./guitarcovers/__pycache__ ];
then
rm -r ./guitarcovers/__pycache__
fi


if [ -d ./media ];
then
rm -r ./media
fi


if [ -f ./db.sqlite3 ];
then
rm -r ./db.sqlite3
fi


