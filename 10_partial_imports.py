"""
this became possible due to relative import __init__.py entry, direct method calling
"""

from ecommerce import Database
db2 = Database()

from ecommerce.payments import Products
prod = Products()