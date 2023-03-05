import streamlit as st
def home_pg():
    st.title("County Assessment Project")
    st.markdown(
        """
        This is a ...
        """
    )
    st_lottie("https://assets4.lottiefiles.com/packages/lf20_yrelFtPfpX.json", key="user") # pip install st_lottie
    st_lottie("https://assets7.lottiefiles.com/packages/lf20_llbjwp92qL.json", key="user") # pip install st_lottie
    
    
    st.title("About the Variables/Algorithm")
    st.markdown(
        """
        List of variables: 
        
        Things to do: 
            
            1. Add map of subway, bus, railway, and other public transportations after querying the user's selected coords (after county analysis and post location decision)
            
            2. __
        """
    )

    st.title("Sources")
    st.markdown(
        """
        ___
        [___](https://google.com)
        """
    )

    st.info("Toggle the sidebar menu on the left to navigate to different pages.")
