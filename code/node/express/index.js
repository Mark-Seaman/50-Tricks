var express = require('express');
var app = express();

app.get('/name/*:name?/edit', function(req, res, next) {
    var name = req.params.name;
    name = name ? name.toLowerCase() : '';
    if ('mark' === name) {
        res.send('Edit away, '+name);
    }
    res.send('Permission denied, '+name);
    //next();
});

app.get('/name/*:name?', function(req, res, next) {
    var name = req.params.name;
    name = name ? name.toLowerCase() : '';
    if ('mark' === name) {
        res.send('Welcome, '+name);
    }
    res.send('Bad name, '+name);
    //next();
});

app.get('/:name', function(req, res, next) {
    var name = req.params.name;
    name = name ? name.toLowerCase() : '';
    if ('mark' === name) {
        res.send('Welcome, '+name);
    }
    res.send('Bad name, '+name);
    //next();
});


app.get('/', function(req, res){
    res.send('<h1>What is your name?</h1>'+
             '<a href="/Mark">My name is Mark</a><br/>'+
             '<a href="/Biff">My name is Biff</a><br/>'+
             '<a href="/Biff/Dude">Unmatched url</a><br/>'+
             '<a href="/name/Mark">My name is Mark</a><br/>'+
             '<a href="/name/Mark/edit">Edit as Mark</a><br/>'+
             '<a href="/name/mystery/name/edit">You cannot edit</a>');
});

app.get('/*?', function(req, res){
    res.send('You are not permitted to be here!');
});


var port = 8080;
app.listen(port);
console.log('Listening on port ' + port);
