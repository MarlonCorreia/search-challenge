## In memory Solution


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