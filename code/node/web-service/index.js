var express = require('express');
var app = express();
var store = require('./store')


// Get the variable
app.get('/get/:var?', function(req,res){
    name = req.params.var
    store.recall('test/'+name,function(key,value){
        //console.log("get var=" + name + ", val="+value);
        res.send('Get '+name+' = '+value);
    });
});


// Set the variable
app.get('/set/:var?/:val?', function(req,res){
    name = req.params.var
    val  = req.params.val
    store.save('test/'+name,val,function(key,value){
        //console.log("set var=" + name + ", val="+val); 
        res.redirect('/get/'+name);
    });
});


// Test page
app.get('/', function(req, res){
    res.send('<h1>Test setting and getting variables</h1>'+
             '<a href="/get/abc">Get ABC</a><br/>'+
             '<a href="/set/abc/hello">Set ABC = hello</a><br/>'+
             '<a href="/set/abc/goodbye">Set ABC = goodbye</a><br/>'+
             '<a href="/set/abc/bad thing">Set ABC = bad thing</a><br/>'+
             '<a href="/bad">Bad link</a>');
});


// Missing page
app.get('/*?', function(req, res){
    res.send('You are not permitted to be here!');
});


var port = 8080;
app.listen(port);
console.log('Listening on port ' + port);
