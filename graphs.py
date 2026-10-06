# ============================================================
# IBM HR ANALYTICS
# graphs.py
# Plotly Graphs Only
# ============================================================

import plotly.express as px


# ============================================================
# COMMON PROFESSIONAL THEME
# ============================================================

def apply_theme(fig, title=None):

    if title:
        fig.update_layout(title=title)

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial",
            size=13
        ),
        title_font=dict(
            size=20
        ),
        margin=dict(
            l=40,
            r=40,
            t=65,
            b=45
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    fig.update_xaxes(
        showgrid=False
    )

    fig.update_yaxes(
        gridcolor="rgba(255,255,255,0.10)"
    )

    return fig


# ============================================================
# 1. ATTRITION DISTRIBUTION
# ============================================================

def attrition_distribution(df):

    data = (
        df["Attrition"]
        .value_counts()
        .reset_index()
    )

    data.columns = ["Attrition", "Employees"]

    fig = px.pie(
        data,
        names="Attrition",
        values="Employees",
        hole=0.55,
        title="Employee Attrition Distribution"
    )

    fig.update_traces(
        textinfo="label+percent",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Employees: %{value}<br>"
            "Percentage: %{percent}"
            "<extra></extra>"
        )
    )

    return apply_theme(fig)


# ============================================================
# 2. DEPARTMENT-WISE EMPLOYEE COUNT
# ============================================================

def department_employee_count(df):

    data = (
        df["Department"]
        .value_counts()
        .reset_index()
    )

    data.columns = ["Department", "Employees"]

    fig = px.bar(
        data,
        x="Department",
        y="Employees",
        title="Department-wise Employee Count",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 3. DEPARTMENT-WISE ATTRITION
# ============================================================

def department_attrition(df):

    data = (
        df.groupby(["Department", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="Department",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Department-wise Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 4. JOB ROLE EMPLOYEE COUNT
# ============================================================

def job_role_employee_count(df):

    data = (
        df["JobRole"]
        .value_counts()
        .reset_index()
    )

    data.columns = ["JobRole", "Employees"]

    data = data.sort_values(
        "Employees",
        ascending=True
    )

    fig = px.bar(
        data,
        x="Employees",
        y="JobRole",
        orientation="h",
        title="Employee Count by Job Role",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 5. JOB ROLE-WISE ATTRITION
# ============================================================

def job_role_attrition(df):

    data = (
        df.groupby(["JobRole", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="JobRole",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Job Role-wise Attrition"
    )

    fig.update_layout(
        xaxis_tickangle=-35
    )

    return apply_theme(fig)


# ============================================================
# 6. OVERTIME VS ATTRITION
# ============================================================

def overtime_attrition(df):

    data = (
        df.groupby(["OverTime", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="OverTime",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Overtime vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 7. JOB SATISFACTION VS ATTRITION
# ============================================================

def job_satisfaction_attrition(df):

    data = (
        df.groupby(["JobSatisfaction", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="JobSatisfaction",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Job Satisfaction vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Job Satisfaction Level",
        yaxis_title="Number of Employees"
    )

    return apply_theme(fig)


# ============================================================
# 8. AGE DISTRIBUTION
# ============================================================

def age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=20,
        title="Employee Age Distribution"
    )

    return apply_theme(fig)


# ============================================================
# 9. AGE VS ATTRITION
# ============================================================

def age_attrition(df):

    fig = px.histogram(
        df,
        x="Age",
        color="Attrition",
        nbins=20,
        barmode="overlay",
        opacity=0.75,
        title="Age Distribution by Attrition"
    )

    return apply_theme(fig)


# ============================================================
# 10. GENDER-WISE ATTRITION
# ============================================================

def gender_attrition(df):

    data = (
        df.groupby(["Gender", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="Gender",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Gender-wise Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 11. BUSINESS TRAVEL VS ATTRITION
# ============================================================

def business_travel_attrition(df):

    data = (
        df.groupby(["BusinessTravel", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="BusinessTravel",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Business Travel vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 12. MONTHLY INCOME DISTRIBUTION
# ============================================================

def income_distribution(df):

    fig = px.histogram(
        df,
        x="MonthlyIncome",
        nbins=30,
        title="Monthly Income Distribution"
    )

    return apply_theme(fig)


# ============================================================
# 13. MONTHLY INCOME VS ATTRITION
# ============================================================

def income_attrition(df):

    fig = px.box(
        df,
        x="Attrition",
        y="MonthlyIncome",
        color="Attrition",
        title="Monthly Income vs Attrition"
    )

    return apply_theme(fig)


# ============================================================
# 14. DISTANCE FROM HOME VS ATTRITION
# ============================================================

def distance_attrition(df):

    fig = px.box(
        df,
        x="Attrition",
        y="DistanceFromHome",
        color="Attrition",
        title="Distance from Home vs Attrition"
    )

    return apply_theme(fig)


# ============================================================
# 15. YEARS AT COMPANY VS ATTRITION
# ============================================================

def years_company_attrition(df):

    fig = px.box(
        df,
        x="Attrition",
        y="YearsAtCompany",
        color="Attrition",
        title="Years at Company vs Attrition"
    )

    return apply_theme(fig)


# ============================================================
# 16. JOB LEVEL VS ATTRITION
# ============================================================

def job_level_attrition(df):

    data = (
        df.groupby(["JobLevel", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="JobLevel",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Job Level vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 17. WORK-LIFE BALANCE VS ATTRITION
# ============================================================

def work_life_balance_attrition(df):

    data = (
        df.groupby(["WorkLifeBalance", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="WorkLifeBalance",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Work-Life Balance vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 18. ENVIRONMENT SATISFACTION VS ATTRITION
# ============================================================

def environment_satisfaction_attrition(df):

    data = (
        df.groupby(["EnvironmentSatisfaction", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="EnvironmentSatisfaction",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Environment Satisfaction vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 19. TRAINING FREQUENCY VS ATTRITION
# ============================================================

def training_attrition(df):

    data = (
        df.groupby(["TrainingTimesLastYear", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="TrainingTimesLastYear",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Training Frequency vs Attrition"
    )

    return apply_theme(fig)


# ============================================================
# 20. PERFORMANCE RATING VS ATTRITION
# ============================================================

def performance_attrition(df):

    data = (
        df.groupby(["PerformanceRating", "Attrition"])
        .size()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        data,
        x="PerformanceRating",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Performance Rating vs Attrition",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    return apply_theme(fig)


# ============================================================
# 21. TOTAL KPI DATA
# ============================================================

def get_kpi_data(df):

    total_employees = len(df)

    attrition_count = (
        df["Attrition"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .sum()
    )

    attrition_rate = (
        (attrition_count / total_employees) * 100
        if total_employees > 0
        else 0
    )

    overtime_employees = (
        df["OverTime"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .sum()
    )

    average_age = df["Age"].mean()

    return {
        "total_employees": total_employees,
        "attrition_count": int(attrition_count),
        "attrition_rate": round(attrition_rate, 2),
        "overtime_employees": int(overtime_employees),
        "average_age": round(average_age, 1)
    }