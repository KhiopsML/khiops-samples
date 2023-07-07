"""The functions in this script sort and recode the Customer dataset

This script must be executed in the same directory of the Customer dataset.
"""
import os

from khiops import core as kh


def sort_customer_database():
    """Sort each table by key"""
    print("Sorting Customer Dataset by key...")
    # Set the file paths for the "Customer" table and sort it
    customer_kdic_path = "Customer.kdic"
    data_table_path = os.path.join("unsorted", "Customer-unsorted.txt")
    output_data_table_path = os.path.join("sorted", "Customer.txt")
    kh.sort_data_table(
        customer_kdic_path, "Customer", data_table_path, output_data_table_path
    )

    # Set the file paths for the "Address" table and sort it
    data_table_path = os.path.join("unsorted", "Address-unsorted.txt")
    output_data_table_path = os.path.join("sorted", "Address.txt")
    kh.sort_data_table(
        customer_kdic_path, "Address", data_table_path, output_data_table_path
    )

    # Set the file paths for the "Service" table and sort it
    data_table_path = os.path.join("unsorted", "Service-unsorted.txt")
    output_data_table_path = os.path.join("sorted", "Service.txt")
    kh.sort_data_table(
        customer_kdic_path, "Service", data_table_path, output_data_table_path
    )

    # Set the file paths for the "Usage" table and sort it
    data_table_path = os.path.join("unsorted", "Usage-unsorted.txt")
    output_data_table_path = os.path.join("sorted", "Usage.txt")
    kh.sort_data_table(
        customer_kdic_path, "Usage", data_table_path, output_data_table_path
    )


def recode_customer_database():
    """Recoding process

    The customer table is a multi-table database using a snowflake schema.
    This function applies a recoding using some new attributes that summarize the
    content of the folder (see variables with derivation rules in the Customer
    dictionary, in file Customer.kdic)
    """
    print("Recoding Customer database")

    # Set the file paths for caracteristiques
    customer_kdic_path = os.path.join("CustomerRecoded.kdic")
    customer_data_table_path = "Customer.txt"
    address_data_table_path = "Address.txt"
    service_data_table_path = "Service.txt"
    usage_data_table_path = "Usage.txt"
    output_data_table_path = "Recoded_Customer.txt"

    # Deploy the recoding model to the database
    kh.deploy_model(
        customer_kdic_path,
        "Customer",
        customer_data_table_path,
        output_data_table_path,
        additional_data_tables={
            "Customer`Address": address_data_table_path,
            "Customer`Services": service_data_table_path,
            "Customer`Services`Usages": usage_data_table_path,
        },
    )


def all_steps():
    sort_customer_database()
    recode_customer_database()


if __name__ == "__main__":
    all_steps()
