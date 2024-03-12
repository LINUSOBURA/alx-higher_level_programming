#!/usr/bin/node

const args = process.argv;

const fs = require('fs');

function readFileContent (filename, callback) {
  fs.readFile(filename, 'utf8', function (err, data) {
    if (err) {
      callback(err);
      return;
    }
    callback(null, data);
  });
}

readFileContent(args[2], function (err, f1Content) {
  if (err) {
    console.error(err);
    return;
  }

  readFileContent(args[3], function (err, f2Content) {
    if (err) {
      console.error(err);
      return;
    }

    const content = f1Content + '\n' + f2Content;

    fs.writeFile(args[4], content, function (err) {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  });
});
