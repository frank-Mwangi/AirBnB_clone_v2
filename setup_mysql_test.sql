-- script that prepares MySQL server for hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON perfomance_schema.* TO hbnb_test@localhost;
