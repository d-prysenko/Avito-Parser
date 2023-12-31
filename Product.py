import sqlite3
from peewee import *
from Settings import Settings

db = SqliteDatabase(Settings().cwd + '/products.db')

def createTables():
    db.create_tables([Product])

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    id = AutoField(column_name='id')
    product_id = TextField(column_name='product_id', null=True)
    title = TextField(column_name='title', null=True)
    params = TextField(column_name='params', null=True)
    ram = IntegerField(column_name='ram', null=True)
    url = TextField(column_name='url', null=True)


    class Meta:
        table_name = 'products'