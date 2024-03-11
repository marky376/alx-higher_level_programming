#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num) || num < 0) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
