# CustmoerExtended Dataset
This sample illustrates the case of a multi-table database with a snowflake schema and external
tables. This is only for illustrative purposes; no data analysis can be performed with this sample,
given its tiny size.

## Schema description

As in the `Customer` dataset, the `Customer` is the main statistical unit. This time it is described 
by a more complex snowflake schema:
```
    # Customer hierarchy
    Customer
    |
    |-- Address
    |   |
    |   |.. City
    |
    |-- Services
        |
        |.. Product
        |
        |-- Usages
            |
            |.. Product

    # City hierarchy
    City
    |
    |.. Country

    # Country hierarchy
    Country

    # Product hierarchy
    Product

```      
There are three additional entities independent from `Customer`: `City`, `Country` and `Product`
which are **external tables**.

`Customer` hierarchy:
- A customer:
  - has at most 1 address (0:1 relationship)
  - has at most n services (0:n relationship)
- A service has at most n usages (0:n relationship).
- A service:
  - references a unique product
  - has at most n usages (0:n relationship).
- An usage references a unique product (the same that references the corresponding service)
- An address references a unique city

`City` hierarchy:
- A city references a unique country


The `Country` and `Product` hierarchy consists only of a single table.

The references to records in external tables must be 0:1 relationships (`Entity` dictionary keyword)
and the keys are spcefied explicitly between brackets (eg. `Entity(City) city [id_city]`)

A mental model for relationships:
- Relations described by the main table key may be thought "has-a" (eg. a customer has
  a service)
- Relations described by a foreing key (ie. external tables) may be thought as "references-to" (eg.
  a city references a country)


## Mapping to table files
A multi-table database, described using a dictionary, has to be mapped to a set of table files. Each
node of a folder, identified by its data root table and a data path, must be mapped to a table file.

The mapping `CustomerExtended` schema is the following:

| Root       | Path                 | Data File      |
|------------|----------------------|----------------|
| `Customer` |                      | `Customer.txt` |
| `Customer` |  `Address`           | `Address.txt`  |
| `Customer` |  `Services`          | `Service.txt`  |
| `Customer` |  ``Services`Usages`` | `Usage.txt`    |
| `City`     |                      | `City.txt`     |
| `Country`                         | `Country.txt`  |
| `Product`                         | `Product.txt`  |


## Recoding a multi-table database

The `recode_customer.py` python script contains the `recode_customer_database` function that allows
to recode `CustomerExtended` database.

The input database must be fully specified, with table files for the folder.

The output database must specify at least one output table file, for the root of the folder.
The other tables of the folder can also be specified, if requested.

The `recode_customer_database` function recodes the `Customer` table by adding new attributes that
summarizing the content of each customer file. The results are stored in `Recoded_Customer.txt`

You may consult the file `CustomerRecoded.kdic` to see the exact table transformation.
