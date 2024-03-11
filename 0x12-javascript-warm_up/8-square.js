#!/usr/bin/node

const args = process.argv;

const size = parseInt(args[2]);
let j = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (j < size) {
    console.log('X'.repeat(size));
    j += 1;
  }
}
