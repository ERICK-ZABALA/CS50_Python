#!/usr/local/bin/python

value = int(input("m: "))
#new_value = value.replace("14",'1260000000000000000').replace("1",'90000000000000000').replace('50','4500000000000000000')

if value == 1:
    value=str(value)
    new_value=value.replace('1','90000000000000000')
    print("E:",new_value)

if value == 14:
    value=str(value)
    new_value=value.replace('14','1260000000000000000')
    print("E:",new_value)

if value == 50:
    value=str(value)
    new_value=value.replace('50','4500000000000000000')
    print("E:",new_value)
