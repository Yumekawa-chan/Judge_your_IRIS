import joblib
import tkinter as tk

def predict(parameters): # modelの読み込み
    model = joblib.load('./model.pkl')
    params = parameters.reshape(1,-1)
    pred = model.predict(params)
    return pred

def getName(label): # isisの花の判定
    print(label)
    if label == 0:
        return "Iris Setosa"
    elif label == 1: 
        return "Iris Versicolor"
    elif label == 2: 
        return "Iris Virginica"
    else: 
        return "Error"

# TKINTER ZONE 
root = tk.Tk()
root.title("Judge Iris")
root.geometry("400x300")

label1 = tk.Label(root,text="Judge Iris",font=("Times",20))
label1.place(x=130,y=20)

root.mainloop()
