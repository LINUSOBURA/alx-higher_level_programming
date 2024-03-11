#!/usr/bin/node

const args = process.argv;
const numbers = [];

if (args.length < 3) {
  console.log(0);
} else if (args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    const arg = parseInt(args[i]);
    numbers.push(arg);
  }

  numbers.sort((a, b) => b - a);

  console.log(numbers[1]);
}
