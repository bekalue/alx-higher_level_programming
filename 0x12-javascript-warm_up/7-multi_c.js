#!/usr/bin/node
/**
 * nPrint - Prints a string n times.
 * @param {Number} n - The number of times to print the string.
 * @param {String} txt - The string to print.
 */
function nPrint (n, txt) {
  if (Number.isNaN(n)) {
    console.log('Missing number of occurrences');
  } else if (n >= 0) {
    for (let i = 0; i < n; i++) {
      console.log(txt);
    }
  }
}

nPrint(Number.parseInt(process.argv[2]), 'C is fun');
