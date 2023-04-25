#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(`${process.argv[2]}`, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (body) {
      const characFilms = JSON.parse(body).results.filter(y => y.characters.find(x => x.match(/\/people\/18\/?$/)));
      console.log(characFilms.length);
    }
  });
}
