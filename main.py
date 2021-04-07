"""
modules are just python files and
__init__.py gives it the identity of package rather than just folders
"""
import ecommerce.database

db_object = ecommerce.database.Database()

from ecommerce.database import Database

db_object1 = Database()

from ecommerce.database import Database as db

db_object2 = db()
db_object2.x = 80
db_object2.y = 90
print(db_object2.x,db_object2.y)