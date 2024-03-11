#!/usr/bin/node

const args = process.argv;

const integer = parseInt(args[2]);
let result = 1;

function factorial (a) {
  for (let i = 1; i <= a; i++) {
    result *= i;
  }
  return result;
}

console.log(factorial(integer));
