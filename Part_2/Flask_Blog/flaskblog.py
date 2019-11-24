from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__=='__main__':
    app.run(debug=True)