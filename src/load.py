from extract_sql_server import *

def load_data(dataframe,table_name):
    global conn
    if not conn:
        try:
            conn=establish_conn()
        except Exception as e:
            print(f"Error connetion:{e}")
            return False
    cursor=conn.cursor()
    try:
        print(f'\n Preparing to create table {table_name}\n...')
        df=pd.read_sql(f"select * from {table_name}",conn)
        if not df.empty:
            response=input(f'\n{table_name} already exists.\nDo you want to delete table {table_name}..?\nSelect Y for deleting, anyother will skip creation..!\n')
            if response.lower()=='y':
                cursor.execute(f"drop table {table_name}")
                print(f'Successfully dropped table {table_name}.')
            else:
                print('\nNew table creation denied or invalid response. Table creation terminated.')
                return None
                
        cursor.execute(f"""create table {table_name}
                       (Proj_name varchar(100),
                       Owner_name varchar(100),
                       [Start] DATE,
                       [End] DATE,
                       Priority_Level varchar(100),
                       Budget float,
                       Status varchar(100))
                       """)
        conn.commit()
        print(f"Table {table_name} created successfully!")
    except Exception as e:
        print(f"Error creating table:{e}")
        return None
    try:
        print(f"Inserting data into {table_name}..")
        for row in dataframe.itertuples():
            cursor.execute(f'''
    insert into {table_name}
       values(?,?,?,?,?,?,?)
       ''',
       row.Proj_Name,
       row.Owner_Name,
       row.Start,
       row.End,
       row.Priority_Level,
       row.Budget,
       row.Status
                  )
        conn.commit()
        print(f"Insertion success.")
    except Exception as e:
        print(f"Error inserting data:{e}")
        return None
    finally:
        if cursor:
            cursor.close()