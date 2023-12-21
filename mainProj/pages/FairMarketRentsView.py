import pandas as pd

# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

prefix_file_path = r"C:\Users\smyu2\OneDrive\Documents\GitHub\CountyAssessmentProject\mainProj\FairMarketRents_Data"

# df=pd.read_csv(r"FloridaData.xlsx")

df=pd.read_csv(r"GeoData_FloridaData.csv")



import pandas as pd

# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

sheet_url = 'https://docs.google.com/spreadsheets/d/19cWFCEYeEOBlqEZbWFjHO-2UnPJvPONI8VAqjk8OKVg/edit#gid=416065513'
csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(csv_export_url)

# prefix_file_path = "/content/drive/MyDrive/FairMarketRents_Analysis_Data/"

# df=pd.read_csv(prefix_file_path+"FloridaData.gsheet")

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


df1.Niche_Rank = pd.to_numeric(df1.Niche_Rank, errors='coerce') # turns the ranking into float types bc pandas sort doesnt do well with integers
df_temp = df1.sort_values('Niche_Rank', ascending=True)
df_temp = df_temp.dropna(axis=1, thresh=8)


SELECT_COUNTY = "Alachua County"


def calculate_weighted_score(factors, data):
    if set(factors.keys()) != set(data.keys()):
        raise ValueError("Factors and data keys do not match.")

    weighted_sum = 0
    for factor, weight in factors.items():
        weighted_sum += data[factor] * weight

    return weighted_sum


# Health Outcomes
prematureDeath = 0.5
poorOrFairHealth = 0.1
poorPhysicalHealthDays = 0.1
poorMentalHealthDays = 0.1
lowBirthweight = 0.2

health_outcomes_factors = {
    'prematureDeath': 0.5,
    'poorOrFairHealth': 0.1,
    'poorPhysicalHealthDays': 0.1,
    'poorMentalHealthDays': 0.1,
    'lowBirthweight': 0.2,
}
data = {
    'prematureDeath': df_temp['Death'][SELECT_COUNTY], # just death for now
    'poorOrFairHealth': df_temp[][SELECT_COUNTY],
    'poorPhysicalHealthDays': df_temp[][SELECT_COUNTY],
    'poorMentalHealthDays': df_temp[][SELECT_COUNTY],
    'lowBirthweight': df_temp[][SELECT_COUNTY]
}

weighted_score = calculate_weighted_score(health_outcomes_factors, data)
print(f"Weighted score: {weighted_score}")



# Health Factors
adultSmoking = 0.1
adultObesity = 0.05
foodEnvironmentIndex = 0.02
physicalInactivity = 0.02
accessToExerciseOpportunities = 0.01
excessiveDrinking = 0.025
alcoholImpairedDrivingDeaths = 0.025
sexuallyTransmittedInfection_Diseases = 0.025
teenPregnancy = 0.025

health_factors = {
    'adultSmoking': 0.1,
    'adultObesity': 0.05,
    'foodEnvironmentIndex': 0.02,
    'physicalInactivity': 0.02,
    'accessToExerciseOpportunities': 0.01,
    'excessiveDrinking': 0.025,
    'alcoholImpairedDrivingDeaths': 0.025,
    'sexuallyTransmittedInfection_Diseases': 0.025,
    'teenPregnancy': 0.025,
}

data = {
    '': df_temp[''][SELECT_COUNTY], # no data
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY]
}

weighted_score = calculate_weighted_score(health_factors, data)
print(f"Weighted score: {weighted_score}")


# Clinical Care
percentOfInsured = 0.05
primaryCare = 0.03
dentists = 0.01
mentalHealthProviders = 0.01
preventativeHospitalStays = 0.05
mammographyScreening = 0.025
fluVaccinations = 0.025

clinical_care_factors = {
    'percentOfInsured': 0.05,
    'primaryCare': 0.03,
    'dentists': 0.01,
    'mentalHealthProviders': 0.01,
    'preventativeHospitalStays': 0.05,
    'mammographyScreening': 0.025,
    'fluVaccinations': 0.025,
}
data = {
    'percentOfInsured': (df_temp['Count of People With Health Insurance'][SELECT_COUNTY] / df_temp[''][SELECT_COUNTY]),
    'primaryCare': df_temp[''][SELECT_COUNTY], # no data
    'dentists': df_temp[''][SELECT_COUNTY],
    'mentalHealthProviders': df_temp[''][SELECT_COUNTY],
    'preventativeHospitalStays': df_temp[''][SELECT_COUNTY],
    'mammographyScreening': df_temp[''][SELECT_COUNTY],
    'fluVaccinations': df_temp[''][SELECT_COUNTY]
}

weighted_score = calculate_weighted_score(clinical_care_factors, data)
print(f"Weighted score: {weighted_score}")

# Social Economic
highSchoolCompletion = 0.05
collegePursuement = 0.05
unemployment = 0.1
poverty = 0.075
incomeInequality = 0.025
singleParentHouseholds = 0.025
socialAssociations = 0.025
violentCrime = 0.025
injuryDeaths = 0.025

social_economic_factors = {
    'highSchoolCompletion': 0.05,
    'collegePursuement': 0.05,
    'unemployment': 0.1,
    'poverty': 0.075,
    'incomeInequality': 0.025,
    'singleParentHouseholds': 0.025,
    'socialAssociations': 0.025,
    'violentCrime': 0.025,
    'injuryDeaths': 0.025,
}
data = {
    'highSchoolCompletion': ( (df_temp['Count_Person'][SELECT_COUNTY] - df_temp['Count of People With Educational Attainment Less Than High School'][SELECT_COUNTY]) / df_temp['Count_Person'][SELECT_COUNTY]),
    'collegePursuement': df_temp['Count of People With Educational Attainment of Bachelors Degree or Higher'][SELECT_COUNTY],
    'unemployment': df_temp['Unemployment Rate'][SELECT_COUNTY],
    'poverty': df_temp['Count of Household: Family Household, Below Poverty Level in The Past 12 Months'][SELECT_COUNTY],
    'incomeInequality': df_temp['Gender Income Inequality'][SELECT_COUNTY],
    'singleParentHouseholds': df_temp[''][SELECT_COUNTY], #unknown
    'socialAssociations': df_temp[''][SELECT_COUNTY],
    'violentCrime': df_temp[''][SELECT_COUNTY],
    'injuryDeaths': df_temp[''][SELECT_COUNTY]
}

weighted_score = calculate_weighted_score(social_economic_factors, data)
print(f"Weighted score: {weighted_score}")

# Physical Environment
airPollutionParticulateMatter = 0.025
drinkingWaterViolations = 0.025
housingProblems = 0.02
drivingToWork = 0.02
longCommute = 0.01
publicTransportation = 0.1

physical_environment_factors = {
    'airPollutionParticulateMatter': 0.025,
    'drinkingWaterViolations': 0.025,
    'housingProblems': 0.02,
    'drivingToWork': 0.02,
    'longCommute': 0.01,
    'publicTransportation': 0.1,
}
data = {
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY],
    '': df_temp[''][SELECT_COUNTY]
}

# healthOutcomes
# healthFactors
# clinicalCare
# socialEconomic
# physicalEnvironment

# https://data.cms.gov/api-docs

# County_Health = dict()

 