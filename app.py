import joblib
import tkinter as tk
import numpy as np
from tkinter import messagebox

def predict(parameters): # modelの読み込み
    model = joblib.load('./model.pkl')
    params = parameters.reshape(1,-1)
    pred = model.predict(params)
    return pred

def getName(label): # isisの花の判定
    print(label)
    if label == 0:
        return "Your iris is Setosa!"
    elif label == 1: 
        return "Your iris is Versicolor!"
    elif label == 2: 
        return "Your iris is Virginica!"
    else: 
        return "Error!!!"

def judge(): # button押下時
    result=np.array([txt1.get(),txt2.get(),txt3.get(),txt4.get()])
    pred = predict(result)
    name = getName(pred)
    messagebox.showinfo("Judgement result", name)
    print(name)

# TKINTER ZONE 
root = tk.Tk()
root.iconbitmap('./iris.ico')
root.title("Judge your Iris")
root.geometry("400x250")

label1 = tk.Label(root,text="Judge your Iris",font=("Times",20))
label1.place(x=110,y=10)

# 各特徴
label2 = tk.Label(root,text="Sepal Length(cm)",font=("Times",10))
label2.place(x=30,y=80)

label3 = tk.Label(root,text="Sepal Width(cm)",font=("Times",10))
label3.place(x=30,y=120)

label4 = tk.Label(root,text="Petal Length(cm)",font=("Times",10))
label4.place(x=30,y=160)

label5 = tk.Label(root,text="Petal Width(cm)",font=("Times",10))
label5.place(x=30,y=200)

txt1 = tk.Entry(width = 15)
txt1.place(x=140,y=80)
txt2 = tk.Entry(width = 15)
txt2.place(x=140,y=120)
txt3 = tk.Entry(width = 15)
txt3.place(x=140,y=160)
txt4 = tk.Entry(width = 15)
txt4.place(x=140,y=200)

result = [txt1.get(),txt2.get(),txt3.get(),txt4.get()]

btn = tk.Button(root,width=10,text="Judge!",command=judge)
btn.place(x=280,y=125)


root.mainloop()
