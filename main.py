import ttkbootstrap
import json
from ttkbootstrap.constants import *

app = ttkbootstrap.Window(title="小於菟计划", themename="darkly")
app.place_window_center()
app.iconbitmap('./images/XiaoWuTu_plan.ico')
big_label = ttkbootstrap.Label(app, text="小於菟计划", font=("楷体", 20))
width = app.winfo_width()
big_label.pack(pady=width / 2)
Treeview = ttkbootstrap.Treeview(master=app, columns=[0, 1], show=HEADINGS)
try:
    with open("plans.json") as jsons:
        plans = json.load(jsons)
    with open("plans.json", "w") as jsons:
        json.dump(plans, jsons, ensure_ascii=False)
except:
    plans = []
    with open("plans.json", "w") as jsons:
        json.dump(plans, jsons, ensure_ascii=False)
for plan in plans:
    Treeview.insert('', END, values=plan)
Treeview.heading(0, text='时间')
Treeview.heading(1, text="计划")
Treeview.column(0, width=200)
Treeview.column(1, anchor=CENTER, width=1000)
b1 = ttkbootstrap.Label(app, text="您的计划列表", font=("楷体", 10))
b1.pack()
Treeview.pack(anchor=NE, fill=X)
app.mainloop()
