#!/usr/bin/node

const fs = require('fs');

// Path to the file we want to read
const filePath = process.argv[2];

// Asynchronously read from the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
