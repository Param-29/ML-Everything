# import psycopg2
import pandas as pd
'''
conn = psycopg2.connect(database="ny_taxi",
                        host="localhost",
                        user="root",
                        password="root",
                        port="5432")

cursor = conn.cursor()

''' 


df = pd.read_parquet('yellow_tripdata_2022-01.parquet')

print(df.columns)