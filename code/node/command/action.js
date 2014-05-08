#!/usr/bin/node
// Perform a file listing

var exec       = require('child_process').exec;

// Function to execute any command and apply an action on its output
var doCommand = function(command, action) {
    exec(command,  function(error, stdout) {
        if (error) {
            console.log(error)
        } 
        else {
            if (action) action(stdout)
        }
    });
};

// Call commands with different actions
doCommand('ls', function(stdout) {} );
doCommand('pwd');
doCommand('echo $USER@`hostname`', function(stdout) {console.log(stdout)} );
doCommand('df');
doCommand('du -s',function(stdout) {console.log(stdout)});

