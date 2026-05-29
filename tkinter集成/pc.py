import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import random
from time import sleep
import os

def climb():
    save_air = "text" # 定义保存路径,如果不存在则创建
    os.makedirs(save_air, exist_ok=True)
    save_path = os.path.join(save_air, "href.txt") # 定义保存文件路径

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
    }

    main = tk.Tk()                           # 创建主窗口
    main.title("GUI爬虫")
    main.geometry("500x400")

    label1 = tk.Label(main,text="网站爬取(目前只能爬链接)",font=("宋体",15),bg="#88cce3")
    label1.pack(pady=10)

    label2 = tk.Label(main,text="请输入要爬取的网址",font=("宋体",15))
    label2.pack(pady=10)
    entry = tk.Entry(main,font=("宋体",10),width=40)
    entry.pack(pady=5,padx=5)

    wait = random.randint(1,3)

    def func1():  
        url = entry.get().strip()
        if not url:
            label3.config(text="请输入网址",fg="red")
            return           # 发送HTTP请求并返回响应
        try:
            response = requests.get(url,headers=headers,timeout=10)
            print("请求中...")
            sleep(wait)
            print("请求完成,状态码: " + str(response.status_code))
            return response
        except requests.RequestException:
            label3.config(text="请求失败",fg="red")
            return None

    def func2(res):       # 解析HTML并提取链接，保存到文本文件
        global page
        global wait
        if res is None:
            return
        try:
            soup = BeautifulSoup(res.text,"html.parser")
            all_links = set()  # 使用集合去重
            for a_tag in soup.find_all("a"):
                href = a_tag.get("href")
                if href and href.strip():
                    all_links.add(href.strip())
            with open(save_path,"a",encoding="utf-8") as f:
                for link in all_links:
                    f.write(link + "\n")
            long = len(all_links)
            label3.config(text=f"爬取完成,共提取{long}个链接",fg="green")
        except Exception as e:
            label3.config(text="解析失败",fg="red")
            print("解析错误: " + str(e))
            
    def run():    # 运行爬虫，调用func1和func2
        res = func1()
        func2(res)

    button = tk.Button(main,text="爬取",command=run,width=20,height=1)
    button.pack(pady=10)
    label3 = tk.Label(main,text="状态栏",font=("宋体",15),fg="black")
    label3.pack(pady=10)   # 状态栏显示爬虫的当前状态

    main.mainloop()