console.log ("Account.js start");

var mongoose = require('mongoose');
mongoose.connect('localhost', 'test');

var AccountSchema = new mongoose.Schema({
    email:     { type: String, unique: true },
    password:  { type: String },
    name: {
        first:   { type: String },
        last:    { type: String }
    },
});

var Account = mongoose.model('Account', AccountSchema);

//-----------------------------------------------------------------------------

var register = function(email, password, firstName, lastName) {
    console.log('Registering ' + email);
    var user = new Account({
        email: email,
        name: { first: firstName, last: lastName },
        password: password
    });
    user.save(function(err) {
        if (err) {
            return console.log(err);
        };
        return console.log('Account was created');
    });
    console.log('Save command was sent');
}

//-----------------------------------------------------------------------------

var login = function(email, password) {
    console.log ('login (%s,%s)',email,password);
    Account.findOne({ email: email}, function(err,doc){
        console.log ("login %s done", doc);
    });
};

register ('me@here1.com', "My Password", "Mark", "1");
//register ('me@here2.com', "My Password", "Mark", "2");
//register ('me@here3.com', "My Password", "Mark", "3");
//console.log (mongoose.db.find());

//login ("My x", "My Password");

console.log (Account.find())

// Clear out old entries
console.log ("Account clear");
Account.remove({ email:'me@here1.com'});
Account.remove({ email:'me@here2.com'});
Account.remove({ email:'me@here3.com'});

console.log ("Account.js done");
