# Ministry of Magic Tableau HR Dashboard End-to-End Project

![](https://github.com/brucec0des/SQL-Python-Tableau-Harry-Potter-Project/blob/main/ASSETS/mom4.png)

## Project Overview

This project is an end-to-end data analysis solution designed to extract critical business insights from the Ministry of Magic's HR database. I utilized Python & AI for dataset creation, data processing and analysis, SAS for advanced querying, and structured problem-solving techniques to solve key business questions, and Tableau to data visualization. This project helped me to refine my skills in data manipulation, SAS querying, and data pipeline creation while utilizing AI when appropriate to increase efficiency.

![Dashboard Preview](https://github.com/brucec0des/SQL-Python-Tableau-Harry-Potter-Project/blob/main/ASSETS/HR%20%20Summary.png)

## ⭐Live Dashboard Demo: [Click here to explore the interactive demo!](https://public.tableau.com/app/profile/bruce.harper8067/viz/MinistryofMagicHRDashboard/HRSummary)

---

## Project Steps

### 1. Set Up the Environment
   - **Tools Used**: ChatGPT, Python, SAS Studio, Tableau
   - **Goal**: Use AI and Python to generate a robust dataset to query in SAS Studio and visualize using Tableau.

### 2. Generate the Python script
   - **ChatGPT Prompt**: Submit the following prompt to ChatGPT:
   ```
   Generate python script to generate a realistic Harry Potter themed dataset of 8950 records for the Ministry of Magic's human resources department. The dataset should include the following attributes:
   Employee ID: A unique identifier.
   First Name: Randomly generated using common European first names.
   Last Name: Randomly generated using any of the first 200 surnames you can find from the Harry Potter universe.
   Gender: Randomly chosen with a 46% probability for ‘Female’ and a 54% probability for ‘Male’.
   Country and City: Randomly assigned from a predefined list of European countries and their cities.
   Hire Date: Randomly generated with custom probabilities for each year from 2015 to 2024.
   Department: Randomly chosen from a list of departments with specified probabilities.
   Job Title: Randomly selected based on the department, with specific probabilities for each job title within the department.
   Education Level: Determined based on the job title, chosen from a predefined mapping of job titles to education levels.
   Performance Rating: Randomly selected from ‘Excellent’, ‘Good’, ‘Satisfactory’, ‘Needs Improvement’ with specified probabilities.
   Overtime: Randomly chosen with a 30% probability for ‘Yes’ and a 70% probability for ‘No’.
   Salary: Generated based on the department and job title, within specific ranges.
   Birth Date: Generated based on age group distribution and job title requirements, ensuring consistency with the hire date.
   Termination Date: Assigned to a subset of employees (11.2% of the total) with specific probabilities for each year from 2015 to 2024, ensuring the termination date is at least 6 months after the hire date.
   Adjusted Salary: Calculated based on gender, education level, and age, applying specific multipliers and increments.
   Be sure to structure the code cleanly, using functions where appropriate, and include comments to explain each step of the process.
   ```

### 3. Install Required Libraries and Load Data in VS Code
   - **Libraries**: Open VS Code, create a new virtual environment and install necessary Python libraries using:
     ```bash
     pip install pandas numpy sqlalchemy psycopg
     ```
   - **Loading Data**: Read the data into a Pandas DataFrame for initial analysis and transformations.

### 4. Explore the Data
   - **Goal**: Conduct an initial data exploration to understand data distribution, check column names, types, and identify potential issues.
   - **Analysis**: Use functions like `.info()`, `.describe()`, and `.head()` to get a quick overview of the data structure and statistics.

### 5. Data Cleaning
   - **Remove Duplicates**: Identify and remove duplicate entries to avoid skewed results.
   - **Handle Missing Values**: Drop rows or columns with missing values if they are insignificant; fill values where essential.
   - **Fix Data Types**: Ensure all columns have consistent data types (e.g., dates as `datetime`, prices as `float`).
   - **Currency Formatting**: Use `.replace()` to handle and format currency values for analysis.
   - **Validation**: Check for any remaining inconsistencies and verify the cleaned data.

### 6. Load Data into SAS Studio
   - **Upload CSV File to SAS Studio**: Create a new folder in SAS Studio and upload the CSV file there
   - **Libary Creation**: Use the libname statement to create a new library to hold the dataset
   - **Importing the Data**: Use proc import to convert the CSV file into a database for SAS querying

```
LIBNAME ministry "/home/bruceharp20/ministry/"; 

PROC IMPORT datafile="/home/bruceharp20/ministry/ministry_of_magic_hr_dataset.csv" out=MINISTRY.ministry dbms=csv;
run;

```

### 7. SAS Analysis: Complex Queries and Business Problem Solving
   - **Business Problem-Solving**: Write and execute SAS queries to answer critical business questions.
   - **Documentation**: Keep clear notes of each query's objective, approach, and results.
--- 

## Business Problems and Solutions

### 1. Find the average salary of employees working in the Auror Office department.

```sql
	PROC SQL;
		SELECT MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		WHERE department = 'Auror Office';
	QUIT;
```

### 2. Filter the dataset to list all employees who have "Excellent" performance ratings

```sql
	PROC SQL;
		SELECT *
		FROM MINISTRY.MINISTRY
		WHERE performance_rating = 'Excellent';
	QUIT;
```

### 3. Create a summary of the average adjusted salary grouped by gender

```sql
	PROC SQL;
		SELECT gender, MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		GROUP BY gender;
	QUIT;
```

### 4. List the names of the employees terminated from the company

```sql
	PROC SQL;
		SELECT first_name, last_name
		FROM MINISTRY.MINISTRY
		WHERE termination_date IS MISSING;
	QUIT;
```

### 5. Calculate the number of employees per country and sort the result in descending order

```sql
	PROC SQL;
		SELECT country, COUNT(*) AS total
		FROM MINISTRY.MINISTRY
		GROUP BY country
		ORDER BY total DESC;
	QUIT;
```

### 6. Create a new column to calculate the employee's tenure (in years) based on the difference between today's date and the hire_date

```sql
	DATA tenure;
		SET MINISTRY.MINISTRY;
		tenure = INTCK('year', hire_date, today());
	RUN;
```

### 7. Identify the top 3 cities with the highest average salaries and list the city names along with their average salary

```sql
	PROC SQL OUTOBS=3;
		SELECT city, MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		GROUP BY city
		ORDER BY avg_salary DESC;
	QUIT;
```

### 8. For each job title, calculate the total salary paid to all employees holding that title

```sql
	PROC SQL;
		SELECT job_title, SUM(adjusted_salary) AS total_salary
		FROM MINISTRY.MINISTRY
		GROUP BY job_title;
	QUIT;
```

### 9. Create a summary report of the number of employees grouped by their education level and overtime status

```sql
	PROC SQL;
		SELECT education_level, overtime, COUNT(*) as total_employees
		FROM MINISTRY.MINISTRY
		GROUP BY education_level, overtime;
	QUIT;
```

### 10. Create a flag column in the dataset indicating if an employee is eligible for a promotion based on the following criteria:
   - Performance rating is "Excellent"
   - Tenure is more than 3 years

```sql
	DATA promotion_flag;
		SET MINISTRY.MINISTRY;
		tenure = INTCK('year', hire_date, today());
		promotion_eligible = (performance_rating = "Excellent" AND tenure > 3);
	RUN;
```
---

### 8. Create the Dashboard

#### Guidelines for Creating the Dashboard

**User Story - HR Dashboard**
- As an HR manager, I want a comprehensive dashboard to analyze human resources data, providing both summary views for high-level insights and detailed employee records for in-depth analysis

**Summary View**
The summary view should be divided into three main sections: Overview, Demographics, and Income Analysis

**Overview** 
- The Overview section should provide a snapshot of the overall HR metrics, including:

   - Display the total number of hired employees, active employees, and terminated employees.
   - Visualize the total number of hired and terminated employees over the years.
   - Present a breakdown of total employees by department and job titles.
   - Compare total employees between headquarters (HQ) and branches (New York is the HQ)
   - Show the distribution of employees by city and state.

**Demographics**
- The Demographics section should offer insights into the composition of the workforce, including:

   - Present the gender ratio in the company.
   - Visualize the distribution of employees across age groups and education levels.
   - Show the total number of employees within each age group.
   - Show the total number of employees within each education level.
   - Present the correlation between employees’s educational backgrounds and their performance ratings.

**Income**
- The income analysis section should focus on salary-related metrics, including:

   - Compare salaries across different education levels for both genders to identify any discrepancies or patterns.
   - Present how the age correlate with the salary for employees in each department.

**Employee Records View**

- Provide a comprehensive list of all employees with necessary information such as name, department, position, gender, age, education, and salary.
- Users should be able to filter the list based on any of the available columns.

### 9. Project Publishing and Documentation
- **Documentation**: Maintain well-structured documentation of the entire process in Markdown or a Jupyter Notebook.
- **Project Publishing**: Publish the completed project on GitHub or any other version control platform, including:
   - The `README.md` file (this document).
   - Jupyter Notebooks (if applicable).
   - SAS query scripts.
   - Data files (if possible) or steps to access them.
   - Tableau workspace

---

## Requirements

- **Python 3.8+**
- **SAS Databases**: SAS Studio
- **Python Libraries**:
  - `pandas`, `numpy`, `sqlalchemy`, `psycopg`
- **ChatGPT** (for dataset creation)
- **Tableau Public** (for data visualization)

---

## Inspiration

While watching Harry Potter and the Deathly Hallows: Part One, there's a scene where Harry, Ron, and Harmoine are caught in the woods by Ministry of Magic bounty hunters. Harry gives them a fake name which they reference against a list of all known wizards.  It got me thinking: what does this database look like? What sort of SAS queries would a data analyst for the Ministry of Magic make? After doing some research, I realized how easily I could leverage AI and Python's Faker library to answer these questions with a custom dataset based on the Harry Potter universe.

![](https://github.com/brucec0des/SAS-Python-Tableau-Harry-Potter-Project/blob/main/ASSETS/momai.jpg)

---

## Author - Bruce Harper

This project is part of my portfolio, showcasing the Tableau, SQL & Python skills essential for data analyst roles. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!

---