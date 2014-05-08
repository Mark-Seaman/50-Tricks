var express = require('express')
var hash    = require('./pass').hash

var app = module.exports = express()

app.set('view engine', 'jade');
app.set('views', __dirname);

app.use(express.bodyParser());
app.use(express.cookieParser('shhhh, very secret'));
app.use(express.session());

// Session-persisted message middleware
app.use(function(req, res, next){
  var err = req.session.error
    , msg = req.session.success;
  delete req.session.error;
  delete req.session.success;
  res.locals.message = '';
  if (err) res.locals.message = '<p class="msg error">' + err + '</p>';
  if (msg) res.locals.message = '<p class="msg success">' + msg + '</p>';
  next();
});

//-----------------------------------------------------------------------------
// Register Users

var users = {}

function add_user(username, password) {
    hash(password, function(err, salt, hash){
        if (err) throw err;
        users[username] = { name: username, salt:salt, hash:hash};
    });
}

add_user('sluss',  'Mark Sluss') 
add_user('steph',  'Stephanie Farrell') 
add_user('seaman', 'Mark Seaman') 
add_user('ronz',   'Ron Zadsadinski') 

//-----------------------------------------------------------------------------
// Authenticate users

// Query the password store for the given username
// Hash the password/salt of POST info
function authenticate(name, pass, fn) {
  if (!module.parent) console.log('authenticating %s:%s', name, pass);
  var user = users[name];
  if (!user) return fn(new Error('cannot find user'));
  hash(pass, user.salt, function(err, hash){
    if (err) return fn(err);
    if (hash == user.hash) return fn(null, user);
    fn(new Error('invalid password'));
  })
}

// Go to the login page if not restricted
function restrict(req, res, next) {
    if (req.session.user) {
        next();
    } 
    else {
        req.session.error = 'Access denied!';
        res.redirect('/login');
    }
}

// Start on the login page
app.get('/', function(req, res){
  res.redirect('login');
});

// Offer up the user page
app.get('/restricted', restrict, function(req, res){
    res.render('home', { user: req.session.user.name } );
});


//-----------------------------------------------------------------------------
// Handle login

app.get('/login', function(req, res){
  res.render('login');
});

app.post('/login', function(req, res){
  authenticate(req.body.username, req.body.password, function(err, user){
    if (user) {
      // Regenerate session when signing in
      // to prevent fixation 
      req.session.regenerate(function(){
        // Store the user's primary key 
        // in the session store to be retrieved,
        // or in this case the entire user object
        req.session.user = user;
        req.session.success = 'Authenticated as ' + user.name
          + ' click to <a href="/logout">logout</a>. '
          + ' You may now access <a href="/restricted">/restricted</a>.';
        res.redirect('back');
      });
    } else {
      req.session.error = 'Authentication failed, please check your '
        + ' username and password.'
        + ' (use "tj" and "foobar")';
      res.redirect('login');
    }
  });
});

app.get('/logout', function(req, res){
  // destroy the user's session to log them out
  // will be re-created next request
  req.session.destroy(function(){
    res.redirect('/');
  });
});


//-----------------------------------------------------------------------------
app.listen(8080);
console.log('Express started on port 8080');

