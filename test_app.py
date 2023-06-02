from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/testapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Users ID: {self.id}, name: {self.name}>'


'''user1 = Users(name = 'Benson')
user2 = Users(name = 'Benjamin')
user3 = Users(name = 'Samson')
user4 = Users(name = 'Samsonite')
user5 = Users(name = 'Christy')
user6 = Users(name = 'Chris')
user7 = Users(name = 'Geetha')'''

with app.app_context():
    db.create_all()
    #db.session.add_all([user1, user2, user3, user4, user5, user6, user7])
    #db.session.commit()

@app.route('/')
def index():
    user = Users.query.filter_by(name='Benson').count()
    '''str = ''
    for i in user:
        str += ' ' + i.name
    print(str)'''
    return str(user)
    

if __name__ == '__main__':
    app.run(debug=True)