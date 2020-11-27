# from model.modelDB import StudentCourse
#
# def getCoursesByStudentId(studentId):
#     """根据学号查询已修读课程"""
#     courses = StudentCourse.query.filter_by(studentId=studentId)
#     return list(map(lambda x:x.cId,courses))
#

from model.modelDB import Course
def getCourse():
    """查询所有的课程信息，在前端展示"""
    courseTable=Course.query.all()
    return map(lambda x:x.to_json(),courseTable)