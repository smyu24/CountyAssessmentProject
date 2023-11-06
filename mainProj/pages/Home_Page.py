from functools import partial
from streamlit_elements import nivo, media, mui, sync, lazy, editor, elements, event, dashboard

import json
import streamlit as st

from functools import partial
from streamlit_elements import nivo, media, mui, sync, lazy, editor, elements, event, dashboard

import json
import streamlit as st

from streamlit import session_state as state
from types import SimpleNamespace

from uuid import uuid4
from abc import ABC, abstractmethod
from contextlib import contextmanager

"""
Streamlit Elements is a component that gives you the tools to compose beautiful applications with Material UI widgets, Monaco, Nivo charts, 
and more. It also includes a feature to create draggable and resizable dashboards.

** Use NIVO FOR DATA VISUALIZATION
"""
class Dashboard:
    DRAGGABLE_CLASS = "draggable"

    def __init__(self):
        self._layout = []

    def _register(self, item):
        self._layout.append(item)

    @contextmanager
    def __call__(self, **props):
        # Draggable classname query selector.
        props["draggableHandle"] = f".{Dashboard.DRAGGABLE_CLASS}"

        with dashboard.Grid(self._layout, **props):
            yield

    class Item(ABC):

        def __init__(self, board, x, y, w, h, **item_props):
            self._key = str(uuid4())
            self._draggable_class = Dashboard.DRAGGABLE_CLASS
            self._dark_mode = True
            board._register(dashboard.Item(
                self._key, x, y, w, h, **item_props))

        def _switch_theme(self):
            self._dark_mode = not self._dark_mode

        @contextmanager
        def title_bar(self, padding="5px 15px 5px 15px", dark_switcher=True):
            with mui.Stack(
                className=self._draggable_class,
                alignItems="center",
                direction="row",
                spacing=1,
                sx={
                    "padding": padding,
                    "borderBottom": 1,
                    "borderColor": "divider",
                },
            ):
                yield

                if dark_switcher:
                    if self._dark_mode:
                        mui.IconButton(mui.icon.DarkMode,
                                       onClick=self._switch_theme)
                    else:
                        mui.IconButton(mui.icon.LightMode, sx={
                                       "color": "#ffc107"}, onClick=self._switch_theme)

        @abstractmethod
        def __call__(self):
            """Show elements."""
            raise NotImplementedError


class Card(Dashboard.Item):
    DEFAULT_CONTENT = (
        "This impressive paella is a perfect party dish and a fun meal to cook "
        "together with your guests. Add 1 cup of frozen peas along with the mussels, "
        "if you like."
    )

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="Shrimp and Chorizo Paella",
                subheader="September 14, 2016",
                avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class,
            )
            mui.CardMedia(
                component="img",
                height=194,
                image="https://mui.com/static/images/cards/paella.jpg",
                alt="Paella dish",
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(content)

            with mui.CardActions(disableSpacing=True):
                mui.IconButton(mui.icon.Favorite)
                mui.IconButton(mui.icon.Share)


class Radar(Dashboard.Item):
    DEFAULT_DATA = [
        {"taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114},
        {"taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72},
        {"taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99},
        {"taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30},
        {"taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103},
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.Radar()
                mui.Typography("Radar chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Radar(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    keys=["chardonay", "carmenere", "syrah"],
                    indexBy="taste",
                    valueFormat=">-.2f",
                    margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                    borderColor={"from": "color"},
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={"theme": "background"},
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )


class Player(Dashboard.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._url = "https://www.youtube.com/watch?v=CmSKVW1v0xM"

    def _set_url(self, event):
        self._url = event.target.value

    def __call__(self):
        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.OndemandVideo()
                mui.Typography("Media player")

            with mui.Stack(direction="row", spacing=2, justifyContent="space-evenly", alignItems="center", sx={"padding": "10px"}):
                mui.TextField(defaultValue=self._url, label="URL", variant="standard", sx={
                              "flex": 0.97}, onChange=lazy(self._set_url))
                mui.IconButton(mui.icon.PlayCircleFilled,
                               onClick=sync(), sx={"color": "primary.main"})

            media.Player(self._url, controls=True, width="100%", height="100%")


class Pie(Dashboard.Item):
    DEFAULT_DATA = [
        {"id": "java", "label": "java", "value": 465,
            "color": "hsl(128, 70%, 50%)"},
        {"id": "rust", "label": "rust", "value": 140,
            "color": "hsl(178, 70%, 50%)"},
        {"id": "scala", "label": "scala", "value": 40,
            "color": "hsl(322, 70%, 50%)"},
        {"id": "ruby", "label": "ruby", "value": 439,
            "color": "hsl(117, 70%, 50%)"},
        {"id": "elixir", "label": "elixir",
            "value": 366, "color": "hsl(286, 70%, 50%)"}
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.PieChart()
                mui.Typography("Pie chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Pie(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    innerRadius=0.5,
                    padAngle=0.7,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="grey",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={"from": "color"},
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        {"match": {"id": "ruby"}, "id": "dots"},
                        {"match": {"id": "c"}, "id": "dots"},
                        {"match": {"id": "go"}, "id": "dots"},
                        {"match": {"id": "python"}, "id": "dots"},
                        {"match": {"id": "scala"}, "id": "lines"},
                        {"match": {"id": "lisp"}, "id": "lines"},
                        {"match": {"id": "elixir"}, "id": "lines"},
                        {"match": {"id": "javascript"}, "id": "lines"}
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )


class Editor(Dashboard.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._dark_theme = False
        self._index = 0
        self._tabs = {}
        self._editor_box_style = {
            "flex": 1,
            "minHeight": 0,
            "borderBottom": 1,
            "borderTop": 1,
            "borderColor": "divider"
        }

    def _change_tab(self, _, index):
        self._index = index

    def update_content(self, label, content):
        self._tabs[label]["content"] = content

    def add_tab(self, label, default_content, language):
        self._tabs[label] = {
            "content": default_content,
            "language": language
        }

    def get_content(self, label):
        return self._tabs[label]["content"]

    def __call__(self):
        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):

            with self.title_bar("0px 15px 0px 15px"):
                mui.icon.Terminal()
                mui.Typography("Editor")

                with mui.Tabs(value=self._index, onChange=self._change_tab, scrollButtons=True, variant="scrollable", sx={"flex": 1}):
                    for label in self._tabs.keys():
                        mui.Tab(label=label)

            for index, (label, tab) in enumerate(self._tabs.items()):
                with mui.Box(sx=self._editor_box_style, hidden=(index != self._index)):
                    editor.Monaco(
                        css={"padding": "0 2px 0 2px"},
                        defaultValue=tab["content"],
                        language=tab["language"],
                        onChange=lazy(partial(self.update_content, label)),
                        theme="vs-dark" if self._dark_mode else "light",
                        path=label,
                        options={
                            "wordWrap": True
                        }
                    )

            with mui.Stack(direction="row", spacing=2, alignItems="center", sx={"padding": "10px"}):
                mui.Button("Apply", variant="contained", onClick=sync())
                mui.Typography("Or press ctrl+s", sx={"flex": 1})


class DataGrid(Dashboard.Item):
    DEFAULT_COLUMNS = [
        {"field": 'id', "headerName": 'ID', "width": 90},
        {"field": 'firstName', "headerName": 'First name',
            "width": 150, "editable": True, },
        {"field": 'lastName', "headerName": 'Last name',
            "width": 150, "editable": True, },
        {"field": 'age', "headerName": 'Age', "type": 'number',
            "width": 110, "editable": True, },
    ]
    DEFAULT_ROWS = [
        {"id": 1, "lastName": 'Snow', "firstName": 'Jon', "age": 35},
        {"id": 2, "lastName": 'Lannister', "firstName": 'Cersei', "age": 42},
        {"id": 3, "lastName": 'Lannister', "firstName": 'Jaime', "age": 45},
        {"id": 4, "lastName": 'Stark', "firstName": 'Arya', "age": 16},
        {"id": 5, "lastName": 'Targaryen', "firstName": 'Daenerys', "age": None},
        {"id": 6, "lastName": 'Melisandre', "firstName": None, "age": 150},
        {"id": 7, "lastName": 'Clifford', "firstName": 'Ferrara', "age": 44},
        {"id": 8, "lastName": 'Frances', "firstName": 'Rossini', "age": 36},
        {"id": 9, "lastName": 'Roxie', "firstName": 'Harvey', "age": 65},
    ]

    def _handle_edit(self, params):
        print(params)

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_ROWS

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.ViewCompact()
                mui.Typography("Data grid")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                mui.DataGrid(
                    columns=self.DEFAULT_COLUMNS,
                    rows=data,
                    pageSize=5,
                    rowsPerPageOptions=[5],
                    checkboxSelection=True,
                    disableSelectionOnClick=True,
                    onCellEditCommit=self._handle_edit,
                )

def home_pg():
    st.title("County Assessment Project :house_with_garden: :office: :department_store:")
    st.markdown(
        """
        Things to have on front page...
        Social Media Feeds Widget: Embed your project's social media feeds, showing the latest posts and updates to encourage visitors to follow your profiles.
        Contact or Support Widget:Provide a widget with contact information, including a phone number and email address.; Offer a "Chat with Us" or "Support" option for real-time assistance.
        Newsletter Signup Widget:Include a widget that prompts users to subscribe to your newsletter to receive updates on new property listings, market insights, and industry news.
        Calendar
        Latest Blog Posts Widget:Display links to your most recent blog posts or articles on real estate trends, property buying tips, and related topics.
        Market Trends Widget:Display graphs or charts illustrating real estate market trends, such as price fluctuations, supply and demand, or market activity.
        Noticed Trends

        """
    )
    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            editor=Editor(board, 0, 0, 6, 11, minW=3, minH=3),
            player=Player(board, 0, 12, 6, 10, minH=5),
            pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
            radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
            card=Card(board, 6, 7, 3, 7, minW=2, minH=4),
            data_grid=DataGrid(board, 6, 13, 6, 7, minH=4),
        )
        state.w = w

        w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Data grid", json.dumps(
            DataGrid.DEFAULT_ROWS, indent=2), "json")
        w.editor.add_tab("Radar chart", json.dumps(
            Radar.DEFAULT_DATA, indent=2), "json")
        w.editor.add_tab("Pie chart", json.dumps(
            Pie.DEFAULT_DATA, indent=2), "json")
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            w.editor()
            w.player()
            w.pie(w.editor.get_content("Pie chart"))
            w.radar(w.editor.get_content("Radar chart"))
            w.card(w.editor.get_content("Card content"))
            w.data_grid(w.editor.get_content("Data grid"))

    
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
                - sickly: (air purity, pollution)
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

    st.title("Demographic And Socioeconomic Information Sources")
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
