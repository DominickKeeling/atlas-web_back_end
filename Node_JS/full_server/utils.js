const fs = require('fs').promises;
const path = require('path');

async function readDatabase(filePath) {
    const fullPath = path.resolve(filePath);
    try {
        const data = await fs.readFile(fullPath, 'utf-8');
        const lines = data.trim().split('\n');
        const validLines = lines.filter(line => line.trim() !== '');
        const header = validLines.shift();
        const students = validLines.map(line => line.split(',').map(item => item.trim()));

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
        return fields;
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = readDatabase;
