#!/usr/bin/env python3
#Student ID: sparaskevilo

def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName # SSDP becomes global replacing Seneca after function2 is called in main block
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

schoolName = 'Seneca'

print('print() in main on schoolName:',schoolName) # Will print Seneca
function1() # Will print SICT
print('print() in main on schoolName:',schoolName) # Will print SICT
function2() # Will print SSDO
print('print() in main on schoolName:',schoolName) # Will print SSDO