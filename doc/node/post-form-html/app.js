var express = require('express');
var app     = express();
var http    = require('http');
var server  = http.createServer(app);

app.use(express.bodyParser()); // Automatically parses form data

app.get('/', function(req, res){
    res.sendfile('index.html');
});

app.post('/', function(req, res){
    res.send("<h1>"+req.body.user+"</h1>");
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
