#!/usr/bin/node
const request = require("request");

const url = process.argv[2];

request(url, { timeout: 10000 }, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data);
    } catch (error) {
      console.error("Error parsing JSON:", error);
    }
  }
});
