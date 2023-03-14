#!/usr/bin/node

/**
 * factorial - computes and prints a factorial.
 * @param {Number} n - the number to compute the factorial for.
 * @returns the factorial number.
 */
function factorial (n) {
  return n === 0 || Number.isNaN(n) ? 1 : n * factorial(n - 1);
}
console.log(factorial(Number.parseInt(process.argv[2])));
