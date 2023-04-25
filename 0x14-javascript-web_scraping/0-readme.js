#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (error, response) => {
    if (error) {
      console.log(error);
    } else {
      console.log(response.toString('utf-8'));
    }
  });
}
