# display csv in years in toggleable formal with years (descending on the top row) ('22-'19)
import pandas
import os

# separate by HUD Area Code, then get HUD Metro Fair Market Rent Area Name; all relevant data per 
sibB = os.path.dirname(__file__)
print(sibB)
sibB = sibB[:sibB.rindex("\\")]
sibB=sibB+r"\FMR_Data"
print(sibB)
print(os.listdir(sibB))
for filename in os.listdir(sibB):
    if filename.endswith('.xlsx'):
        print(filename, os.path.isfile(filename)) # pandas.read_excel(r"C:\Users\smyu2\streamlitProj\CountyAssessmentProject\mainProj\FMR_Data\2019.xlsx", sheet_name=str(filename), index_col=0)
        xls = pandas.ExcelFile('2019.xlsx')
        print(xls)
        df1 = pandas.read_excel(xls, '2019.xlsx')
        print(df1)
        with pandas.read_excel(fr"{sibB}\{str(filename)}", sheet_name=str(filename), index_col=0) as f:
            print(f)
            #print(f.columns.ravel())
            #print(f[''].tolist())
"""
excel = pd.ExcelFile("stocks.xlsx")
excel.sheet_names # outputs sheet names in directory

excel = pd.ExcelFile("stocks.xlsx") # parses excel and outputs in row and column format
df = excel.parse()
df.head()

https://www.nbshare.io/notebook/894032303/Pandas-Read-and-Write-Excel-File/
"""

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

def display_Results():
    return
