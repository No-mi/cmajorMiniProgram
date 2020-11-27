from model.modelDB import StudentCourse


def getCoursesByStudentId(studentId):
    """根据姓名查询学生信息"""
    course = StudentCourse.query.filter_by(studentId=studentId)
    print("course",course)
    return  course
