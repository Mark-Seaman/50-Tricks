var express = require('express');
var http    = require('http');
var app     = express();
var server  = http.createServer(app);
var exec    = require('child_process').exec;

app.set('view engine', 'jade');
app.set('view options', { layout: false });
app.set('views', __dirname+'/views');

app.use(express.bodyParser()); // Automatically parses form data


// Handle GET
app.get('/', function(req, res){
    res.render('command',{command: 'No command', results: 'No results'});    
});

// Handle POST
app.post('/', function(req, res){
    command = req.body.command;
    exec(command, function(error, stdout) {
        res.render('command',{command: command, results: stdout});    
    });
});


// Static files
app.get('/views/*?:file?', function(req, res){
    file = req.params.file;
    res.sendfile ('views/'+file);
});


var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
