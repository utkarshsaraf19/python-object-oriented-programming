"""
absolute imports
modules are just python files and
__init__.py gives it the identity of package rather than just folders
"""
import ecommerce_module.database
db_object = ecommerce_module.database.Database()

from ecommerce_module.database import Database
db_object1 = Database()

from ecommerce_module import database
db_object2 = database.Database()

from ecommerce_module.database import Database as db
db_object3 = db()
db_object3.x = 80
db_object3.y = 90
print(db_object3.x,db_object3.y)


