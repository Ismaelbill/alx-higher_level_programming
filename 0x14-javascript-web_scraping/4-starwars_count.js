#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_, res, body) {
  const data = JSON.parse(body);
  let j = 0;
  for (const i of data.results) {
    for (const k of i.characters) {
      if (k.includes(18)) { j++; }
    }
  }
  console.log(j);
});
