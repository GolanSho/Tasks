import csv
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Iolredi8b4!",
    database="old_res"
)
cursor = db.cursor()

# Open the CSV file
with open('/home/shapi/Downloads/Lotto.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row if it exists
    # header = next(reader)  # Remove this line if there is no header row

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the values from the row
        # for clm in range(7):
        value1 = row[0]
        value2 = row[1]
        value3 = row[2]
        value4 = row[3]
        value5 = row[4]
        value6 = row[5]
        value7 = row[6]

        # Extract additional values as needed

        # Create the SQL query
        query = "INSERT INTO numbers (num1, num2, num3, num4, num5, num6, num7) VALUES (%s, %s, %s, %s, %s, %s, %s)"  # Modify this query as per your table structure

        # Execute the query with the row values
        cursor.execute(query, (value1, value2, value3, value4, value5, value6, value7))  # Add additional values as needed

        # Commit the changes to the database
        db.commit()

# Close the database connection
db.close()
