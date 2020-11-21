import unittest
import testing.postgresql
import psycopg2
import psycopg2.extras
import src.classes as classes

class TestDBClass(unittest.TestCase):

    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()
        self.conn = psycopg2.connect(**self.postgresql.dsn())
        self.cur = self.conn.cursor()
        self.cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Test_batch (
            Id varchar(255) UNIQUE,
            name varchar
        );
        """)

    def test_create_table(self):
        self.cur.execute(""" 
            CREATE TABLE IF NOT EXISTS Products (
            Id varchar(255) UNIQUE,
            name varchar
        );
        """)
     
        bol_response = False
        try:
            self.cur.execute("SELECT EXISTS (SELECT * FROM Products)")
            bol_response = True
        except:
            pass
        
        self.assertEqual(bol_response, True)

    def test_insert_batch(self):
        batch = [(111, "iphone x"), (23434, "Galaxy Samsung s5"), (9459459, "Luqidificador")]
        psycopg2.extras.execute_batch(self.cur ,"INSERT INTO Test_batch(id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING", batch)

        self.cur.execute("""
            SELECT COUNT(*) 
            FROM Test_batch
            WHERE id IN ('111', '23434', '9459459');
        """)

        result = self.cur.fetchall()
        
        self.assertEqual(result[0][0], 3 )


if __name__ == '__main__':
    unittest.main() 