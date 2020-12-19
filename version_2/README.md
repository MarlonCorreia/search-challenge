### Update: The PostgreSQL instance that this solution was using was terminated =] 

## PostgreSQL Solution

For this solution, I've strongly used PostgreSQL. Just creating a table to add all of the products existing in inputted file, and then creating an Index using the name of the products.  

## Requirements

You need to have installed in your machine:

- Python 3.8.X
- Pip

To install the dependencies, run:

```bash
$ pip install - r requirements.txt
```

## Usage

To use this service, you can run:

```bash
$ python src/main.py
```

This will execute both process of the service, the **population of DB already creating the indexes** and after that, the **search process**. This service can also be called separately by specifying an argument:

- Index process:

```bash
$ python src/main.py index
```

Again, the index process will read the file passed and populate the DataBase, already creating the indexes that can be used to query

- Search:
```bash
$ python src/main.py search
```

In this process, the user will be asked to input a query to make the search 

**Single Query Search**

Returns the first 20 products that has the inputted query in it's name

<img src="https://i.imgur.com/BurPToF.png" width="600">

**Multi Query Search**

Returns the first 20 products that has all the inputted words somewhere in it's name

<img src="https://i.imgur.com/zcPEwMN.png" width="600">

## Performance 

I want to address something about this solution. I'm hosting my PostgreSQL in the free tier of a service called [ElephantSQL](https://www.elephantsql.com/). And this is way it feels a little bit slow, while testing with local postgreSQL or a docker image, it was actually faster than the In Memory Version (version_1). 

My decision of hosting the postgreSQL in this service it's based on two things: avoid unnecessary complicated step for the person who'll test this (local psql configuration) and the fact that this service isn't appropriate for a docker, in my opinion. 

## Tests

To run the tests:

```bash
$  python -m unittest
```

## Observation

For some linux distros, like Ubuntu, use **python3** and **pip3** commands.

