import os

from khiops import core as kh

# Preprocess:
# - transforms the tables according to AccidentsPreprocess.kdic
# - sorts the transformed tables by their keys
output_sep = "\t"
print("Creating ../Vehicles.txt")
kh.deploy_model(
    "AccidentsPreprocess.kdic",
    "Vehicle",
    "./vehicules-2018.csv",
    "./UnsortedVehicles.csv",
    header_line=True,
    field_separator=",",
    output_header_line=True,
    output_field_separator=output_sep,
)
kh.sort_data_table(
    "../Accidents.kdic",
    "Vehicle",
    "./UnsortedVehicles.csv",
    "../Vehicles.txt",
    sort_variables=["AccidentId", "VehicleId"],
    output_header_line=True,
    output_field_separator=output_sep,
)
os.remove("./UnsortedVehicles.csv")

print("Creating ../Users.txt")
kh.deploy_model(
    "AccidentsPreprocess.kdic",
    "User",
    "./usagers-2018.csv",
    "./UnsortedUsers.csv",
    header_line=True,
    field_separator=",",
    output_header_line=True,
    output_field_separator=output_sep,
)
kh.sort_data_table(
    "../Accidents.kdic",
    "User",
    "./UnsortedUsers.csv",
    "../Users.txt",
    sort_variables=["AccidentId", "VehicleId"],
    output_header_line=True,
    output_field_separator=output_sep,
)
os.remove("./UnsortedUsers.csv")

print("Creating ../Places.txt")
kh.deploy_model(
    "AccidentsPreprocess.kdic",
    "Place",
    "./lieux-2018.csv",
    "./UnsortedPlaces.csv",
    header_line=True,
    field_separator=",",
    output_header_line=True,
    output_field_separator=output_sep,
)
kh.sort_data_table(
    "../Accidents.kdic",
    "Place",
    "./UnsortedPlaces.csv",
    "../Places.txt",
    sort_variables=["AccidentId"],
    output_header_line=True,
    output_field_separator=output_sep,
)
os.remove("./UnsortedPlaces.csv")

print("Creating ../Accidents.txt")
kh.deploy_model(
    "AccidentsPreprocess.kdic",
    "Accident",
    "./caracteristiques-2018.csv",
    "./UnsortedAccidents.csv",
    header_line=True,
    field_separator=",",
    output_header_line=True,
    output_field_separator=output_sep,
)
kh.sort_data_table(
    "../Accidents.kdic",
    "Accident",
    "./UnsortedAccidents.csv",
    "../Accidents.txt",
    sort_variables=["AccidentId"],
    output_header_line=True,
    output_field_separator=output_sep,
)
os.remove("./UnsortedAccidents.csv")
