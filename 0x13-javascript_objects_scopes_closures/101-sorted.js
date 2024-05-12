#!/usr/bin/node

const dict = require('./101-data').dict;
const obj = {};

Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (obj[value] === undefined) { obj[value] = []; }
  obj[value].push(key);
});

console.log(obj);
