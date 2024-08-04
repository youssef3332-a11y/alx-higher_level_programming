#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    return ('#'.repeat(this.w) + '\n').repeat(this.h - 1) + '#'.repeat(this.w);
  }
}
module.exports = Rectangle;
