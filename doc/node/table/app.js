var express = require('express');
var http = require('http');
var app = express();
var server = http.createServer(app);

app.set('view engine', 'jade');
app.set('view options', { layout: false });
app.set('views', __dirname);


app.get('/?', function(req, res){
    var data =  {
        items: { x: {name: 'Mark', price: 'Cheap'}, y: {name: 'Stacie', price: 'Free'} },
    };        
    
    res.render('index',data);    
});

app.get('/item/:id', function(req, res) {
    var data =  { 
        id:    req.params.id,
        item:  {name: 'Mark', price: 'Cheap'}
    };        
    res.render('item', data);
});

var port = 8080;
server.listen(port);
console.log('Listening on port ' + port);
