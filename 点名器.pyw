import random
import tkinter
import os 
global mode
import tkinter.messagebox
import time
import threading
import traceback

mode = 'big'
random_state = 'no'
namelist1 = ['空名单',[]]
namelist2 = ['空名单',[]]
namelist3 = ['空名单',[]]
namelist4 = ['空名单',[]]
class_list =[1,2,3]
lock = 'no'
if os.path.exists(os.getcwd() + '\\名单'):
    for files in os.walk(os.getcwd() + '\\名单'):
        print(files[2])
        i = 1
        for exactfile in files[2]:
            if i <= 4:
                try:
                    filename = os.getcwd() + '\\名单\\' + exactfile
                    listnamefile = open(filename, 'r', encoding='utf-8')
                    if i == 1:
                        namelist1[0] = exactfile
                        namelist1[1] = listnamefile.readlines()
                    if i == 2:
                        namelist2[0] = exactfile
                        namelist2[1] = listnamefile.readlines()
                    if i == 3:
                        namelist3[0] = exactfile
                        namelist3[1] = listnamefile.readlines()
                    if i == 4:
                        namelist4[0] = exactfile
                        namelist4[1] = listnamefile.readlines()
                    listnamefile.close()
                    i = i + 1
                except IOError:
                    pass
            else:
                pass
        
else:
    os.system('mkdir ' + os.getcwd()+'\名单')
    tkinter.messagebox.showinfo('错误','没有名单，已创建了一个文件夹 名单（处在与本程序同一目录下），导入名单，只需要先新建一个文件 ：文件名：名单名   文件内容：你需要的名单（注意：一个名字占一行）')
    os._exit(0)

try:
    while True:
        namelist1[1].remove('\n')
except BaseException:
    pass
try:
    while True:
        namelist2[1].remove('\n')
except BaseException:
    pass
try:
    while True:
        namelist3[1].remove('\n')
except BaseException:
    pass
try:
    while True:
        namelist4[1].remove('\n')
except BaseException:
    pass
def get_random_name():
    global random_state
    if random_state == 'no':
        random_state = 'yes'
        showname_thread = threading.Thread(target=get_random_name_thread)
        showname_thread.start()
        butinfo.set(' 点此查看结果 ')
        butinfo1.set('停止')
    else:
        random_state = 'no'
        butinfo.set('     开始     ')
        butinfo1.set('开始')
            
def ui_control():
    while True:
        global lock
        if lock == 'no':
            window.wm_attributes('-topmost', 1)
        time.sleep(0.1)
        
def get_random_name_thread():
    global random_state
    try:
        while random_state == 'yes':
            if str(v.get()) == '1':
                name.set(random.choice(namelist1[1]))
                random.shuffle(namelist1[1])
            if str(v.get()) == '2':
                name.set(random.choice(namelist2[1]))
                random.shuffle(namelist2[1])
            if str(v.get()) == '3':
                name.set(random.choice(namelist3[1]))
                random.shuffle(namelist3[1])
            if str(v.get()) == '4':
                name.set(random.choice(namelist4[1]))
                random.shuffle(namelist4[1])
            time.sleep(0.005)
    except BaseException as e:
        global lock
        lock = 'yes'
        time.sleep(0.1)
        tkinter.messagebox.showerror('错误！','随机点名错误，很可能没有这个名单，或者名单为空，详情：'+str(e))
        lock = 'no'


def switch_mode():
    global mode
    if mode == 'big':
        mode = 'small'
        mini_location = '280x50' + '+' + str(int(window.winfo_screenwidth() - 300)) + '+' + str(10)
        window.geometry(mini_location)
        window.attributes('-alpha', 0.7)
        window.title('点名器')
        mini_ready_name_place.place(x=5, y=0)
        mini_start_button.place(x=160, y=0)
       # mini_girl_start_button.place(x=177, y=0)
        #mini_boy_start_button.place(x=177, y=20)
        back_button.place(x=230, y=0)
    else:
     os._exit(0)


def get_back():
    global mode
    mode = 'big'
    mini_ready_name_place.place_forget()
    mini_start_button.place_forget()
    #mini_girl_start_button.place_forget()
    #mini_boy_start_button.place_forget()
    back_button.place_forget()
    back_location = '530x300' + '+' + str(int(window.winfo_screenwidth() / 2 - 265)) + '+' + \
               str(int(window.winfo_screenheight() / 2 - 200))
    window.geometry(back_location)
    window.attributes('-alpha', 1)

def show_about():
    global lock
    lock = 'yes'
    time.sleep(0.1)
    tkinter.messagebox.showinfo('关于','更多请到https://wsdjb14.github.io/')
    lock = 'no'
                                
window = tkinter.Tk()
window.resizable(0, 0)
window.protocol("WM_DELETE_WINDOW", switch_mode)
location = '530x300' + '+' + str(int(window.winfo_screenwidth() / 2 - 265)) + '+' + \
           str(int(window.winfo_screenheight() / 2 - 200))
window.geometry(location)
window.title('                                                                           点此进入迷你模式=====>')
window.attributes("-toolwindow", True)
window['background'] = 'white'
window.wm_attributes('-topmost', 1)
name = tkinter.StringVar()
name.set('准备好')
butinfo = tkinter.StringVar()
butinfo.set('     开始     ')
butinfo1 = tkinter.StringVar()
butinfo1.set('开始')
ready_name_place = tkinter.Label(window, textvariable=name, bg='white', font=('宋体', 80))
ready_name_place.place(x=100, y=50)
start_button = tkinter.Button(window, textvariable=butinfo, font=('宋体', 20), command=get_random_name,
                              relief='groove', bg='white')
start_button.place(x=155, y=200)
# girl_start_button = tkinter.Button(window, text='  点女生  ', font=('楷体', 15), command=get_girl_random_name,
#                                   relief='groove', bg='white')
# girl_start_button.place(x=330, y=220)
# boy_start_button = tkinter.Button(window, text='  点男生  ', font=('楷体', 15), command=get_boy_random_name, relief='groove',
#                                  bg='white')
# boy_start_button.place(x=100, y=220)
mini_ready_name_place = tkinter.Label(window, textvariable=name, bg='white', font=('宋体', 25))
mini_start_button = tkinter.Button(window,  textvariable=butinfo1, font=('宋体', 18), command=get_random_name, relief='groove',
                                   bg='white', height=1)
# mini_girl_start_button = tkinter.Button(window, text='点女生', font=('楷体', 10), command=get_girl_random_name,
#                                        relief='groove', bg='white')
# mini_boy_start_button = tkinter.Button(window, text='点男生', font=('楷体', 10), command=get_boy_random_name,
#                                       relief='groove', bg='white')
# back_button = tkinter.Button(window, text='x', font=('宋体', 18), command=get_back,
#                              relief='groove', bg='white')
info_lab = tkinter.Label(window, text='好好好,', bg='white',
                         font=('宋体', 5))
info_lab.place(x=0, y=290)
v = tkinter.IntVar()
v.set(1)
chosebut1 = tkinter.Radiobutton(window, text=namelist1[0], variable=v, value=1, bg='white')
chosebut2 = tkinter.Radiobutton(window, text=namelist2[0], variable=v, value=2, bg='white')
chosebut3 = tkinter.Radiobutton(window, text=namelist3[0], variable=v, value=3, bg='white')
chosebut4 = tkinter.Radiobutton(window, text=namelist4[0], variable=v, value=4, bg='white')
chosebut1.place(x=0, y=250)
chosebut2.place(x=140, y=250)
chosebut3.place(x=280, y=250)
chosebut4.place(x=420, y=250)
about_button = tkinter.Button(window, text='关于', command=show_about,
                              relief='groove', bg='white')
about_button.place(x=500, y=280)
ui_thread = threading.Thread(target=ui_control)
ui_thread.start()
window.mainloop()
