import pandas as pd
import plotly.io as pio
import graphs


# Load dataset
df = pd.read_csv(
    "Data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# List of graphs
charts = [
    ("Employee Attrition Distribution", graphs.attrition_distribution(df)),
    ("Department-wise Employee Count", graphs.department_employee_count(df)),
    ("Department-wise Attrition", graphs.department_attrition(df)),
    ("Employee Count by Job Role", graphs.job_role_employee_count(df)),
    ("Job Role-wise Attrition", graphs.job_role_attrition(df)),
    ("Overtime vs Attrition", graphs.overtime_attrition(df)),
    ("Job Satisfaction vs Attrition", graphs.job_satisfaction_attrition(df)),
    ("Employee Age Distribution", graphs.age_distribution(df)),
    ("Age Distribution by Attrition", graphs.age_attrition(df)),
    ("Gender-wise Attrition", graphs.gender_attrition(df)),
    ("Business Travel vs Attrition", graphs.business_travel_attrition(df)),
    ("Monthly Income Distribution", graphs.income_distribution(df)),
    ("Monthly Income vs Attrition", graphs.income_attrition(df)),
    ("Distance from Home vs Attrition", graphs.distance_attrition(df)),
    ("Years at Company vs Attrition", graphs.years_company_attrition(df)),
    ("Job Level vs Attrition", graphs.job_level_attrition(df)),
    ("Work-Life Balance vs Attrition", graphs.work_life_balance_attrition(df)),
    ("Environment Satisfaction vs Attrition",
     graphs.environment_satisfaction_attrition(df)),
    ("Training Frequency vs Attrition", graphs.training_attrition(df)),
    ("Performance Rating vs Attrition", graphs.performance_attrition(df))
]


# Create one HTML page containing all graphs
html_parts = [
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IBM HR Analytics - Plotly Graphs</title>

        <style>
            body {
                background: #0b1120;
                color: white;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 30px;
            }

            h1 {
                text-align: center;
                margin-bottom: 40px;
            }

            .chart {
                background: #111827;
                border-radius: 18px;
                padding: 20px;
                margin-bottom: 35px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.35);
            }
        </style>
    </head>

    <body>

    <h1>IBM HR Analytics - Data Visualization</h1>
    """
]

for index, (title, fig) in enumerate(charts):

    chart_html = pio.to_html(
        fig,
        full_html=False,
        include_plotlyjs=True if index == 0 else False
    )

    html_parts.append(
        f"""
        <div class="chart">
            {chart_html}
        </div>
        """
    )

html_parts.append(
    """
    </body>
    </html>
    """
)

# Save HTML
with open(
    "plotly_graphs.html",
    "w",
    encoding="utf-8"
) as file:
    file.write("\n".join(html_parts))

print("All graphs generated successfully!")
print("Open: plotly_graphs.html")