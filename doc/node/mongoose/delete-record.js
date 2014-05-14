// Run mongo DB
console.log ("mongo.js start");

var mongoose = require('mongoose');

mongoose.connect('localhost', 'test');

var noteSchema = mongoose.Schema({ name:'string', text:'string' });

var Note    = mongoose.model('Note', noteSchema);

var myNote = new Note({ name: 'My First Note', text:'No content for this note' });

// Find one object
Note.remove (function (err, notes) {
    if (err) console.log('Error during find');
    console.log('Notes: '+Note.find());
    mongoose.disconnect();
})

console.log ("mongo.js done");
