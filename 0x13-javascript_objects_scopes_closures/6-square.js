#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareWithCharPrint;
