# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:12:00 2020

@author: pepro
"""
filename = r'\laurynOrnament.gcode' #your gcode file goes here
gcode = r"C:\Users\pepro\Desktop" + str(filename) #your gcode file location goes here

file = open(gcode)
code = file.readlines()
Colors = ['brown','black','white'] #what color each extruder is in your prusa slicer (extruder 1 = wood, etc.)
print(len(code))

flag = False

count = 1
for line in code:
    count +=1
    if flag:
        if line.startswith('T'):
            print(Colors[int(line[1])])
            input('press any button when done loading')
    words = line.split()
    if count == len(code):
        print('done color changing')
        break
    for command in words:
        if command == 'M600':
            flag = True
        else:
            flag = False

file.close()