#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).title);
  });
}
