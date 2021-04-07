"""
this became possible due to relative import __init__.py entry, direct method calling
"""

from ecommerce_module import Database
db2 = Database()

from ecommerce_module.payments_module import Products
prod = Products()