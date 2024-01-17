#!/usr/bin/node
const req = require('request');
const filmID = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

req(filmUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      req(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    });
  }
});
