from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.auth.models import User
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as main_bp
from .email import send_email

@main_bp.route('/')
def index():
  
    context = {
        'user': current_user
    }
    return render_template('home.html', **context)
    #  **context used to be in with the home html

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main_bp.route('/listofusers')
@login_required
def listofusers():
    context = {
        'users': User.query.all()
    }
    return render_template('listofusers.html', **context)

@main_bp.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    if request.method == 'POST':
        form_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'budget': request.form['budget'],
            'message': request.form['message']
        }
        send_email(form_data)
        flash('Thank you for your suggestion!', 'primary')
        return redirect(url_for('main.contact'))

    return render_template('contact.html')