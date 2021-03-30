from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import shortuuid

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role_id=db.Column(db.Integer)
    # _list = [] #Keeps track of the users
    #can instantiate init method
    #can add a role to the user class
    #workout- have shop owner. only shop owner can create or add product. if current_user.email = tomiwa.omidiran@coding temple, display page. Can do this with  jinja statements. Or use aflask package
    #or everytime user is instantiated add another field for auth so they dont have admin priviledges
    #each user when insantiated they have privledges to view products but not do anything else, one admin user based on user id or email that can change all the other users permissions.

    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = f'{self.first_name}{self.last_name}@gmail.com'.lower()

    def create_password_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password_hash(self, password_to_verify):
        return check_password_hash(self.password, password_to_verify)

    def save(self):
        self.create_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
            return f'<User: {self.email}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    create = db.Column(db.Boolean(), default=False)
    delete = db.Column(db.Boolean(), default=False)
    modify = db.Column(db.Boolean(), default=False)
    
    def from_dict(self, data):
        for field in ['name', 'create', 'delete', 'modify']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        role={
            "id":self.id,
            "name":self.name,
            "create":self.create,
            "delete":self.delete,
            "modify":self.modify,
        }
        return role