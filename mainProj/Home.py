import geopandas as gpd
import datetime
import os
import pathlib
import requests
import zipfile
import pandas as pd
import pydeck as pdk
import geopandas as gpd
import streamlit as st
import leafmap.colormaps as cm
from leafmap.common import hex_to_rgb
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

with st.sidebar: 
    tabs = on_hover_tabs(tabName=['Home', '1_Housing', 'Settings'], 
                            iconName=['dashboard', 'money', 'economy'],
                            styles = {'navtab': {'background-color':'#111',
                                                'color': '#818181',
                                                'font-size': '18px',
                                                'transition': '.05s',
                                                'white-space': 'nowrap',
                                                'text-transform': 'uppercase'},
                                    'iconStyle':{'position':'fixed',
                                                'left':'7.5px',
                                                'text-align': 'left'},
                                    'tabStyle' : {'list-style-type': 'none',
                                                    'margin-bottom': '30px',
                                                    'padding-left': '30px'}},
                            key="1")
_ = """PARAMETER DEF/DESCRIPTION ;;;;; ADD A TOGGLEABLE BUTTON ON THE BOTTOM OF THE NAVBAR that IS SEPARATE FROM THE NAVBAR (BLOCK) THAT DISABLES THE JS SLIDING/EXTENDING
tabName: This is the name of the tab
iconName: This is the name of the icon you wish to use in the sidebar
styles: Borrowed an implementation from the wonderful Victoryhb implementation. It just has four html elements with css styles which you can adapt as you would if you were in a css file. It employs styles from glamor which allows for other implementations like hover, active etc as demonstrated below. Now you can create your own navigation bar and customize the tabs to meet the specs of your custom tab.
    'navtab' which is the div container that contains the tabs
    'tabOptionsStyle' which is the span container that contains the icons and tabName
    'iconStyle' which is the icon tag that contains the icons
    'tabStyle' which is the list contains the tabName
"""

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
    ___
    [___](https://google.com)
    """
)

st.info("Toggle the sidebar menu on the left to navigate to different pages.")
