# Customer Dataset
This sample illustrates the case of a multi-table database with a snowflake schema.
This is only for illustrative purpose; no data analysis can be performed with this sample, given its
tiny size.

## Schema description

The `Customer` is the main statistical unit. It is described by the following snowflake schema:
```
    Customer
    |
    |-- Address
    |
    |-- Services
        |
        |-- Usages
```      
- A customer:
  - has at most 1 address (0:1 relationship)
  - has at most n services (0:n relationship)
- A service has at most n usages (0:n relationship).

In the Khiops dictionary, 0:1 relationships are described using the `Entity` keyword, whereas 0:n
relationships are described using the `Table` keyword.

The customer, its address, services and usages constitute the customer's file. All the secondary
records "belong" to the customer's file, and their keys are organized hierarchically.


## Mapping to table files

A multi-table database, described using a dictionary, has to be mapped to a set of table files. Each
node of a folder, identified by its data root table and a data path, must be mapped to a table file.

The mapping `Customer` schema is the following:

| Root       | Path                 | Data File      |
|------------|----------------------|----------------|
| `Customer` |                      | `Customer.txt` |
| `Customer` |  `Address`           | `Address.txt`  |
| `Customer` |  `Services`          | `Service.txt`  |
| `Customer` |  ``Services`Usages`` | `Usage.txt`    |


## Sorting a multi-table database

For efficiency reasons, the analysis of a multi-table database requires the all data files are
sorted by key. The `sort_and_recode_customer.py` python script contains the `sort_customer_database`
function that sorts the `Customer` database using the default key (`id_customer`).

You can test the script on an unsorted version of the `Customer` dataset located in the `unsorted`
directory.

## Recoding a multi-table database

The `sort_and_recode_customer.py` python script also contains a `recode_customer_database` function
that allows to recode `Customer` multi-table database (note that for recoding the database must be
sorted by key, see above).

The input database must be fully specified, with table files for the folder.

The output database must specify at least one output table file, for the root of the folder.
The other tables of the folder can also be specified, if requested.

The `recode_customer_database` function recodes the `Customer` table by adding new attributes that
summarizing the content of each customer file. The results are stored in `Recoded_Customer.txt`
file.

You may consult the file `CustomerRecoded.kdic` to see the exact table transformation.
