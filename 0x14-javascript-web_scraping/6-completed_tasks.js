#!/usr/bin/node

const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', function (_, res, body) {
  const data = JSON.parse(body);

  const obj = {};
  let j = 0;
  let i = 1;
  for (i; i <= 10; i++) {
    j = 0;
    for (const user of data) {
      if (user.userId === i) {
        if (user.completed === true) { j++; }
      }
    }
    obj[`${i}`] = j;
  }
  console.log(obj);
});
