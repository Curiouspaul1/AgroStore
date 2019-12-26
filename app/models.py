from app import db

class User(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100),unique=True)
    telephone = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50),unique=True)
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

class Permission:
    BUY = 1
    SELL = 2
    RATE = 4
    ADMIN = 16

class Role(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(50))
    default = db.Column(db.Boolean,default=False,index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User',backref='role')

    # sets permission for each instance to zero if it has "None" permission
    def __init__(self,**kwargs):
        super(Role,self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def has_permission(self,perm):
        return self.permissions & perm == perm

    def add_permission(self,perm):
        if not self.has_permission(perm):
           self.permissions += perm


    def remove_permission(self,perrm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permission(self):
        self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            'SELLER':[Permission.BUY,Permission.SELL,Permission.RATE],
            'USER' : [Permission.BUY,Permission.RATE],
            'ADMIN' : [Permission.BUY,Permission.RATE,Permission.SELL,Permission.ADMIN]
        }

        default = 'USER'
        for r in roles:
            role = Role.query.filter_by(name=roles[r]).first()  # check to see if role exists
            if role is None:    # if role doesn't exist already
                role = Role(name=r)     # create role
            role.reset_permission()     # reset role permission
            for perm in roles[r]:       # assign role permission
                role.add_permission(perm)

            role.default = role.name == default # assigns the role as default if its name == the set default role in this method

            db.session.add(role)
        db.session.commit()
    
class Space(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    telephone = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    space_cat_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    products = db.relationship('Product',backref='product.id')

class Product(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.String(20))
    images = db.Column(db.LargeBinary)
    product_cat_id = db.Column(db.Integer,db.ForeignKey('product_cat.id'))

class Product_cat(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100))
    products = db.relationship('Product',backref='product_cat')

class Space_cat(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(100))
    stores = db.relationship('Space',backref='space_cat')
