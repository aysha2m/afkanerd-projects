import sqlite3
import pandas as pd

db_path = r'C:\Users\itcomplex\Desktop\vscpp\vault.db'

db_path = r'C:\Users\itcomplex\Desktop\vscpp\vault.db'  
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()


print("Tables in the database:")
for table in tables:
    print(table[0])
    
conn = sqlite3.connect(db_path)

query = "SELECT * FROM entities LIMIT 5"  

df = pd.read_sql_query(query, conn)


print("Column Names:", df.columns)

print(df.head())

conn.close()


df['date_created'] = pd.to_datetime(df['date_created'])  
print(df['date_created'].describe() )

print(df['country_code'].value_counts())

print(df['server_state'].value_counts())
