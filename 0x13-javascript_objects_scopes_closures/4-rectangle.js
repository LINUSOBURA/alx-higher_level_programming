#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && w > 0 && h && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempWidth = this.width;
    const tempheight = this.height;
    this.width = tempheight;
    this.height = tempWidth;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
