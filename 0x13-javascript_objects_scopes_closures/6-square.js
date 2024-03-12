#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) console.log('C'.repeat(this.size));
    } else {
      this.print();
    }
  }
};
