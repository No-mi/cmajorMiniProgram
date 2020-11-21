from .modelDB import *
def getStudentUserByUserName(username):
    user=StudentUser.query.filter_by(username=username).first()
    print(user)
    return user