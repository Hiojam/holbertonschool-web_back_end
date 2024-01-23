const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a request to the Star Wars API and count movies with "Wedge Antilles"
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeMovies = filmsData.filter(film => film.characters.includes('https://swapi-api.hbtn.io/api/people/18/'));
    console.log(wedgeMovies.length);
  }
});
