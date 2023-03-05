# display csv in years in toggleable formal with years (descending on the top row) ('22-'19)
import pandas
import os

sibB = os.path.dirname(__file__)
print(sibB)
sibB = sibB[:sibB.rindex("\\")]
sibB=sibB+r"\FMR_Data"
print(sibB)
print(os.listdir(sibB))
for filename in os.listdir(sibB):
    if filename.endswith('.xlsx'):
        print(filename)
        with pandas.read_excel(fr"{sibB}\{str(filename)}", index_col=0) as f:
            print(f)
            #print(f.columns.ravel())
            #print(f[''].tolist())
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

def find_Area_Code_Per_Year():
    pandas.read_excel(sheet_name="2019.xlsx", index_col=0)
    pandas.read_excel(sheet_name="2020.xlsx", index_col=0)
    pandas.read_excel(sheet_name="2021.xlsx", index_col=0)
    pandas.read_excel(sheet_name="2022.xlsx", index_col=0)
    pandas.read_excel(sheet_name="2023.xlsx", index_col=0)

    # with open('employee_birthday.txt') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #             line_count += 1
    #     print(f'Processed {line_count} lines.')
    return

def display_Results():
    return
