## In memory Solution

For this solution I rely on the creation of two data structure that will represent my catalog of produtos, and the indexes for facilitating the search in this catalog.  

Catalog: 
```json
{
    "productId": {
        "name": "productName"
    }
}
```

Indexes:
```json
{
    "uniqueTermInCatalog": ["productId", "productId", "productId" ...]
}
```

This index structure facilitate the search process because I can simply try to retrive all the products that has an specific term in it's name by calling the position in the dict: 

```python
dict[query] eg: dict['iphone']
```

For the multi query search, I create a list of all the products returning for all the calls in the dict. And then return to the user only the productId's that repeated `{query_size}` times. 

## Requirements

For this solution, I only used standard Python lib's, so Python It's only thing you'll need:

- Python 3.8.X

## Usage

To run this solution, call

```bash
$ python src/main.py
```
After this, the indexes creation process will begin (it takes about 1 sec for this amount of products) and you will prompt to make a search, eg:
 

- Single Query Search

Returns the first 20 produtcs that has the inputed query in it's name

<img src="https://i.imgur.com/BbRF0rD.png" width="600">

- Multi Query Search

Returns the first 20 produtcs that has all the inputed words somewhere in it's name

<img src="https://i.imgur.com/On94Dv3.png" width="600">


Obs: To run Python3 in some Linux distros, like Ubuntu, use `python3`

## Tests 

To run the tests use:

```bash
$ python -m unittest  
```