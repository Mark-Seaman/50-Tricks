var http = require("http");

http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Mark's awesome server is running");
  response.end();
}).listen(8080);

console.log("Connect at http://localhost:8080");
