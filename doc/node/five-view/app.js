#!/usr/bin/node
// Run a web server to demo 5 views


var express = require('express');
var http    = require('http');
var app     = express();
var server  = http.createServer(app);
var fs      = require('fs');

//-----------------------------------------------------------------------------
// File manipulations

// List the files and perform an action
var list_files = function (path, action) {
    fs.readdir(path, function(err, files) {
        if (err) files = ['No directory'];
        action({ files:files });
    });
}

// Read the file and perform an action
var read_file = function (path, action) {
    fs.readFile(path, 'utf8', function(err, data) {
        if (err) data = 'No file found';
        action({ id:path, data:data });
    });
}

// Read the file and perform an action
var write_file = function (path, text, action) {
    var stream = fs.createWriteStream(path);
    stream.once('open', function(fd) {
        stream.write(text+"\n");
        stream.end();
        action();
    });
}


//-----------------------------------------------------------------------------
// Web site pages

app.set('view engine', 'jade');
app.set('view options', { layout: false });
app.set('views', __dirname+'/views');
app.use(express.bodyParser()); // Automatically parses form data


// Static files
app.get('/views/*?:file?', function(req, res){
    res.sendfile ('views/'+req.params.file);
});

// List view
app.get('/', function(req, res){
    list_files ('.', function (data) { res.render ('list', data) });
});

// New view
app.get('/new', function(req, res) {
    res.render ('edit', {path:'', text:''} ); 
});

// Detail view
app.get('/:id', function(req, res) {
    read_file (req.params.id, function (data) { 
        res.render ('detail',  data); 
    });
});

// Edit view
app.get('/:id/edit', function(req, res) {
    path = req.params.id;
    read_file (path, function (data) { 
        res.render ('edit', {path:path, text:data.data} ); 
    });
});

// Save view
app.post('/save', function(req, res){
    f = req.body.path;
    t = req.body.text.replace(/\r/gm,'');
    if (req.param('cancel')) return res.redirect ('/'+f); 
    write_file (f, t, function () {
        res.redirect ('/'+f); 
    });
});


// Start the server
var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
console.log('wf http://localhost:' + port);
