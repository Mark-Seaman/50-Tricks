var fs      = require('fs');


// List the files and perform an action
var list_files = function (path, action) {
    fs.readdir(path, function(err, files) {
        if (err) files = ['No directory'];
        action({ files:files });
    });
}

// Read the file and perform an action
var read_file = function (path, action) {
    fs.readFile(path, 'utf8', function(err, data) {
        if (err) data = 'No file found';
        action({ id:path, data:data });
    });
}

// Read the file and perform an action
var write_file = function (path, text, action) {
    var stream = fs.createWriteStream(path);
    stream.once('open', function(fd) {
        stream.write(text+"\n");
        stream.end();
        action();
    });
}


exports.list  = list_files;
exports.read  = read_file;
exports.write = write_file;
