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

# Calculating and comparing statistical properties for five different countries comparing different indicators

# Using pandas describe function to calculate statistical properties for five countries
print("\nCalculating describe of Methane emissions (% change from 1990) for five different countries")
print('\nDescribe\n', df_years.iloc[4:, [31, 107, 183, 259, 335]].describe())

# Calculating mean using numpy for five countries
print("\nCalculating mean of Methane emissions (% change from 1990) for five different countries")
print('\nMean\n', np.mean(df_years.iloc[4:, [31, 107, 183, 259, 335]]))

# Calculating standard deviation using numpy for five countries
print("\nCalculating Standard Deviation of Methane emissions (% change from 1990) for five different countries")
print('\nStandard Deviation\n', np.std(df_years.iloc[4:, [31, 107, 183, 259, 335]]))

print("\nCalculating Kurtosis of population growth (annual %) indicator for three countries")

# Calculating kurtosis using scipy.stats for Belgium
print('\nKurtosis of Belgium :', st.kurtosis(df_countries.iloc[4, 4:]))

# Calculating kurtosis using scipy.stats for Bulgaria
print('Kurtosis of Bulgaria :', st.kurtosis(df_countries.iloc[100, 4:]))

# Calculating kurtosis using scipy.stats for Colombia
print('Kurtosis of Colombia :', st.kurtosis(df_countries.iloc[200, 4:]))

print("\nCalculating Skewness of population growth (annual %) indicator for three countries")
# Calculating skewness using scipy.stats for Belgium
print('\nSkewness of Belgium :', st.skew(df_countries.iloc[4, 4:]))

# Calculating skewness using scipy.stats for Bulgaria
print('Skewness of Bulgaria :', st.skew(df_countries.iloc[100, 4:]))

# Calculating skewness using scipy.stats for Colombia
print('Skewness of Colombia :', st.skew(df_countries.iloc[200, 4:]))

# Calculating correlation between indicators for Belgium and Bulgaria
correlation_df = df_countries.iloc[[2, 4, 50, 38, 43, 74, 75, 78, 80, 126, 114], 5:12]
print('\nPearson Correlation \n', correlation_df.corr())
# Defining correlation using Kendall method
print('\nKendall Correlation \n', correlation_df.corr(method='kendall'))

# Plotting heat map to calculate correlation between indicators
plt.figure(figsize=(15, 15))
cbm = plt.imshow(correlation_df.corr(), aspect='auto')
cb = plt.colorbar(cbm)
cb.set_label('Correlation Range', fontsize=60)
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Urban population',
                                'Population, total',
                                'Energy use',
                                'CO2 emissions from solid fuel consumption',
                                'CO2 emissions from liquid fuel consumption',
                                'Arable land',
                                'Agricultural land'], rotation=90, fontsize=30)
plt.yticks([0, 1, 2, 3, 4, 5, 6], ['Urban population',
                                'Population, total',
                                'Energy use',
                                'CO2 emissions from solid fuel consumption',
                                'CO2 emissions from liquid fuel consumption',
                                'Arable land',
                                'Agricultural land'], fontsize=30)

# Plotting line graph of average Methane Emission for five countries
plt.figure(figsize=(40, 40))
plt.rcParams.update({'font.size': 60})
plt.plot(np.mean(df_years.iloc[4:, [31, 107, 183, 259, 335]]), label='Methane emission', linewidth=20)
plt.xlabel('\nCountries', fontsize=60)
plt.ylabel('\nMean of Methane emissions (% change from 1990)', fontsize=60)
plt.title('Average Methane emission of five countries', fontsize=70)
plt.legend()
plt.show()

# Plotting the line graph between two indicators: Co2 emissions from solid fuel consumption
# and Co2 emissions from liquid fuel consumption over the years
plt.figure(figsize=(10, 8))
plt.rcParams.update({'font.size': 17})
plt.plot(df_countries.iloc[37, 20:30], label='Co2 emissions from solid fuel consumption (% of total)', color='red', linewidth=3)
plt.plot(df_countries.iloc[42, 20:30], label='Co2 emissions from liquid fuel consumption (% of total)', color='blue',
         linewidth=3)
plt.xlabel('Years', fontsize=15)
plt.ylabel('Co2 emission Percentage', fontsize=15)
plt.title('Co2 emission over years for Belgium', fontsize=20)
plt.legend(fontsize=10, loc='upper right')
plt.show()

# Plotting pie chart of electric power consumption over the years (1976-1985)
plt.figure(figsize=(30, 30))
plt.rcParams.update({'font.size': 34})
years = ['1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985']
plt.pie(df_countries.iloc[50, 20:30], labels=years, autopct='%1.1f%%')
plt.legend(loc='upper right')
plt.title('Electric power consumption (kWh per capita)', fontsize=55)
plt.show()

# Plotting graph of Energy use (kg of oil equivalent per capita) for five countries
plt.figure(figsize=(40, 40))

