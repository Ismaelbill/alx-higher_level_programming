#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_, res, body) {
  const data = JSON.parse(body);
  const character = 'https://swapi-api.alx-tools.com/api/people/18/';
  let j = 0;
  for (const i of data.results) {
    for (const k of i.characters) {
      if (character === k) { j++; }
    }
  }
  console.log(j);
});
