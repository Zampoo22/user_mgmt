# import mysql.connector

# # Establish a connection to the MySQL server
# connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employees'
# )

# # Create a cursor object to execute SQL queries
# cursor = connection.cursor()

# # Example: Insert data into a table
# insert_query = "INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s)"

# # Data to be inserted
# data_to_insert = ('value1', 'value2', 'value3')

# # Execute the query
# cursor.execute(insert_query, data_to_insert)

# # Commit the changes
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()
