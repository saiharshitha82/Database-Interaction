import json
import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore
from datetime import datetime

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "my_database"  
DB_USER = "postgres"      
DB_PASSWORD = "N@tural1997"  

# Connect to PostgreSQL
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    connection.autocommit = True
    cursor = connection.cursor()

    
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    print("Data loaded from JSON file:")
    print(data)  # Print the loaded data

    # Insert data into operations_logs table 
    insert_query = sql.SQL("INSERT INTO operations_logs (operation, status, timestamp) VALUES (%s, %s, %s)")
    for entry in data:
        try:           
            timestamp = datetime.fromisoformat(entry['timestamp'])
            print(f"Inserting: {entry}")  # Print each entry before inserting
            cursor.execute(insert_query, (entry['operation'], entry['status'], timestamp))
        except Exception as e:
            print(f"Failed to insert entry {entry}: {e}")

    cutoff_date = datetime(2023, 11, 2)  
    update_query = sql.SQL("UPDATE operations_logs SET status = %s WHERE timestamp < %s")
    new_status = 'archived'  # New status value
    cursor.execute(update_query, (new_status, cutoff_date))
    print(f"{cursor.rowcount} records updated.")

    # Retrieve and print all records from operations_logs
    cursor.execute("SELECT * FROM operations_logs;")
    rows = cursor.fetchall()
    print("Records in operations_logs after update:")
    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
