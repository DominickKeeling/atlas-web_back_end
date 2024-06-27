const http = require('http');
const countStudents = require('./3-read_file_async');

const PORT = 1245;
const databaseFile = process.argv[2];

const server = http.createServer(async (req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain'});
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        res.writeHead(200, {'Content-Type': 'text/plain'});

        try {
            const studentData = await countStudents(databaseFile);
                res.write('This is the list of our students\n');
                res.write(studentData);
                res.end();
        } catch (err) {
            console.error(err);
            res.end('Error: Cannot load the database');
        }
    }
});

server.listen(PORT, () => {
    console.log(`Server is running and listening on port ${PORT}`);
});

module.exports = server;
