import psycopg2
import csv

# Define your database connection parameters 
db_params = {
        "dbname": "gym_graders_dw",
        "user": "etl",
        "password": "demopass",
        "host": "localhost",
        "port": "5432"
        }

# Specify the CSV file name 

csv_file = "gyms_scrape_export.csv" 

# Connect to the PostgresSQL database
try: 
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Connected to the database successfully.")

    # Open the CSV file and load data into PosgreSQL
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Insert each row into the gyms table
            insert_query = """
            INSERT INTO gyms (title, rating, reveiws, description, type, phone, address)
            VALUES (%s, %s,%s, %s,%s, %s,%s);
            """
            cursor.execute(insert_query, (
                row["title"],
                float(row["rating"]) if row["rating"] else None,
                row["reviews"],
                row["description"],
                row["type"],
                row["phone"],
                row["address"]
                ))
    # Commit the transaction
    conn.commit()
    print(f"Data from {csv_file} has been successfully uploaded to the PostgreSQL Database")

except Exception as e:
    print(f"An errror occurred: {e}")

"""
finally:
    # Close the cursor and connection
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.") 

"""
