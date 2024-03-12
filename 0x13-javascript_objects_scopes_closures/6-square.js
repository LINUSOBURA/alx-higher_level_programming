#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c) {
        console.log('C'.repeat(this.size));
      } else {
        console.log('x'.repeat(this.size));
      }
    }
  }
};
