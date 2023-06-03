from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'  #for specifying table name or default will be the class name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self): #this is used for debugging like printing out the values
        return f'<Person ID: {self.id}, name: {self.name}>'
    
user1 = Person(name = 'Benson')
user2 = Person(name = 'Samson')
user3 = Person(name = 'Christy')
user4 = Person(name = 'Sebin')
user5 = Person(name = 'New Person 1')
user6 = Person(name = 'New Person 2')

with app.app_context(): 
    db.create_all()
    db.session.add_all([user1, user2, user3, user4, user5, user6])
    db.session.commit()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
    app.run()