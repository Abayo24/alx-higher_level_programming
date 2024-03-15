Python Object-Relational Mapping Project
This project aims to demonstrate the integration of Python with MySQL databases using both direct SQL queries and SQLAlchemy, an Object Relational Mapper (ORM). The ORM abstracts the interaction with the database, allowing developers to focus on manipulating Python objects rather than writing raw SQL queries.

Table of Contents
Description
Installation
Usage
Files
Credits
Description
In this project, we implement various scripts to interact with a MySQL database named hbtn_0e_0_usa and hbtn_0e_4_usa containing information about states and cities in the USA. The scripts are written in Python and utilize both direct SQL queries using the MySQLdb module and SQLAlchemy for ORM-based interactions.

The tasks covered in this project include:

Fetching all states from the database
Filtering states by name
Filtering states by user input (with protection against SQL injection)
Retrieving all cities from the database
Filtering cities by state name
Defining and using a SQLAlchemy model for the State table
Fetching all states using SQLAlchemy
Fetching the first state using SQLAlchemy
Filtering states by names containing the letter 'a' using SQLAlchemy
Retrieving the state ID by name using SQLAlchemy
Inserting a new state using SQLAlchemy
Updating a state name using SQLAlchemy
Deleting states containing the letter 'a' using SQLAlchemy
Defining and using a SQLAlchemy model for the City table and fetching cities by state
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/alx-higher_level_programming.git
Navigate to the project directory:

bash
Copy code
cd alx-higher_level_programming/0x0F-python-object_relational_mapping
Set up a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Each script in the project corresponds to a specific task as outlined in the project requirements. To run a script, use the following format:

bash
Copy code
./script_name.py <mysql_username> <mysql_password> <database_name> [additional_arguments]
Replace <mysql_username>, <mysql_password>, and <database_name> with your MySQL credentials and the name of the database you want to connect to. Additional arguments may be required for some scripts, such as the state name for filtering tasks.

Files
0-select_states.py: Script to fetch all states from the database.
1-filter_states.py: Script to filter states by name starting with 'N'.
2-my_filter_states.py: Script to filter states by user input with protection against SQL injection.
3-my_safe_filter_states.py: Script to filter states by user input safely using parameterized queries.
4-cities_by_state.py: Script to fetch all cities from the database.
5-filter_cities.py: Script to filter cities by state name.
6-model_state.py: Script to define a SQLAlchemy model for the State table.
7-model_state_fetch_all.py: Script to fetch all states using SQLAlchemy.
8-model_state_fetch_first.py: Script to fetch the first state using SQLAlchemy.
9-model_state_filter_a.py: Script to filter states by names containing the letter 'a' using SQLAlchemy.
10-model_state_my_get.py: Script to retrieve the state ID by name using SQLAlchemy.
11-model_state_insert.py: Script to insert a new state using SQLAlchemy.
12-model_state_update_id_2.py: Script to update a state name using SQLAlchemy.
13-model_state_delete_a.py: Script to delete states containing the letter 'a' using SQLAlchemy.
model_state.py: Module containing the SQLAlchemy model definitions for the State and City tables.
model_city.py: Module containing the SQLAlchemy model definition for the City table.
Credits
This project is part of the ALX Software Engineering Program, provided by ALX + HOLBERTON.
