// Run mongo DB
console.log ("mongo.js start");

var mongoose = require('mongoose');

mongoose.connect('localhost', 'test');

var noteSchema = mongoose.Schema({ name:'string', text:'string' });

var Note    = mongoose.model('Note', noteSchema);

// Find one object
Note.findOne({ name: /3/ }, function (err, notes) {
    if (err) return console.log('Error during find');
    console.log('Find one Note: '+notes.name+',  Text: '+notes.text);
})

// Find one object
Note.find({ name: /Note/ }, function (err, notes) {
    var x=notes.length;
    if (err) return console.log('Error during find');
    notes.forEach(function(note) {
        console.log('Note: '+note.name+',  Text: '+note.text);
    });
});

// Series of filters
Note
.find({ name:/Note/ })
.limit(10)
.sort('-name')
.select('name text')
.exec(function (err, notes) {
    if (err) console.log('Error during find');
    var x=notes.length;
    notes.forEach(function(note) {
        console.log('Note: '+note.name+',  Text: '+note.text);
        if (--x<1) mongoose.disconnect();
    });
});



console.log ("mongo.js done");
