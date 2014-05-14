var server = require("./server");
var router = require("./router");
var requestHandlers = require("./requestHandlers");

var handle         = {}
handle["/"]        = requestHandlers.start;
handle["/results"] = requestHandlers.results;

server.start(router.route, handle);
