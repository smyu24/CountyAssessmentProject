# display csv in years in toggleable formal with years (descending on the top row) ('22-'19)
import os
import polars as pl
# separate by HUD Area Code, then get HUD Metro Fair Market Rent Area Name; all relevant data per
import pandas as pd
pd.read_excel("FY23_FMRs.xlsx")
#print((pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2019.csv")).head())
# @st.cache(allow_output_mutation=True, show_spinner="Fetching data from API...") # fetch from API LOOK HERE
def get_geom_data():
    list_of_df=[]
    list_of_df.append(pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2019.csv"))
    # list_of_df.append(pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2020.csv"))
    # list_of_df.append(pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2021.csv"))
    # list_of_df.append(pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2022.csv"))
    # list_of_df.append(pl.read_csv("https://github.com/smyu24/CountyAssessmentProject/blob/main/mainProj/FMR_Data/2023.csv"))

    df = pl.concat(list_of_df)
    output = (
            df.groupby("HUD Area Code")
            .agg(
                pl.col("HUD Metro Fair Market Rent Area Name"),
                pl.col("SAFMR 0BR"),
                pl.col("SAFMR 0BR - 90% Payment Standard"),
                pl.col("SAFMR 0BR - 110% Payment Standard"),
                pl.col("SAFMR 1BR"),
                pl.col("SAFMR 1BR - 90% Payment Standard"),
                pl.col("SAFMR 1BR - 110% Payment Standard"),
                pl.col("SAFMR 2BR"	),
                pl.col("SAFMR 2BR - 90% Payment Standard"),
                pl.col("SAFMR 2BR - 110% Payment Standard"),
                # pl.col(),
                
                # pl.first("last_name"),
"SAFMR 3BR"	
"SAFMR 3BR - 90% Payment Standard"	
"SAFMR 3BR - 110% Payment Standard"	
"SAFMR 4BR"	
"SAFMR 4BR - 90% Payment Standard"	
"SAFMR 4BR - 110% Payment Standard"
                )
              )
    return output
    
#print(get_geom_data())