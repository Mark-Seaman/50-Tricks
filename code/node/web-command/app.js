// System requirements
var express    = require('express');
var app        = express();
var http       = require('http');
var server     = http.createServer(app);
var exec       = require('child_process').exec;

// Setup environment
app.set('view engine', 'jade');
app.set('view options', { layout: true });
app.set('views', __dirname);

app.use(express.bodyParser()); // Automatically parses form data


// Handle GET
app.get('/', function(req, res){
    res.render('index',{command: 'No command', results: 'No results'});    
});

// Handle POST
app.post('/', function(req, res){
    command = req.body.command;
    p = exec(command, function(error, stdout) {
        res.render('index',{command: command, results: stdout});    
    });
    p.stdin.write("hello jack");
    p.stdin.end();
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
