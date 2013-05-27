#coding: utf-8



from peewee import *
from datetime import date
import datetime
import subprocess



subprocess.call("rm peewee.db",shell=True)
db = SqliteDatabase("peewee.db")

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

class Task(Model):
    owner = ForeignKeyField(Person,related_name="tasks")
    content = CharField()
    h = IntegerField(default=0)
    m = IntegerField(default=0)
    created_at = DateField(default = datetime.datetime.now())

    class Meta:
        database = db






Person.create_table()
Task.create_table()



# wash = Task.create(owner = shinya,content=u"人間",minutes = 30)

# for person in Person.select():
#     print(person.name)
#     for task in person.tasks:
#         print task.content
#         pass


