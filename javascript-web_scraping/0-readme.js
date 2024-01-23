const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file content in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
