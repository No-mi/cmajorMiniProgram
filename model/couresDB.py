# -*- coding: UTF-8 -*-
from model.modelDB import Course

def getAllCourses():
    res = Course.query.all()
    return list(map(lambda x: {"cId": x.cId, "cname": x.cname}, res))
