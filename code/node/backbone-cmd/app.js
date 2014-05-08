var express  = require('express');
var app      = express();
var execSync = require('exec-sync');   

app.configure(function(){
    app.set('view engine', 'jade');
    app.use(express.static(__dirname + '/public'));
});

app.get('/', function(req, res){
    var text = execSync('echo $USER');
    var files = execSync('ls');
    //res.send("<h1>"+text+"</h1><pre>"+files+"</pre>")
    res.render("index.jade", {layout:false, files:'here is a file list'});
});

app.listen(8080);
