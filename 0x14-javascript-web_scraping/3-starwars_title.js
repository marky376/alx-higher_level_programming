#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const url = baseUrl + movieId;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const movieTitle = JSON.parse(body);
  console.log(movieTitle.title);
});
