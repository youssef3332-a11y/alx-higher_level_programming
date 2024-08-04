#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log('#'.repeat(this.width) + '\n').repeat(this.height - 1) + '#'.repeat(this.w);
  }
}
module.exports = Rectangle;
