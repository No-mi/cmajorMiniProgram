# # import tempfile
# from reportlab.lib import colors
# from reportlab.pdfbase import pdfmetrics
# # from reportlab.pdfbase.pdfmetrics import registerFontFamily
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import Paragraph, SimpleDocTemplate, Table
# # from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
# from reportlab.lib.styles import getSampleStyleSheet
# # from reportlab.lib.enums import TA_JUSTIFY
# # from io import BytesIO
#
# from model.applicationDB import getApplicationByOpenID
# # 获取申请表信息
# # application = getApplicationByOpenID(Application.openID)

def application2pdf(openID):
    """:cvar
    根据传入的openID,把相应的申请表的信息生成一张pdf，然后返回pdf
    """
    # import tempfile
    from reportlab.lib import colors
    from reportlab.pdfbase import pdfmetrics
    # from reportlab.pdfbase.pdfmetrics import registerFontFamily
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Table
    # from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
    from reportlab.lib.styles import getSampleStyleSheet
    # from reportlab.lib.enums import TA_JUSTIFY
    # from io import BytesIO

    from model.applicationDB import getApplicationByOpenID
    # 获取申请表信息
    application = getApplicationByOpenID(openID)
    pdfmetrics.registerFont(TTFont('SimSun', './SimSun.ttf'))  # 默认不支持中文，需要注册字体
    pdfmetrics.registerFont(TTFont('SimSunBd', './SimSun-bold.ttf'))
    # registerFontFamily('SimSun', normal='SimSun', bold='SimSunBd', italic='VeraIt', boldItalic='VeraBI')

    stylesheet = getSampleStyleSheet()  # 获取样式集

    # 获取reportlab自带样式
    Normal = stylesheet['Normal']
    BodyText = stylesheet['BodyText']
    Italic = stylesheet['Italic']
    Title = stylesheet['Title']
    Heading1 = stylesheet['Heading1']
    Heading2 = stylesheet['Heading2']
    Heading3 = stylesheet['Heading3']
    Heading4 = stylesheet['Heading4']
    Heading5 = stylesheet['Heading5']
    Heading6 = stylesheet['Heading6']
    Bullet = stylesheet['Bullet']
    Definition = stylesheet['Definition']
    Code = stylesheet['Code']

    # 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
    Normal.fontName = 'SimSun'
    Italic.fontName = 'SimSun'
    BodyText.fontName = 'SimSun'
    Title.fontName = 'SimSunBd'
    Heading1.fontName = 'SimSun'
    Heading2.fontName = 'SimSun'
    Heading3.fontName = 'SimSun'
    Heading4.fontName = 'SimSun'
    Heading5.fontName = 'SimSun'
    Heading6.fontName = 'SimSun'
    Bullet.fontName = 'SimSun'
    Definition.fontName = 'SimSun'
    Code.fontName = 'SimSun'

    story = []

    # Table 表格

    table_data = [
                  ['姓名', '%s'%application.name, '学号','%s'%application.studentID],
                  ['学院', '%s'%application.institute, '专业','%s'%application.major,'年级','%s'%application.grade],
                  ['编号', '%s'%application.openID, '电话','%s'%application.phoneNumber,'是否降级','%s'%application.downGrade],
                  ['毕业后选择', '%s'%application.choiceAfterGraduating, '是否读博','%s'%application.doctor,'身份证号','%s'%application.ID],
                  ['四级/六级', '%s'%application.CET, '四级六级成绩','%s'%application.CETScore,'绩点','%s'%application.GPA],
                  ['已修读课程','%s'%application.courses],
                  ]
    table_style = [
                    ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
                    ('FONTSIZE', (0, 0), (-1, 0), 15),  # 第一行的字体大小
                    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐

                    ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
                 ]
    table = Table(data=table_data, style=table_style, colWidths=180)

    story.append(Paragraph("四川大学转专业申请表", Title))
    story.append(table)

    # file
    try:
        doc = SimpleDocTemplate('/pdfs/application_'+str(openID)+'.pdf')
        doc.build(story)
    except Exception as e:
        print('application2pdf failed')
        return False
    print('application2pdf successed')
    return True
#保险起见，给varchar或text赋值时一定要带上单引号！
application2pdf('111')