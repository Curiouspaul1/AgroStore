from app import __call__,db
import os
from app.models import User,Role,Space,Product,Product_cat,Space_cat
from flask_migrate import Migrate

app = __call__(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role,Space=Space,Product=Product,Product_cat=Product_cat,Space_cat=Space_cat)