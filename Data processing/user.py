class User:
    def __init__(self, name, email, age, gender, marital_status, education, employment_status, occupation, income, expenses, has_health_insurance, insurance_type):
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender
        self.marital_status = marital_status
        self.education = education
        self.employment_status = employment_status
        self.occupation = occupation
        self.income = income
        self.expenses = expenses
        self.has_health_insurance = has_health_insurance
        self.insurance_type = insurance_type

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'gender': self.gender,
            'marital_status': self.marital_status,
            'education': self.education,
            'employment_status': self.employment_status,
            'occupation': self.occupation,
            'income': self.income,
            'has_health_insurance': self.has_health_insurance,
            'insurance_type': self.insurance_type,
            **self.expenses
        }
