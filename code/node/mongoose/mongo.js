// Run mongo DB
console.log ("mongo.js start");

var mongoose = require('mongoose');

mongoose.connect('localhost', 'test');

var noteSchema = mongoose.Schema({ name:'string', text:'string' });

var Note    = mongoose.model('Cat', noteSchema);

var myNote = new Note({ name: 'My First Note', text:'No content for this note' });

// Save in the DB
myNote.save(function (err) {
  if (err)  console.log('Error during save');
    console.log('myNote saved in DB');
});


// Find one object
Note.findOne({ name: 'My First Note' }, function (err, notes) {
    if (err) console.log('Error during find');
    console.log('Find one Note: '+notes.name+',  Text: '+notes.text);
})

// Query for one object 
var query = Note.findOne({ 'name': 'My First Note' });
query.select('name');
query.exec(function (err, note) {
  if (err) return  console.log('Error during query');
    console.log('Query %s: %s', 'Name', note.name) 
})

// Query for a collection
Note.find({ 'name': 'My First Note' }).exec(function (err, notes) {
    if (err) console.log('Error during find');
    console.log('xxxFind Notes: '+notes);
});

// Series of filters
Note
.find({ text:'No content for this note' })
.where('name').equals('My First Note')
.limit(10)
.sort('-name')
.select('name text')
.exec(function (err, notes) {
    if (err) console.log('Error during find');
    console.log('Find Notes: '+notes.name+',  Text: '+notes.text);
});

console.log ("mongo.js done");
