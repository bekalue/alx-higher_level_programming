#!/usr/bin/node

/**
 * add - prints the addition of 2 integers
 * @param {Number} a - the first integer
 * @param {Number} b - the second integer
 */
function add (a, b) {
  console.log(a + b);
}

add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]));
