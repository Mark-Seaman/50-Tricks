var express = require('express');
var app = express();

app.configure(function(){
    app.set('view engine', 'jade');
    app.use(express.static(__dirname));
});

app.get('/', function(req, res){
    res.render("index.jade", {layout:false});
});

app.get('/record', function(req, res){
    res.render("record.jade", {layout:false});
});

app.get('/view', function(req, res){
    res.render("view.jade", {layout:false});
});

app.get('/select', function(req, res){
    res.render("select.jade", {layout:false});
});

app.listen(8080);
