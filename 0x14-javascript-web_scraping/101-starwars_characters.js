#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films';

if (process.argv.length > 2) {
  request(`${API_URL}/${process.argv[2]}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
