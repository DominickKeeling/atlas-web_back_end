// Import the readline module, which allows us to read user input from the
// terminal
const readline = require('readline');

// Create a readline interface with the input coming from the standard input
// (process.stdin) 
// and the output going to the standard output (process.stdout)
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Define a function to prompt the user for their name
function promptUser() {
  // Print a welcome message to the user
  console.log("Welcome to Holberton School, what is your name?");
  
  // Use the readline interface to ask the user for their name
  rl.question("Name: ", (answer) => {
    // Print a message to the user with their name
    console.log(`Your name is: ${answer}`);
    
    // Close the readline interface
    rl.close();
    
    // Exit the process with a status code of 0 (indicating success)
    process.exit(0);
  });
}

// Define an event handler for the SIGINT signal (which is sent when the user
//presses Ctrl+C)
process.on('SIGINT', () => {
  // Print a message to the user when the program is interrupted
  console.log('\nThis important software is closing');
  
  // Exit the process with a status code of 0 (indicating success)
  process.exit(0);
});

// Call the promptUser function to start the program
promptUser();
