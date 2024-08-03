#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (_, res, body) => {
  const data = JSON.parse(body);
  callFunc(data.characters, 0);
});

function callFunc (url, i) {
  request(url[i], (_, res, body) => {
    const data = JSON.parse(body);
    console.log(data.name);
    if (i + 1 < url.length) {
      callFunc(url, i + 1);
    }
  });
}
