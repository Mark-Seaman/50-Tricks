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

#-----------------------------------------------------------------------------
# Application Variables

bottles_on_wall = init(100)
has_beer        = init(True)

#-----------------------------------------------------------------------------
# Variable usage

def bar_keep():
    bottles = getValue(bottles_on_wall)
    if getValue(bottles_on_wall)>0:
        print 'Take one down, pass it around'
        bottles -= 1
        print '%d bottles on wall'% bottles
        setValue(bottles_on_wall, bottles)
        setValue(has_beer,True)

def drinker():
    if getValue(has_beer):
        print 'Drink beer'
        setValue(has_beer,False)


for i in range(10):
    bar_keep()
    drinker()


