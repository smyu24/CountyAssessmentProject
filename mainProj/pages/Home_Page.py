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
            
            2. __
        """
    )

    st.title("Sources")
    st.markdown(
        """
        [___](https://google.com)
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