#coding: utf-8



from peewee import *
from datetime import date
import datetime
import subprocess

a = u"お"


subprocess.call("rm peewee.db",shell=True)
db = SqliteDatabase("peewee.db")

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Task(Model):
    owner = ForeignKeyField(Person,related_name="tasks")
    content = CharField()
    hours = IntegerField(default=0)
    minutes = IntegerField(default=0)
    created_at = DateField(default = datetime.datetime.now())

    class Meta:
        database = db


Person.create_table()
Task.create_table()

shinya = Person(name="harada shinya",birthday=date(1989,02,19),is_relative=True)
shinya.save()


wash = Task.create(owner = shinya,content=u"人間",minutes = 30)

for person in Person.select():
    print(person.name)
    for task in person.tasks:
        pass


