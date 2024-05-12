#!/usr/bin/node

const argv = process.argv.slice(2); let max;

function secondBig (arr) {
  if (arr.length === 0 || arr.length === 1) {
    console.log(0);
  } else {
    arr = arr.map((el) => (el * 1));
    max = Math.max(...arr);
    arr.splice(arr.indexOf(max), 1);
    console.log(Math.max(...arr));
  }
}

secondBig(argv);
