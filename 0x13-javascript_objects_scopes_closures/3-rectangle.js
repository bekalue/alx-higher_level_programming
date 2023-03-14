#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    const rows = new Array(this.width);
    for (let i = 0; i < this.width; i++) { rows.push('X'); }
    let lines = new Array(this.height);
    lines = lines.fill(rows.join(''), 0, this.height);
    console.log(lines.join('\n'));
  }
};
