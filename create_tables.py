import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
        
    INPUT:
    - cur : psycopg2.connect.cursor. That use to execute PostgreSQL 
    - conn : psycopg2.connect. That use to create connection to PostgreSQL
    
    """
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create each table using the queries in `create_table_queries` list.
        
    INPUT:
    - cur : psycopg2.connect.cursor. That use to execute PostgreSQL 
    - conn : psycopg2.connect. That use to create connection to PostgreSQL
    
    """
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Prepare or Reset our environment with create all necessary of this project.
    
    - Read the config values from `dwh.cfg`
    - Establishes connection with the sparkifydwh database on Amazon Redshift and gets
    cursor to it.  
    - Drops (if exists) and Creates all tables. 
    - Finally, closes the connection. 
    """
    
    # Read the config values from `dwh.cfg`
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # Create connection and cursor for access the sparkifydwh database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    # Drops (if exists) and Creates all tables.
    drop_tables(cur, conn)
    create_tables(cur, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()