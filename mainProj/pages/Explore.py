def explore():
    import streamlit as st
    import pandas as pd
    import folium
    from streamlit_folium import st_folium
    import geopandas as gpd

    import os, inspect, sys

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    
    # https://towardsdatascience.com/creating-choropleth-maps-with-pythons-folium-library-cfacfb40f56a

    APP_TITLE = 'Fraud and Identity Theft Report'
    APP_SUB_TITLE = 'Source: Federal Trade Commission'

    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    map = folium.Map(location=[38, -96.5], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')
    
    choropleth = folium.Choropleth(
        geo_data='./us-state-boundaries.geojson',
        # data=df,
        columns=('State Name', 'State Total Reports Quarter'),
        key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name', 'population', 'per_100k'], labels=False)
    )
    
    st_map = st_folium(map, width=700, height=450)





    temp = """# center on Liberty Bell, add marker
    # bi-directional data transfer functionability"""
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)
    folium.Marker(
        [39.965570, -75.180966],
        popup="Philadelphia Museum of Art",
        tooltip="Philadelphia Museum of Art",
    ).add_to(m)

    temp = """
    # call to render Folium map in Streamlit
    # st_data = st_folium(m, width=725)"""
    output = st_folium(
        m, width=700, height=500, returned_objects=["last_object_clicked"]
    )

    temp = """
    #If you don't need any data returned from the map, you can just pass returned_objects=[] to st_folium. The streamlit app will not rerun when the user interacts with the map, and you will not get any data back from the map.

    # m = folium.Map(location=CENTER_START, zoom_start=8)
    # fg = folium.FeatureGroup(name="Markers")
    # for marker in st.session_state["markers"]:
    #     fg.add_child(marker)

    # st_folium(
    #     m,
    #     center=st.session_state["center"],
    #     zoom=st.session_state["zoom"],
    #     key="new",
    #     feature_group_to_add=fg,
    #     height=400,
    #     width=700,
    # )
    

    # m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

    # # If you want to dynamically add or remove items from the map,
    # # add them to a FeatureGroup and pass it to st_folium
    # fg = folium.FeatureGroup(name="State bounds")
    # fg.add_child(folium.features.GeoJson(bounds))

    # capitals = STATE_DATA

    # for capital in capitals.itertuples():
    #     fg.add_child(
    #         folium.Marker(
    #             location=[capital.latitude, capital.longitude],
    #             popup=f"{capital.capital}, {capital.state}",
    #             tooltip=f"{capital.capital}, {capital.state}",
    #             icon=folium.Icon(color="green")
    #             if capital.state == st.session_state["selected_state"]
    #             else None,
    #         )
    #     )

    # out = st_folium(
    #     m,
    #     feature_group_to_add=fg,
    #     center=center,
    #     width=1200,
    #     height=500,
    # )

    """




    import folium
    import pandas as pd

    eco_footprints = pd.read_csv("footprint.csv")
    max_eco_footprint = eco_footprints["Ecological footprint"].max()
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )

    m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
    folium.Choropleth(
        geo_data=political_countries_url,
        data=eco_footprints,
        columns=("Country/region", "Ecological footprint"),
        key_on="feature.properties.name",
        bins=(0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, max_eco_footprint),
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name="Ecological footprint per capita",
        name="Countries by ecological footprint per capita",
    ).add_to(m)
    folium.LayerControl().add_to(m)

    m.save("footprint.html")






    temp = """#simple_popup"""
    import folium
    import streamlit as st
    from folium.features import Marker, Popup

    from streamlit_folium import st_folium

    st.write("# Simple Popup & Tooltip")

    return_on_hover = st.checkbox("Return on hover?")

    with st.echo("below"):
        m = folium.Map(location=[45, -122], zoom_start=4)

        Marker(
            location=[45.5, -122],
            popup=Popup("Popup!", parse_html=False),
            tooltip="Tooltip!",
        ).add_to(m)

        Marker(
            location=[45.5, -112],
            popup=Popup("Popup 2!", parse_html=False),
            tooltip="Tooltip 2!",
        ).add_to(m)

        out = st_folium(m, height=200, return_on_hover=return_on_hover)

        st.write("Popup:", out["last_object_clicked_popup"])
        st.write("Tooltip:", out["last_object_clicked_tooltip"])
