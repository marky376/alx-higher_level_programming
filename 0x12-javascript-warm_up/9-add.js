#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(add(arg1, arg2));
