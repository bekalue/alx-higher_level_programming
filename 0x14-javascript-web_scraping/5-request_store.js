#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length > 3) {
  request.get(`${process.argv[2]}`).pipe(fs.createWriteStream(process.argv[3]));
}
