#!/usr/bin/python

#------------------------------------------------------------------
# Data
#------------------------------------------------------------------

south = 'south'
north = 'north'
west  = 'west'
east  = 'east'
up    = 'up'
down  = 'down'

opposite = { up:down, down:up, north:south, south:north, east:west, west:east }

places = {}

initial_places = { "boat" : 
            { "name": 'the boat',
              "description":  
 '''
 You wake up on a boat in the middle of an ocean.  Off in the distance you can see land
 to the west.
 '''},
}


initial_places = { "void" : 
                   {
                   "name": 'the void',
                   "description": 'In the beginning there was the darkness of the void',
                   },
                 }

initial_location = 'boat'

location = 'boat'

connection = { }

def create_all_places():
    create ('boat')
    create ('forrest')
    create ('beach')
    create ('castle')
    connect('boat','beach',west)
    connect('forrest','beach',south)
    add_descriptions()

def add_connection(place1,place2,direction):
    if not connection.has_key(place1): connection[place1]={}
    existing = connection[place1]
    existing[direction] = place2
    connection[place1][direction] = place2

def connect (place1, place2, direction):
    add_connection(place1,place2,direction)
    add_connection(place2,place1,opposite[direction])
    print connection

def describe (place, description):
    places[place]["description"] = description

def add_descriptions():
    describe ("boat",'''
     You wake up on a boat in the middle of an ocean.  Off in the distance you can see land
     to the west.
     ''')

    describe ("forrest",'''
     The forrest is very old.  It is dark and creepy in here.  The trees are very dense and
     you feel that everything is moving and crawling.  You experience a sudden revulsion
     and begin shuttering.
    ''')

    describe ('beach', '''
     You are on a pleasant beach.  The day is hot.  You feel very thristy.
    ''')


#------------------------------------------------------------------
# Functions
#------------------------------------------------------------------

def play_game():
    history = []
    places = start_game()
    read_moves(places, 'moves.txt')
    end_game(places)

#------------------------------------------------------------------
# Start 

def start_game():
    places = read_game()
    create_all_places ()
    list_places()
    show_location()

def read_game():
    places = {}
    from game import places
    if (places=={}):
        places = initial_places
    return places

#------------------------------------------------------------------
# Command loop

def read_moves(places, filename):
    #for move in open(filename).readlines():
    #    places = make_a_move(places,move)
    go (west)
    go (north)
    go (south)
    go (east)

def do_command(places,command):
    c = command.split ('"')
    if (len(c)>1 and c[0]=='create '):
        places = create(places,c[1])
    else:
        if (len(c)>0 and c[0]=='list\n'): 
            list_places(places)
        else:
            print 'bad command:', '.', c, '.'
    return places

def make_a_move(places, command):
   # history += [ input ] 
    places = do_command(places,command)
    #print "Last command: ", history[:-1]
    return places

def go(direction=west):
    global location
    here = location
    if (connection[here].has_key(direction)):
        here = connection[here][direction]
    else:
        print "You can't go", direction
    location = here
    show_location()

def create (name):
    places [name] = { 'name': name, 'description': 'It is dark here' }

def list_places():
    print 'This world contains these places: ',
    print ', '.join (places.keys())

def show_location():
    print 'You are in the '+location+'.'
    print places[location]["description"]

#------------------------------------------------------------------
# End

def end_game(places):
    print 'You are now leaving this world.  Everthing fades to black'
    write_game(places)

def write_game(places):
    f = open('game.py','w')
    f.write('places = ')
    f.write(str(places)+"\n")

#------------------------------------------------------------------
# Play

play_game()
