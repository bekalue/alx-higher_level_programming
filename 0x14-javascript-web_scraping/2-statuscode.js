#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request.get(process.argv[2]).on('response', response => {
    console.log(`code: ${response.statusCode}`);
  });
}
