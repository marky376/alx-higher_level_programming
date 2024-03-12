#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = ' ';
	    for (let j = 0; j < this.width; i++)
	    {
		    line += 'X';
	    }
	    console.log(line);
    }
  }
}

module.exports = Rectangle;
