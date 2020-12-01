# import tempfile
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table
# from reportlab.platypus import LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

from model.applicationDB import * #导入application类和相关操作接口

#获取申请表数据
application=getApplicationByOpenID(Application.openID)

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


# 添加自定义样式
stylesheet.add(
    ParagraphStyle(name='body',
                   fontName="SimSun",
                   fontSize=10,
                   textColor='black',
                   leading=20,  # 行间距
                   spaceBefore=0,  # 段前间距
                   spaceAfter=10,  # 段后间距
                   leftIndent=0,  # 左缩进
                   rightIndent=0,  # 右缩进
                   firstLineIndent=20,  # 首行缩进，每个汉字为10
                   alignment=TA_JUSTIFY,  # 对齐方式

                   # bulletFontSize=15,       #bullet为项目符号相关的设置
                   # bulletIndent=-50,
                   # bulletAnchor='start',
                   # bulletFontName='Symbol'
                   )
)
body = stylesheet['body']

story = []

# Table 表格
table_data = [
              ['姓名','%s' % Application.name, '年级','%s'%Application.grade,'学号','%s'%Application.studentID],
              ['编号','%s' % Application.openID, '电话','%s'%Application.phoneNumber,'学院','%s'%Application.institute],
              ['专业','%s' % Application.major, '是否降级','%s'%Application.downGrade,'年级','%s'%Application.grade],
              ['毕业后的选择','%s' % Application.choiceAfterGraduating, '是否读博','%s'%Application.doctor,'身份证号','%s'%Application.ID],
              ['四级/六级','%s' % Application.CET, '四级/六级成绩','%s'%Application.CETScore,'绩点','%s'%Application.GPA],
              ['已修读课程列表','%s'%Application.courses],
             ]
table_style = [
                ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 所有行的字体
                ('FONTSIZE', (0, 0), (-1, 0), 15),  # 第一行的字体大小
                ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐

                #('BACKGROUND', (0, 0), (-1, 0), colors.green),  # 设置第一行背景颜色
                ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
             ]
table = Table(data=table_data, style=table_style, colWidths=180)

story.append(Paragraph("四川大学本科生转专业申请表", Title))
# story.append(Paragraph("<seq id='spam'/>.区块链概念", Heading2))
# story.append(Paragraph(content1, body))
# story.append(Paragraph("<seq id='spam'/>.区块链起源", Heading2))
# story.append(Paragraph(content2, body))
# story.append(Paragraph("<seq id='spam'/>.区块链发展历程", Heading2))
# story.append(Paragraph(content3, body))
story.append(table)

# bytes
# buf = BytesIO()
# doc = SimpleDocTemplate(buf, encoding='UTF-8')
# doc.build(story)
# print(buf.getvalue().decode())

# file
doc = SimpleDocTemplate('/pdfs/hello.pdf')
doc.build(story)