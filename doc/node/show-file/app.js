var fs      = require('fs');
var http    = require('http');
var execSync = require('exec-sync');
var express = require('express');
var app     = express();
var server  = http.createServer(app);

app.set('view engine', 'jade');
app.set('view options', { layout: true });
app.set('views', __dirname);

//app.get('/favicon.ico', function(req, res) {});

// Show the directory list
app.get('/*', function(req, res) {

    // Test for file or directory
    var path = req.url.slice(1);
    console.log("Trying to load"+path)
    fs.lstat(path, function(err, stats) {

        // Handle directories
        if (!err && stats.isDirectory()) {
            // This request is for a directory
            fs.readdir(path, function(err, data){
                res.render('dir', {path: path, files: data});
            });
        }

        // Handle files
        else {
            try {
                //res.send('<h1>page not found</h1><p>No file matches</p>'+
                //         '<p>URL:'+req.url+'</p>');
                var filename = path;
                var content  = execSync('cat '+path); 
                res.render( 'file', {filename: path, content:  content} ); 
            }
            catch(e)
            {
                res.send('<h1>file not found</h1>');
            }
        }
    });
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
