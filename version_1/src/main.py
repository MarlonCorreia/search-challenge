from classes import Catalog
from classes import Indexes
from classes import File

def index_process():
    f = File("dump/catalogo_produtos.json")
    catalog = Catalog()
    indexes = Indexes()

    for line in f.open_file():
        product = f.jsonfy_line(line)
        catalog.add_products(product['id'], product['name'])
        indexes.add_to_index(product['id'], product['name'].casefold())
    
    search(indexes, catalog)

def search(indexes, catalog):
    while True:
        query = input("Make a search:")
        
        if query == "exit":
            break
        elif query != None:
            try:
                print("---- Here are your results ----")
                max_return = 0
                produts = indexes.query_index(query.casefold().split())
                
                for id in  sorted(produts):
                    if max_return == 20:
                        break
    
                    print("productId: {} - Name: {}".format(id, catalog.get_product_name(id)))
                    max_return += 1
            except:
                print("No products found for this search")

    return

if __name__ == "__main__":
    index_process()