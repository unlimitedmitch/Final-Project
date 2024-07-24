from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import SurveyForm
from app import mongo

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def survey_form():
    form = SurveyForm()
    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'email': form.email.data,
            'age': form.age.data,
            'gender': form.gender.data,
            'marital_status': form.marital_status.data,
            'education': form.education.data,
            'employment_status': form.employment_status.data,
            'occupation': form.occupation.data,
            'income': float(form.income.data),
            'expenses': {
                'utilities': float(form.utilities.data or 0),
                'shopping': float(form.shopping.data or 0),
                'healthcare': float(form.healthcare.data or 0),
                'entertainment': float(form.entertainment.data or 0),
                'school_fees': float(form.school_fees.data or 0),
            },
            'health_insurance': {
                'has_insurance': form.has_health_insurance.data,
                'insurance_type': form.insurance_type.data
            }
        }
        mongo.db.user_data.insert_one(user_data)
        flash('Thank you for submitting the survey!', 'success')
        return redirect(url_for('main.thank_you'))
    return render_template('survey_form.html', form=form)

@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')
