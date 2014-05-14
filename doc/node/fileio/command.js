#!/usr/bin/node
// Perform a file listing

var exec       = require('child_process').exec;

var doCommand = function(command) {
    exec(command,  function(error, stdout) {
        if (error) {
            console.log(error)
        } 
        else {
            console.log(stdout)
        }
    });
};

doCommand('ls');
doCommand('pwd');
doCommand('echo $USER@`hostname`');
doCommand('df');
doCommand('du -s');

