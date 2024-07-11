#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const filmURL = `${API_URL}/films/${movieId}/`;

  request(filmURL, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, __, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      })
    );

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr));
  });
} else {
  console.log('Please provide a Movie ID as the first argument.');
}
