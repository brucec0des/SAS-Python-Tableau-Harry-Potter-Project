import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and seed for reproducibility
fake = Faker()
Faker.seed(42)
random.seed(42)

# Constants and predefined data
EUROPEAN_LOCATIONS = {
    "UK": ["London", "Edinburgh", "Bristol"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "Italy": ["Rome", "Milan", "Florence"],
    "Spain": ["Madrid", "Barcelona", "Seville"]
}

# Removed duplicate "Lovegood" from the surnames list
HARRY_POTTER_SURNAMES = [
    "Potter", "Weasley", "Granger", "Malfoy", "Dumbledore", "Snape", "Black", "Lupin", "Lovegood", "Longbottom",
    "Lestrange", "Riddle", "Diggory", "Fletcher", "Krum", "Tonks", "Moody", "Bagman", "Crouch", "Filch",
    "Hagrid", "McGonagall", "Flitwick", "Sprout", "Slughorn", "Trelawney", "Umbridge", "Pettigrew", "Shacklebolt", "Fudge",
    "Skeeter", "Lockhart", "Grindelwald", "Gaunt", "Carrow", "Peverell", "Abbott", "Bones", "Boot", "Brown",
    "Bulstrode", "Chang", "Corner", "Crabbe", "Delacour", "Finch-Fletchley", "Goldstein", "Jordan", "Macmillan", "Nott",
    "Parkinson", "Patil", "Ravenclaw", "Hufflepuff", "Slytherin", "Gryffindor", "Bell", "Zabini", "Greengrass", "Rosier",
    "Travers", "Yaxley", "Selwyn", "Avery", "Blackwood", "Rowle", "Fawley", "Ollivander", "Scamander",
    "Doge", "Hopkirk", "Vance", "Warbeck", "Peakes", "Coote", "Wood", "Davies", "Thomas", "Brown",
    "Creevey", "Summerby", "Towler", "Spinnet", "Bell", "Johnson", "Weasley-Potter", "Delaney", "Fenwick", "Meadowes",
    "Bones", "Burbage", "Carrow", "Dearborn", "Edgecombe", "Frobisher", "Goldstein", "Hornby", "Jugson", "Kirke",
    "McLaggen", "Montague", "Morgana", "Rookwood", "Sloper", "Stebbins", "Twycross",
    "Urquart", "Vaisey", "Warrington", "Wilkes", "Zeller", "Kettleburn", "Merrythought", "Sinistra", "Vector",
    "Binns", "Hooch", "Auror", "Quirrell", "Grubbly-Plank", "Maxime", "Karkaroff", "Rosmerta", "Abercrombie", "Ackerley",
    "Applebee", "Baddock", "Bates", "Bole", "Bundy", "Cadwallader", "Capper", "Chambers", "Cresswell", "Derrick",
    "Fawcett", "Fitzwilliam", "Gudgeon", "Higgs", "Jenkins", "Jones", "Keddle", "King", "Lancaster",
    "MacDougal", "Madley", "Moon", "Mulciber", "Pike", "Pritchard", "Quincey", "Rivers",
    "Runcorn", "Shimpling", "Silvanus", "Smith", "Strout", "Thicknesse", "Thruston", "Wenlock", "Whisp", "Whitby"
]

departments_jobs = {
    "Auror Office": {"Auror": 0.6, "Investigator": 0.4},
    "Department of Mysteries": {"Unspeakable": 1.0},
    "Magical Law Enforcement": {"Hit Wizard": 0.7, "Regulations Officer": 0.3},
    "Magical Creature Department": {"Beast Handler": 0.5, "Dragon Tamer": 0.5},
    "Wand Permits Office": {"Permit Inspector": 1.0}
}

job_education = {
    "Auror": "Advanced Magic Studies",
    "Investigator": "Advanced Magic Studies",
    "Unspeakable": "Mysteries and Advanced Research",
    "Hit Wizard": "Intermediate Wizardry",
    "Regulations Officer": "Basic Wizardry",
    "Beast Handler": "Magical Creatures Training",
    "Dragon Tamer": "Magical Creatures Training",
    "Permit Inspector": "Wizarding Law Basics"
}

performance_ratings = ["Excellent", "Good", "Satisfactory", "Needs Improvement"]
performance_probs = [0.2, 0.5, 0.25, 0.05]

def generate_employee_id(index):
    return f"EMP-{10000 + index}"

def generate_gender():
    return random.choices(["Female", "Male"], weights=[46, 54], k=1)[0]

def select_location():
    country = random.choice(list(EUROPEAN_LOCATIONS.keys()))
    city = random.choice(EUROPEAN_LOCATIONS[country])
    return country, city

def generate_hire_date():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2024, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

def assign_department_and_job():
    department = random.choice(list(departments_jobs.keys()))
    job_title = random.choices(
        list(departments_jobs[department].keys()),
        weights=list(departments_jobs[department].values()),
        k=1
    )[0]
    return department, job_title

def calculate_salary(department, job_title):
    base_salary = {
        "Auror Office": (50000, 70000),
        "Department of Mysteries": (60000, 80000),
        "Magical Law Enforcement": (40000, 60000),
        "Magical Creature Department": (45000, 65000),
        "Wand Permits Office": (30000, 45000)
    }
    salary_range = base_salary[department]
    return random.randint(*salary_range)

def generate_birth_date(hire_date, job_title):
    age_range = {
        "Auror": (25, 40),
        "Investigator": (25, 40),
        "Unspeakable": (30, 50),
        "Hit Wizard": (20, 35),
        "Regulations Officer": (20, 35),
        "Beast Handler": (22, 40),
        "Dragon Tamer": (25, 45),
        "Permit Inspector": (18, 30)
    }
    min_age, max_age = age_range[job_title]
    hire_datetime = datetime.combine(hire_date, datetime.min.time())
    max_birth_date = hire_datetime - timedelta(days=min_age * 365)
    min_birth_date = hire_datetime - timedelta(days=max_age * 365)
    return fake.date_between(start_date=min_birth_date, end_date=max_birth_date)

def assign_termination_date(hire_date):
    if random.random() > 0.888:  # 11.2% chance of termination
        min_termination_date = hire_date + timedelta(days=180)
        max_termination_date = datetime(2024, 12, 31).date()
        if min_termination_date > max_termination_date:
            return None
        return fake.date_between(start_date=min_termination_date, end_date=max_termination_date)
    return None

def calculate_adjusted_salary(salary, gender, education_level, age):
    multiplier = 1.0
    if gender == "Female":
        multiplier += 0.02
    if education_level in ["Advanced Magic Studies", "Mysteries and Advanced Research"]:
        multiplier += 0.05
    if age > 35:
        multiplier += 0.03
    return int(salary * multiplier)

# Generate dataset
data = []

for i in range(8950):
    hire_date = generate_hire_date()
    department, job_title = assign_department_and_job()
    education_level = job_education[job_title]
    birth_date = generate_birth_date(hire_date, job_title)
    
    # Calculate age using date objects
    age = (hire_date - birth_date).days // 365
    
    salary = calculate_salary(department, job_title)
    gender = generate_gender()
    adjusted_salary = calculate_adjusted_salary(salary, gender, education_level, age)
    
    termination_date = assign_termination_date(hire_date)
    
    data.append({
        "Employee ID": generate_employee_id(i),
        "First Name": fake.first_name(),
        "Last Name": random.choice(HARRY_POTTER_SURNAMES),
        "Gender": gender,
        "Country": (country := select_location())[0],
        "City": country[1],
        "Hire Date": hire_date,
        "Department": department,
        "Job Title": job_title,
        "Education Level": education_level,
        "Performance Rating": random.choices(performance_ratings, weights=performance_probs, k=1)[0],
        "Overtime": random.choices(["Yes", "No"], weights=[30, 70], k=1)[0],
        "Salary": salary,
        "Birth Date": birth_date,
        "Termination Date": termination_date,
        "Adjusted Salary": adjusted_salary
    })

# Save dataset to CSV
df = pd.DataFrame(data)
df.to_csv("ministry_of_magic_hr_dataset.csv", index=False)

print("Dataset generated and saved as 'ministry_of_magic_hr_dataset.csv'.")
