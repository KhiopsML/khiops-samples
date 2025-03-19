"""Training of the Accidents dataset

Must be executed within the dataset's directory
"""

from khiops import core as kh

# Train the predictor
print("Training classifier for variable 'Gravity' of 'Accidents'")
kh.train_predictor(
    "Accidents.kdic",
    "Accident",
    "Accidents.txt",
    "Gravity",
    "./GravityAnalysisResults.khj",
    additional_data_tables={
        "Place": "Places.txt",
        "Vehicles": "Vehicles.txt",
        "Vehicles/Users": "Users.txt",
    },
    max_trees=0,  # create an interpretable model
    max_constructed_variables=1000,
)

print("Results available at ./GravityAnalysisResults.khj")
