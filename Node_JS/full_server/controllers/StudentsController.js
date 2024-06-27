const readDatabase = require('../utils');

class StudentsController {
    static async getAllStudents(req, res) {
        try {
            const studentData = await readDatabase(req.filePath);

            let response = 'This is the list of our students\n';

            const sortedFields = object.keys(studentData).sort((a, b) => a.toLowerCase().localeConpare(b.toLowerCase()));

            sortedFields.forEach(field => {
                const students = studentData[field];
                const numberOfStudents = students.length;
                const firstNameList = students.join(',');

                response += `Number of students in ${field}: ${numberOfStudents} List: ${firstNameList}\n`;
            });

            res.status(200).send(response);
        } catch (error) {
            console.error(error);
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const studentData = await readDatabase(req.filePath);

            if (!studentData[major]) {
                return res.status(500).send('No students found in ${major}');
            }

            const firstNameList = studentData[major].join(', ');
            const response = `List: ${firstNameList}`;

            res.status(200).send(response);
        } catch (error) {
            console.error(error);
            res.status(500).send('Cannot load the database');
        }
      }
}


module.exports = StudentsController;
