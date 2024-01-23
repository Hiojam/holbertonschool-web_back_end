const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a request to the JSONPlaceholder API and compute completed tasks by user id
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todosData = JSON.parse(body);
    const completedTasksByUser = {};

    todosData.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
