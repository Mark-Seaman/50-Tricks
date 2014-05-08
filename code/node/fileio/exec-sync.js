#!/usr/bin/node
// Node.JS command execution

var execSync = require('exec-sync');   

var user = execSync('echo $USER');
console.log(user);

var user = execSync('hostname');
console.log(user);

var user = execSync('df');
console.log(user);

var user = execSync('ls');
console.log(user);
