from datetime import datetime
from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import login_required, current_user
from .forms import ProfileUpdateForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = ProfileUpdateForm()

    # Load the current user's profile data into the form
    if request.method == 'GET':
        form.resume.data = current_user.profile.resume
        form.skills.data = current_user.profile.skills
        form.experience.data = current_user.profile.experience

    if form.validate_on_submit():
        # Update the profile with form data
        current_user.profile.resume = form.resume.data
        current_user.profile.skills = form.skills.data
        current_user.profile.experience = form.experience.data
        current_user.profile.job_preferences = form.job_preferences.data
        current_user.profile.updated_at = datetime.now()
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.update_profile'))

    return render_template('update_profile.html', form=form)