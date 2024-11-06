# Database Interaction

Database Operations Automation with JSON Data
# Software Versions
Python: 3.x, PostgreSQL: 12 or above, psycopg2: Latest version (for PostgreSQL connection)
# Setup Instructions
### 1. Clone the repository

   git clone https://github.com/saiharshitha82/Database-Interaction.git
  cd your-repository

### 2. Install the required libraries

  pip install -r requirements.txt
  pip install psycopg2
   
### 3. Download the dataset

Place your data.json file in the root directory of the project. Ensure the data structure matches

# Project Structure

### database_operations.py
Python script that:
1. Loads data from data.json.
2. Inserts records into the operations_logs table in a PostgreSQL database.
3. Updates the status field for records with a timestamp before a specified cutoff date.
4. Retrieves and displays all records from the table.


# Credits
This project was created by Sai Harshitha Mutyala (https://github.com/saiharshitha82) 
