const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Get the movie ID from command line arguments
const movieID = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}`;

// Make a request to the Star Wars API and print the movie title
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
