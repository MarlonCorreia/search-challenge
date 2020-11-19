import unittest
import src.classes as classes

class TestCatalogClass(unittest.TestCase):

    def setUp(self):
        self.c = classes.Catalog()
        self.c.add_products(10, "product_name")

    def test_get_product_name(self):
        response = self.c.get_product_name(10)

        self.assertEqual(response, "product_name")
    
    def test_add_product(self):
        size_before = len(self.c.get_products())
        self.c.add_products(12345, "other_product")

        self.assertEqual(size_before, len(self.c.get_products()) -1)

    def test_get_products(self):
        products = self.c.get_products()

        self.assertNotEqual(products, {})

class TestIndexesClass(unittest.TestCase):

    def setUp(self):
        self.indexes = classes.Indexes()
    
    def test_sanitize_product(self):
        string = "Estojo, Xtrem, Crush, 843 1,4 Litros Black Camouflage"
        result = self.indexes.sanitize_product_name(string)

        self.assertEqual(result, "Estojo Xtrem Crush 843 1,4 Litros Black Camouflage")

    def test_add_to_index(self):
        self.indexes.add_to_index(876, "iphone xs capa") 

        self.assertEqual(self.indexes.indexes["iphone"], [876])
        self.assertEqual(self.indexes.indexes["xs"], [876])
        self.assertEqual(self.indexes.indexes["capa"], [876])
    
    def test_matching_id_for_query(self):
        lista = [10, 20, 30, 33, 10, 40, 50, 10]
        qtd = 3
        result = self.indexes.find_matching_ids_for_all_query_words(lista, qtd)

        self.assertEqual(result, [10])

    def test_query_index(self):
        self.indexes.add_to_index(7658, "maquina de lavar")
        self.indexes.add_to_index(9382, "maquina secar")

        single_query = self.indexes.query_index("lavar".split())
        multi_query = self.indexes.query_index("maquina".split())

        self.assertEqual(single_query, [7658])
        self.assertEqual(multi_query, [7658, 9382])        

if __name__ == '__main__':
    unittest.main() 
