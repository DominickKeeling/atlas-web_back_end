-- CREATEA PROCEDURE THAT AUTOMATICALLY ADDS A CORRECTION FOR A USER
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_id INT;

  -- CHECKS FOR PROJECT
  SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- INSERT THE PROJECT AND GET NEW ID IF IT DOESNT ALREADY EXIST
  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- ADDS THE CORRECTION
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, project_id, score);
END //

DELIMITER ;