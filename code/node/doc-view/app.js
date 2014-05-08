// System requirements
var express    = require('express');
var app        = express();
var http       = require('http');
var server     = http.createServer(app);
var asyncblock = require('asyncblock');
var exec       = require('child_process').exec;

// Setup environment
app.set('view engine', 'jade');
app.set('view options', { layout: true });
app.set('views', __dirname);


// Handle Twitter Bootstrap files
app.get('/bootstrap.min.css', function(req, res){
    res.sendfile ("bootstrap.min.css");
});

// Handle Twitter Bootstrap files
app.get('/bootstrap.min.js', function(req, res){
    res.sendfile ("bootstrap.min.js");
});

// Handle GET
app.get('/:doc', function(req, res){

    // Get the doc to load
    doc = req.params.doc;
    results = 'No Document';

    // Format the document
    asyncblock(function (flow) {
        exec('wiki-html-content '+doc, flow.add());
        results = flow.wait();
            
        // Display the results
        res.render('index',{doc: doc, results: results});    
    });
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
