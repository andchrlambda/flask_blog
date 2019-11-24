from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c15c3d0605e03250cd8e55d50c262105'
"""to get random characters in Python
>>>import secrets
>>>secrets.token_hex(16)
"""

posts = [
    {
        'author': 'Andrea Christelle',
        'title': 'Philosophy for breakfast',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Andrea Christelle',
        'title': 'Philosophy for lunch',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    # the first posts is an argument
    # the second posts is the data

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Must include list of allowed methods"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # success is bootstrap style
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)