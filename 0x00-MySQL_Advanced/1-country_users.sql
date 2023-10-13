-- Create the 'users' table with specified attributes
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country VARCHAR(2) NOT NULL CHECK (country IN ('US', 'CO', 'TN'))
);
