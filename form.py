import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
from demo import *
def submit():
    # load pretrained model 
    model=pickle.load(open('model.pkl','rb'))
    # lấy giá trị các đặc trưng đã nhập vào
    point=np.array([a.get(),ma.get(),mi.get(),ec.get(),c.get(),ex.get(),p.get()],dtype=float)
    # dự đoán kết quả
    if model.predict(point):
        messagebox.showinfo("Label","Besni")
    else:
        messagebox.showinfo("Label","Kecimen")
# tạo giao diện nhập liệu và submit với tkinter
root = tk.Tk()
tk.Label(root, text="Area: ").grid(row=0)
tk.Label(root, text="MajorAxisLength: ").grid(row=1)
tk.Label(root, text="MinorAxisLength: ").grid(row=2)
tk.Label(root, text="Eccentricity: ").grid(row=3)
tk.Label(root, text="ConvexArea: ").grid(row=4)
tk.Label(root, text="Extent: ").grid(row=5)
tk.Label(root, text="Perimeter: ").grid(row=6)
a=tk.Entry(root)
a.grid(row=0,column=1)
ma=tk.Entry(root)
ma.grid(row=1,column=1)
mi=tk.Entry(root)
mi.grid(row=2,column=1)
ec=tk.Entry(root)
ec.grid(row=3,column=1)
c=tk.Entry(root)
c.grid(row=4,column=1)
ex=tk.Entry(root)
ex.grid(row=5,column=1)
p=tk.Entry(root)
p.grid(row=6,column=1)
# button submit khi được chọn sẽ gọi hàm submit
sub=tk.Button(root,text = "Submit",command = submit).grid()
# giá trị  độ đo ứng mới mô hình tốt nhất
tk.Label(root, text="Accuracy: 0.5").grid()
tk.Label(root, text="Precision: 0.5").grid()
tk.Label(root, text="Recall: 0.99").grid()
tk.Label(root, text="F1: 0.67").grid()
root.mainloop()
