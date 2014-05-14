var express = require('express');
var app     = express();
var http    = require('http');
var server  = http.createServer(app);

app.set('view engine', 'jade');
app.set('view options', { layout: true });
app.set('views', __dirname);

app.use(express.bodyParser()); // Automatically parses form data

app.get('/', function(req, res){
    res.render('index',{});    
});

app.post('/', function(req, res){
    res.send("<h1>"+req.body.command+"</h1>");
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
