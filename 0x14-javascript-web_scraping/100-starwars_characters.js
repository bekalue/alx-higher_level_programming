#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films';

if (process.argv.length > 2) {
  request(`${API_URL}/${process.argv[2]}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    const charactersURL = JSON.parse(body).characters;

    charactersURL.forEach(element => {
      request(element, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
}
