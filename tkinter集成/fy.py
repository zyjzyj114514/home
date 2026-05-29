import tkinter as tk
from translate import Translator

def open_translator(main_win):
    win = tk.Toplevel(main_win)
    win.title("中英翻译器")
    win.geometry("500x400")
    win.resizable(False, False)

    def do_translate():
        text = input_entry.get().strip()
        if not text:
            result_label.config(text="请输入内容！", fg="red")
            return
        try:
            t = Translator(from_lang="zh", to_lang="en")
            res = t.translate(text)
            result_label.config(text=res, fg="black")
        except Exception as e:
            result_label.config(text="翻译失败：网络异常", fg="red")

    tk.Label(win, text="输入中文：", font=("宋体", 12)).pack(pady=8)
    input_entry = tk.Entry(win, width=45, font=("宋体", 12))
    input_entry.pack(pady=2)

    tk.Button(win, text="一键翻译", command=do_translate, width=12).pack(pady=10)

    tk.Label(win, text="翻译结果：", font=("宋体", 12)).pack()
    result_label = tk.Label(win, text="", wraplength=420, font=("宋体", 12))
    result_label.pack(pady=5)