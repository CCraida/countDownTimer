import tkinter  as tk

minList = []
secList = []
minSpinboxList = []
secSpinboxList = []

def ckeButtonClick():
    """チェックボックス選択イベント
       タイマー2をON/OFFする。
    """
    if chkState.get():
        minSpinboxList[1]["state"] = "disable"
        secSpinboxList[1]["state"] = "disable"
    else:
        minSpinboxList[1]["state"] = "normal"
        secSpinboxList[1]["state"] = "normal"

root = tk.Tk()
root.geometry("200x100")

# リストの初期化
for i in range(2):
   minList.append(tk.StringVar())
   secList.append(tk.StringVar())

# spinBoxを作成
for i in range(2):
   minList[i].set(0)
   secList[i].set(0)
   minSpinboxList.append(tk.Spinbox(root,from_=0,to=99,textvariable=minList[i]))
   secSpinboxList.append(tk.Spinbox(root,from_=0,to=99,textvariable=secList[i],))
   if i == 1:
        minSpinboxList[1]["state"] = "disable"
        secSpinboxList[1]["state"] = "disable"
    
   minSpinboxList[i].place(height=20, width=30,x=20 ,y=10 + (i*30))
   secSpinboxList[i].place(height=20, width=30,x=60,y=10 + (i*30))

#checkBoxを作成
chkState = tk.BooleanVar()
chkState.set(True)
chkBox = tk.Checkbutton(root, text = 'タイマー2',variable=chkState,command=ckeButtonClick)
chkBox.place(x=100 ,y=10)



root.mainloop()