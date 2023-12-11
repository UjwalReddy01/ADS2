# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:57:46 2023

@author: HP
"""

# Importing pandas package to read the file, for deriving pandas features and stats properties
import pandas as pd
# Importing numpy to read statistical properties
import numpy as np
# Importing matplotlib package for data plotting and visualization
import matplotlib.pyplot as plt
# Importing scipy functions to calculate skewness and kurtosis
import scipy.stats as st

# Defining a function to produce two dataframes, one with countries as columns and one with years as columns
def read_csv_and_transpose(input_file, selected_countries):
    data = pd.read_csv(input_file)
    # Replacing the null values with zeroes using fillna() method
    filled_data = data.fillna(0)
    selected_data = filled_data[filled_data['Country Name'].isin(selected_countries)]
    df_countries = pd.DataFrame(selected_data)
    print(df_countries)
    # Transposing data to derive a dataframe with years as columns
    transpose = pd.DataFrame.transpose(selected_data)
    header = transpose.iloc[0].values.tolist()
    transpose.columns = header
    transpose = transpose.iloc[1:]
    df_years = transpose
    print(transpose)
    return df_countries, df_years

# Calling the function to produce two dataframes by choosing a few countries
df_countries, df_years = read_csv_and_transpose('API_19_DS2_en_csv_v2_4700503-Copy.csv', ['Belgium', 'Bulgaria', 'Colombia', 'Finland', 'United Kingdom'])


