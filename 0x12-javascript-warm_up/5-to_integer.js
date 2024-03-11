#!/usr/bin/node

const args = process.argv;

const arg1 = parseInt(args[2]);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg1);
}
