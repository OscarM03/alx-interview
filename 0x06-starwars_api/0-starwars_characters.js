#!/usr/bin/env node
// module

const request = require('request');

const movieId = process.argv[2];
const apiURL = `https://swapi.dev/api/films/${movieId}/`;

function getMovieInfo () {
  request(apiURL, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie info', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`Error: status code ${response.statusCode}`);
      return;
    }
    const movieinfo = JSON.parse(body);
    const charactersUrls = movieinfo.characters;

    getCharacters(charactersUrls);
  });
}

function getCharacters (charactersUrls) {
  charactersUrls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character,', error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Error: status code: ${response.statusCode}`);
        return;
      }

      const characterDetails = JSON.parse(body);
      console.log(characterDetails.name);
    });
  });
}

getMovieInfo();
