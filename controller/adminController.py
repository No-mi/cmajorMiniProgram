# -*- coding: UTF-8 -*-
import json

from flask import Blueprint,request

from model.applicationDB import getAllApplication, getGradeStatistic, getMajorStatistic, getSexStatistic, \
    getStatisticData, ApplicationTransfor
from model.studentCourseDB import getPassedCoursesByStudenID, getCreditStatistic
from server.adminServer import application2pdf

admin = Blueprint("admin", __name__)  # 实例化teacher蓝图


@admin.route('/getAllApplication')
def getApplications():
    applications = getAllApplication()
    return json.dumps(list(map(lambda x: ApplicationTransfor(x), applications)))


@admin.route('/getStatisticData')
def statisticData():
    return getStatisticData()

# @admin.route('/application2pdf', methods=['GET','POST'])
@admin.route('localhost:5000/admin/application2pdf', methods=['GET','POST'])
def application_pdf():
    openID=request.args.get("openID")
    return application2pdf(openID)

