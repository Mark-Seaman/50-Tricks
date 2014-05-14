#!/usr/bin/python
# Variable communication trick

from varCom  import *
from states  import *
from drinker import *
from barkeep import *

#-----------------------------------------------------------------------------
# Run State machines

for i in range(20):
    print i
    drinker_run()
    bar_keep_run()
    if i==3: trigger(drinker_has_beer)

