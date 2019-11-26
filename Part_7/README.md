# flask_blog
Blog that manages user logins and profiles

Using Python 3.7
Dependencies
 flask (part 1)
 flask-wtf (part 3)
 flask-sqlalchemy (part 4)
 flask-bcrypt (part 6)
 flask-login (part 6)
 Pillow (part 7)

 This application is based on Corey Schafer's 13-part series.

Part 1 - Getting Started
Web references
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

Notes

Terminal commands
To set environment variable
>>> export FLASK_APP=flaskblog.py
>>> flask run

To run in debug mode so that you do not have to stop and restart webserver to register changes.
>>> export = FLASK_DEBUG=1

Part 2 - Templates
Web references
https://getbootstrap.com/docs/4.3/getting-started/introduction/
minute 19 - locations for CSS and JS
Template inheritance
 - a block is a section where child templates can override the parent.

 Notes
 snippets
    navigation.html
    main.html
    main.css
    article.html

 static folder with main.css file

 url_for is a flask function that finds the location of routes. 

 Part 3 - Forms and user input

to get random characters in Python
>>>import secrets
>>>secrets.token_hex(16)

Flash messages (25:00)

Part 4 - Database with Flask-SQLAlchemy
Use SQL database for development; Postgres to deploy

Always use utc when saving dates to a database.

Explanation of capitalization in db models (16:30)

database terminal commands
>>>db.create_all()
>>>from flaskblog import User, Post
>>>user_1 = User(username='andrea, email='e@mail.com', password='password')
>>>db.session.add(user_1)
>>>db.session.commit()
>>>User.query.all()
>>>User.query.filter_by(username='andrea').all()

assign variable to query

>>>ac = User.query.filter_by(username='andrea').first()
>>>ac.id

to assign a variable based on query return
>>> me = User.query.get(1)

>>>db.drop_all()
Drops all db tables and rows

Part 5 - Package Structure
The recommendation is to start with package structure. However, this shows how to convert a module (which has been built so far) to a package. 

Walks through the error of the circular import and how packages provide a workaround.
   -  When a model is imported from a module, Python runs the entire module (it does not just run the model that is imported). Schafer credits Miguel Greenberg's 2016 Pycon talk, Flask at Scale.

To set up the package we created a new folder inside the project directory and transferred forms.py, models.py, templates folder and static folder into it. Created a routes.py, __init__.py, and renamed flaskblog.py to run.py    

To run the applicatin from run.py, the app variable must exist in __init__.py

Imports are redistributed (13:50).

Note that some imports now require dot notation to reference their location from within the package. 

Because decorators used the app variable it must be imported into routes.py

Command line reflects package:
>>>from flaskblog import db
>>>from flaskblog.models import User, Post
>>>db.create_all()

This recreates database inside package. Check by running 'tree' in interpreter.

Part 6 - User Authentication

Demoing flask-bcrypt
>>>from flask_bcrypt import Bcrypt
>>>bcrpyt = Bcrypt()
>>>bcrypt.generate_pasword_hash('testing)
>>>bcrypt.generate_pasword_hash('testing).decode('utf-8') ## yields string

Implement validation of unique users using wtf documentation. Validation is added to the RegistrtionForm class. (14:00)

LoginManager (21:00)***

Creating a route that users can access after they have logged in (35:00)

Ternary conditional (45:00)

Part 7 - User Account and Profile Picture
In account.html, file field errors for picture is handled differently than other error fields (username, email). 

Automatically resize image on upload (35:30)



A special encoding type must be added to form to add image type properly (24:30).
<form method="POST" action="" enctype="multipart/form-data">
This is important because the errors this generates do not make the cause of the error obvious. 

