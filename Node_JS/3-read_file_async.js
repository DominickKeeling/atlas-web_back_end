const fs = require('fs');
const { promisify } = require('util');

const readFileAsync = promisify(fs.readFile)

async function countStudents(path) {
    try {
      const data = await readFileAsync(path, 'utf8');
      const lines = data.trim().split('\n');
      const validLines = lines.filter(line => line.trim() !== '');
      const header = validLines.shift();
      const students = validLines.map(line => line.split(',').map(item => item.trim()));
      const numberOfStudents = students.length;

      console.log(`Number of students: ${numberOfStudents}`);

      const fields = {};
      for (const student of students) {
        const field = student[3];
        const firstname = student[0];
        if (fields[field]) {
          fields[field].push(firstname);
        } else {
          fields[field] = [firstname];
        }
      }
      for (const field in fields) {
        if (field) {
          console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
      }
    } catch (err) {
      throw new Error('Cannot load the database');
    }
}

module.exports =  countStudents;
