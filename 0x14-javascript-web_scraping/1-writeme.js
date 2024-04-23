#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

const textToWrite = argv[3];
const fileName = argv[2];

fs.writeFile(fileName, textToWrite, 'utf8', (err) => {
  if (err) throw err;
});
