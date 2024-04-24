#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const dict = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (!dict(todo.userId)) {
        dict[todo.userId] = 1;
      } else {
        dict[todo.userId] += 1;
      }
    }
  });
  console.log(dict);
});
