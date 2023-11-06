import streamlit as st
import random

"""
Complete Profile.py to have preset and modifiable settings for user prioities

- workers: (by major, layoffs, hirings, median salary)
- parents: (education pre k to highschool, parks, safety, tree density, health care quality(readyness), etc)
- sickly: (air purity, pollution)
- 20-30 yrs: population pyramid
- students: higher education pursuement rates
"""

def profile():
    st.title("PROFILE")
    st.checkbox('Toggle defintion helper')


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
    

    st.text("1. Power distance (PDI)")
    pdi = st.slider('To which extent you accept that individuals in societies are not equal?',
                    0, 100, 0, help="", key="pdi")

    st.text("2. Individualism (IDV)")
    idv = st.slider('How independent you would like to be in your society?',
                    0, 100, 0, help="", key="idv")

    st.text("3. Masculinity (MAS)")
    mas = st.slider('How much are you driven by competition, achievement and success and able to sacrifice caring for '
                    'others and quality of life?',
                    0, 100, 0, help="", key="mas")

    st.text("4. Uncertainty avoidance (UAI)")
    uai = st.slider('To which extent you feel threatened by ambiguous or unknown situations and try to avoid them ?',
                    0, 100, 0, help="", key="uai")

    st.text("5. Long term orientation (LTO)")
    lto = st.slider('How much do you consider past when dealing with future and present challenges?',
                    0, 100, 0, help="", key="lto")

    st.text("6. Indulgence (IND)")
    ind = st.slider('To which extent you would like to express your desires and impulses??',
                    0, 100, 0, help="", key="ind")


    
    st.text("Access to subway, bus, railway, and other public transportations after querying the user's selected coords (after county analysis and post location decision)")
    st.text("poverty rate by state")
    st.text("gender workforce")
    st.text("economic growth / projected growth")
    st.text("Financial crises")
    st.text("Monopoly, labor, consolidation, and competition")
    st.text("Aggregate demand - Income inequality is claimed to lower aggregate demand, leading to large segments of formerly middle class consumers unable to afford as many goods and services. This pushes production and overall employment down.")
    st.text("Income mobility - move from one income group into another; economic opportunity (Over lifetimes; Between generations)")
    st.text("Poverty")
    st.text("Debt")

    st.text("Political polarization")
    st.text("Political inequality")
    st.text("Class system")
    st.text("Political change")
    st.text("Health")
    st.text("Financing of social programs")
    st.text("Justice")
    st.text("Education")
    st.text("Parenting assistance")
    st.text("Healthcare")
    st.text("Public welfare and infrastructure spending")
    st.text("Taxes")
    st.text("Tax expenditures")

    st.text("Gini index between states - compare inequality (by race, gender, employment) within and between jurisdictions, using a variety of income measures and data sources, with differing results")

    # variables to take into consideration into the algorithm
    st.text("* nearby biology affluence")
    st.text("* county economical affluence")
    st.text("* community investment")
    st.text("* population density")
    st.text("* safety/crime (fbi data and the type of crimes (petty to serious))")
    st.text("* house prices (rising, falling, stagnant (potential of growth))")
    st.text("* GIS data")
    st.text("* community activity/involvment")
    st.text("* neighborhood data?")
    st.text("* user’s marital status, education, number of dependents, and employments")
    st.text("* public transportation")
    st.text("Labor force participation rate")

    st.text("Maybe: * types of people such as race, ethnicity, religion? * geo restrictions such as restricting analysis to west coast or east coast, etc")

    st.text("""Kit towards certain groups of individuals:
        - workers: (by major, layoffs, hirings, median salary)
        - parents: (education pre k to highschool, parks, safety, tree density, health care quality(readyness), etc)
        - sickly: (air purity, pollution)
        - 20-30 yrs: population pyramid
        - students: higher education pursuement rates""")







    def randomisation_callback():
        st.session_state.pdi = random.randint(1, 100)
        st.session_state.idv = random.randint(1, 100)
        st.session_state.mas = random.randint(1, 100)
        st.session_state.uai = random.randint(1, 100)
        st.session_state.lto = random.randint(1, 100)
        st.session_state.ind = random.randint(1, 100)

    randomised = st.button('Randomise answers', on_click=randomisation_callback)



    distance_metric = st.selectbox('What distance metric would you like to use?',
                                list(distance_calculations.AVAILABLE_DISTANCES.keys()))
    k = st.number_input('How many top countries to display?', value=4, min_value=1, max_value=10)

    selected_countries_names = st.multiselect(
        'Choose countries you want to compare:',
        all_countries_names,
        st.session_state["default_countries"])