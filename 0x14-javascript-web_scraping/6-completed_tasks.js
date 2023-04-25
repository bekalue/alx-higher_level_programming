#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    }

    const usersComplete = {};
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (!usersComplete[element.userId]) {
          usersComplete[element.userId] = 0;
        }
        usersComplete[element.userId]++;
      }
    });
    console.log(usersComplete);
  }
  );
}
