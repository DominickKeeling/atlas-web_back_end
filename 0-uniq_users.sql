-- Write a sql script that creates a table users
-- table contains 3 columns: id, email, name
CREATE TABLE IF NOT EXISTS users  (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(225) NOT NULL UNIQUE,
  name VARCHAR(225)
);

