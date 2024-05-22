#!/usr/bin/node
//display title of film by id/release order using starwars API
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
