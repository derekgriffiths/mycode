#!/usr/bin/env python3

#imports shutil and os modules
import shutil
import os

# sets my working directory
os.chdir('/home/student/mycode/')

# moves the raynor file to the ceph_storage directory
shutil.move('raynor.obj', 'ceph_storage/')

# asks the user to chose a new name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')


# Renaming the kerrigan file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



