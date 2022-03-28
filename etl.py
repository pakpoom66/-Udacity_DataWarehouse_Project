import configparser
import psycopg2
from sql_queries import *
from time import time

def load_staging_tables(cur, conn):
    """
    Read data from json file, Load the json data to Staging Tables (stg_events, and stg_songs tables). Using the queries in `copy_table_queries` list.
    
    - Log data (s3://udacity-dend/log_data) => stg_events
    - Song data (s3://udacity-dend/song_data) => stg_songs
    
    INPUT:
    - cur : psycopg2.connect.cursor. That use to execute PostgreSQL 
    - conn : psycopg2.connect. That use to create connection to PostgreSQL
    
    """
    
    print("\n\n===== Load Data to Staging Tables =====")
    stagingloadTimes = []
    
    for query in copy_table_queries:
        t0 = time()
        cur.execute(query)
        conn.commit()
        loadTime = time()-t0
        stagingloadTimes.append(loadTime)
        
    for i in range(len(staging_table_list)):
        print(" - {0} {1:.2f} sec\n".format(staging_table_list[i], stagingloadTimes[i]))
        

def insert_tables(cur, conn):
    """
    ETL from Staging Tables (stg_events, and stg_songs table) to Data Models (songplays, users, songs, artists, and time tables). Using the queries in `insert_table_queries` list.
    
    INPUT:
    - cur : psycopg2.connect.cursor. That use to execute PostgreSQL 
    - conn : psycopg2.connect. That use to create connection to PostgreSQL
    
    """
    
    print("===== Insert Data to DWH Tables =====")
    DWHloadTimes = []
    
    for query in insert_table_queries:
        t0 = time()
        cur.execute(query)
        conn.commit()
        loadTime = time()-t0
        DWHloadTimes.append(loadTime)
        
    for i in range(len(dwh_table_list)):
        print(" - {0} {1:.2f} sec\n".format(dwh_table_list[i], DWHloadTimes[i]))

def main():
    """
    Create connection and cursor for access to sparkifydb DWH database. Its Start point for this ETL process. 
    After all insertion successful, it will drop all temp tables and closes the connection.
    
    - Read the config values from `dwh.cfg`
    - Establishes connection with the sparkifydwh database on Amazon Redshift and gets
    cursor to it.  
    - Call load_staging_tables() function for Load json data to Staging Tables
    - Call insert_tables() function for Insert Data from Staging Tables to Data Models
    - Finally, closes the connection. 
    
    """
    
    # Read the config values from `dwh.cfg`
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # Create connection and cursor for access the sparkifydwh database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    # Load json data to Staging Tables
    load_staging_tables(cur, conn)
    
    # Insert Data from Staging Tables to Data Models
    insert_tables(cur, conn)
    
    print('\n***** Summary records each tables *****')
    cur.execute(count_all_tables)
    row = cur.fetchone()
    while row:
       print('The data in "{}" table have {} record(s)'.format(row[0], row[1]))
       row = cur.fetchone()

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()