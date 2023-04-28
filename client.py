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
from datetime import datetime

global cwd
cwd = os.getcwd()

global sleepingtime
sleepingtime = 5 # time period for client ot ask server for temperature

global thread_started
thread_started = 0

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
root.title("Visteon Labs Client Control")
root.geometry( "360x550" )

def start_client():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th1 == 0:
        th1  = 1
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_ON)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th1 = 0
        B_th1.config(image = img_switch_OFF)
    
    stop_from_server = 0
    while not stop_from_server:
        time.sleep(sleepingtime)
        try:
            s = socket.socket()  # Create a socket object
            port = 50000  # Reserve a port for your service every new transfer wants a new port or you must wait.
            #s.connect(("10.185.24.23", port))
            s.connect(("10.185.24.30", port))

            if th1:
                st = "1"
            elif th2:
                st = "2"
            elif th3:
                st = "3"
            elif th4:
                st = "4"
            elif th5:
                st = "5"
            elif th6:
                st = "6"
            elif th7:
                st = "7"
            elif th8:
                st = "8"
            elif th9:
                st = "9"
            elif th10:
                st = "10"
            elif th11:
                st = "11"
            elif th12:
                st = "12"
            elif th13:
                st = "13"
            elif th14:
                st = "14"
            elif th15:
                st = "15"
            else:
                st = " OFF"
            #print("st is: " + st)
            byt = st.encode()
            s.send(byt)
            
            while not stop_from_server:
                data = s.recv(1024)
                string_data = data.decode("utf-8")
                if data:
                    if string_data == "stop":
                        print("Server for TH" + st + " is Offline")
                        break
                    else:
                        nowtime = datetime.now()
                        current_time = nowtime.strftime("%H:%M:%S")
                        print("[" + current_time + "] " + string_data)
                    break

                else:
                    print('no data received')
                    #stop_from_server = 1
                    pass
                print('closing')
                s.close()
        except:
            nowtime = datetime.now()
            current_time = nowtime.strftime("%H:%M:%S")
            print("[" + current_time + "] " + 'server is busy')

    #print('closing')
    #s.close()

#client_thread = Thread(target=start_client)
#client_thread.start()


def btn01_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th1 == 0:
        th1  = 1
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_ON)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th1 = 0
        B_th1.config(image = img_switch_OFF)
    #client_thread = Thread(target=start_client)
    #client_thread.start()

def btn02_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th2 == 0:
        th1  = 0
        th2  = 1
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_ON)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th2 = 0
        B_th2.config(image = img_switch_OFF)
def btn03_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th3 == 0:
        th1  = 0
        th2  = 0
        th3  = 1
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_ON)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th3 = 0
        B_th3.config(image = img_switch_OFF)
def btn04_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th4 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 1
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_ON)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th4 = 0
        B_th4.config(image = img_switch_OFF)
def btn05_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th5 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 1
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_ON)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th5 = 0
        B_th5.config(image = img_switch_OFF)
def btn06_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th6 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 1
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_ON)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th6 = 0
        B_th6.config(image = img_switch_OFF)
def btn07_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th7 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 1
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_ON)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th7 = 0
        B_th7.config(image = img_switch_OFF)
def btn08_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th8 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 1
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_ON)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th8 = 0
        B_th8.config(image = img_switch_OFF)
def btn09_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th9 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 1
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_ON)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th9 = 0
        B_th9.config(image = img_switch_OFF)
def btn10_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th10 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 1
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_ON)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th10 = 0
        B_th10.config(image = img_switch_OFF)
def btn11_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th11 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 1
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_ON)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th11 = 0
        B_th11.config(image = img_switch_OFF)
def btn12_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th12 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 1
        th13 = 0
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_ON)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th12 = 0
        B_th12.config(image = img_switch_OFF)
def btn13_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th13 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 1
        th14 = 0
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_ON)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_OFF)
    else:
        th13 = 0
        B_th13.config(image = img_switch_OFF)
def btn14_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th14 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 1
        th15 = 0
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_ON)
        B_th15.config(image = img_switch_OFF)
    else:
        th14 = 0
        B_th14.config(image = img_switch_OFF)
def btn15_press():
    global th1
    global th2
    global th3
    global th4
    global th5
    global th6
    global th7
    global th8
    global th9
    global th10
    global th11
    global th12
    global th13
    global th14
    global th15
    if th15 == 0:
        th1  = 0
        th2  = 0
        th3  = 0
        th4  = 0
        th5  = 0
        th6  = 0
        th7  = 0
        th8  = 0
        th9  = 0
        th10 = 0
        th11 = 0
        th12 = 0
        th13 = 0
        th14 = 0
        th15 = 1
        B_th1.config(image = img_switch_OFF)
        B_th2.config(image = img_switch_OFF)
        B_th3.config(image = img_switch_OFF)
        B_th4.config(image = img_switch_OFF)
        B_th5.config(image = img_switch_OFF)
        B_th6.config(image = img_switch_OFF)
        B_th7.config(image = img_switch_OFF)
        B_th8.config(image = img_switch_OFF)
        B_th9.config(image = img_switch_OFF)
        B_th10.config(image = img_switch_OFF)
        B_th11.config(image = img_switch_OFF)
        B_th12.config(image = img_switch_OFF)
        B_th13.config(image = img_switch_OFF)
        B_th14.config(image = img_switch_OFF)
        B_th15.config(image = img_switch_ON)
    else:
        th15 = 0
        B_th15.config(image = img_switch_OFF)

def fileselect1():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect2():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect3():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect4():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect5():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect6():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect7():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect8():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect9():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect10():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect11():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect12():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect13():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect14():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return
def fileselect15():
    messagebox.showinfo("Message", "Select Chamber ON/OFF")
    return

def start_thread():
    global thread_started
    if thread_started:
        messagebox.showinfo("Message", "Client Already Started!")
        return
    else:
        thread_started = 1
        B_start.config(image = img_start_green)
        client_thread = Thread(target=start_client)
        client_thread.start()

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
img_start_blue = ImageTk.PhotoImage(Image.open(cwd + "\\images\\start_blue.png"))
img_start_green = ImageTk.PhotoImage(Image.open(cwd + "\\images\\start_green.png"))
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

B_start = Button(image = img_start_blue,command = start_thread, compound=CENTER)
B_start.grid(row=9, column=0, columnspan = 10)

root.mainloop()
