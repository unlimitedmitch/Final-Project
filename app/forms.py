from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired, NumberRange, Email, Length, ValidationError

class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=120)])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    marital_status = RadioField('Marital Status', choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], validators=[DataRequired()])
    education = SelectField('Education Level', choices=[
        ('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    employment_status = SelectField('Employment Status', 
                                    choices=[
                                        ('', 'Select'),
                                        ('employed', 'Employed'),
                                        ('self_employed', 'Self Employed'),
                                        ('unemployed', 'Unemployed')
                                    ],
                                    validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=100)])
    income = DecimalField('Total Annual Income ($)', validators=[DataRequired(), NumberRange(min=0)])
    
    # Expenses
    utilities = DecimalField('Utilities ($)', validators=[NumberRange(min=0)])
    shopping = DecimalField('Shopping ($)', validators=[NumberRange(min=0)])
    healthcare = DecimalField('Healthcare ($)', validators=[NumberRange(min=0)])
    entertainment = DecimalField('Entertainment ($)', validators=[NumberRange(min=0)])
    school_fees = DecimalField('School fees ($)', validators=[NumberRange(min=0)])
    
    # Health Insurance
    has_health_insurance = RadioField('Do you have health insurance?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    insurance_type = SelectField('Type of Health Insurance', choices=[
        ('', 'Select'),
        ('private', 'Private'),
        ('public', 'Public'),
        ('employer', 'Employer-provided'),
        ('none', 'None')
    ])

    submit = SubmitField('Submit')

    def validate_insurance_type(self, field):
        if self.has_health_insurance.data == 'yes':
            if field.data == '':
                raise ValidationError('Please select the type of health insurance.')
            if field.data == 'none':
                raise ValidationError('If you have health insurance, please select a type other than "None".')
        elif self.has_health_insurance.data == 'no':
            if field.data != 'none':
                raise ValidationError('If you don\'t have health insurance, please select "None".')