#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const size = this.height;
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < size; i++) console.log(c.repeat(size));
  }
}
module.exports = Square;
