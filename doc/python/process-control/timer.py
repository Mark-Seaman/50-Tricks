from threading import Timer


# Create a timed event
def schedule(event):
    t = Timer(2, event)
    t.start()


# Do a one time event
def onetime():
    print "onetime"

# Recurring event (exit after 4)
def recurring():
    global x
    x+=1
    print 'recurring',x
    if x<3:
        schedule (recurring)

x = 0
schedule (onetime)
schedule (recurring)

print 'Done with app'
