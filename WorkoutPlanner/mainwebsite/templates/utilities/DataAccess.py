import pyodbc
from argon2 import PasswordHasher

ph = PasswordHasher()

connection_string = (
    "Driver=ODBC Driver 17 for SQL Server;"
    "Server=4CD717890BFCP\SQLEXPRESS;"
    "Database=QuotingSystem;"
    "UID=SoftE;"
    "PWD=SoftE;")

def verify_user(username, password):
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT userID, password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
       
        cursor.close()
        connection.close()

        if result:
            try:


                if result and ph.verify(result[1], password):
                   
                    return "correct"
            except Exception as error:
                print(f"Error! Code: {type(error).__name__}, Message: {error}")
        else:
            return "Username or password incorrect! :("
           
       
    except Exception as error:
        print(f"Error! Code: {type(error).__name__}, Message: {error}")

def getUserID(username):
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT userID FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
       
        cursor.close()
        connection.close()

        userID = result[0]

     
        return userID  
       
    except Exception as error:
        print(f"Error! Code: {type(error).__name__}, Message: {error}")