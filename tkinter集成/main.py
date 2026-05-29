import tkinter as tk
from tkinter import ttk
import threading
from time import sleep
from js import js
from fy import open_translator
from pc import climb

main = tk.Tk()
main.title("注册页面")
main.geometry("500x400")
#主窗口

label0 = tk.Label(main, text="请选择性别", font=("宋体",9))
label0.pack(pady=10)

xing = ttk.Combobox(main, values=["男","女","其他"], width=40, font=("宋体",9))
xing.current(0)
xing.pack(pady=10)
#设置性别选择框，默认选择男

label1 = tk.Label(main, text="Username", font=("宋体",12))
label1.pack(pady=10)
entry1 = tk.Entry(main, font=("宋体",12))
entry1.pack(pady=10)
#设置用户名

label2 = tk.Label(main, text="Password", font=("宋体",12))
label2.pack(pady=10)

entry2 = tk.Entry(main, font=("宋体",12), show="*")
entry2.pack(pady=10)
#设置密码，输入框的显示为*，以保护用户隐私

label3 = tk.Label(main, text="状态栏", font=("宋体",12))
label3.pack(pady=10)

def welcome():      #用于显示欢迎页面
    main.withdraw()  # 隐藏主窗口
    main1 = tk.Toplevel(main)
    main1.title("欢迎页面")
    main1.geometry("500x400")

    label4 = tk.Label(main1, text="再次输入密码", font=("宋体",12))#用于在欢迎页面输入密码
    label4.pack(pady=10)
    entry3 = tk.Entry(main1, font=("宋体",12))
    entry3.pack(pady=10)

    def password():       #用于在欢迎页面验证密码是否正确
        password = entry3.get().strip()
        password_yuan = entry2.get().strip()
        if password == password_yuan:
            main1.after(0, lambda: label4.config(text="密码正确,欢迎", fg="green"))
        else:
            main1.after(0, lambda: label4.config(text="密码错误,请重试", fg="red"))

    button1 = tk.Button(main1, text="确认", font=("宋体",12), command=password)
    button1.pack(pady=10)
    #按下按钮验证密码是否正确

    def jump():#用于在欢迎页面验证密码正确后跳转到选择页面
        main1.destroy()  # 销毁欢迎页面
        main2 = tk.Tk()  # 创建选择窗口
        main2.title("选择页面")
        main2.geometry("500x400")
        
        label5 = tk.Label(main2, text="选择功能", font=("宋体",12))
        label5.pack(pady=10)

        btn_js = tk.Button(main2, text="计算器", command=js, font=("宋体",12))
        btn_js.pack(pady=10)
        btn_fy = tk.Button(main2, text="翻译器", command=lambda: open_translator(main2), font=("宋体",12))
        btn_fy.pack(pady=10)
        btn_pc = tk.Button(main2, text="链接爬取", command=lambda: climb(), font=("宋体",12))
        btn_pc.pack(pady=10)

    button2 = tk.Button(main1, text="跳转", font=("宋体",12), command=jump)
    button2.place(relx=0.98,rely=0.98,anchor="se")   # 将按钮放置在窗口的右下角
    #用于返回注册页面

def show():   #用于填写用户名和密码
    username = entry1.get().strip()
    pwd = entry2.get().strip()
    sex = xing.get()

    if not username and not pwd:
        main.after(0, lambda: label3.config(text="请输入用户名和密码", fg="red"))
    elif not username:
        main.after(0, lambda: label3.config(text="请输入用户名", fg="red"))
    elif not pwd:
        main.after(0, lambda: label3.config(text="请输入密码", fg="red"))

    elif sex == "男":
        main.after(500, lambda: label3.config(text=f"你好,{username}先生", fg="black"))
    elif sex == "女":
        main.after(500, lambda: label3.config(text=f"你好,{username}女士", fg="black"))
    else:
        main.after(500, lambda: label3.config(text=f"你好,{username}朋友", fg="black"))
    main.after(1500, welcome)#在显示欢迎页面之前，先显示欢迎信息，等待1.5秒后再显示欢迎页面

def start_check():    #用于在点击注册按钮后启动一个线程来检查输入的用户名和密码，并显示欢迎页面
    threading.Thread(target=show, daemon=True).start()

button = tk.Button(main, text="注册", font=("宋体",12), command=start_check)
button.pack(pady=10)  #点击注册按钮后，显示欢迎页面

if __name__ == "__main__":   #我也不知道这个if __name__ == "__main__":有什么用，反正就写上了
    main.mainloop()    #不写显示不了