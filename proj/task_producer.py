# -*- coding: utf-8 -*-
"""
@Time    : 2018-08-24 13:57
@Author  : DukeMoon
"""
import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
import django

django.setup()

from demoapp.tasks import add

if __name__ == '__main__':
    print("实时任务")
    print(datetime.datetime.now().isoformat())
    res = add.delay(2, 3)
    print(datetime.datetime.now().isoformat())
    print("result:", res.get())
    print(datetime.datetime.now().isoformat())

    print("延时任务")
    res = add.apply_async((2, 3), countdown=3)
    print(datetime.datetime.now().isoformat())
    print("result:", res.get())
    print(datetime.datetime.now().isoformat())
