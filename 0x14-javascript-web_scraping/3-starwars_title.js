#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (_, res, body) => {
  const data = (JSON.parse(body));
  console.log(data.title);
});
