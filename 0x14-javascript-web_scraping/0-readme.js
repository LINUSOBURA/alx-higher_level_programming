#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
