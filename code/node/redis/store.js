// Set up permanent storage using redis

//Use Redis to set up a store for key-value pairs
var redis = require("redis"),
    store = redis.createClient()


// Save the item for later
var save = function (key,value,action){
    store.set(key,value);
    if (action) { action(key,value); }
}


// Recall a previously stored item
var recall = function(key,action){
    store.get(key, function (err, value) { 
        if (err) {
            console.log("Get error: " + err);
        } else {
            if (action) { action(key,value); }
        }
    });
}


// Shut down the redis server so the app will close
var alldone = function (x,y) {
    console.log("About to end");
    store.end();
}


// Exports
exports.save   = save;
exports.recall = recall;
exports.done   = alldone;
