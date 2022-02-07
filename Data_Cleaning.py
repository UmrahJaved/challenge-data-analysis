"""
Importing required libraries
"""

import pandas as pd
import numpy as np

"""
Reading csv file using Pandas
"""

immo_web = pd.read_csv("https://raw.githubusercontent.com/adityachugh02/challenge-collecting-data/master/data_clean_2"
                       ".csv")

"""
Finding null values in csv file
"""

missing_values = ["N\a", "na", np.nan]
immo_web = pd.read_csv(
    "https://raw.githubusercontent.com/adityachugh02/challenge-collecting-data/master/data_clean_2.csv",
    na_values=missing_values)
immo_web.isnull().sum()


"""
Replacing null values with correct data
"""


updated_immo_web = immo_web.fillna({
    "bedroom": 2.0, "area": round(immo_web['area'].mean()), "equipped_kitchen": "Installed", "furnished": 0.0,
    "open_fire": 0.0, "terrace": 0.0, "terrace_area": 10.0, "garden": 0.0,
    "garden_area": 5, "surface": round(immo_web['surface'].mean()), "surface_plot": round(immo_web['surface'].mean()),
    "facades": 1.0, "state": "Good", "swimming_pool": 0.0})

"""
Saving updated data to clean_data csv file
"""

updated_immo_web.to_csv("clean_data.csv", index=False)