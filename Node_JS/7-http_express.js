const express = require('express');
const fs = require('fs').promises;
const path = require('path');

const app = express();

async function countStudents(filePath) {
    const fullPath = path.resolve(filePath);
    try {
        const data = await fs.readFile(fullPath, 'utf-8');
        const lines = data.trim().split('\n');
        const validLines = lines.filter(line => line.trim() !== '');
        const header = validLines.shift();
        const students = validLines.map(line => line.split(',').map(item => item.trim()));
        const numberOfStudents = students.length;

        let result = `Number of students: ${numberOfStudents}\n`;

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
                result += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
            }
        }
        return result;
      } catch (err) {
          throw new Error('Cannot load the database');
      }
}

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    try {
        const message = 'This is the list of our students\n';
        const studentInfo = await countStudents(process.argv[2]);
        res.send(`${message}\n${studentInfo}`);
    } catch (err) {
        console.error(err);
        res.end('Error: Cannot load the database');
    }
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`The server is running on ${PORT}`);
});

module.exports = app;
