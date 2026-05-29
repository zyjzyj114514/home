import tkinter as tk

def js():
    main = tk.Tk()
    main.title("计算机")
    main.geometry("500x300")

    def func1():
        num = entry1.get()
        num2 = entry2.get()
        
        if num.isdigit() and num2.isdigit():
            result = int(num) + int(num2)
            label4.config(text="结果: " + str(result),fg="black")
        elif num == "" or num2 == "":
            label4.config(text="请输入两个数字",fg="red")
        elif (not num.isdigit()) and (not num2.isdigit()):
            label4.config(text="两个输入都不是数字",fg="red")
        elif not num.isdigit():
            label4.config(text="第一个输入不是数字",fg="red")
        elif not num2.isdigit():
            label4.config(text="第二个输入不是数字",fg="red")

    def func2():
        num = entry1.get()
        num2 = entry2.get()
        
        if num.isdigit() and num2.isdigit():
            result = int(num) * int(num2)
            label4.config(text="结果: " + str(result),fg="black")
        elif num == "" or num2 == "":
            label4.config(text="请输入两个数字",fg="red")
        elif (not num.isdigit()) and (not num2.isdigit()):
            label4.config(text="两个输入都不是数字",fg="red")
        elif not num.isdigit():
            label4.config(text="第一个输入不是数字",fg="red")
        elif not num2.isdigit():
            label4.config(text="第二个输入不是数字",fg="red")

    label1 = tk.Label(main,text="计算",font=("宋体",15))
    label1.pack(pady=10)

    label2 = tk.Label(main,text="请输入第一个数字",font=("宋体",15))
    label2.pack()
    entry1 = tk.Entry(main,font=("宋体",15))
    entry1.pack(pady=5,padx=5)

    label3 = tk.Label(main,text="请输入第二个数字",font=("宋体",15))
    label3.pack()
    entry2 = tk.Entry(main,font=("宋体",15))
    entry2.pack(pady=5,padx=5)

    button_frame = tk.Frame(main)
    button_frame.pack(pady=10)

    button1 = tk.Button(button_frame,text="相加",command=func1,width=20,height=1)
    button1.pack(side=tk.LEFT,padx=50,pady=10)
    button2 = tk.Button(button_frame,text="相乘",command=func2,width=20,height=1)
    button2.pack(side=tk.RIGHT,padx=50,pady=10)   

    label4 = tk.Label(main,text="结果:"+"",font=("宋体",15),fg="black")
    label4.pack(pady=5)

    main.mainloop()