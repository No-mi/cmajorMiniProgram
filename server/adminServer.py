import tempfile

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from io import BytesIO

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

# 段落
content1 = "<para><u color='red'><font fontSize=13>区块链</font></u>是分布式数据存储、<strike color='red'>点对点传输</strike>、共识机制、" \
           "<font color='red' fontSize=13>加密算法</font>等计算机技术的<font name='SimSunBd'>新型应用模式</font>。<br/>" \
           "&nbsp&nbsp<a href='www.baidu.com' color='blue'>区块链（Blockchain）</a>，" \
           "是比特币的一个重要概念，它本质上是一个去中心化的数据库，同时作为比特币的底层技术，是一串使用密码学方法相关联产生的" \
           "数据块，每一个数据块中包含了一批次比特币网络交易的信息，用于验证其信息的有效性（防伪）和生成下一个区块 [1]。</para>"

content2 = "区块链起源于比特币，2008年11月1日，一位自称中本聪(SatoshiNakamoto)的人发表了《比特币:一种点对点的电子现金系统》" \
           "一文 [2]  ，阐述了基于P2P网络技术、加密技术、时间戳技术、区块链技术等的电子现金系统的构架理念，这标志着比特币的诞生" \
           "。两个月后理论步入实践，2009年1月3日第一个序号为0的创世区块诞生。几天后2009年1月9日出现序号为1的区块，并与序号为" \
           "0的创世区块相连接形成了链，标志着区块链的诞生 [5]  。<br/><img src='./1.jpg' width=180 height=100 valign='top'/><br/><br/><br/><br/><br/>"

content3 = "2008年由中本聪第一次提出了区块链的概念 [2]  ，在随后的几年中，区块链成为了电子货币比特币" \
           "的核心组成部分：作为所有交易的公共账簿。通过利用点对点网络和分布式时间戳服务器，区块链数据库能够进行自主管理。为比特币而发明的区块链使它成为" \
           "第一个解决重复消费问题的数字货币。比特币的设计已经成为其他应用程序的灵感来源。<br/>&nbsp&nbsp 2014年，区块链2.0成为一个关于去中心" \
           "化区块链数据库的术语。对这个第二代可编程区块链，经济学家们认为它是一种编程语言，可以允许用户写出更精密和智能的协议 " \
           "[7]  。因此，当利润达到一定程度的时候，就能够从完成的货运订单或者共享证书的分红中获得收益。区块链2.0技术跳过了交易" \
           "和“价值交换中担任金钱和信息仲裁的中介机构”。它们被用来使人们远离全球化经济，使隐私得到保护，使人们“将掌握的信息兑换" \
           "成货币”，并且有能力保证知识产权的所有者得到收益。第二代区块链技术使存储个人的“永久数字ID和形象”成为可能，并且对“潜在" \
           "的社会财富分配”不平等提供解决方案 [8]  。<br/>&nbsp&nbsp 2016年1月20日，中国人民银行数字货币研讨会宣布对数字货币研究取得阶段性成果。" \
           "会议肯定了数字货币在降低传统货币发行等方面的价值，并表示央行在探索发行数字货币。中国人民银行数字货币研讨会的表达大大" \
           "增强了数字货币行业信心。这是继2013年12月5日央行五部委发布关于防范比特币风险的通知之后，第一次对数字货币表示明确的态度" \
           "。 [9] <br/>&nbsp&nbsp 2016年12月20日，数字货币联盟——中国FinTech数字货币联盟及FinTech研究院正式筹建 [10]  。<br/>&nbsp&nbsp如今，比特币仍是" \
           "数字货币的绝对主流，数字货币呈现了百花齐放的状态，常见的有bitcoin、litecoin、dogecoin、dashcoin，除了货币的应用" \
           "之外，还有各种衍生应用，如以太坊Ethereum、Asch等底层应用开发平台以及NXT，SIA，比特股，MaidSafe，Ripple等行业应用 [11]  。"

# Table 表格

image = Image('./1.jpg')
image.drawWidth = 160
image.drawHeight = 100
table_data = [['year我是标题行，\n\n比较特殊，不能上下居中\n', '我的背景色被绿了', '我是标题，我比别人大\n'],
              ['2017\n我是换行符，\n单元格中的字符串只能用我换行', '3', '12'],
              [Paragraph('指定了列宽，可以在单元格中嵌入paragraph进行自动换行，不信你看我', body), '4', '13'],
              ['2017', '5', '我们是表格'],
              ['2017', '我是伪拆分单元格，\n通过合并前hou两个兄弟得到', '15'],
              ['2018', '7', '16'],
              [Paragraph(content1, body), '8', [image, Paragraph('这样我可以在一个单元格内同时显示图片和paragraph', body)]],
              ['2018', '我们被合并了，合并的值为右上角单元格的值', '18'],
              ['我被绿了', '10', '19'],
              ]
table_style = [
    ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
    ('FONTSIZE', (0, 0), (-1, 0), 15),  # 第一行的字体大小
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐

    ('SPAN', (-2, -2), (-1, -1)),  # 合并
    ('SPAN', (0, 4), (0, 5)),  # 合并
    ('SPAN', (2, 4), (2, 5)),  # 合并
    ('BACKGROUND', (0, 0), (-1, 0), colors.green),  # 设置第一行背景颜色
    ('TEXTCOLOR', (0, -1), (0, -1), colors.green),  # 设置表格内文字颜色
    ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
]
table = Table(data=table_data, style=table_style, colWidths=180)

story.append(Paragraph("区块链", Title))
story.append(Paragraph("<seq id='spam'/>.区块链概念", Heading2))
story.append(Paragraph(content1, body))
story.append(Paragraph("<seq id='spam'/>.区块链起源", Heading2))
story.append(Paragraph(content2, body))
story.append(Paragraph("<seq id='spam'/>.区块链发展历程", Heading2))
story.append(Paragraph(content3, body))
story.append(table)

# bytes
# buf = BytesIO()
# doc = SimpleDocTemplate(buf, encoding='UTF-8')
# doc.build(story)
# print(buf.getvalue().decode())

# file
doc = SimpleDocTemplate('hello.pdf')
doc.build(story)