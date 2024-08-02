#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (_, res, body) {
  try {
    fs.writeFileSync(process.argv[3], body);
  } catch (err) {
    console.log(err);
  }
});
