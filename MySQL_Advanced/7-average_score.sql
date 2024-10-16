-- Creates the stored procedure to compute and store the average score for a userss

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg_score FLOAT DEFAULT 0;

  -- Calculates the average score
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE user_id = user_id;

  -- Update the user's average_score 
  UPDATE users
  SET average_score = IFNULL(avg_score, 0)
  WHERE id = user_id;
END //

DELIMITER ;