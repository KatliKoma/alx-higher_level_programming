#!/usr/bin/node
// stores content of a webpage in a file
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let filename = '';
  if (process.argv[3] !== undefined) {
    filename = process.argv[3];
  }
  fs.writeFile(filename, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
