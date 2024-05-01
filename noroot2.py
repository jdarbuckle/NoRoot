#!/usr/bin/env python

#absolute path to the file
FILE_PATH = '/home/jarbuckle/Documents/passwd1'

#check variables
BIN_BASH = '/bin/bash'
NOLOGIN = '/usr/sbin/nologin'

#file handle with read switch, we then use the readlines method to navigate each line
with open(FILE_PATH, 'r') as file_object:
    lines = file_object.readlines()

#empty list
newpasswd = []

#for loop using split to create a lists of list to parse through
for record in [x.split(':') for x in lines]:

'''we then check the third object, change it to an integer and check if it is userID 1000+ and if the object in the last position on the list is not the string noloin already'''
    if int(record [2]) >= 1000 and 'nologin' not in record [-1]:

'''any line that does not meet these requrements has their object in last position adjusted to
/usr/bin/nologin removing their access to log in with root privileges'''
        record[-1] = '/usr/bin/nologin\n'
#we then append the records with that change
    newpasswd.append(':'.join(record))

#and with the write switch on we take those changes and apply them to the passwd1 file.
with open(FILE_PATH, 'w') as file_object:
    file_object.writelines(newpasswd)

#this tool should adjust system user accounts to remove shell access in one executable.
