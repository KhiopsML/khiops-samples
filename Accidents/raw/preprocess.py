import os
import shutil

from khiops import core as kh


# Preprocess:
# - transforms the tables according to AccidentsPreprocess.kdic
# - sorts the transformed tables by their keys
# - reencodes it in UTF-8
def preprocess_file(dictionary_name, raw_table_path, target_dir):
    # Transform and sort the raw data table
    kh.deploy_model(
        "./AccidentsPreprocess.kdic",
        dictionary_name,
        raw_table_path,
        f"./Unsorted{dictionary_name}s.txt",
        header_line=True,
        field_separator=",",
        output_header_line=True,
        output_field_separator="\t",
    )
    kh.sort_data_table(
        "../Accidents.kdic",
        dictionary_name,
        f"./Unsorted{dictionary_name}s.txt",
        f"./Latin1{dictionary_name}s.txt",
        header_line=True,
        field_separator="\t",
        output_header_line=True,
        output_field_separator="\t",
    )

    # Encode in UTF-8
    os.makedirs(target_dir, exist_ok=True)
    with open(f"./Latin1{dictionary_name}s.txt", "rb") as latin1_file:
        target_path = f"{target_dir}/{dictionary_name}s.txt"
        with open(target_path, "wb") as output_file:
            output_file.write(latin1_file.read().decode("latin1").encode("utf8"))

    # Clean temporary files
    os.remove(f"./Unsorted{dictionary_name}s.txt")
    os.remove(f"./Latin1{dictionary_name}s.txt")


if __name__ == "__main__":
    # Preprocess the table
    raw_tables = {
        "Accident": "caracteristiques-2018.csv",
        "Place": "lieux-2018.csv",
        "Vehicle": "vehicules-2018.csv",
        "User": "usagers-2018.csv",
    }
    for dictionary_name, raw_table_path in raw_tables.items():
        print(f"Preprocessing Table '{dictionary_name}'")
        preprocess_file(dictionary_name, raw_table_path, "./NoTarget")

    # Create the target
    print(
        "Creating Target 'Gravity' in Table 'Accidents' and "
        "Removing 'Gravity' from Table 'Users'"
    )
    kh.deploy_model(
        "./AccidentsCreateTarget.kdic",
        "Accident",
        f"./NoTarget/Accidents.txt",
        f"../Accidents.txt",
        additional_data_tables={
            "Accident`Place": "./NoTarget/Places.txt",
            "Accident`Vehicles": "./NoTarget/Vehicles.txt",
            "Accident`Vehicles`Users": "./NoTarget/Users.txt",
        },
        output_additional_data_tables={
            "Accident`Place": "../Places.txt",
            "Accident`Vehicles": "../Vehicles.txt",
            "Accident`Vehicles`Users": "../Users.txt",
        },
    )

    # Clean up
    shutil.rmtree("./NoTarget")
