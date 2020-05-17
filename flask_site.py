from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#To import the secret key
from dotenv import load_dotenv
import os
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('KEY')


posts = [
    {
        'author':'Saurav',
        'title':'My travel',
        'content':'first post content',
        'date_posted':'April 20, 2020'
    },
    {
        'author':'Joe',
        'title':'Other doc',
        'content':'First post content',
        'date_posted':'April 20, 2017'
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'addkj' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)