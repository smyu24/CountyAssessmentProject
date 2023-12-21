# https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2023_code/2023summary.odn

import pandas as pd

# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

prefix_file_path = "/content/drive/MyDrive/FairMarketRents_Analysis_Data/"

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

df=pd.read_excel(r"mainProj/Florida/FloridaData.xlsx")

df1=df.drop(df.columns[[0, 1, 2]], axis = 1) # column cut
df1=df1.rename(columns=df1.iloc[0])
# print(df1.head(0))
df1=df1.drop(index=[0]) # drop top row
df1=df1.dropna(how='all')


NicheRankingFl=[
    'Leon County',
    'Seminole County',
    'Alachua County',
    'St. Johns County',
    'Hillsborough County',
    'Orange County',
    'Brevard County',
    'Sarasota County',
    'Pinellas County',
    'Clay County',
    'Martin County',
    'Dual County',
    'Okaloosa County',
    'Palm Beach County',
    'Indian River County',
    'Nassau County',
    'Escambia County',
    'Broward County',
    'Manatee County',
    'Walton County',
    'Paso County',
    'Santa Rosa County',
    'Lake County',
    'Monroe County',
    'Lee County',
    'Collier County',
    'Wakulla County',
    'Bay County',
    'Flagler County',
    'Volusia County',
    'Sumter County',
    'Union County',
    'Jackson County',
    'Lafayette County',
    'Columbia County',
    'Suwannee County',
    'Polk County',
    'Highlands County',
    'Marion County',
    'Charlotte County',
    'Calhoun County',
    'Miami-Dade County',
    'Dixie County',
    'Hernando County',
    'Gilchrist County',
    'Osceola County',
    'St. Lucie County',
    'Okeechobee County',
    'Gulf County',
    'Glades County',
    'Taylor County',
    'Citrus County',
    'Liberty County',
    'Gadsden County',
    'Baker County',
    'Levy County',
    'Franklin County',
    'Jefferson County',
    'Putnam County',
    'Washington County',
    'Holmes County',
    'Bradford County',
    'Hardee County',
    'Hamilton County',
    'Madison County',
    'DeSoto County',
    'Hendry County'
]

res = {val: idx + 1 for idx, val in enumerate(NicheRankingFl)}

df_FloridaNiche=pd.DataFrame.from_dict([res])
print(df_FloridaNiche)


# df1.Niche_Rank = pd.to_numeric(df1.Niche_Rank, errors='coerce') # turns the ranking into float types bc pandas sort doesnt do well with integers
df_temp = df1.sort_values('Niche_Rank', ascending=True)

