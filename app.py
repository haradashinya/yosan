#coding: utf-8

from flask import Flask
from models.thing import Person
from models.thing import Task
import models.thing as thing
import datetime
app = Flask(__name__)

ITEMS = []

@app.before_request
def before_req():
    pass
@app.after_request
def after_req():
    pass


shinya = Person.create(name="harada shinya",birthday=datetime.date(1989,02,19))
print shinya


def create_task(_content,_h = 0,_m = 0):
    return Task.create(owner = shinya,content = u"%s" % _content,h = _h, m = _m)

def show_tasks():
    res = []
    for t in Task.select().join(Person)\
            .where(Person.name=='harada shinya')\
            .order_by(Task.created_at):
        total = t.h * 60 + t.m
        d = {
                "id": t.id, "content": t.content,
                "created_at": t.created_at,
                "h": t.h, "m": t.m,
                "total": total
                }

        res.append(d)
    return res

def show_log(count = 10):
    return show_tasks()[0:10]





create_task(u"お問い合せフォームの送信h",1,30)
print show_tasks()
print show_log()









