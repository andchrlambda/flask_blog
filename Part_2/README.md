# flask_blog
Blog that manages user logins and profiles

Using Python 3.7
Dependencies
 flask (part 1)

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
