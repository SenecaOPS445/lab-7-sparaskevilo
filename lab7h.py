#!/usr/bin/env python3
# StudentID: sparaskevilo

def function1():
    print('print() in function1 on schoolName:', schoolName) # schoolName not defined yet. Will be defined in main block

def function2():
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca College' # Seneca College now the schoolName variable
print('print() in main on schoolNamel;',schoolName)
function1()

print('print() in main on schoolName:',schoolName)
function2()

print('print() in main on schoolName:',schoolName)