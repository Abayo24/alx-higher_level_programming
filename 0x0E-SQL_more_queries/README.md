
0x0E-SQL_more_queries
Description
This project consists of a series of SQL scripts aimed at enhancing your understanding of MySQL databases and SQL queries. Each script tackles specific tasks related to user management, table creation, data manipulation, and query optimization. These scripts are part of the ALX Higher Level Programming curriculum.

Table of Contents
General Info
Requirements
Tasks
Resources
Quiz Questions
Copyright
General Info
Language: SQL
Database: MySQL
Version: MySQL 8.0.25
Platform: Ubuntu 20.04 LTS
Tools: vi, vim, emacs
Execution Environment: MySQL Server
Credentials: root/root for local MySQL server, user credentials as specified in scripts
Requirements
All scripts are designed to be executed on Ubuntu 20.04 LTS using MySQL 8.0.25.
All files should have a newline at the end.
SQL queries should be commented just before execution.
File names should start with a number followed by a description.
All SQL keywords should be in uppercase.
A README.md file is mandatory for each project.
Tasks
My Privileges!
Script: 0-privileges.sql
Description: Lists all privileges of specified MySQL users.
Root User
Script: 1-create_user.sql
Description: Creates a MySQL server user with all privileges.
Read User
Script: 2-create_read_user.sql
Description: Creates a database and user with SELECT privilege only.
Always a Name
Script: 3-force_name.sql
Description: Creates a table with a non-null name field.
ID Can't Be Null
Script: 4-never_empty.sql
Description: Creates a table with a non-null ID field.
Unique ID
Script: 5-unique_id.sql
Description: Creates a table with a unique ID field.
States Table
Script: 6-states.sql
Description: Creates a database and table for states.
Cities Table
Script: 7-cities.sql
Description: Creates a database and table for cities with a foreign key constraint.
Cities of California
Script: 8-cities_of_california_subquery.sql
Description: Lists all cities of California without using JOIN.
Genre ID by Show
Script: 10-genre_id_by_show.sql
Description: Lists shows with at least one genre linked.
Genre ID for All Shows
Script: 11-genre_id_all_shows.sql
Description: Lists all shows and their associated genre IDs.
No Genre
Script: 12-no_genre.sql
Description: Lists shows without a linked genre.
Number of Shows by Genre
Script: 13-count_shows_by_genre.sql
Description: Lists genres and the number of shows linked to each.
My Genres
Script: 14-my_genres.sql
Description: Lists all genres of a specified show.
Only Comedy
Script: 15-comedy_only.sql
Description: Lists all comedy shows.
List Shows and Genres
Script: 16-shows_by_genre.sql
Description: Lists all shows and their associated genres.
