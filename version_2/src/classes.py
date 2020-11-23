import psycopg2
import psycopg2.extras
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class DataBase():
    
    def __init__(self):
        self.conn = psycopg2.connect("""
        host={}
        dbname={} 
        user={} 
        password={}
        """.format(os.environ['HOST_DB'], os.environ['DBNAME'], os.environ['USER_DB'], os.environ['PASSWORD_DB']))
        self.cur = self.conn.cursor()

    def create_table(self):
         self.cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Products (
            Id varchar(255) UNIQUE,
            name varchar
        );
        """)

    def insert_batch(self, batch):
        """
        Using execute.batch to reduce the number of roundtrips to the db 
        """
        psycopg2.extras.execute_batch(self.cur ,"INSERT INTO Products(id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING", batch)

    def create_index(self):
        self.cur.execute(""" 
        ALTER TABLE Products
        ADD COLUMN IF NOT EXISTS indexes tsvector;
        UPDATE Products
        SET indexes = to_tsvector(name);
        CREATE INDEX IF NOT EXISTS document_idx
            ON Products(name);
        """)


    def query_db(self, searchterm):
        self.cur.execute("""
        SELECT id, name 
        FROM Products 
        WHERE indexes @@ plainto_tsquery(%s)
        ORDER BY id ASC
        LIMIT 20
        """, (searchterm,))
        return self.cur.fetchall()
    
    def commit_db(self):
        self.conn.commit()

    def close_conn(self):
        self.conn.close()
    
class File():

    def __init__(self, filepath):
        self.filepath = filepath

    def open_file(self):
        with open(self.filepath) as catalog:
            return catalog.readlines()
    
    def jsonfy_line(self, line):
        return json.loads(line)
