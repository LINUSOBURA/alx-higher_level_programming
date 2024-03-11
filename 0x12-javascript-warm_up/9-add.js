#!/usr/bin/node

const args = process.argv;

const firstInteger = parseInt(args[2]);
const secondInteger = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstInteger, secondInteger));
