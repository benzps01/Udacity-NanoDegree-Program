DROP DATABASE IF EXISTS bookshelf;
DROP DATABASE IF EXISTS test_db;
DROP USER IF EXISTS student;
CREATE DATABASE bookshelf;
CREATE DATABASE test_db;
CREATE USER student WITH ENCRYPTED PASSWORD 'student';
GRANT ALL PRIVILEGES ON DATABASE bookshelf TO student;
GRANT ALL PRIVILEGES ON DATABASE test_db TO student;
ALTER USER student CREATEDB;
ALTER USER student WITH SUPERUSER;