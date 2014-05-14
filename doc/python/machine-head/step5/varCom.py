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

def trigger(var):
    setValue(var, True)

def triggered(var):
    if changed(var) and var[0]:
        var[0]=False
        var[1]=False
        return True
    return False

#-----------------------------------------------------------------------------
# Application Events

# Events for bar keep
bar_keep_request        = init(False)
bar_keep_got_one        = init(False)
bar_keep_passed_bottle  = init(False) 

# Events for drinker
drinker_has_beer        = init(False)
drinker_done            = init(False)

