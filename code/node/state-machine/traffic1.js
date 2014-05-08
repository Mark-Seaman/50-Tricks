console.log ("Traffic Light");

//-----------------------------------------------------------------------------
// State machine 

var ongreen  = function () { console.log('ON Green')  };
var onyellow = function () { console.log('ON Yellow') };
var onred    = function () { console.log('ON Red')    };

var state  = 'green'
var states = { 'green':  [ ongreen,  { 'yellow': 'yellow' } ], 
               'yellow': [ onyellow, { 'red':    'red'    } ], 
               'red':    [ onred,    { 'green':  'green'  } ] };

var nextState = function(event) {
    trans = states[state][1];
    if (! trans.hasOwnProperty(event)) return;
    state = states[state][1][event];
    states[state][0]();
}    

//-----------------------------------------------------------------------------
// Print function

var print = function(s) {
    console.log(s)
}

var printState = function(obj) {
    for(var i in obj)  {
        print(i);
        for (var j in obj[i][1]) 
            print('   '+j);
    }
}

var printEvents = function(list) {
    for(var i in list)  print(list[i]);
}

//printState (states);

//-----------------------------------------------------------------------------
// Traffic light app

// Test states with illegal transition attempts
var events = [ 'yellow', 'red', 'green', 'yellow',  'green', 'red', 'green', 'red', 'yellow', 'red', ];
//printEvents(events);

if (states.hasOwnProperty('green'))
    print ('Has green property');
else
    print ('No green property');

for(var i in events)  nextState(events[i]);

