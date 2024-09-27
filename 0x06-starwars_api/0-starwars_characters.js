#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

const movieId = argv[2];

function logNames (ListOfNames) {
  ListOfNames.forEach(name => {
    console.log(name);
  });
}

function getNames (charcters) {
  return charcters.map(character => {
    return new Promise((resolve, reject) => {
      request.get(character, (e, r, b) => {
        try {
          const data = JSON.parse(b);
          resolve(Promise.resolve(data.name));
        } catch (error) {
          reject(error);
        }
      });
    });
  });
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (e, r, b) => {
  if (r.statusCode === 200) {
    const allCharacters = getNames(JSON.parse(b).characters);
    Promise.all(allCharacters)
      .then(names => logNames(names))
      .catch(e => console.error(e));
  }
});
