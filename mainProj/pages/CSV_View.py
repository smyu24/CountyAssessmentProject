import polars as pl

pl.Config.set_tbl_hide_dataframe_shape(True)

prefix_file_path = "/content/drive/MyDrive/FMR_Analysis_Data/"

df_2023=pl.read_csv(prefix_file_path+"FY23_FMRs.csv")
df_2023.select(sorted(df_2023.columns))

df_2022=pl.read_csv(prefix_file_path+"FY22_FMRs_revised.csv")
df_2022.select(sorted(df_2022.columns))

df_2021=pl.read_csv(prefix_file_path+"FY21_4050_FMRs_rev.csv")
df_2021.select(sorted(df_2021.columns))



print(df_2023.select(sorted(df_2023.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
),
df_2022.select(sorted(df_2022.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
),
df_2021.select(sorted(df_2021.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
))

print("\n\n\n")

df_23_21=[df_2023.select(sorted(df_2023.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
),
df_2022.select(sorted(df_2022.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
),
df_2021.select(sorted(df_2021.columns)).filter(
    (pl.col('hud_area_code') == 'METRO33860M33860')
)]

print(df_23_21)