import pandas as pd
# 与AutoCAD连接
from pyautocad import Autocad,APoint
acad = Autocad(create_if_not_exists = True)

# 读取Excel文件
xlsx = pd.ExcelFile('扩容升级板件安装槽位表.xlsx')

# 选择表名
sheet_name = 'Sheet1'

# 读取Excel表数据
df = pd.read_excel(xlsx, sheet_name)

# 获取表的最大行数
max_row = df.shape[0]


# 标点
p11 = APoint(0, 0);      p12 = APoint(250, 0);       p13 = APoint(1800, 0);      p14 = APoint(2050, 0);      p15 = APoint(3600, 0);      p16 = APoint(3850, 0);      p17 = APoint(4250, 0)
p21 = APoint(0, 220);    p22 = APoint(250, 220);     p23 = APoint(1800, 220);    p24 = APoint(2050, 220);    p25 = APoint(3600, 220);    p26 = APoint(3850, 220);    p27 = APoint(4250, 220)
p31 = APoint(0, 440);    p32 = APoint(250, 440);     p33 = APoint(1800, 440);    p34 = APoint(2050, 440);    p35 = APoint(3600, 440)
p41 = APoint(0, 660);    p42 = APoint(250, 660);                                                             p45 = APoint(3600, 660);    p46 = APoint(3850, 660)
p51 = APoint(0, 880);    p52 = APoint(250, 880);     p53 = APoint(1800, 880);    p54 = APoint(2050, 880);    p55 = APoint(3600, 880)
p61 = APoint(0, 1100);   p62 = APoint(250, 1100);    p63 = APoint(1800, 1100);   p64 = APoint(2050, 1100);   p65 = APoint(3600, 1100);   p66 = APoint(3850, 1100);   p67 = APoint(4250, 1100)
p71 = APoint(0, 1320);   p72 = APoint(250, 1320);    p73 = APoint(1800, 1320);   p74 = APoint(2050, 1320);   p75 = APoint(3600, 1320);   p76 = APoint(3850, 1320);   p77 = APoint(4250, 1320)
p81 = APoint(0, 1540);                                                                                       p85 = APoint(3600, 1540);                               p87 = APoint(4250, 1540)
ptittle = APoint(0, 1320)

# 连线
acad.model.AddLine(p11, p17)
acad.model.AddLine(p21, p27)
acad.model.AddLine(p31, p35)
acad.model.AddLine(p41, p45)
acad.model.AddLine(p51, p55)
acad.model.AddLine(p61, p67)
acad.model.AddLine(p71, p77)
acad.model.AddLine(p81, p87)

acad.model.AddLine(p11, p81)
acad.model.AddLine(p12, p72)
acad.model.AddLine(p13, p33)
acad.model.AddLine(p14, p34)
acad.model.AddLine(p15, p75)
acad.model.AddLine(p17, p87)

acad.model.AddLine(p53, p73)
acad.model.AddLine(p54, p74)
acad.model.AddLine(p16, p76)


A = "1"
text = acad.model.AddText((A.center(3, " ")), p11, 90)
A = "2"
text = acad.model.AddText((A.center(3, " ")), p13, 90)
A = "3"
text = acad.model.AddText((A.center(3, " ")), p21, 90)
A = "4"
text = acad.model.AddText((A.center(3, " ")), p23, 90)
A = "5"
text = acad.model.AddText((A.center(3, " ")), p51, 90)
A = "6"
text = acad.model.AddText((A.center(3, " ")), p53, 90)
A = "7"
text = acad.model.AddText((A.center(3, " ")), p61, 90)
A = "8"
text = acad.model.AddText((A.center(3, " ")), p63, 90)
A = "9"
text = acad.model.AddText((A.center(3, " ")), p31, 90)
A = "10"
text = acad.model.AddText((A.center(3, " ")), p41, 90)
A = "11"
text = acad.model.AddText((A.center(3, " ")), p15, 90)
A = "12"
text = acad.model.AddText((A.center(3, " ")), p65, 90)
A = "13"
text = acad.model.AddText((A.center(3, " ")), p45, 90)

A = "                                             CXP"
text = acad.model.AddText((A.center(3, " ")), p32, 90)
A = "                                             CXP"
text = acad.model.AddText((A.center(3, " ")), p42, 90)
A = "    PIU"
text = acad.model.AddText((A.center(3, " ")), p16, 90)
A = "    PIU"
text = acad.model.AddText((A.center(3, " ")), p66, 90)
A = "    FAN"
text = acad.model.AddText((A.center(3, " ")), p46, 90)

i = 0
for i in range(max_row):
    #写字
    if df.iloc[i, 4] == 1:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p12,70)

    if df.iloc[i, 4] == 2:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p14,70)

    if df.iloc[i, 4] == 3:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p22,70)

    if df.iloc[i, 4] == 4:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p24,70)

    if df.iloc[i, 4] == 5:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p52,70)

    if df.iloc[i, 4] == 6:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p54,70)

    if df.iloc[i, 4] == 7:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p62,70)

    if df.iloc[i, 4] == 8:
        B = df.iloc[i, 3]
        text=acad.model.AddText((B.center(3," ")),p64,70)

# 写网元名
C = df.iloc[i-1, 0]
text = acad.model.AddText((C.center(3, " ")), ptittle, 90)
