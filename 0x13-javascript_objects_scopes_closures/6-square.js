#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (!(c === undefined)) {
      for (let i = 0; i < this.size; i++) console.log(c.repeat(this.size));
    } else {
      this.print();
    }
  }
};
