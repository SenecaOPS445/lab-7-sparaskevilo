#!/usr/bin/env python3
# Student ID: sparaskevilo

def function1():
    # Object a in function1 is unrelated to object a in function2
    a = 'object_function1'
    print('print() call in functin 1 on a:',a)

def function2():
    # Object a in function2 is unrelation to object a in function1
    a = 'function2_object2'
    print('print() call in function2 on a:',a)

# You cant get the value of a in function1 or function2

a = 'object_in_main'

print('print() call in main on a:',a) # This will call the a object storing object_in_main
function1() # This will return the print statement and value of a defined in function1

print('print() call in main on a:',a) # This will call the a object storing object_in_main
function2() # This will return the print statement and value of a defined in function2

print('print() call in main on a:',a) # This will call the a object storing object_in_main
