var express = require('express');
var http    = require('http');
var app     = express();
var server  = http.createServer(app);
var fs      = require('fs');

app.set('view engine', 'jade');
app.set('view options', { layout: false });
app.set('views', __dirname);


// List the files and perform an action
var list_files = function (path, action) {
    fs.readdir(path, function(err, files) {
        if (err) files = ['No directory'];
        //var f = ''; files.forEach(function(element) { f += element+', '; });
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

// Directory view
app.get('/', function(req, res){
    list_files ('.', function (data) { res.render ('dir', data) });
});


//File view
app.get('/:id', function(req, res) {
    read_file (req.params.id, function (data) { res.render ('file',  data) });
});


var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
