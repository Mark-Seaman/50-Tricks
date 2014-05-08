var express = require('express');
var http = require('http');
var app = express();
var server = http.createServer(app);

app.set('view engine', 'jade');
app.set('view options', { layout: true });
app.set('views', __dirname);

app.get('/page1', function(req, res, next) {
  res.render('page1');
});

app.get('/page2', function(req, res, next) {
  res.render('page2');
});

app.get('/?', function(req, res){
  res.render('index');
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
