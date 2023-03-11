import streamlit as st

def home_pg():
    st.title("County Assessment Project")
    st.markdown(
        """
        This is a ...
        """
    )
    
    st.title("About the Variables/Algorithm")
    st.markdown(
        """
        List of variables: 
        
        Things to do: 
            
            1. Add map of subway, bus, railway, and other public transportations after querying the user's selected coords (after county analysis and post location decision)
            
            # https://www.countyhealthrankings.org/explore-health-rankings/county-health-rankings-model/health-factors/health-behaviors/diet-and-exercise/food-environment-index?year=2022
            # https://www.countyhealthrankings.org/explore-health-rankings/our-methods/calculating-ranks

            # basic health and life ammentities

            P_{1}: Probability at birth of not surviving to age 60 (times 100)
                Probability at birth of not surviving to age 60 (% of cohort), 2000–2005. Varies from 7.1% for Japan to 11.8% for the USA. This is the indicator that is best known for all countries (including the ones not on the list). The US has specific values associated with disease characteristics of poverty. Worse values start only at position 35 of the HDI, indicating that many countries could climb on an extended list based on this, knocking down lower ranked countries on the above list.
            P_{2}: Adults lacking functional literacy skills
                People lacking functional literacy skills (% of people scoring in the range called "Level 1" in the International Adult Literacy Survey, age 16–65, 1994–2003). Varies from 7.5% for Sweden to 47.0% for Italy. These figures are higher than most commonly cited illiteracy rates due to the choice of the literacy test.
            P_{3}: Population below income poverty line (50% of median adjusted household disposable income)
                Long-term unemployment (12 months or more, % of labour force), 2005. Varies from 0.4% for the United States to 5.0% for Germany. This indicator has by far the greatest variation, with a value as high as 9.3% at HDI position 37.
            P_{4}: Rate of long-term unemployment (lasting 12 months or more)
                Population below 50% of median adjusted household disposable income (%), 1994–2002. Varies from 5.4% for Finland to 17% for the US.

            poverty rate by state
            gender workforce
            economic growth / projected growth
            Financial crises
            Monopoly, labor, consolidation, and competition
            Aggregate demand - Income inequality is claimed to lower aggregate demand, leading to large segments of formerly middle class consumers unable to afford as many goods and services. This pushes production and overall employment down.
            Income mobility - move from one income group into another; economic opportunity
                Over lifetimes
                Between generations
            Poverty
            Debt

            Political polarization
            Political inequality
            Class system
            Political change
            Health
            Financing of social programs
            Justice
            Education
            Parenting assistance
            Healthcare
            Public welfare and infrastructure spending
            Taxes
            Tax expenditures

            Gini index between states - compare inequality (by race, gender, employment) within and between jurisdictions, using a variety of income measures and data sources, with differing results

            # variables to take into consideration into the algorithm
                * nearby biology affluence
                * county economical affluence
                * community investment
                * population density
                * safety/crime (fbi data and the type of crimes (petty to serious))
                * house prices (rising, falling, stagnant (potential of growth))
                * GIS data
                * community activity/involvment
                * neighborhood data??
                * user’s marital status, education, number of dependents, and employments
                * public transportation
            Labor force participation rate

            Maybe: 
                * "types of people" such as race, ethnicity, religion?
                * geo restrictions such as restricting analysis to west coast or east coast, etc

            Kit towards certain groups of individuals:
                - workers: (by major, layoffs, hirings, median salary)
                - parents: (education pre k to highschool, parks, safety, tree density, health care quality(readyness), etc)
                - sickly: (air purity, pollution, )
                - 20-30 yrs: population pyramid
                - students: higher education pursuement rates

            # Design
            A single page web page that allows users to select all factors possible, updating and submitting relevant information and then updating the page to do adequete analysis and output.
            factors such as layoffs, major type, age, health status, etc

            ## output
            graphs, figures, numerical analysis 
            state and homes that have the most potential for growth (residential status only; no commerical)

            ### TODO
            a way to cross reference and triangulate for data quality and quantity control. this allows us to have a greater sample size without compromising data quality or have repetition

            Could use KML file data to show general GIS in future implementations
            (human modified geography data)
        """
    )

    st.title("Sources")
    st.markdown(
        """
        [Data Commons](https://www.datacommons.org/)
        [Data.org](https://data.org/)
        [Kaggle](https://www.kaggle.com/)
        [Redfin](https://www.redfin.com/)
        [Zillow](https://www.zillow.com/)
        [FBI](https://www.fbi.gov/)
        [BLS](https://www.bls.gov/)
        [EPA](https://www.epa.gov/)
        [Google](https://google.com)
        """
    )

    st.info("Toggle the sidebar menu on the left to navigate to different pages.")
    st.button('Click me')
    st.checkbox('I agree')
    st.radio('Pick one', ['cats', 'dogs'])
    st.selectbox('Pick one', ['cats', 'dogs'])
    st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    st.slider('Pick a number', 0, 100, key="1231")
    st.select_slider('Pick a size', ['S', 'M', 'L'])
    st.text_input('First name')
    st.number_input('Pick a number', 0, 10)
    st.text_area('Text to translate')
    st.date_input('Your birthday')
    st.time_input('Meeting time')
    st.file_uploader('Upload a CSV')