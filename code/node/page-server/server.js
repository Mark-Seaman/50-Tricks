// server.js serves pages

var http = require("http");
var url = require("url");

// Start serving requests
function start(route, handle) {

    // When a request is made call the handler to create the response
    function onRequest(request, response) {
        var postData = "";
        var pathname = url.parse(request.url).pathname;
        
        console.log("Request for " + pathname + " received.");
        request.setEncoding("utf8");
        route(handle, pathname, response, postData);
    }
 
    // Listen on port 8080
    http.createServer(onRequest).listen(8080);
    console.log("Server has started.");
}

// Called from index.js
exports.start = start;
