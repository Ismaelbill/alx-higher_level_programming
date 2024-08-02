#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_, res, body) {
  const data = JSON.parse(body);

  const obj = {};
  for (const user of data) {
    if (obj[user.userId] === undefined) { obj[user.userId] = 0; }
    if (user.completed) { obj[user.userId]++; }
  }
  console.log((obj));
});
