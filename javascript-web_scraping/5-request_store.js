const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the specified URL and store the body in a file
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the body content to the specified file path
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`Body content successfully stored in ${filePath}`);
      }
    });
  }
});
