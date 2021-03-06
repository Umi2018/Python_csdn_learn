import os
from tkinter import Tk, Menu, Label, Button
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo

# from 实用主义学Python.抠图.抠除背景 import remove_bg

from removebg import RemoveBg

rmbg = RemoveBg('GiQrvx9AuuS6DH2Svh3JBfVK', 'error.log')

def remove_bg(img_path):
    rmbg.remove_background_from_img_file(img_path)

IMGPATH = ''

class GUI(object):
    def __init__(self, window):
        self.window = window
        self.window.title('去除图片背景')
        self.window.geometry('300x200')
        menubar = Menu(self.window)

        #定义空菜单
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='帮助', command=self.helpme)
        filemenu.add_separator()

        #显示
        self.l = Label(window, text='')
        self.l.pack(padx=5, pady=10) #固定窗口

        #选择照片
        btn1 = Button(window, text='选择照片', width=15, height=2, command=self.get_img)
        btn1.pack()

        #生成图片
        self.send_btn = Button(window, text='去除背景', width=15, height=2, command=self.gen_img)
        self.send_btn.pack()

    def helpme(self):
        showinfo('帮助', '请关注公众号，联系作者')

    def get_img(self):
        global IMGPATH
        #选择文件
        filenames = askopenfilenames(filetypes=(('jpeg img', '*.jpeg'),
                                                ('jpg img', '*.jpg'), ('png img', "*.png")
                                                ))
        if len(filenames) > 0:
            fnlist = [fn for fn in filenames]
            fnstr = '\n'.join(fnlist)
            self.l.config(text=fnstr)
            IMGPATH = fnlist
        else:
            self.l.config(text='目前没有选择任何图片文件')

    def gen_img(self):
        global IMGPATH
        respathlist = []
        for imgpath in IMGPATH:
            filepath, tempfilename = os.path.split(imgpath)
            filename, extension = os.path.splitext(tempfilename)
            remove_bg(imgpath)
            respathlist.append(imgpath)
        respath = ' '.join(respathlist)
        showinfo('完成生成', f'图片处理完成，路径为: {respath}')


#创建窗口
window = Tk()
GUI(window)
#显示窗口，必须在所有控件后
window.mainloop()