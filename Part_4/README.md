# flask_blog
Blog that manages user logins and profiles

Using Python 3.7
Dependencies
 flask (part 1)
 flask-wtf (part 3)
 flask-sqlalchemy (part 4)

 This application is based on Corey Schafer's 13-part series.

Part 1 - Getting Started
Web references
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

Notes

Terminal commands
To set environment variable
>>> export FLASK_APP=flaskblog.py
>>> flask run

To run in debug mode so that you do not have to stop and restart webserver to show every change.
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
Use SQL database for development

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

Part 5


