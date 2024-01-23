const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the string to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content written to ${filePath}`);
  }
});
