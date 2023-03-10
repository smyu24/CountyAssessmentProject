# display csv in years in toggleable formal with years (descending on the top row) ('22-'19)
import pandas
import os

# separate by HUD Area Code, then get HUD Metro Fair Market Rent Area Name; all relevant data per 
sibB = os.path.dirname(__file__)
sibB = sibB[:sibB.rindex("\\")]
sibB=sibB+r"\FMR_Data"

print(sibB)
# need perms to modify or read the csv files; chmod is not installed on powershell
df = pandas.read_csv("2019.csv", sep=',', header=0)

# for filename in os.listdir(r"C:\Users\smyu2\OneDrive\GitHub\CountyAssessmentProj\CountyAssessmentProject\mainProj\FMR_Data"):
#     if filename.endswith('.xlsx'):
#         print(filename, os.path.isfile(r"C:\Users\smyu2\OneDrive\GitHub\CountyAssessmentProj\CountyAssessmentProject\mainProj\FMR_Data\2019.xlsx")) # pandas.read_excel(r"C:\Users\smyu2\streamlitProj\CountyAssessmentProject\mainProj\FMR_Data\2019.xlsx", sheet_name=str(filename), index_col=0)
#         xls = pandas.ExcelFile('2019.xlsx')
#         print(xls)
#         df1 = pandas.read_excel(xls, '2019.xlsx')
#         print(df1)
#         with pandas.read_excel(fr"{sibB}\{str(filename)}", sheet_name=str(filename), index_col=0) as f:
#             print(f)

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

