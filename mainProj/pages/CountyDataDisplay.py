DOC="""
https://github.com/PablocFonseca/streamlit-aggrid
https://staggrid-examples.streamlit.app/
EXAMPLES TAKEN FROM HERE

filter by fmr code
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

ADVICE="https://okld-gallery.streamlit.app/?p=pandas-profiling USE THIS FOR GENERAL REPORT"

def county():
    np.random.seed(42)

    _datafill="###################################"
    @st.cache_data()
    def fetch_data(samples):
        deltas = cycle([
                pd.Timedelta(weeks=-2),
                pd.Timedelta(days=-1),
                pd.Timedelta(hours=-1),
                pd.Timedelta(0),
                pd.Timedelta(minutes=5),
                pd.Timedelta(seconds=10),
                pd.Timedelta(microseconds=50),
                pd.Timedelta(microseconds=10)
                ])
        dummy_data = {
            "date_time_naive":pd.date_range('2021-01-01', periods=samples),
            "apple":np.random.randint(0,100,samples) / 3.0,
            "banana":np.random.randint(0,100,samples) / 5.0,
            "chocolate":np.random.randint(0,100,samples),
            "group": np.random.choice(['A','B'], size=samples),
            "date_only":pd.date_range('2020-01-01', periods=samples).date,
            "timedelta":[next(deltas) for i in range(samples)],
            "date_tz_aware":pd.date_range('2022-01-01', periods=samples, tz="Asia/Katmandu")
        }
        return pd.DataFrame(dummy_data)

    col1, col2, col3, col4, col5 = st.columns((1,1,1,1,2))
    
    with col1:
        sample_size = st.number_input("Rows", min_value=10, value=30)
    
    with col2:
        grid_height = st.number_input("Grid height", min_value=200, max_value=800, value=300)

    with col3:
        return_mode = st.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
        return_mode_value = DataReturnMode.__members__[return_mode]

    with col4:
        update_mode = st.selectbox("Update Mode", list(GridUpdateMode.__members__), index=len(GridUpdateMode.__members__)-1)
        update_mode_value = GridUpdateMode.__members__[update_mode]

    with col5:
        #features
        fit_columns_on_grid_load = st.checkbox("Fit Grid Columns on Load")

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
        enable_pagination = st.checkbox("Enable pagination", value=False)
        if enable_pagination:
            st.subheader("Pagination options")
            paginationAutoSize = st.checkbox("Auto pagination size", value=True)
            if not paginationAutoSize:
                paginationPageSize = st.number_input("Page size", value=5, min_value=0, max_value=sample_size)

    df = fetch_data(sample_size)

    #Infer basic colDefs from dataframe types
    gb = GridOptionsBuilder.from_dataframe(df)

    #customize gridOptions
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
    gb.configure_column("date_only", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='yyyy-MM-dd', pivot=True)
    gb.configure_column("date_tz_aware", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='yyyy-MM-dd HH:mm zzz', pivot=True)

    gb.configure_column("apple", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=2, aggFunc='sum')
    gb.configure_column("banana", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=1, aggFunc='avg')
    gb.configure_column("chocolate", type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="R$", aggFunc='max')

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
        chart_data = df.loc[:,['apple','banana','chocolate']].assign(source='total') # replace with db column names

        if not selected_df.empty :
            selected_data = selected_df.loc[:,['apple','banana','chocolate']].assign(source='selection')
            chart_data = pd.concat([chart_data, selected_data])

        chart_data = pd.melt(chart_data, id_vars=['source'], var_name="item", value_name="quantity")
        #st.dataframe(chart_data)
        chart = alt.Chart(data=chart_data).mark_bar().encode(
            x=alt.X("item:O"),
            y=alt.Y("sum(quantity):Q", stack=False),
            color=alt.Color('source:N', scale=alt.Scale(domain=['total','selection'])),
        )

        st.header("Component Outputs - Example chart")
        st.altair_chart(chart, use_container_width=True)


        st.subheader("Returned grid data:") 
        #returning as HTML table bc streamlit has issues when rendering dataframes with timedeltas:
        # https://github.com/streamlit/streamlit/issues/3781
        st.markdown(grid_response['data'].to_html(), unsafe_allow_html=True)






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



    @st.cache_data()
    def get_data_ex4():
        df = pd.DataFrame(
            np.random.randint(0, 100, 50).reshape(-1, 5), columns=list("abcde")
        )
        return df

    df = get_data_ex4()
    st.markdown("""
    ## Two grids 
    As in other streamlit components, it is possible to render two components for the same data using distinct ```key``` parameters.
    """)

    st.subheader("Input data")
    st.dataframe(df)

    st.subheader("Editable Grids")
    c1, c2 = st.columns(2)
    with c1:
        grid_return1 = AgGrid(df, key='grid1', editable=True)
        st.text("Grid 1 Return")
        st.write(grid_return1['data'])

    with c2:
        grid_return2 = AgGrid(df,  key='grid2', editable=True)
        st.text("Grid 2 Return")
        st.write(grid_return2['data'])



Experimental="""
CHECK THIS OUT LATER: https://okld-gallery.streamlit.app/?p=pandas-profiling

import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)

"""




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