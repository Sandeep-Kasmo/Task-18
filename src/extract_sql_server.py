import pyodbc
import pandas as pd
conn=None


def establish_conn():
    global conn
    try:
        conn=pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    r'Server=SANDY\SQLEXPRESS;'
    'Trusted_Connection=yes;'
    'Database=PythonLearningDB;'
        )
        if conn:
            print('connected')
            return conn
    except Exception as e:
        print(f'Errror conneting to sql server:{e}')
        return None

def extract_data(query):
    global conn
    if conn is None:
        try:
            conn=establish_conn()
        except Exception as e:
            print(f'Unable to connect to server:{e}')
            return False
    cursor=conn.cursor()
    try:
        dataframe=pd.read_sql(query,conn)
        return dataframe
    except Exception as e:
        print(f"Unable to load data:{e}")
        return None
    finally:
        if cursor:
            cursor.close()


    


def close_conn():
    global conn
    if conn:
        conn.close()
        print('closed connection')


        

