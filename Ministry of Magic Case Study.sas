/*
MINISTRY OF MAGIC SAS/SQL CASE STUDY

## PREPARATION;
-- import the dataset into SAS Studio:
*/

libname ministry "/home/bruceharp20/ministry/"; 

proc import datafile="/home/bruceharp20/ministry/ministry_of_magic_hr_dataset.csv" out=MINISTRY.ministry dbms=csv;

run;


*## QUESTIONS & ANSWERS;

*1. Find the average salary of employees working in the Auror Office department;

	PROC SQL;
		SELECT MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		WHERE department = 'Auror Office';
	QUIT;

*2. Filter the dataset to list all employees who have "Excellent" performance ratings;

	PROC SQL;
		SELECT *
		FROM MINISTRY.MINISTRY
		WHERE performance_rating = 'Excellent';
	QUIT;

*3. Create a summary of the average adjusted salary grouped by gender;

	PROC SQL;
		SELECT gender, MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		GROUP BY gender;
	QUIT;

*4. List the names of the employees terminated from the company;

	PROC SQL;
		SELECT first_name, last_name
		FROM MINISTRY.MINISTRY
		WHERE termination_date IS MISSING;
	QUIT;

*5.  Calculate the number of employees per country and sort the result in descending order;

	PROC SQL;
		SELECT country, COUNT(*) AS total
		FROM MINISTRY.MINISTRY
		GROUP BY country
		ORDER BY total DESC;
	QUIT;

*6.  Create a new column to calculate the employee's tenure (in years) based on the difference between today's date and the hire_date;

	DATA tenure;
		SET MINISTRY.MINISTRY;
		tenure = INTCK('year', hire_date, today());
	RUN;

*7. Identify the top 3 cities with the highest average salaries and list the city names along with their average salary;

	PROC SQL OUTOBS=3;
		SELECT city, MEAN(adjusted_salary) AS avg_salary
		FROM MINISTRY.MINISTRY
		GROUP BY city
		ORDER BY avg_salary DESC;
	QUIT;

*8.  For each job title, calculate the total salary paid to all employees holding that title;

	PROC SQL;
		SELECT job_title, SUM(adjusted_salary) AS total_salary
		FROM MINISTRY.MINISTRY
		GROUP BY job_title;
	QUIT;

*9. Create a summary report of the number of employees grouped by their education level and overtime status;

	PROC SQL;
		SELECT education_level, overtime, COUNT(*) as total_employees
		FROM MINISTRY.MINISTRY
		GROUP BY education_level, overtime;
	QUIT;


/*
-- 10. Create a flag column in the dataset indicating if an employee is eligible for a promotion based on the following criteria:
		- Performance rating is "Excellent"
		- Tenure is more than 3 years
*/

	DATA promotion_flag;
		SET MINISTRY.MINISTRY;
		tenure = INTCK('year', hire_date, today());
		promotion_eligible = (performance_rating = "Excellent" AND tenure > 3);
	RUN;
