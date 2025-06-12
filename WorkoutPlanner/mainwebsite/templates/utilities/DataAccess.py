# import pyodbc

# connection_string = (
#     r"Driver={ODBC Driver 17 for SQL Server};"
#     r"Server=10.221.64.20\SQLEXPRESS;"
#     r"Database=Blackpoint;"
#     f"UID=;"
#     f"PWD=;"
#     r"Column Encryption Setting=Enabled;"
# )

# conn = pyodbc.connect(connection_string)
# cursor = conn.cursor()

# def createUser(username, email, password, name):
#     cursor = conn.cursor()
    
#     insert_query = '''
#             INSERT INTO users (username, email, password_hash, full_name)
#             VALUES (?, ?, ?, ?)
#         '''
        
#     cursor.execute(insert_query, (username, email, password_hash, full_name))
#     conn.commit()