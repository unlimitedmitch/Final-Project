from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_database']
collection = db['user_data']

# Sample data for dummy generation
names = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis']
emails = ['john@example.com', 'jane@example.com', 'alice@example.com', 'bob@example.com', 'charlie@example.com']
genders = ['male', 'female', 'other']
marital_statuses = ['single', 'married', 'divorced', 'widowed']
education_levels = ['high school', 'bachelors', 'masters', 'phd', 'other']
employment_statuses = ['employed', 'unemployed', 'self_employed']
occupations = ['engineer', 'teacher', 'doctor', 'salesperson', 'manager']
insurance_types = ['private', 'public', 'employer', 'none']

def generate_dummy_data(num_records):
    dummy_data = []
    for _ in range(num_records):
        record = {
            'name': random.choice(names),
            'email': random.choice(emails),
            'age': random.randint(18, 80),
            'gender': random.choice(genders),
            'marital_status': random.choice(marital_statuses),
            'education': random.choice(education_levels),
            'employment_status': random.choice(employment_statuses),
            'occupation': random.choice(occupations),
            'income': round(random.uniform(20000, 150000), 2),
            'expenses': {
                'utilities': round(random.uniform(1000, 10000), 2),
                'shopping': round(random.uniform(1000, 10000), 2),
                'healthcare': round(random.uniform(250, 10000), 2),
                'entertainment': round(random.uniform(1000, 10000), 2),
                'school_fees': round(random.uniform(0, 10000), 2),
            },
            'health_insurance': {
                'has_insurance': random.choice(['yes', 'no']),
                'insurance_type': random.choice(insurance_types)
            }
        }
        dummy_data.append(record)
    return dummy_data

# Generate and insert dummy data
num_records = 500  # Adjust this number as needed
dummy_data = generate_dummy_data(num_records)
result = collection.insert_many(dummy_data)

print(f"Successfully inserted {len(result.inserted_ids)} dummy records into the database.")
