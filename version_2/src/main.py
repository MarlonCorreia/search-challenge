from classes import DataBase
from classes import File
import sys


def index_process():
    file = File('dump/catalogo_produtos.json')
    db = DataBase()
    db.create_table()
    
    batch = []
    for line in file.open_file():
        product = file.jsonfy_line(line)
        batch.append((product['id'], product['name']))
        
    db.insert_batch(batch)  
    db.create_index()
    db.commit_db()
    db.close_conn()

   
def search():
    db = DataBase()
    
    while True:
        query = input("make a search: ")
        
        if query == "exit":
            break
        elif query != None:
            try:
                result = db.query_db(query)
                print("------ here are your results ------")

                for product in result:
                    print("productId: {} - Name: {}".format(product[0], product[1]))
            except:
                print("No products Found")
            
if __name__ == "__main__": 
    try:
        if sys.argv[1] == "search":
            search()
        elif sys.argv[1] == "index":
            index_process()
    except:
        index_process()  
        search()
    
