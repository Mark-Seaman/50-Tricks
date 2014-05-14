#!/bin/bash
# Perform a file listing

node <<EOF

var exec       = require('child_process').exec;
 
console.log('List of files')

exec('ls $HOME',  function(error, stdout) {
   console.log(stdout)
});

EOF
