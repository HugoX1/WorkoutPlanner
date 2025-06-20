import pyodbc
from argon2 import PasswordHasher

ph = PasswordHasher()

connection_string = (
    r"Driver=ODBC Driver 17 for SQL Server;"
    r"Server=DESKTOP-T0MNT6G\SQLEXPRESS;"
    r"Database=WorkoutPlanner;"
    r"UID=TEST;"
    r"PWD=TEST123;"
    r"Column Encryption Setting=Enabled;")

def verify_user(username, password):
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT user_id, password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
       
        cursor.close()
        connection.close()

        if result:
            try:
                if result and ph.verify(result[1], password):
                    return True
            except Exception as error:
                print(f"Error! Code: {type(error).__name__}, Message: {error}")
        else:
            return False
        
    except Exception as error:
        print(f"Error! Code: {type(error).__name__}, Message: {error}")

def sign_up(username, email, password):
    print('signing up')
    
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        password_hash = ph.hash(password)

        print(username, email, password)

        insert_query = '''
            INSERT INTO users (full_name, email, password_hash)
            VALUES (?, ?, ?)
        '''
        
        cursor.execute(insert_query, (username, email, password_hash))
        connection.commit()
        return True

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
        
def getDataFromID(userId):
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT full_name, email FROM users WHERE user_id = ?", (userId,))
        result = cursor.fetchone()
       
        cursor.close()
        connection.close()

        print(result)
        return result  
    
    except Exception as error:
        print(f"Error! Code: {type(error).__name__}, Message: {error}")