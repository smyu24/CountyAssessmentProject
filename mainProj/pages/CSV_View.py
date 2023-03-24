# display csv in years in toggleable formal with years (descending on the top row) ('22-'19)
import os

# separate by HUD Area Code, then get HUD Metro Fair Market Rent Area Name; all relevant data per 
sibB = os.path.dirname(__file__)
sibB = sibB[:sibB.rindex("\\")]
sibB=sibB+r"\FMR_Data"

print(sibB)

import polars as pl

list_of_df=[]
for filename in os.listdir(r"C:\Users\smyu2\OneDrive\GitHub\CountyAssessmentProj\CountyAssessmentProject\mainProj\FMR_Data"):
    if filename.endswith('.csv'):
        print(filename, os.path.isfile(r"C:\Users\smyu2\OneDrive\GitHub\CountyAssessmentProj\CountyAssessmentProject\mainProj\FMR_Data\2019.xlsx")) # pandas.read_excel(r"C:\Users\smyu2\streamlitProj\CountyAssessmentProject\mainProj\FMR_Data\2019.xlsx", sheet_name=str(filename), index_col=0) 
        list_of_df.append(pl.read_csv(filename))

df = pl.concat(list_of_df)
output = (
        df.groupby("HUD Area Code")
        .agg(
            pl.col("HUD Area Code").mean()
            )
          )
"ZIPCode"
"HUD Area Code"
"HUD Metro Fair Market Rent Area Name"
"SAFMR 0BR"	
"SAFMR 0BR - 90% Payment Standard"	
"SAFMR 0BR - 110% Payment Standard"	
"SAFMR 1BR"	
"SAFMR 1BR - 90% Payment Standard"	
"SAFMR 1BR - 110% Payment Standard"	
"SAFMR 2BR"	
"SAFMR 2BR - 90% Payment Standard"	
"SAFMR 2BR - 110% Payment Standard"	
"SAFMR 3BR"	
"SAFMR 3BR - 90% Payment Standard"	
"SAFMR 3BR - 110% Payment Standard"	
"SAFMR 4BR"	
"SAFMR 4BR - 90% Payment Standard"	
"SAFMR 4BR - 110% Payment Standard"