"""Training of the Accidents dataset

Must be executed within the dataset's directory
"""
from os import path

from khiops import core as kh

# Train the predictor
print("Training classifier for variable 'Gravity' of 'Accidents'")
kh.train_predictor(
    "Accidents.kdic",
    "Accident",
    "Accidents.txt",
    "Gravity",
    "GravityAnalysis",
    additional_data_tables={
        "Accident`Place": "Places.txt",
        "Accident`Vehicles": "Vehicles.txt",
        "Accident`Vehicles`Users": "Users.txt",
    },
    max_trees=0,  # create an interpretable model
    max_constructed_variables=1000,
)

print(f"Results available at GravityAnalysis")
