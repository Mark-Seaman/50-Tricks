#!/usr/bin/python
# Variable communication trick

#-----------------------------------------------------------------------------
# Variable handling

def init(value):
    return [value,value]

def setValue(var, value):
    var[0] = value

def getValue(var):
    return var[0]

def changed(var):
    if var[0]!=var[1]:
        var[1]=var[0]
        return True
    return False
