#!/usr/bin/node

/**
 * sPrint - Prints a square
 * @param {Number} n - The size of the square
 * @param {String} txt - The string to print.
 */
function sPrint (n, txt) {
  if (Number.isNaN(n)) {
    console.log('Missing size');
  } else if (n >= 0) {
    const row = new Array(n);
    for (let i = 0; i < n; i++) { row.push(txt); }
    let lines = new Array(n);
    lines = lines.fill(row.join(''), 0, n);
    console.log(lines.join('\n'));
  }
}
sPrint(Number.parseInt(process.argv[2]), 'X');
