#!/usr/bin/node

const fs = require('fs');
const Filepath = process.argv[2];
const content = process.argv[3];
fs.writeFile(Filepath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});`
