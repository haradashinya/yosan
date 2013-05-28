#coding: utf-8

from models.thing import Person
from models.thing import Task
import models.thing as thing
import datetime
from bottle import route,run

ITEMS = []


shinya = Person.create(name="harada shinya",birthday=datetime.date(1989,2,19))

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

def show_tasks_in_current_month():
    '''
    show all tasks in current month

    TODO: change end_date by each month.(ex. if Feburary, then end_date should
    set to "28 or 29?")
    '''
    res = []
    year =  int(str(datetime.datetime.now()).split("-")[0])
    month = int(str(datetime.datetime.now()).split("-")[1])
    end_date = 30
    for d in Task.select().join(Person)\
            .where(Person.name == 'harada shinya')\
            .where(Task.created_at > datetime.datetime(year,month,1))\
            .where(Task.created_at < datetime.datetime(year,month,end_date))\
            .order_by(Task.created_at):
                res.append(d)
    # return res
    return [item.content for item in res]


create_task(u"お問い合せフォームの送信h",1,30)
# print show_tasks()
# print show_log()
print(show_tasks_in_current_month())










