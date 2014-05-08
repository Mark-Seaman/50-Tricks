#!/bin/bash
# Perform a file listing

node <<EOF

files = 'None'

console.log('Start');

var asyncblock = require('asyncblock');
var exec       = require('child_process').exec;

asyncblock(function (flow) {
    exec('ls', flow.add());
    files = flow.wait();
    console.log(files);    // There'll be trailing \n in the output
    console.log('Done');
});

EOF
