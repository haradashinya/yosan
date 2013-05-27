#coding: utf-8

from flask import Flask
from models.thing import Person
from models.thing import Task
import models.thing as thing
import datetime
app = Flask(__name__)

@app.before_request
def before_req():
    pass
@app.after_request
def after_req():
    pass


shinya = Person.create(name="harada shinya",birthday=datetime.date(1989,02,19))
print shinya


def create_task(_content,_h = 0,_m = 0):
    task = Task.create(owner = shinya,content = u"%s" % _content,h = _h, m = _m)
    print "callled create_task"

create_task(u"お問い合せフォームの送信",1,30)









