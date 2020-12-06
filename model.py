from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os
import datetime
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):
    # TODO: Add model fields here
    name = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Task(Model):
    # TODO: Add model fields here
    name = CharField()
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)

    class Meta:
        database = db

