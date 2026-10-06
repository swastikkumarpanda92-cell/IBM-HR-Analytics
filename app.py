import pandas as pd

# ============================================================
# IBM HR ANALYTICS - DATA ANALYSIS
# Step 1: Data Loading, Cleaning & Exploratory Analysis
# ============================================================

print("\n" + "=" * 70)
print("              IBM HR ANALYTICS PROJECT")
print("       Employee Attrition Analysis - Step 1")
print("=" * 70)

# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = "Data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(file_path)

print("\n[1] DATASET LOADED SUCCESSFULLY")
print("-" * 70)

# ============================================================
# 2. DATA PREVIEW
# ============================================================

print("\n[2] FIRST 5 ROWS")
print("-" * 70)
print(df.head().to_string())

# ============================================================
# 3. DATASET SIZE
# ============================================================

print("\n[3] DATASET SIZE")
print("-" * 70)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ============================================================
# 4. COLUMN INFORMATION
# ============================================================

print("\n[4] COLUMN NAMES")
print("-" * 70)

for i, column in enumerate(df.columns, start=1):
    print(f"{i:2}. {column}")

# ============================================================
# 5. DATA TYPES
# ============================================================

print("\n[5] DATA TYPES")
print("-" * 70)
print(df.dtypes.to_string())

# ============================================================
# 6. MISSING VALUES
# ============================================================

print("\n[6] MISSING VALUES")
print("-" * 70)

missing_values = df.isnull().sum()

print(missing_values.to_string())

total_missing = missing_values.sum()

print(f"\nTotal Missing Values: {total_missing}")

# ============================================================
# 7. DUPLICATE ROWS
# ============================================================

print("\n[7] DUPLICATE ROWS")
print("-" * 70)

duplicate_count = df.duplicated().sum()

print(f"Duplicate Rows: {duplicate_count}")

# ============================================================
# 8. REMOVE DUPLICATES
# ============================================================

if duplicate_count > 0:
    df = df.drop_duplicates()
    print("Duplicates removed successfully.")
else:
    print("No duplicates found. Dataset is already clean.")

# ============================================================
# 9. BASIC STATISTICS
# ============================================================

print("\n[8] BASIC STATISTICS")
print("-" * 70)

print(df.describe().to_string())

# ============================================================
# 10. TOTAL EMPLOYEES
# ============================================================

total_employees = len(df)

print("\n[9] TOTAL EMPLOYEES")
print("-" * 70)
print(f"Total Employees: {total_employees}")

# ============================================================
# 11. ATTRITION ANALYSIS
# ============================================================

print("\n[10] ATTRITION ANALYSIS")
print("-" * 70)

attrition_count = df["Attrition"].value_counts()

print(attrition_count.to_string())

employees_left = (df["Attrition"] == "Yes").sum()
employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = (employees_left / total_employees) * 100

print(f"\nEmployees Left   : {employees_left}")
print(f"Employees Stayed : {employees_stayed}")
print(f"Attrition Rate   : {attrition_rate:.2f}%")

# ============================================================
# 12. DEPARTMENT ANALYSIS
# ============================================================

print("\n[11] DEPARTMENT-WISE EMPLOYEE COUNT")
print("-" * 70)

department_count = df["Department"].value_counts()

print(department_count.to_string())

print("\nDEPARTMENT-WISE ATTRITION")
print("-" * 70)

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

print(department_attrition.to_string())

# ============================================================
# 13. JOB ROLE ANALYSIS
# ============================================================

print("\n[12] JOB ROLE-WISE EMPLOYEE COUNT")
print("-" * 70)

jobrole_count = df["JobRole"].value_counts()

print(jobrole_count.to_string())

print("\nJOB ROLE-WISE ATTRITION")
print("-" * 70)

jobrole_attrition = pd.crosstab(
    df["JobRole"],
    df["Attrition"]
)

print(jobrole_attrition.to_string())

# ============================================================
# 14. OVERTIME ANALYSIS
# ============================================================

print("\n[13] OVERTIME VS ATTRITION")
print("-" * 70)

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

print(overtime_attrition.to_string())

# ============================================================
# 15. JOB SATISFACTION ANALYSIS
# ============================================================

print("\n[14] JOB SATISFACTION VS ATTRITION")
print("-" * 70)

satisfaction_attrition = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"]
)

print(satisfaction_attrition.to_string())

# ============================================================
# 16. BUSINESS TRAVEL ANALYSIS
# ============================================================

print("\n[15] BUSINESS TRAVEL VS ATTRITION")
print("-" * 70)

travel_attrition = pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"]
)

print(travel_attrition.to_string())

# ============================================================
# 17. GENDER ANALYSIS
# ============================================================

print("\n[16] GENDER VS ATTRITION")
print("-" * 70)

gender_attrition = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

print(gender_attrition.to_string())

# ============================================================
# 18. MARITAL STATUS ANALYSIS
# ============================================================

print("\n[17] MARITAL STATUS VS ATTRITION")
print("-" * 70)

marital_attrition = pd.crosstab(
    df["MaritalStatus"],
    df["Attrition"]
)

print(marital_attrition.to_string())

# ============================================================
# 19. EDUCATION FIELD ANALYSIS
# ============================================================

print("\n[18] EDUCATION FIELD VS ATTRITION")
print("-" * 70)

education_attrition = pd.crosstab(
    df["EducationField"],
    df["Attrition"]
)

print(education_attrition.to_string())

# ============================================================
# 20. AGE ANALYSIS
# ============================================================

print("\n[19] AGE ANALYSIS")
print("-" * 70)

print(f"Average Age: {df['Age'].mean():.2f}")

print("\nAverage Age by Attrition:")
print(
    df.groupby("Attrition")["Age"]
    .mean()
    .round(2)
    .to_string()
)

# ============================================================
# 21. MONTHLY INCOME ANALYSIS
# ============================================================

print("\n[20] MONTHLY INCOME ANALYSIS")
print("-" * 70)

print(f"Average Monthly Income: {df['MonthlyIncome'].mean():.2f}")

print("\nAverage Monthly Income by Attrition:")
print(
    df.groupby("Attrition")["MonthlyIncome"]
    .mean()
    .round(2)
    .to_string()
)

# ============================================================
# 22. YEARS AT COMPANY ANALYSIS
# ============================================================

print("\n[21] EXPERIENCE ANALYSIS")
print("-" * 70)

print(f"Average Years at Company: {df['YearsAtCompany'].mean():.2f}")

print("\nAverage Years at Company by Attrition:")
print(
    df.groupby("Attrition")["YearsAtCompany"]
    .mean()
    .round(2)
    .to_string()
)

# ============================================================
# 23. WORK-LIFE BALANCE
# ============================================================

print("\n[22] WORK-LIFE BALANCE VS ATTRITION")
print("-" * 70)

worklife_attrition = pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"]
)

print(worklife_attrition.to_string())

# ============================================================
# 24. ENVIRONMENT SATISFACTION
# ============================================================

print("\n[23] ENVIRONMENT SATISFACTION VS ATTRITION")
print("-" * 70)

environment_attrition = pd.crosstab(
    df["EnvironmentSatisfaction"],
    df["Attrition"]
)

print(environment_attrition.to_string())

# ============================================================
# 25. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                     PROJECT SUMMARY")
print("=" * 70)

print(f"Total Employees       : {total_employees}")
print(f"Employees Left        : {employees_left}")
print(f"Employees Stayed      : {employees_stayed}")
print(f"Attrition Rate        : {attrition_rate:.2f}%")
print(f"Departments           : {df['Department'].nunique()}")
print(f"Job Roles             : {df['JobRole'].nunique()}")
print(f"Education Fields      : {df['EducationField'].nunique()}")
print(f"Missing Values        : {df.isnull().sum().sum()}")
print(f"Duplicate Rows        : {df.duplicated().sum()}")

print("=" * 70)
print("          STEP 1 - DATA ANALYSIS COMPLETED")
print("=" * 70)

print("\nDataset is ready for dashboard development.")