#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (_, res, body) => {
  const data = JSON.parse(body);
  for (const i of data.characters) {
    request(i, (_, res, body) => {
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
