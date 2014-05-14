// Requests for the home page
function start(response) {
    page(response, 'Home page', '/results', 'Switch to results page')
}

// Requests for the results page
function results(response) {
    page(response, 'Results page', '/', 'Switch to home page')
}

// Create a page of the correct type
function page(response,title,page,other) {
    console.log("Request handler 'start' was called.");
    var body = '<html>'+
        '  <h1>'+title+'</h1>'+
        '  <a href="'+page+'">'+other+'</a>'+
        '</html>';
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}

// Called from index.js
exports.results = results;
exports.start   = start;

