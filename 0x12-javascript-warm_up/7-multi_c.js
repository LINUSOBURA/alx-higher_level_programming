#!/usr/bin/node

const args = process.argv;

const arg1 = parseInt(args[2]);
let i = 0;

if (isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  while (i < arg1) {
    console.log('C is fun');
    i += 1;
  }
}
