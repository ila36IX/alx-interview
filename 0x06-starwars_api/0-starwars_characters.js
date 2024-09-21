#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function sendRequest(characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (e, response, b) => {
    if (e) {
      console.log(e);
    } else {
      console.log(JSON.parse(b).name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (e, response, b) => {
  if (e) {
    console.log(e);
  } else {
    const characterList = JSON.parse(b).characters;

    sendRequest(characterList, 0);
  }
});
