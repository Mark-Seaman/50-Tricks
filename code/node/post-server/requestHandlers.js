var exec = require("child_process").exec;


var querystring = require("querystring"),
    fs = require("fs"),
    formidable = require("formidable");

function start(response) {
    console.log("Request handler 'start' was called.");
    var body = '<html>'+
        '<head>'+
        '<meta http-equiv="Content-Type" content="text/html; '+
        'charset=UTF-8" />'+
        '</head>'+
        '<body>'+
        '  <h1>Post This</h1>'+
        '  <form action="/results" method="post">'+
        '    <textarea name="text" rows="20" cols="60"></textarea>'+
        '    <input type="submit" value="Submit text" />'+
        '  </form>'+
        '</body>'+
        '</html>';
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}

function results(response, postData) {
    console.log("Request handler 'upload' was called.");
    d = postData.slice(5);
    d = d.replace(/\%0D\%0A/g, '\n').replace(/\+/g, ' ')
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write('<h1>Posted Data</h1>');
    response.write('<pre>'+d+'</pre>');
    response.end();
}

exports.results = results;
exports.start   = start;

