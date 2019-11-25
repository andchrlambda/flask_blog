from datetime import datetime
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    """posts is not a column, but establishes a one-to-many relationship
    between User and Post (one user can have man posts.)
    """

    def __repr__(self):
        return f"User('{self.username}, '{self.email}, '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}, '{self.date_posted}')" 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    """Using uppercase 'P' for 'Post' in User model when we define the relationship
    with the post. Using lowercase 'u'  'user.id' in the Post model. 
    That is because in the User model we are referencing the Post class
    and the foreign key references the table name and the column name so it
    is lowercase. The User model automatically has this table name set for 
    lowercase user, and the Post model will have a table name automatically set
    to lowercase post. 
    """