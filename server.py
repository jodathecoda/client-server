import os
import shutil
from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import socket  # Import socket module
from tkinter import filedialog as fd
from tkinter import messagebox
from os.path import exists
from threading import Thread
import time

global cwd
cwd = os.getcwd()

global th1
th1 = 0
global th2
th2 = 0
global th3
th3 = 0
global th4
th4 = 0
global th5
th5 = 0
global th6
th6 = 0
global th7
th7 = 0
global th8
th8 = 0
global th9
th9 = 0
global th10
th10 = 0
global th11
th11 = 0
global th12
th12 = 0
global th13
th13 = 0
global th14
th14 = 0
global th15
th15 = 0

global filename_log1
filename_log1 = ""

global filename_log2
filename_log2 = ""

global filename_log3
filename_log3 = ""

global filename_log4
filename_log4 = ""

global filename_log5
filename_log5 = ""

global filename_log6
filename_log6 = ""

global filename_log7
filename_log7 = ""

global filename_log8
filename_log8 = ""

global filename_log9
filename_log9 = ""

global filename_log10
filename_log10 = ""

global filename_log11
filename_log11 = ""

global filename_log12
filename_log12 = ""

global filename_log13
filename_log13 = ""

global filename_log14
filename_log14 = ""

global filename_log15
filename_log15 = ""


# Create object
root = Tk()
root.title("Visteon Labs Server Control")
root.geometry( "360x550" )

def start_server():
    global filename_log1
    global th1
    port = 50000  # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()  # Create a socket object
    #host = ""  # Get local machine name
    #s.bind(('localhost', port))  # Bind to the port
    host = "10.185.24.23"
    s.bind((host, port))
    s.listen(5)  # Now wait for client connection.

    print('Server listening ...')

    stop_from_client = 0
    while True:
        conn, address = s.accept()  # Establish connection with client.
        while not stop_from_client:
            try:
                print('Got connection from', address)
                data = conn.recv(1024)
                string_data = data.decode("utf-8")
                print('Request from TH' + string_data)
                if string_data == "1" and th1 == 1:
                    f_reading = open(filename_log1, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "2" and th2 == 1:
                    f_reading = open(filename_log2, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "3" and th3 == 1:
                    f_reading = open(filename_log3, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "4" and th4 == 1:
                    f_reading = open(filename_log4, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "5" and th5 == 1:
                    f_reading = open(filename_log5, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "6" and th6 == 1:
                    f_reading = open(filename_log6, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "7" and th7 == 1:
                    f_reading = open(filename_log7, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "8" and th8 == 1:
                    f_reading = open(filename_log8, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "9" and th9 == 1:
                    f_reading = open(filename_log9, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "10" and th10 == 1:
                    f_reading = open(filename_log10, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "11" and th11 == 1:
                    f_reading = open(filename_log11, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "12" and th12 == 1:
                    f_reading = open(filename_log12, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "13" and th13 == 1:
                    f_reading = open(filename_log13, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "14" and th14 == 1:
                    f_reading = open(filename_log14, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                elif string_data == "15" and th15 == 1:
                    f_reading = open(filename_log15, "r")
                    lines = f_reading.readlines()
                    f_reading.close()
                    for l in lines:
                        last_line_list = l.split()
                    byt = last_line_list[2].encode()
                    conn.send(byt)
                else:
                    print("No Data")
                    byt = "No Data".encode()
                    conn.send(byt)
                    #byt = "stop".encode()
                    #conn.send(byt)

            except Exception as e:
                print(e)
                break

        conn.close()

server_thread = Thread(target=start_server)
server_thread.start()

def btn01_press():
    global th1
    global filename_log1
    if th1 == 0:
        if exists(filename_log1):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th1 = 1
        B_th1.config(image = img_switch_ON)
    else:
        th1 = 0
        B_th1.config(image = img_switch_OFF)
def btn02_press():
    global th2
    if th2 == 0:
        if exists(filename_log2):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th2 = 1
        B_th2.config(image = img_switch_ON)
    else:
        th2 = 0
        B_th2.config(image = img_switch_OFF)
def btn03_press():
    global th3
    if th3 == 0:
        if exists(filename_log3):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th3 = 1
        B_th3.config(image = img_switch_ON)
    else:
        th3 = 0
        B_th3.config(image = img_switch_OFF)
def btn04_press():
    global th4
    if th4 == 0:
        if exists(filename_log4):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th4 = 1
        B_th4.config(image = img_switch_ON)
    else:
        th4 = 0
        B_th4.config(image = img_switch_OFF)
def btn05_press():
    global th5
    if th5 == 0:
        if exists(filename_log5):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th5 = 1
        B_th5.config(image = img_switch_ON)
    else:
        th5 = 0
        B_th5.config(image = img_switch_OFF)
def btn06_press():
    global th6
    if th6 == 0:
        if exists(filename_log6):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th6 = 1
        B_th6.config(image = img_switch_ON)
    else:
        th6 = 0
        B_th6.config(image = img_switch_OFF)
def btn07_press():
    global th7
    if th7 == 0:
        if exists(filename_log7):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th7 = 1
        B_th7.config(image = img_switch_ON)
    else:
        th7 = 0
        B_th7.config(image = img_switch_OFF)
def btn08_press():
    global th8
    if th8 == 0:
        if exists(filename_log8):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th8 = 1
        B_th8.config(image = img_switch_ON)
    else:
        th8 = 0
        B_th8.config(image = img_switch_OFF)
def btn09_press():
    global th9
    if th9 == 0:
        if exists(filename_log9):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th9 = 1
        B_th9.config(image = img_switch_ON)
    else:
        th9 = 0
        B_th9.config(image = img_switch_OFF)
def btn10_press():
    global th10
    if th10 == 0:
        if exists(filename_log10):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th10 = 1
        B_th10.config(image = img_switch_ON)
    else:
        th10 = 0
        B_th10.config(image = img_switch_OFF)
def btn11_press():
    global th11
    if th11 == 0:
        if exists(filename_log11):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th11 = 1
        B_th11.config(image = img_switch_ON)
    else:
        th11 = 0
        B_th11.config(image = img_switch_OFF)
def btn12_press():
    global th12
    if th12 == 0:
        if exists(filename_log12):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th12 = 1
        B_th12.config(image = img_switch_ON)
    else:
        th12 = 0
        B_th12.config(image = img_switch_OFF)
def btn13_press():
    global th13
    if th13 == 0:
        if exists(filename_log13):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th13 = 1
        B_th13.config(image = img_switch_ON)
    else:
        th13 = 0
        B_th13.config(image = img_switch_OFF)
def btn14_press():
    global th14
    if th14 == 0:
        if exists(filename_log14):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th14 = 1
        B_th14.config(image = img_switch_ON)
    else:
        th14 = 0
        B_th14.config(image = img_switch_OFF)
def btn15_press():
    global th15
    if th15 == 0:
        if exists(filename_log15):
            pass
        else:
            messagebox.showinfo("Message", "Select Log file!")
            return
        th15 = 1
        B_th15.config(image = img_switch_ON)
    else:
        th15 = 0
        B_th15.config(image = img_switch_OFF)

def fileselect1():
    global filename_log1
    filename_log1 = fd.askopenfilename()
def fileselect2():
    global filename_log2
    filename_log2 = fd.askopenfilename()
def fileselect3():
    global filename_log3
    filename_log3 = fd.askopenfilename()
def fileselect4():
    global filename_log4
    filename_log4 = fd.askopenfilename()
def fileselect5():
    global filename_log5
    filename_log5 = fd.askopenfilename()
def fileselect6():
    global filename_log6
    filename_log6 = fd.askopenfilename()
def fileselect7():
    global filename_log7
    filename_log7  = fd.askopenfilename()
def fileselect8():
    global filename_log8
    filename_log8 = fd.askopenfilename()
def fileselect9():
    global filename_log9
    filename_log9 = fd.askopenfilename()
def fileselect10():
    global filename_log10
    filename_log10 = fd.askopenfilename()
def fileselect11():
    global filename_log11
    filename_log11 = fd.askopenfilename()
def fileselect12():
    global filename_log12
    filename_log12 = fd.askopenfilename()
def fileselect13():
    global filename_log13
    filename_log13 = fd.askopenfilename()
def fileselect14():
    global filename_log14
    filename_log14 = fd.askopenfilename()
def fileselect15():
    global filename_log15
    filename_log15 = fd.askopenfilename()

# Images
img_visteon = ImageTk.PhotoImage(Image.open(cwd + "\\images\\visteon.png"))
#img_chamber = ImageTk.PhotoImage(Image.open(cwd + "\\images\\chamber.png"))
img_th01 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th01.png"))
img_th02 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th02.png"))
img_th03 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th03.png"))
img_th04 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th04.png"))
img_th05 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th05.png"))
img_th06 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th06.png"))
img_th07 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th07.png"))
img_th08 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th08.png"))
img_th09 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th09.png"))
img_th10 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th10.png"))
img_th11 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th11.png"))
img_th12 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th12.png"))
img_th13 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th13.png"))
img_th14 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th14.png"))
img_th15 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\th15.png"))
img_cold = ImageTk.PhotoImage(Image.open(cwd + "\\images\\cold.png"))
img_mild = ImageTk.PhotoImage(Image.open(cwd + "\\images\\mild.png"))
img_hot = ImageTk.PhotoImage(Image.open(cwd + "\\images\\hot.png"))
img_notemp = ImageTk.PhotoImage(Image.open(cwd + "\\images\\notemp.png"))
img_switch_ON = ImageTk.PhotoImage(Image.open(cwd + "\\images\\switch_ON.png"))
img_switch_OFF = ImageTk.PhotoImage(Image.open(cwd + "\\images\\switch_OFF.png"))
img_bar1 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\bar1.png"))
img_bar2 = ImageTk.PhotoImage(Image.open(cwd + "\\images\\bar2.png"))


L_visteon = Label(image = img_visteon, compound=CENTER)
L_visteon.grid(row=0, column=0, columnspan = 10)


B_th1 = Button(image = img_switch_OFF,command = btn01_press, compound=LEFT)
B_th1.grid(row=1, column=0)

B_ch1 = Button(image = img_th01,command = fileselect1, compound=LEFT)
B_ch1.grid(row=2, column=0)

B_th2 = Button(image = img_switch_OFF,command = btn02_press, compound=LEFT)
B_th2.grid(row=1, column=1)

B_ch2 = Button(image = img_th02,command = fileselect2, compound=LEFT)
B_ch2.grid(row=2, column=1)

B_th3 = Button(image = img_switch_OFF,command = btn03_press, compound=LEFT)
B_th3.grid(row=1, column=2)

B_ch3 = Button(image = img_th03,command = fileselect3, compound=LEFT)
B_ch3.grid(row=2, column=2)

B_th4 = Button(image = img_switch_OFF,command = btn04_press, compound=LEFT)
B_th4.grid(row=1, column=3)

B_ch4 = Button(image = img_th04,command = fileselect4, compound=LEFT)
B_ch4.grid(row=2, column=3)

B_th5 = Button(image = img_switch_OFF,command = btn05_press, compound=LEFT)
B_th5.grid(row=1, column=4)

B_ch5 = Button(image = img_th05,command = fileselect5, compound=LEFT)
B_ch5.grid(row=2, column=4)

L_bar1 = Label(image = img_bar1, compound=CENTER)
L_bar1.grid(row=3, column=0, columnspan = 10)

B_th6 = Button(image = img_switch_OFF,command = btn06_press, compound=LEFT)
B_th6.grid(row=4, column=0)

B_ch6 = Button(image = img_th06,command = fileselect6, compound=LEFT)
B_ch6.grid(row=5, column=0)

B_th7 = Button(image = img_switch_OFF,command = btn07_press, compound=LEFT)
B_th7.grid(row=4, column=1)

B_ch7 = Button(image = img_th07,command = fileselect7, compound=LEFT)
B_ch7.grid(row=5, column=1)

B_th8 = Button(image = img_switch_OFF,command = btn08_press, compound=LEFT)
B_th8.grid(row=4, column=2)

B_ch8 = Button(image = img_th08,command = fileselect8, compound=LEFT)
B_ch8.grid(row=5, column=2)

B_th9 = Button(image = img_switch_OFF,command = btn09_press, compound=LEFT)
B_th9.grid(row=4, column=3)

B_ch9 = Button(image = img_th09,command = fileselect9, compound=LEFT)
B_ch9.grid(row=5, column=3)

B_th10 = Button(image = img_switch_OFF,command = btn10_press, compound=LEFT)
B_th10.grid(row=4, column=4)

B_ch10 = Button(image = img_th10,command = fileselect10, compound=LEFT)
B_ch10.grid(row=5, column=4)

L_bar2 = Label(image = img_bar2, compound=CENTER)
L_bar2.grid(row=6, column=0, columnspan = 10)

B_th11 = Button(image = img_switch_OFF,command = btn11_press, compound=LEFT)
B_th11.grid(row=7, column=0)

B_ch11 = Button(image = img_th11,command = fileselect11, compound=LEFT)
B_ch11.grid(row=8, column=0)

B_th12 = Button(image = img_switch_OFF,command = btn12_press, compound=LEFT)
B_th12.grid(row=7, column=1)

B_ch12 = Button(image = img_th12,command = fileselect12, compound=LEFT)
B_ch12.grid(row=8, column=1)

B_th13 = Button(image = img_switch_OFF,command = btn13_press, compound=LEFT)
B_th13.grid(row=7, column=2)

B_ch13 = Button(image = img_th13,command = fileselect13, compound=LEFT)
B_ch13.grid(row=8, column=2)

B_th14 = Button(image = img_switch_OFF,command = btn14_press, compound=LEFT)
B_th14.grid(row=7, column=3)

B_ch14 = Button(image = img_th14,command = fileselect14, compound=LEFT)
B_ch14.grid(row=8, column=3)

B_th15 = Button(image = img_switch_OFF,command = btn15_press, compound=LEFT)
B_th15.grid(row=7, column=4)

B_ch15 = Button(image = img_th15,command = fileselect15, compound=LEFT)
B_ch15.grid(row=8, column=4)

root.mainloop()
