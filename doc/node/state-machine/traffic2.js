console.log ("Traffic Light");

var print = function(s) { console.log(s) }

//-----------------------------------------------------------------------------
// State machine 

var ongreen  = function () { console.log('Green')  };
var onyellow = function () { console.log('Yellow') };
var onred    = function () { console.log('Red')    };

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
// Traffic light app

// Test states with illegal transition attempts
var events = [ 'yellow', 'red', 'green', 
               'yellow',  'green', 'red', 
               'green', 'red', 'yellow', 
               'red' ];

// Automatically advance on a timer
var count = 0;
setInterval(function() { 
    i = count++ % events.length;
    print (i);
    nextState(events[i])
}, 1000);