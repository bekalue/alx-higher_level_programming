#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);

console.log(Number.isNaN(num) ? 'Not a number' : 'My number: ' + num);
