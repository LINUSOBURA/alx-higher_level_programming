#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const films = data.results;

    let count = 0;

    for (const film of films) {
      if (
        film.characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/'
        )
      ) {
        count += 1;
      }
    }
    console.log(count);
  }
});
