#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);

    for (const characters of data.characters) {
      request(characters, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    }
  }
});
