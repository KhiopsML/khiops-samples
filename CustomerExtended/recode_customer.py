"""The functions in this recode the CustomerExtended dataset

This script must be executed in the same directory of the CustomerExtended dataset.
"""

from khiops import core as kh


def recode_customer_database():
    """Recoding process

    The customer table is a multi-table database using a snowflake schema.
    This function applies a recoding using some new attributes that summarize the
    content of the folder (see variables with derivation rules in the Customer
    dictionary, in file Customer.kdic)
    """
    print("Recoding CustomerExtended database")
    # Set the file paths for caracteristiques
    customer_kdic_path = "CustomerRecoded.kdic"
    customer_data_table_path = "Customer.txt"
    address_data_table_path = "Address.txt"
    service_data_table_path = "Service.txt"
    usage_data_table_path = "Usage.txt"
    city_data_table_path = "City.txt"
    country_data_table_path = "Country.txt"
    product_data_table_path = "Product.txt"
    output_data_table_path = "Recoded_Customer.txt"

    # Recode the database
    kh.deploy_model(
        customer_kdic_path,
        "Customer",
        customer_data_table_path,
        output_data_table_path,
        additional_data_tables={
            "Address": address_data_table_path,
            "Services": service_data_table_path,
            "Services/Usages": usage_data_table_path,
            "/City": city_data_table_path,
            "/Country": country_data_table_path,
            "/Product": product_data_table_path,
        },
    )


if __name__ == "__main__":
    recode_customer_database()
