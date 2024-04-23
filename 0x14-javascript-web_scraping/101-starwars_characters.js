#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);

    const charactersPromises = data.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, response, body) => {
          if (err) {
            reject(err);
          } else {
            const charData = JSON.parse(body);
            resolve(charData.name);
          }
        });
      });
    });

    Promise.all(charactersPromises)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
