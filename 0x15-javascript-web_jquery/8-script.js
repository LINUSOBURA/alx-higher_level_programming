#!/usr/bin/node
fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    data.results.forEach((film) => {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
