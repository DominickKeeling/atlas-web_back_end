-- ddrops view if exists
DROP VIEW IF EXISTS need_meeting;

-- CREATES THE VIEW NEED MEETING FOR STUDENTS WHO HAVE A SCORE UNDERS 80
CREATE VIEW need_meeting AS
SELECT name
FROM  students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));