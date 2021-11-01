"""

Chapter 10

files we might deal with as QA engineer


- yaml (similar to dictionaries)
- csv
-text(fixed width)
- xml
- json

opening in python:
open('C/dev/basics/data/somfile) as alias names:
    # some code to do with file
    # read line by line
    exit or close the file

with open('C/dev/basics/data/somfile) as alias names:
    # some code to do with file
    # read line by line
    # it will close the file and clean the memory


windows  C:\dev\basics\data\

linux/mac C:\\dev\\basics\\data\ - first backslash - hey linux means.second backslash - literal backslash

windows  C:/dev/basics/data/
linux/mac C:/dev/basics/data/

"""

from yaml import *

# spesific library to handle yaml file


myfile = "./../data/names.txt"


def read_file_1(filepath):
    with open(filepath) as names:
        # print(names) # returns the object of the file (reference from the memory)
        # print(names.read()) # returns body of the file
        print(names.readline())  # reads the current line
        print(names.readline())  # reads the next line
        print(names.readlines())  # creats the list from rest of lines
        print(names.name)  # return from the name of the file


def read_file_lines(filepath):
    try:
        with open(filepath) as data:
            for line in data.readlines():
                print('line value: ', line, end='')
                print("\nWoow, I have read file;")
                print(f"division for fun: {5 / 0}")
    except FileNotFoundError as err:
        print(f"Please check your filepath.\n{err}")
    except ZeroDivisionError as err:
        print(f"OOHH come on man, simple math. {err}")
    finally:
        print('read_file_lines functions comleted!')


def load_yaml(filepath):
    with open(filepath) as data:
        doc = safe_load(data)
        return doc


students_path = "../data/students.yml"

# read_file_1(myfile)
# read_file_lines(myfile)

doc = load_yaml(students_path)
web_url = doc['credentials']['url']
uname = doc['credentials']['username']
pword = doc['credentials']['password']

bird1 = doc["student1"]["calling_birds"][0]
all_birds = doc['student1']['calling_birds']

print('trying to get the url: ', web_url)
print('trying to get the username: ', uname)
print('trying to get the password: ', pword)
print('first bird in the list: ', bird1)
print('all birds in the list: ', all_birds)

print("Completed!!!!!!!!!!!!!!!!")
"""
try:
    # regular code to execute
except SpecificErrorType as aliasNameForErrorMsg:
    # way to handle if above Error happens
except SpecificErrorType as aliasNameForErrorMsg:
    # way to handle if above Error happens
except SpecificErrorType as aliasNameForErrorMsg:
    # way to handle if above Error happens    



"""
