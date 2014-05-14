//Use Redis to set up a store for key-value pairs

var store = require("./store");


// Test the read/write scenario

store.recall('name', function(key,value) {
    console.log('get name = '+value);

    store.save('name','Ishmael', function(key,value) {
        console.log('set name = '+value);
        
        store.recall('name', function(key,value) {
            console.log('get name = '+value);
            
            store.save('name','Bob', function(key,value) {
                console.log('set name = '+value);
                
                store.recall('name', function(key,value) {
                    console.log('get name = '+value);
                    store.done();
                });
            });
        });
    });
});
