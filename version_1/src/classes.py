import json
import re
from collections import Counter


class Catalog():
    """ 
    This is data abstraction for a catalog of products, it consists in a dict:
    {
        productId:{
            "name": productName
        },    
    }    
    """
    products = {}

    def __init__(self, ):
        pass

    def get_products(self):
        return self.products
    
    def get_product_name(self, id):
        try:
            return self.products[id]['name']
        except:
            return

    def add_products(self, id, name):
        self.products[id] = {
            'name': name
        }
        

class Indexes():
    """
    This is a dataStructure that will be used as indexes for product searching:

    {
        unique_Word_In_All_Products_Names_In_The_Catalog: [productId, productId...]
    },

    """
    indexes = {}

    def __init__(self):
        pass
    
    def add_to_index(self, id, name):
        sanitized_name = self.sanitize_product_name(name)
        
        for word in sanitized_name.split():
            try:
                self.indexes[word].add(id)
            except:
                self.indexes[word] = {id}

        return
    
    def query_index(self, query):
        """
        Receive a query as a list of words, example: ["iphone"] or ["iphone", "xs"]
        returns a list of productId's that all the words in the query have in commom on the index 
        """
        if len(query) > 1:
            id_lists = []
            for word in query:
                id_lists += self.indexes[word]

            return self.find_matching_ids_for_all_query_words(id_lists, len(query))
        
        return self.indexes[query[0]]

    def find_matching_ids_for_all_query_words(self, id_lists, query_qtd):
        """
        Receive a list all productId's that had index association with a multiquery search, and the query size
        Returns a list of only the id's that all the query's have in commom. Using Python collections/Couter to represent a multiset
        """
        c = Counter(id_lists)
        commom_ids = [k for k, v in c.items() if v == query_qtd]
        
        return commom_ids

    def sanitize_product_name(self, name):
        """
        Remove the difference of querys like "iphone" and "iphone,"
        """
        name = re.sub(r'(\w+),\s', r'\1 ', name)
        
        return name


class File():
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def open_file(self):
        with open (self.file_path) as catalog:
            return catalog.readlines() 
    
    def jsonfy_line(self, line):
        return json.loads(line)