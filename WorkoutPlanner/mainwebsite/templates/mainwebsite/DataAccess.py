import pyodbc

connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=10.221.64.20\SQLEXPRESS;"
    r"Database=Blackpoint;"
    f"UID=;"
    f"PWD=;"
    r"Column Encryption Setting=Enabled;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
