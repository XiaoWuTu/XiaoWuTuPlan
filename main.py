import pickle
import threading
from os import system

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
    l6 = ttkbootstrap.Label(lf, text="请输入计划开始时间(格式：时：分，时分均为两位数（0补齐），冒号为英文状态。):",
                            font=("楷体", 10))
    b4 = ttkbootstrap.Button(lf, text="确认添加", command=get_append, width=300)
    l7 = ttkbootstrap.Label(lf, text="请输入计划截止时间(格式：时：分，时分均为两位数（0补齐），冒号为英文状态。):",
                            font=("楷体", 10))
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
    for _ in plans:
        r = r + 1
    plans.append([r + 1, start_time, end_time, what])
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
    global l8, l9, e4_content, e4, cbo, b4, r1, r2, r3
    l8 = ttkbootstrap.Label(lf, text="计划修改页面", font=("楷体", 20))
    l9 = ttkbootstrap.Label(lf, text="请选择要修改计划的序号", font=("楷体", 10))
    e4_content = ttkbootstrap.StringVar()
    e4 = ttkbootstrap.Entry(lf, width=300, textvariable=e4_content)
    plan = 0
    plans_number = []
    for _ in plans:
        plan = plan + 1
        plans_number.append(plan)
    cbo = ttkbootstrap.Combobox(
        master=lf,
        font=("仿宋", 10),
        values=plans_number,
        width=210
    )
    l8.pack()
    l9.pack()
    cbo.pack()

    def ensure(event):
        global cbo_get
        cbo_get = int(cbo.get()) - 1

    cbo.bind('<<ComboboxSelected>>', ensure)
    variable_value = ttkbootstrap.StringVar()
    variable_value_dist = {
        "1": "修改计划的起始时间",
        "2": "修改计划的截止时间",
        "3": "修改计划的内容"
    }
    r1 = ttkbootstrap.Radiobutton(lf, text='修改起始时间', variable=variable_value, value=1, width=50)
    r1.pack(side=ttkbootstrap.LEFT)
    r2 = ttkbootstrap.Radiobutton(lf, text='修改截止时间', variable=variable_value, value=2, width=50)
    r2.pack(side=ttkbootstrap.LEFT)
    r3 = ttkbootstrap.Radiobutton(lf, text='修改计划内容', variable=variable_value, value=3, width=50)
    r3.pack(side=ttkbootstrap.LEFT)

    def ensure():
        global l10, l11, l12, de3, l13, e5_content, e5
        r1.pack_forget()
        r2.pack_forget()
        r3.pack_forget()
        b4.pack_forget()
        l9.pack_forget()
        e4.pack_forget()
        cbo.pack_forget()
        if variable_value.get() == "1":
            l10 = ttkbootstrap.Label(lf, text=variable_value_dist[variable_value.get()] + "页面", font=("楷体", 15))
            l10.pack()
            l11 = ttkbootstrap.Label(lf, text="原计划起始时间:" + plans[cbo_get][1], font=("楷体", 10))
            l11.pack()
            l12 = ttkbootstrap.Label(lf, text="请选择修改后的计划起始日期：", font=("楷体", 10))
            l12.pack()
            de3 = ttkbootstrap.DateEntry(lf, width=207)
            de3.pack()
            l13 = ttkbootstrap.Label(lf,
                                     text="请输入修改后的计划开始时间(格式：时：分，时分均为两位数（0补齐），冒号为英文状态。):",
                                     font=("楷体", 10))
            l13.pack()
            e5_content = ttkbootstrap.StringVar()
            e5 = ttkbootstrap.Entry(lf, width=300, textvariable=e5_content)
            b5 = ttkbootstrap.Button(lf, text="确定修改", command=get_modification, width=20)
            b5.pack()

    b4 = ttkbootstrap.Button(lf, text="确定", command=ensure, width=20)
    b4.pack(side=ttkbootstrap.LEFT)


def get_modification():
    start_time = str(de3.entry.get()) + " " + str(e5_content.get())
    plans[cbo_get][1] = start_time
    with open("plans.pickle", "wb+") as f:
        pickle.dump(plans, f)
    system('reboot')


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
