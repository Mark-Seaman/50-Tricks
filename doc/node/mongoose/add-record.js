// Run mongo DB
console.log ("mongo.js start");

var mongoose = require('mongoose');

mongoose.connect('localhost', 'test');

var noteSchema = mongoose.Schema({ name:'string', text:'string' });

var Note    = mongoose.model('Note', noteSchema);

var notesSaved = 0;

var saveNote = function (name, text) {
    var myNote = new Note({ name: name, text:text });
    myNote.save(function (err) {
        if (err)  console.log('Error during save');
        console.log('myNote saved in DB');
        if (++notesSaved > 2) mongoose.disconnect();
    });
}

saveNote ('Note 1', 'No content for this note');
saveNote ('Note 2', 'None');
saveNote ('Note 3', 'No comment');

console.log ("mongo.js done");
