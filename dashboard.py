import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="IBM HR Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DATA PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR
    / "Data"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv(DATA_PATH)

    data = data.drop_duplicates()

    return data


try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "Dataset not found.\n\n"
        "Please make sure the CSV file is inside the Data folder."
    )

    st.stop()


# ============================================================
# COLORS
# ============================================================

BLUE = "#1677ff"
PURPLE = "#9b4de3"
GREEN = "#16e6a5"
RED = "#e05a47"


# ============================================================
# THEME COLORS
# ============================================================

if st.session_state.dark_mode:

    BACKGROUND = "#061426"
    SIDEBAR = "#06101e"
    CARD = "#091c35"
    BORDER = "#174d84"
    TEXT = "#f4f7ff"
    MUTED = "#9db8dd"
    GRID = "#173657"

else:

    BACKGROUND = "#eef4fb"
    SIDEBAR = "#ffffff"
    CARD = "#ffffff"
    BORDER = "#b8cce3"
    TEXT = "#10233e"
    MUTED = "#55708f"
    GRID = "#cbd8e8"


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ======================================================
       MAIN APPLICATION
       ====================================================== */

    .stApp {{
        background: {BACKGROUND};
        color: {TEXT};
    }}

    .main .block-container {{
        max-width: 1500px;
        padding: 25px 32px 40px 32px;
    }}


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {{
        background: {SIDEBAR} !important;
        border-right: 1px solid {BORDER};
    }}

    section[data-testid="stSidebar"] > div {{
        padding: 25px 18px;
    }}

    section[data-testid="stSidebar"] label {{
        color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
        background-color: #05080d !important;
        border: 1px solid #24568b !important;
        border-radius: 7px !important;
        color: white !important;
        min-height: 40px !important;
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] span {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] svg {{
        fill: white !important;
    }}

    div[data-baseweb="popover"] {{
        background-color: #081525 !important;
        border: 1px solid #24568b !important;
        border-radius: 8px !important;
    }}

    div[data-baseweb="popover"] li {{
        background-color: #081525 !important;
        color: white !important;
    }}

    div[data-baseweb="popover"] li:hover {{
        background-color: #12345a !important;
        color: white !important;
    }}

    div[data-baseweb="popover"] li[aria-selected="true"] {{
        background-color: #174d84 !important;
        color: white !important;
    }}


    /* ======================================================
       SIDEBAR RADIO
       ====================================================== */

    section[data-testid="stSidebar"]
    div[data-testid="stRadio"] label {{
        color: {TEXT} !important;
        font-size: 13px !important;
    }}


    /* ======================================================
       NORMAL BUTTONS
       ====================================================== */

    .stButton > button {{
        background-color: #1268db !important;
        color: white !important;
        border: 1px solid #287de5 !important;
        border-radius: 7px !important;
        font-weight: 700 !important;
    }}

    .stButton > button:hover {{
        background-color: #0d56ba !important;
        color: white !important;
        border-color: #4b9cff !important;
    }}

    .stButton > button p {{
        color: white !important;
    }}


    /* ======================================================
       DOWNLOAD BUTTONS
       BLACK BOX + WHITE TEXT
       ====================================================== */

    .stDownloadButton > button {{
        background-color: #05080d !important;
        color: #ffffff !important;
        border: 1px solid #24568b !important;
        border-radius: 8px !important;
        min-height: 45px !important;
        font-weight: 700 !important;
        box-shadow: none !important;
    }}

    .stDownloadButton > button:hover {{
        background-color: #0b1726 !important;
        color: #ffffff !important;
        border-color: #1677ff !important;
    }}

    .stDownloadButton > button:focus {{
        background-color: #05080d !important;
        color: #ffffff !important;
        border-color: #1677ff !important;
    }}

    .stDownloadButton > button p {{
        color: #ffffff !important;
    }}

    .stDownloadButton > button span {{
        color: #ffffff !important;
    }}


    /* ======================================================
       HEADER
       ====================================================== */

    .dashboard-title {{
        color: {TEXT};
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 4px;
    }}

    .dashboard-subtitle {{
        color: #9ab8e8;
        font-size: 14px;
        margin-bottom: 18px;
    }}

    .top-line {{
        height: 1px;
        background: linear-gradient(
            90deg,
            #1677ff,
            #28598e,
            transparent
        );
        margin-bottom: 20px;
    }}


    /* ======================================================
       KPI CARDS
       ====================================================== */

    div[data-testid="stMetric"] {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 18px 20px;
        min-height: 110px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.18);
    }}

    div[data-testid="stMetricLabel"] {{
        color: {MUTED} !important;
        font-size: 12px !important;
        font-weight: 800 !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {TEXT} !important;
        font-size: 29px !important;
        font-weight: 800 !important;
    }}

    div[data-testid="stMetricDelta"] {{
        color: {GREEN} !important;
        font-size: 11px !important;
    }}


    /* ======================================================
       SECTION TITLES
       ====================================================== */

    .section-title {{
        color: {TEXT};
        font-size: 19px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 8px;
    }}


    /* ======================================================
       PLOTLY CHART CARDS
       ====================================================== */

    div[data-testid="stPlotlyChart"] {{
        background: {CARD} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 10px !important;
        padding: 5px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.18) !important;
        margin-bottom: 14px !important;
    }}


    /* ======================================================
       DATAFRAME CONTAINER
       ====================================================== */

    div[data-testid="stDataFrame"] {{
        background-color: #05080d !important;
        border: 1px solid #24568b !important;
        border-radius: 8px !important;
    }}


    /* ======================================================
       EXPANDER
       ====================================================== */

    div[data-testid="stExpander"] {{
        background-color: {CARD} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 8px !important;
    }}


    /* ======================================================
       DIVIDER
       ====================================================== */

    hr {{
        border-color: #173657 !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# IBM"
    )

    st.markdown(
        "## HR ANALYTICS"
    )

    st.caption(
        "Employee Attrition Dashboard"
    )

    st.divider()

    st.markdown(
        "### Navigation"
    )

    navigation = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "💡 Insights",
            "📊 Reports",
            "⚙️ Settings"
        ],
        label_visibility="collapsed"
    )

    if navigation == "🏠 Dashboard":
        st.session_state.page = "Dashboard"

    elif navigation == "💡 Insights":
        st.session_state.page = "Insights"

    elif navigation == "📊 Reports":
        st.session_state.page = "Reports"

    elif navigation == "⚙️ Settings":
        st.session_state.page = "Settings"

    st.divider()

    st.markdown(
        "### 🔎 Filters"
    )

    departments = sorted(
        df["Department"]
        .dropna()
        .unique()
        .tolist()
    )

    job_roles = sorted(
        df["JobRole"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_department = st.selectbox(
        "Department",
        ["All Departments"] + departments,
        key="department_filter"
    )

    selected_role = st.selectbox(
        "Job Role",
        ["All Job Roles"] + job_roles,
        key="role_filter"
    )

    selected_overtime = st.selectbox(
        "Overtime",
        ["All", "Yes", "No"],
        key="overtime_filter"
    )

    selected_attrition = st.selectbox(
        "Attrition",
        ["All", "Yes", "No"],
        key="attrition_filter"
    )

    if st.button(
        "↻ Reset All Filters",
        use_container_width=True
    ):

        st.session_state.department_filter = "All Departments"
        st.session_state.role_filter = "All Job Roles"
        st.session_state.overtime_filter = "All"
        st.session_state.attrition_filter = "All"

        st.rerun()

    st.divider()

    st.markdown(
        "### 🗃 Dataset Info"
    )

    st.write(
        f"**Employees:** {len(df):,}"
    )

    st.write(
        f"**Features:** {len(df.columns)}"
    )

    st.write(
        f"**Missing Values:** "
        f"{int(df.isnull().sum().sum())}"
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

if selected_department != "All Departments":

    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

if selected_role != "All Job Roles":

    filtered_df = filtered_df[
        filtered_df["JobRole"] == selected_role
    ]

if selected_overtime != "All":

    filtered_df = filtered_df[
        filtered_df["OverTime"] == selected_overtime
    ]

if selected_attrition != "All":

    filtered_df = filtered_df[
        filtered_df["Attrition"] == selected_attrition
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_employees = len(filtered_df)

employees_left = int(
    (filtered_df["Attrition"] == "Yes").sum()
)

employees_stayed = int(
    (filtered_df["Attrition"] == "No").sum()
)

if total_employees > 0:

    attrition_rate = (
        employees_left /
        total_employees
    ) * 100

    average_age = filtered_df["Age"].mean()

else:

    attrition_rate = 0

    average_age = 0


# ============================================================
# CHART PREPARATION FUNCTION
# ============================================================

def prepare_chart(
    fig,
    title,
    height=350
):

    fig.update_layout(

        title=dict(
            text=title,
            font=dict(
                size=15,
                color=TEXT
            )
        ),

        height=height,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color=TEXT
        ),

        margin=dict(
            l=50,
            r=25,
            t=55,
            b=50
        ),

        legend=dict(
            font=dict(
                color=TEXT
            )
        ),

        hoverlabel=dict(
            bgcolor="#0b1d33",
            font_color="white"
        )
    )

    fig.update_xaxes(
        gridcolor=GRID
    )

    fig.update_yaxes(
        gridcolor=GRID
    )

    return fig


# ============================================================
# DASHBOARD PAGE
# ============================================================

if st.session_state.page == "Dashboard":

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        '<div class="dashboard-title">'
        'IBM HR Analytics Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Employee Attrition Analysis & Workforce Intelligence'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="top-line"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # THEME BUTTON
    # ========================================================

    top_left, top_right = st.columns(
        [8, 1]
    )

    with top_right:

        if st.button(
            "☼ Theme",
            use_container_width=True
        ):

            st.session_state.dark_mode = (
                not st.session_state.dark_mode
            )

            st.rerun()


    # ========================================================
    # KPI CARDS
    # ========================================================

    k1, k2, k3, k4 = st.columns(4)

    with k1:

        st.metric(
            label="TOTAL EMPLOYEES",
            value=f"{total_employees:,}",
            delta="Current filtered workforce"
        )

    with k2:

        st.metric(
            label="EMPLOYEES LEFT",
            value=f"{employees_left:,}",
            delta="Attrition = Yes"
        )

    with k3:

        st.metric(
            label="ATTRITION RATE",
            value=f"{attrition_rate:.2f}%",
            delta="Employee turnover"
        )

    with k4:

        st.metric(
            label="AVG. AGE",
            value=f"{average_age:.1f}",
            delta="Workforce average"
        )


    # ========================================================
    # EMPTY FILTER RESULT
    # ========================================================

    if filtered_df.empty:

        st.warning(
            "No employees match the selected filters."
        )

        st.stop()


    # ========================================================
    # GRAPH 1 + GRAPH 2
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        'Workforce Overview'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    # GRAPH 1
    with col1:

        attrition_counts = (
            filtered_df["Attrition"]
            .value_counts()
            .reindex(
                ["No", "Yes"],
                fill_value=0
            )
        )

        fig = go.Figure(
            go.Pie(
                labels=[
                    "Stayed",
                    "Left"
                ],
                values=[
                    attrition_counts["No"],
                    attrition_counts["Yes"]
                ],
                hole=0.62,
                marker=dict(
                    colors=[
                        BLUE,
                        PURPLE
                    ]
                ),
                textinfo="percent",
                hovertemplate=
                "<b>%{label}</b><br>"
                "Employees: %{value}<br>"
                "%{percent}"
                "<extra></extra>"
            )
        )

        fig.add_annotation(
            text=(
                f"<b>{attrition_rate:.2f}%</b>"
                "<br>"
                "<span style='font-size:11px'>"
                "Attrition Rate"
                "</span>"
            ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(
                color=TEXT,
                size=17
            )
        )

        fig = prepare_chart(
            fig,
            "Employee Attrition Distribution",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 2
    with col2:

        data = pd.crosstab(
            filtered_df["Department"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["Department"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE,
                text=data["No"],
                textposition="outside"
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["Department"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE,
                text=data["Yes"],
                textposition="outside"
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Department-wise Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 3 + GRAPH 4
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 3
    with col1:

        data = (
            filtered_df["JobRole"]
            .value_counts()
            .sort_values()
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data.values,
                y=data.index,
                orientation="h",
                marker_color=BLUE,
                text=data.values,
                textposition="outside"
            )
        )

        fig = prepare_chart(
            fig,
            "Job Role-wise Employee Count",
            400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 4
    with col2:

        data = (
            filtered_df
            .groupby("JobRole")["Attrition"]
            .apply(
                lambda x:
                (x == "Yes").mean() * 100
            )
            .sort_values()
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data.values,
                y=data.index,
                orientation="h",
                marker_color=PURPLE,
                text=[
                    f"{x:.1f}%"
                    for x in data.values
                ],
                textposition="outside"
            )
        )

        fig = prepare_chart(
            fig,
            "Job Role-wise Attrition Rate",
            400
        )

        fig.update_xaxes(
            title="Attrition Rate (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 5 + GRAPH 6
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 5
    with col1:

        data = pd.crosstab(
            filtered_df["OverTime"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["OverTime"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE,
                text=data["No"],
                textposition="outside"
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["OverTime"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE,
                text=data["Yes"],
                textposition="outside"
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Overtime vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 6
    with col2:

        fig = px.histogram(
            filtered_df,
            x="Age",
            color="Attrition",
            nbins=18,
            barmode="group",
            color_discrete_map={
                "No": BLUE,
                "Yes": PURPLE
            }
        )

        fig = prepare_chart(
            fig,
            "Age Distribution by Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 7 + GRAPH 8
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 7
    with col1:

        fig = px.box(
            filtered_df,
            x="Attrition",
            y="MonthlyIncome",
            color="Attrition",
            points="outliers",
            color_discrete_map={
                "No": BLUE,
                "Yes": PURPLE
            }
        )

        fig = prepare_chart(
            fig,
            "Monthly Income vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 8
    with col2:

        data = pd.crosstab(
            filtered_df["JobSatisfaction"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["JobSatisfaction"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE,
                text=data["No"],
                textposition="outside"
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["JobSatisfaction"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE,
                text=data["Yes"],
                textposition="outside"
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Job Satisfaction vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 9 + GRAPH 10
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 9
    with col1:

        data = pd.crosstab(
            filtered_df["EnvironmentSatisfaction"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["EnvironmentSatisfaction"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["EnvironmentSatisfaction"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Environment Satisfaction vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 10
    with col2:

        data = pd.crosstab(
            filtered_df["RelationshipSatisfaction"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["RelationshipSatisfaction"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["RelationshipSatisfaction"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Relationship Satisfaction vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 11 + GRAPH 12
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 11
    with col1:

        data = pd.crosstab(
            filtered_df["WorkLifeBalance"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["WorkLifeBalance"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["WorkLifeBalance"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Work-Life Balance vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 12
    with col2:

        data = pd.crosstab(
            filtered_df["JobInvolvement"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["JobInvolvement"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["JobInvolvement"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Job Involvement vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 13 + GRAPH 14
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 13
    with col1:

        data = pd.crosstab(
            filtered_df["PerformanceRating"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["PerformanceRating"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["PerformanceRating"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Performance Rating vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 14
    with col2:

        data = pd.crosstab(
            filtered_df["BusinessTravel"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["BusinessTravel"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["BusinessTravel"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Business Travel vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 15 + GRAPH 16
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 15
    with col1:

        data = pd.crosstab(
            filtered_df["MaritalStatus"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["MaritalStatus"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["MaritalStatus"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Marital Status vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 16
    with col2:

        data = pd.crosstab(
            filtered_df["EducationField"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["EducationField"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["EducationField"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Education Field vs Attrition",
            350
        )

        fig.update_xaxes(
            tickangle=-25
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 17 + GRAPH 18
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 17
    with col1:

        data = pd.crosstab(
            filtered_df["Gender"],
            filtered_df["Attrition"]
        ).reset_index()

        if "No" not in data.columns:
            data["No"] = 0

        if "Yes" not in data.columns:
            data["Yes"] = 0

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=data["Gender"],
                y=data["No"],
                name="Stayed",
                marker_color=BLUE
            )
        )

        fig.add_trace(
            go.Bar(
                x=data["Gender"],
                y=data["Yes"],
                name="Left",
                marker_color=PURPLE
            )
        )

        fig.update_layout(
            barmode="group"
        )

        fig = prepare_chart(
            fig,
            "Gender vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 18
    with col2:

        fig = px.box(
            filtered_df,
            x="Attrition",
            y="DistanceFromHome",
            color="Attrition",
            points="outliers",
            color_discrete_map={
                "No": BLUE,
                "Yes": PURPLE
            }
        )

        fig = prepare_chart(
            fig,
            "Distance From Home vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GRAPH 19 + GRAPH 20
    # ========================================================

    col1, col2 = st.columns(2)


    # GRAPH 19
    with col1:

        fig = px.box(
            filtered_df,
            x="Attrition",
            y="YearsAtCompany",
            color="Attrition",
            points="outliers",
            color_discrete_map={
                "No": BLUE,
                "Yes": PURPLE
            }
        )

        fig = prepare_chart(
            fig,
            "Years at Company vs Attrition",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # GRAPH 20
    with col2:

        correlation_data = filtered_df[
            [
                "Age",
                "MonthlyIncome",
                "TotalWorkingYears",
                "JobSatisfaction",
                "PerformanceRating"
            ]
        ].copy()

        correlation_data["Attrition"] = (
            filtered_df["Attrition"]
            .map(
                {
                    "No": 0,
                    "Yes": 1
                }
            )
        )

        correlation_matrix = (
            correlation_data
            .corr(numeric_only=True)
        )

        fig = px.imshow(
            correlation_matrix,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1
        )

        fig = prepare_chart(
            fig,
            "Workforce Correlation Heatmap",
            350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# INSIGHTS PAGE
# ============================================================

elif st.session_state.page == "Insights":

    st.markdown(
        '<div class="dashboard-title">'
        'Workforce Insights'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Insights based on the currently selected filters.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # OVERTIME ANALYSIS
    # ========================================================

    overtime_yes = filtered_df[
        filtered_df["OverTime"] == "Yes"
    ]

    overtime_no = filtered_df[
        filtered_df["OverTime"] == "No"
    ]

    overtime_yes_rate = (

        (overtime_yes["Attrition"] == "Yes").mean() * 100

        if len(overtime_yes) > 0

        else 0
    )

    overtime_no_rate = (

        (overtime_no["Attrition"] == "Yes").mean() * 100

        if len(overtime_no) > 0

        else 0
    )


    # ========================================================
    # TOP DEPARTMENT
    # ========================================================

    department_counts = (
        filtered_df["Department"]
        .value_counts()
    )

    if len(department_counts) > 0:

        top_department = department_counts.idxmax()

    else:

        top_department = "N/A"


    # ========================================================
    # TOP ROLE
    # ========================================================

    role_counts = (
        filtered_df["JobRole"]
        .value_counts()
    )

    if len(role_counts) > 0:

        top_role = role_counts.idxmax()

    else:

        top_role = "N/A"


    # ========================================================
    # INSIGHT CARDS
    # ========================================================

    c1, c2 = st.columns(2)

    with c1:

        st.info(
            f"📈 **Attrition Rate:** "
            f"{attrition_rate:.2f}%"
        )

        st.info(
            f"🏢 **Largest Department:** "
            f"{top_department}"
        )

        st.info(
            f"💼 **Most Common Job Role:** "
            f"{top_role}"
        )

    with c2:

        st.info(
            f"⏰ **Overtime Attrition:** "
            f"{overtime_yes_rate:.2f}%"
        )

        st.info(
            f"🚫 **No Overtime Attrition:** "
            f"{overtime_no_rate:.2f}%"
        )

        st.info(
            f"🎂 **Average Age:** "
            f"{average_age:.1f} years"
        )


# ============================================================
# REPORTS PAGE
# ============================================================

elif st.session_state.page == "Reports":

    st.markdown(
        '<div class="dashboard-title">'
        'HR Reports'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Download reports generated from the filtered dataset.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # FILTERED DATASET
    # ========================================================

    st.subheader(
        "📄 Filtered Employee Dataset"
    )

    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇ Download Filtered CSV",
        data=csv_data,
        file_name="IBM_HR_Filtered_Data.csv",
        mime="text/csv",
        use_container_width=True
    )


    st.divider()


    # ========================================================
    # HR SUMMARY
    # ========================================================

    st.subheader(
        "📊 HR Summary"
    )

    summary = pd.DataFrame(
        {
            "Metric": [
                "Total Employees",
                "Employees Left",
                "Employees Stayed",
                "Attrition Rate",
                "Average Age"
            ],

            "Value": [
                total_employees,
                employees_left,
                employees_stayed,
                f"{attrition_rate:.2f}%",
                f"{average_age:.1f}"
            ]
        }
    )


    # --------------------------------------------------------
    # DARK SUMMARY TABLE
    # --------------------------------------------------------

    summary_style = (
        summary.style
        .set_properties(
            **{
                "background-color": "#05080d",
                "color": "#ffffff",
                "border-color": "#24568b",
                "font-size": "14px"
            }
        )
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "#0b1726"),
                        ("color", "#ffffff"),
                        ("border", "1px solid #24568b"),
                        ("font-weight", "700"),
                        ("text-align", "left")
                    ]
                },
                {
                    "selector": "td",
                    "props": [
                        ("background-color", "#05080d"),
                        ("color", "#ffffff"),
                        ("border", "1px solid #24568b")
                    ]
                }
            ]
        )
    )

    st.table(
        summary_style
    )


    # ========================================================
    # SUMMARY DOWNLOAD
    # ========================================================

    summary_csv = summary.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇ Download HR Summary",
        data=summary_csv,
        file_name="IBM_HR_Summary.csv",
        mime="text/csv",
        use_container_width=True
    )


    st.divider()


    # ========================================================
    # FILTERED DATA PREVIEW
    # ========================================================

    st.subheader(
        "👁 Filtered Data Preview"
    )

    st.dataframe(
        filtered_df.head(20),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# SETTINGS PAGE
# ============================================================

elif st.session_state.page == "Settings":

    st.markdown(
        '<div class="dashboard-title">'
        'Dashboard Settings'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Customize the dashboard appearance and view dataset information.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # THEME
    # ========================================================

    st.subheader(
        "🎨 Theme"
    )

    current_theme = (
        "Dark"
        if st.session_state.dark_mode
        else "Light"
    )

    selected_theme = st.radio(
        "Select dashboard theme",
        [
            "Dark",
            "Light"
        ],
        index=(
            0
            if current_theme == "Dark"
            else 1
        )
    )

    if selected_theme != current_theme:

        st.session_state.dark_mode = (
            selected_theme == "Dark"
        )

        st.rerun()


    st.divider()


    # ========================================================
    # DATASET INFORMATION
    # ========================================================

    st.subheader(
        "🗃 Dataset Information"
    )

    st.write(
        f"Total records: **{len(df):,}**"
    )

    st.write(
        f"Total features: **{len(df.columns)}**"
    )

    st.write(
        f"Missing values: "
        f"**{int(df.isnull().sum().sum())}**"
    )

    st.write(
        f"Filtered records: "
        f"**{len(filtered_df):,}**"
    )


    st.divider()


    # ========================================================
    # DATASET COLUMNS
    # ========================================================

    st.subheader(
        "📋 Dataset Columns"
    )

    column_info = pd.DataFrame(
        {
            "Column Name": df.columns,
            "Data Type": [
                str(dtype)
                for dtype in df.dtypes
            ]
        }
    )

    st.dataframe(
        column_info,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "IBM HR Analytics Dashboard • "
    "Python • Pandas • Plotly • Streamlit"
)