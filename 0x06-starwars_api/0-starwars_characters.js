#!/bin/env node
const request = require('request');
const { argv } = require('node:process');
const { error } = require('node:console');

const movie_id = argv[2];

function logNames(ListOfNames) {
  ListOfNames.forEach(name => {
    console.log(name);
  })
}

function getNames(charcters) {
  return charcters.map(character => {
    return new Promise((resolve, reject) => {
      request.get(character, (e, r, b) => {
        try {
          const data = JSON.parse(b);
          resolve(Promise.resolve(data.name));
        } catch (error) {
          reject(error);
        }
      })
    })
  });
}

url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;
request.get(url, (e, r, b) => {
  if (r.statusCode === 200) {
    const allCharacters = getNames(JSON.parse(b).characters);
    Promise.all(allCharacters)
      .then(names => logNames(names))
      .catch(e => console.error(e));
  }
})
