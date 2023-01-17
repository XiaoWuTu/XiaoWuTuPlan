import pickle
import threading

import ttkbootstrap
from ttkbootstrap.constants import *

app = ttkbootstrap.Window(title="小於菟计划", themename="darkly")
app.iconbitmap('./images/XiaoWuTu_plan.ico')
big_label = ttkbootstrap.Label(app, text="小於菟计划", font=("楷体", 20))


def _():
    p1 = ttkbootstrap.Progressbar(ttkbootstrap.Frame(app, name="您的成功进度条").pack(fill=BOTH, expand=YES))
    p1.place(width=1920, height=20)
    p1.start()


width = app.winfo_width()
height = app.winfo_height()
t = threading.Thread(target=_)
t.start()
big_label.pack(pady=width / 2)
Treeview = ttkbootstrap.Treeview(master=app, columns=str([0, 1, 2, 3]), show=HEADINGS)
try:
    with open("plans.pickle", 'rb+') as p:
        plans = pickle.load(p)
except:
    plans = []
    with open("plans.pickle", "wb+") as p:
        pickle.dump(plans, p)
with open("plans.pickle", 'rb+') as p:
    plans = pickle.load(p)
for plan in plans:
    Treeview.insert('', END, values=plan)
Treeview.heading(0, text='序号')
Treeview.heading(1, text="起始时间")
Treeview.heading(2, text="结束时间")
Treeview.heading(3, text="计划内容")
Treeview.column(0, width=50)
Treeview.column(1, width=150)
Treeview.column(2, width=150)
Treeview.column(3, width=1050)
l1 = ttkbootstrap.Label(app, text="您的计划列表", font=("楷体", 10))
l1.pack()
Treeview.pack(anchor=NE, fill=X)
lf = ttkbootstrap.Labelframe(text="工具栏：", width=1920, height=120)


def cls_append():
    try:
        l2.pack_forget()
        e1.pack_forget()
        l3.pack_forget()
        l4.pack_forget()
        de1.pack_forget()
        de2.pack_forget()
        e2.pack_forget()
        l5.pack_forget()
        l6.pack_forget()
        b4.pack_forget()
        l7.pack_forget()
        e3.pack_forget()
    except:
        pass


def append():
    global l2, e1, l3, l4, de1, de2, e2, l5, l6, b4, e1_content, e2_content, l7, e3, e3_content, e1_content
    e1_content = ttkbootstrap.StringVar()
    l2 = ttkbootstrap.Label(lf, text="计划添加页面", font=("楷体", 20))
    e1 = ttkbootstrap.Entry(lf, width=300, textvariable=e1_content)
    l3 = ttkbootstrap.Label(lf, text="请选择计划起始日期：", font=("楷体", 10))
    l4 = ttkbootstrap.Label(lf, text="请选择计划截止日期：", font=("楷体", 10))
    de1 = ttkbootstrap.DateEntry(lf, width=207)
    de2 = ttkbootstrap.DateEntry(lf, width=207)
    e2_content = ttkbootstrap.StringVar()
    e2 = ttkbootstrap.Entry(lf, width=300, textvariable=e2_content)
    l5 = ttkbootstrap.Label(lf, text="请输入计划内容：", font=("楷体", 10))
    l6 = ttkbootstrap.Label(lf, text="请输入计划开始时间(格式：时：分，时分均为两位数（0补齐），冒号为英文状态。):")
    b4 = ttkbootstrap.Button(lf, text="确认添加", command=get_append, width=300)
    l7 = ttkbootstrap.Label(lf, text="请输入计划截止时间(格式：时：分，时分均为两位数（0补齐），冒号为英文状态。):")
    e3_content = ttkbootstrap.StringVar()
    e3 = ttkbootstrap.Entry(lf, width=300, textvariable=e3_content)
    l2.pack()
    l5.pack()
    e1.pack()
    l3.pack()
    de1.pack()
    l6.pack()
    e2.pack()
    l4.pack()
    de2.pack()
    l7.pack()
    e3.pack()
    b4.pack()


def get_append():
    start_time = str(de1.entry.get()) + " " + str(e2_content.get())
    end_time = str(de2.entry.get()) + " " + str(e3_content.get())
    what = str(e1_content.get())
    r = 0
    for i in plans:
        r = r + 1
    plans.append((r + 1, start_time, end_time, what))
    with open("plans.pickle", "wb+") as f:
        pickle.dump(plans, f)
    z = 0
    for plan in plans:
        if z == r:
            Treeview.insert('', END, values=plan)
        z = z + 1
    cls_append()


def modification():
    cls_append()


def backspace():
    cls_append()


b1 = ttkbootstrap.Button(lf, text="添加一项计划", command=append, width=300)
b2 = ttkbootstrap.Button(lf, text="修改一项计划", command=modification, width=300)
b3 = ttkbootstrap.Button(lf, text="删除一项计划", command=backspace, width=300)
lf.pack()
b1.pack()
b2.pack()
b3.pack()
app.mainloop()
