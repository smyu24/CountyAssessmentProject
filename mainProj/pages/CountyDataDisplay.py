DOC="""
https://github.com/PablocFonseca/streamlit-aggrid
https://staggrid-examples.streamlit.app/
EXAMPLES TAKEN FROM HERE

filter by fmr code
by state, (GIS and other data visualization)
"""

import enum
import typing

import pandas as pd
from scipy.spatial import distance
import streamlit as st
#from sklearn import decomposition
import numpy as np
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder, JsCode

from distutils import errors
from distutils.log import error
import altair as alt
from itertools import cycle

import requests
import os, sys, inspect


ADVICE="https://okld-gallery.streamlit.app/?p=pandas-profiling USE THIS FOR GENERAL REPORT"

def county():
    st.title("Fair Market Rents Data and Trends")
    st.markdown(
            """**Introduction:** This section is designed to visualize and display data for regional and state Fair Market Rent trends. 
            The data sources include [United States Department of Housing and Urban Development](https://www.huduser.gov/portal/datasets/fmr.html) and ___
        """)
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    
    FMR_AVAIL_YEARS = os.listdir(r"C:\Users\smyu2\OneDrive\Documents\GitHub\CountyAssessmentProject\mainProj\FairMarketRents_Data")
    
    SELECTION_FMR = st.selectbox('Year To Display', (FMR_AVAIL_YEARS))
    
    @st.cache_data()
    def fetch_data(YEAR):
        dataset = pd.read_csv(fr"FairMarketRents_Data/{YEAR}", encoding='utf-8') 
        return pd.DataFrame(dataset)

    col1, col2, col3, col4, col5 = st.columns((1,1,1,1,2))
    
    with col1:
        sample_size = st.number_input("Rows", min_value=10, value=30)
    
    with col2:
        grid_height = st.number_input("Grid height", min_value=200, max_value=800, value=280)

    with col3:
        return_mode = st.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
        return_mode_value = DataReturnMode.__members__[return_mode]

    with col4:
        update_mode = st.selectbox("Update Mode", list(GridUpdateMode.__members__), index=len(GridUpdateMode.__members__)-1)
        update_mode_value = GridUpdateMode.__members__[update_mode]

    with col5:
        #features
        fit_columns_on_grid_load = st.checkbox("Fit Grid Columns on Load", value=True)
        enable_selection=st.checkbox("Enable row selection", value=False)

    col1_2, col2_2 = st.columns((1,1))

    with col1_2:
        if enable_selection:
            st.subheader("Selection options")
            selection_mode = st.radio("Selection Mode", ['single','multiple'], index=1)

            use_checkbox = st.checkbox("Use check box for selection", value=True)
            if use_checkbox:
                groupSelectsChildren = st.checkbox("Group checkbox select children", value=True)
                groupSelectsFiltered = st.checkbox("Group checkbox includes filtered", value=True)

            if ((selection_mode == 'multiple') & (not use_checkbox)):
                rowMultiSelectWithClick = st.checkbox("Multiselect with click (instead of holding CTRL)", value=False)
                if not rowMultiSelectWithClick:
                    suppressRowDeselection = st.checkbox("Suppress deselection (while holding CTRL)", value=False)
                else:
                    suppressRowDeselection=False

    with col2_2:
        enable_pagination = st.checkbox("Enable pagination", value=True)
        if enable_pagination:
            st.subheader("Pagination options")
            paginationAutoSize = st.checkbox("Auto pagination size", value=True)
            if not paginationAutoSize:
                paginationPageSize = st.number_input("Page size", value=5, min_value=0, max_value=sample_size)

    df = fetch_data(SELECTION_FMR)



    #Infer basic colDefs from dataframe types
    gb = GridOptionsBuilder.from_dataframe(df)

    #customize gridOptions
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

    gb.configure_column("pop", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("fmr_0", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("fmr_1", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("fmr_2", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("fmr_3", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("fmr_4", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')


    #configures last row to use custom styles based on cell's value, injecting JsCode on components front end
    cellsytle_jscode = JsCode("""
    function(params) {
        if (params.value == 'A') {
            return {
                'color': 'white',
                'backgroundColor': 'darkred'
            }
        } else {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
        }
    };
    """)
    gb.configure_column("group", cellStyle=cellsytle_jscode)

    if enable_pagination:
        if paginationAutoSize:
            gb.configure_pagination(paginationAutoPageSize=True)
        else:
            gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=paginationPageSize)

    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()



    _GridDisplay="##########################"#Display the grid
    st.header("CSV FMR Data Displayed and Graphed")

    grid_response = AgGrid(
        df, 
        gridOptions=gridOptions,
        height=grid_height, 
        width='100%',
        data_return_mode=return_mode_value, 
        update_mode=update_mode_value,
        fit_columns_on_grid_load=fit_columns_on_grid_load,
        allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
        )

    df = grid_response['data']
    selected = grid_response['selected_rows']
    selected_df = pd.DataFrame(selected).apply(pd.to_numeric, errors='coerce')


    with st.spinner("Displaying results..."):
        #displays the chart
        chart_data = df.loc[:,['fmr_0','fmr_1', 'fmr_2', 'fmr_3', 'fmr_4']].assign(source='total') # replace with db column names

        if not selected_df.empty :
            selected_data = selected_df.loc[:,['fmr_0','fmr_1', 'fmr_2', 'fmr_3', 'fmr_4']].assign(source='selection')
            chart_data = pd.concat([chart_data, selected_data])

        chart_data = pd.melt(chart_data, id_vars=['source'], var_name="item", value_name="quantity")
        #st.dataframe(chart_data)
        chart = alt.Chart(data=chart_data).mark_bar().encode(
            x=alt.X("item:O"),
            y=alt.Y("sum(quantity):Q", stack=False),
            color=alt.Color('source:N', scale=alt.Scale(domain=['total','selection'])),
        )
        st.altair_chart(chart, use_container_width=True)



# ['fmr_0','fmr_1', 'fmr_2', 'fmr_3', 'fmr_4']
    url = "https://www.ag-grid.com/example-assets/master-detail-data.json"
    df = pd.read_json(url)
    df["callRecords"] = df["callRecords"].apply(lambda x: pd.json_normalize(x))

    gridOptions = {
        # enable Master / Detail
        "masterDetail": True,
        "rowSelection": "single",
        # the first Column is configured to use agGroupCellRenderer
        "columnDefs": [
            {
                "field": "name",
                "cellRenderer": "agGroupCellRenderer",
                "checkboxSelection": True,
            },
            {"field": "account"},
            {"field": "calls"},
            {"field": "minutes", "valueFormatter": "x.toLocaleString() + 'm'"},
        ],
        "defaultColDef": {
            "flex": 1,
        },
        # provide Detail Cell Renderer Params
        "detailCellRendererParams": {
            # provide the Grid Options to use on the Detail Grid
            "detailGridOptions": {
                "rowSelection": "multiple",
                "suppressRowClickSelection": True,
                "enableRangeSelection": True,
                "pagination": True,
                "paginationAutoPageSize": True,
                "columnDefs": [
                    {"field": "callId", "checkboxSelection": True},
                    {"field": "direction"},
                    {"field": "number", "minWidth": 150},
                    {"field": "duration", "valueFormatter": "x.toLocaleString() + 's'"},
                    {"field": "switchCode", "minWidth": 150},
                ],
                "defaultColDef": {
                    "sortable": True,
                    "flex": 1,
                },
            },
            # get the rows for each Detail Grid
            "getDetailRowData": JsCode(
                """function (params) {
                    console.log(params);
                    params.successCallback(params.data.callRecords);
        }"""
            ).js_code,
        },
    }

    r = AgGrid(
        df,
        gridOptions=gridOptions,
        height=500,
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED
    )


a="""
HOFSTEDE_DIMENSIONS = ['pdi', 'idv', 'mas', 'uai', 'lto', 'ind', 'ivr']
AVAILABLE_DISTANCES = {
    "Euclidean": distance.euclidean,
    "Cosine": distance.cosine,
    "Manhattan": distance.cityblock,
    "Correlation": distance.correlation,
}

AVAILABLE_DECOMPOSITION = {
    'PCA': decomposition.PCA,
    'FastICA': decomposition.FastICA,
    'NMF': decomposition.NMF,
    "MiniBatchSparsePCA": decomposition.MiniBatchSparsePCA,
    "SparsePCA": decomposition.SparsePCA,
    "TruncatedSVD": decomposition.TruncatedSVD
}

TO_PERCENT = 100.0
SQUARE = 2
PandasDataFrame = typing.TypeVar('pandas.core.frame.DataFrame')



@st.cache_data
def normalise_distance_matrix(
        distances: PandasDataFrame,
        max_distance: float
) -> PandasDataFrame:
    return distances.applymap(lambda x: x / max_distance * TO_PERCENT)


@st.cache_data
def generate_2d_coords(
        dimensions: PandasDataFrame,
        algorithm: str
) -> PandasDataFrame:
    algo = AVAILABLE_DECOMPOSITION[algorithm]
    reduced = algo(n_components=2)
    ret = pd.DataFrame(reduced.fit_transform(dimensions.transpose()), index=dimensions.columns)
    if algorithm in ('FastICA', 'NMF'):
        return ret.applymap(lambda x: x * TO_PERCENT)
    return ret


#------
import math

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet, ImageURL
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

DEFAULT_COLORMAP = "coolwarm_r"
DEFAULT_FORMAT = '.0f'
DEFAULT_TEXT_ROTATION_DEGREES = 80
POLAR_PLOT_Y_TICKS_RANGE = [i for i in range(0, 120, 20)]
POLAR_Y_TICKS_SIZE = 7
POLAR_X_TICKS_SIZE = 8
COLOR_GREY = "grey"
COLOR_DARKS_LATE_GREY = "darkslategrey"
FONT_FAMILY_SANS_SERIF = 'sans-serif'
MAX_VALUE_PER_DIMENSION = 100
SOLID_LINE_STYLE = 'solid'
SCATTERPLOT_COLOR_MAP = 'Spectral'
SCATTERPLOT_FONT_SIZE = 9
SCATTERPLOT_LINE_STYLE = '--'
SCATTERPLOT_TITLE = "Cultural distance in 2D"
RADAR_PLOTS_COLOR_MAP = "Set2"
RADAR_PLOTS_PADDING = 1.5
RADAR_PLOT_SIZE = 1000
DISPLAY_DPI = 96
RADAR_PLOT_TITLE_FONT_SIZE = 11
RADAR_PLOT_TITLE_Y_POSITION = 1.2
RADAR_PLOT_ALPHA_CHANNEL = 0.4
TEXT_COORDS_OFFSET_POINTS = 'offset points'


def generate_heatmap(
        distances: PandasDataFrame,
        show_clusters: bool
) -> plt.Figure:
    fig, ax = plt.subplots()
    plt.xticks(rotation=DEFAULT_TEXT_ROTATION_DEGREES)
    if show_clusters:
        fig = sns.clustermap(distances, cmap=DEFAULT_COLORMAP, annot=True, fmt=DEFAULT_FORMAT)
    else:
        sns.heatmap(distances, ax=ax, cmap=DEFAULT_COLORMAP, annot=True, fmt=DEFAULT_FORMAT)
        fig.tight_layout()
    return fig


def generate_scatterplot(
        coords: PandasDataFrame
) -> plt.Figure:
    data = {str(key): val for key, val in coords.to_dict(orient="list").items()}
    data["names"] = coords.index
    max_x, max_y = max(data['0']), max(data['1'])
    min_x, min_y = min(data['0']), min(data['1'])
    x_margin, y_margin = (max_x - min_x) * 0.2, (max_y - min_y) * 0.2
    fig = figure(width=800, height=800, x_range=(min_x - x_margin, max_x + x_margin),
                 y_range=(min_y - y_margin, max_y + y_margin), title="Culture distance in 2D")
    source = ColumnDataSource(data=data)
    labels = LabelSet(x='0', y='1', text='names',
                      x_offset=10, y_offset=10, source=source, render_mode='canvas')
    fig.add_layout(labels)
    for country_name, country_coords in coords.iterrows():
        img = ImageURL(url=dict(value=COUNTRY_URLS[country_name]), x=country_coords[0],
                       y=country_coords[1], w=5, h=2, anchor="center")
        fig.add_glyph(source, img)
    return fig


def generate_radar_plot(
        dimensions: PandasDataFrame,
        reference: PandasDataFrame | None = None
) -> plt.Figure:
    fig = plt.figure(figsize=(RADAR_PLOT_SIZE/DISPLAY_DPI, RADAR_PLOT_SIZE/DISPLAY_DPI), dpi=DISPLAY_DPI)

    # Create a color palette:
    my_palette = plt.cm.get_cmap(RADAR_PLOTS_COLOR_MAP, len(dimensions.columns))

    # Loop to plot
    for idx, country in enumerate(dimensions.columns):
        make_spider(idx, country, my_palette(idx), dimensions, reference)

    fig.tight_layout(pad=RADAR_PLOTS_PADDING)
    return fig


def generate_choropleth(
        dimensions: PandasDataFrame,
        dimension_name: str
) -> plt.Figure:
    transposed = dimensions.transpose()
    transposed.reset_index(inplace=True)
    transposed = transposed.rename(columns={'index': 'country'})
    fig = px.choropleth(transposed, locationmode="country names", locations="country", color=dimension_name,
                        hover_name="country", color_continuous_scale=px.colors.sequential.Plasma)
    return fig


def make_spider(
        col: int,
        title: str,
        color: str,
        dimensions: PandasDataFrame,
        reference: PandasDataFrame | None = None
) -> None:

    # number of variable
    categories = list(dimensions.index)
    num_categories = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(num_categories) * 2 * math.pi for n in range(num_categories)]
    angles += angles[:1]

    # Initialise the spider plot
    side_len = math.ceil(math.sqrt(len(dimensions.columns)))
    ax = plt.subplot(side_len, side_len, col+1, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color=COLOR_GREY, size=POLAR_X_TICKS_SIZE)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks(POLAR_PLOT_Y_TICKS_RANGE, list(map(str, POLAR_PLOT_Y_TICKS_RANGE)),
               color=COLOR_GREY, size=POLAR_Y_TICKS_SIZE)
    plt.ylim(0, MAX_VALUE_PER_DIMENSION)

    # Ind1
    values = dimensions[title].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle=SOLID_LINE_STYLE)
    ax.fill(angles, values, color=color, alpha=RADAR_PLOT_ALPHA_CHANNEL)

    # Ind2
    if reference is not None:
        values = reference["distance"].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, color="red", linewidth=1, linestyle="dashed")
        ax.fill(angles, values, color="red", alpha=0.1)

    # Add a title
    plt.title(title, size=RADAR_PLOT_TITLE_FONT_SIZE, color=color, y=RADAR_PLOT_TITLE_Y_POSITION)"""