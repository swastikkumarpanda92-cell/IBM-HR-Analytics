# 📊 IBM HR Analytics Dashboard

A professional interactive HR Analytics dashboard built using **Python, Pandas, Plotly, and Streamlit** to analyze employee attrition and workforce patterns.

---

## 📌 Project Overview

Employee attrition is an important challenge for organizations because frequent employee turnover can affect productivity, workforce stability, and business performance.

This project analyzes the IBM HR Employee Attrition dataset and presents the findings through an interactive Streamlit dashboard.

The dashboard allows users to explore employee data through interactive filters, KPIs, charts, insights, and downloadable reports.

---

## 🎯 Project Objective

The main objectives of this project are:

- Analyze employee attrition patterns.
- Understand workforce distribution.
- Identify factors associated with employee turnover.
- Compare attrition across departments and job roles.
- Analyze the relationship between overtime and attrition.
- Study employee satisfaction and work-related factors.
- Provide an interactive dashboard for HR analysis.
- Generate filtered reports from the dataset.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Pandas | Data processing and analysis |
| Plotly | Interactive data visualization |
| Streamlit | Dashboard development |
| CSV Dataset | Data source |

---

## 📊 Dashboard Features

### 🏠 Dashboard

The main dashboard provides:

- Total Employees KPI
- Employees Left
- Attrition Rate
- Average Age
- Interactive filters
- 20 interactive visualizations
- Department analysis
- Job role analysis
- Overtime analysis
- Satisfaction analysis
- Workforce correlation analysis

---

## 📈 20 Visualizations

The dashboard contains **20 graphs**, organized as **2 graphs per row**.

### Workforce Overview

1. Employee Attrition Distribution
2. Department-wise Attrition

### Job Role Analysis

3. Job Role-wise Employee Count
4. Job Role-wise Attrition Rate

### Workforce Patterns

5. Overtime vs Attrition
6. Age Distribution by Attrition

### Compensation & Satisfaction

7. Monthly Income vs Attrition
8. Job Satisfaction vs Attrition

### Workplace Satisfaction

9. Environment Satisfaction vs Attrition
10. Relationship Satisfaction vs Attrition

### Employee Engagement

11. Work-Life Balance vs Attrition
12. Job Involvement vs Attrition

### Performance & Travel

13. Performance Rating vs Attrition
14. Business Travel vs Attrition

### Employee Demographics

15. Marital Status vs Attrition
16. Education Field vs Attrition
17. Gender vs Attrition

### Experience & Workforce Relationships

18. Distance From Home vs Attrition
19. Years at Company vs Attrition
20. Workforce Correlation Heatmap

---

## 🔎 Interactive Filters

Users can filter the dashboard using:

- Department
- Job Role
- Overtime
- Attrition

A **Reset All Filters** option is also available.

All dashboard calculations and visualizations update according to the selected filters.

---

## 💡 Insights Page

The Insights page provides a quick summary of important workforce indicators, including:

- Overall attrition rate
- Largest department
- Most common job role
- Overtime attrition
- Non-overtime attrition
- Average employee age

---

## 📄 Reports Page

The Reports section provides:

- Filtered employee dataset download
- HR summary report
- Filtered data preview

Users can download the filtered data as CSV files.

---

## ⚙️ Settings Page

The Settings section provides:

- Dashboard theme selection
- Dataset information
- Number of records
- Number of features
- Missing value information
- Filtered record count
- Dataset column information

---

## 🗂️ Project Structure

```text
IBM-HR-Analytics/
│
├── dashboard.py
├── app.py
├── README.md
├── requirements.txt
│
└── Data/
    └── WA_Fn-UseC_-HR-Employee-Attrition.csv