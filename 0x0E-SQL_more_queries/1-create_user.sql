-- creates the MySQL server user user_0d_1.
-- If the user user_0d_1 already exists, your script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
