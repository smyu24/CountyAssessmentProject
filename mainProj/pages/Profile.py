import streamlit as st
import random

def profile():
    st.title("PROFILE")

    st.text("1. Power distance (PDI)")
    pdi = st.slider('To which extent you accept that individuals in societies are not equal?',
                    0, 100, 50, help="", key="pdi")

    st.text("2. Individualism (IDV)")
    idv = st.slider('How independent you would like to be in your society?',
                    0, 100, 50, help="", key="idv")

    st.text("3. Masculinity (MAS)")
    mas = st.slider('How much are you driven by competition, achievement and success and able to sacrifice caring for '
                    'others and quality of life?',
                    0, 100, 50, help="", key="mas")

    st.text("4. Uncertainty avoidance (UAI)")
    uai = st.slider('To which extent you feel threatened by ambiguous or unknown situations and try to avoid them ?',
                    0, 100, 50, help="", key="uai")

    st.text("5. Long term orientation (LTO)")
    lto = st.slider('How much do you consider past when dealing with future and present challenges?',
                    0, 100, 50, help="", key="lto")

    st.text("6. Indulgence (IND)")
    ind = st.slider('To which extent you would like to express your desires and impulses??',
                    0, 100, 50, help="", key="ind")

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