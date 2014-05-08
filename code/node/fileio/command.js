#!/usr/bin/node
// Perform a file listing

var asyncblock = require('asyncblock');
var exec       = require('child_process').exec;

var doCommand = function(command) {
    asyncblock(function (flow) {
            exec(command, flow.add());
            result = flow.wait();
            console.log(result);
    });
};

doCommand('ls');
doCommand('pwd');
doCommand('echo $USER@`hostname`');
doCommand('df');
doCommand('du -s');

