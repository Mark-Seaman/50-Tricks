console.log ("Traffic Light");

var print = function(s) { console.log(s) }

//-----------------------------------------------------------------------------
// State machine 

// Handlers for entering a new state
var ongreen  = function () { console.log('Green')  }
var onyellow = function () { console.log('Yellow') }
var onred    = function () { console.log('Red')    }

// State names
var green  = 'green'
var yellow = 'yellow'
var red    = 'red'

// Event names
var GREEN  = 'GREEN'
var YELLOW = 'YELLOW'
var RED    = 'RED'

// State machine definition
var state  = green
var states = { green:  [ ongreen,  { YELLOW: yellow } ], 
               yellow: [ onyellow, { RED:    red    } ], 
               red:    [ onred,    { GREEN:  green  } ] }

// State machine code
var nextState = function(event) {
    trans = states[state][1]
    if (! trans.hasOwnProperty(event)) { print('Not allowed: '+event); return }
    state = states[state][1][event]
    states[state][0]()
}    

//-----------------------------------------------------------------------------
// Traffic light app

// Test states with illegal transition attempts
 var events = [ YELLOW, RED, GREEN, YELLOW,  GREEN, RED, GREEN, RED, YELLOW, RED ];


print ("Wait for 5 seconds...")
setTimeout(function() {

    // Automatically advance on a timer
    var count = 0;
    setInterval(function() {i = count++ % events.length;  nextState(events[i])}, 1000);

}, 5000);
