#!/usr/bin/node

const sqr = require('./5-square.js');

class Square extends sqr {
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
