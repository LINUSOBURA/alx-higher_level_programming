#!/usr/bin/node

fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    $('#character').text(data.name);
  });
