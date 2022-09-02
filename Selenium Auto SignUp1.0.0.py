import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import math
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
from pathlib import Path
#from tkinter import filedialog
import os

#sign_up(username, mailID, mobileNO, password, Cpassword)

win = Tk()
#win.geometry('480x360')
win.resizable(0,0)
win.title('Auto Sign up')
font = 'Lemon'

def get_csv():
    global my_csv, printer, data
    file = filedialog.askopenfilename()
    f_path = Path(file)
    my_csv = file
    printer.insert(END, f"{f_path.name} Selected\n")
    try:
        printer.insert(END, 'Opening CSV...\n')
        data = pd.read_csv(my_csv)
        printer.insert(END, "CSV file read Completed!\n")
    except:
        printer.insert(END,"CSV error\n")
    
        
def get_chromedriver():
    global driver, printer,chromeDriver
    file = filedialog.askopenfilename()
    f_path = Path(file)
    chromeDriver = file
    printer.insert(END,f"File chosses is {f_path.name}\n")
    

def sign_up(username, mailID, mobileNO, password, Cpassword):

    driver = webdriver.Chrome(chromeDriver)
    driver.get(website)
    print('Loading...')
    printer.insert(END,"Loading....")
    time.sleep(3)
    name_x = '/html/body/div/div[3]/div/div/div[1]/div/form/div[1]/div/div/input'
    element = driver.find_element(By.XPATH, name_x)
    element.send_keys(username)
    time.sleep(0.5)

    mail_x = '/html/body/div/div[3]/div/div/div[1]/div/form/div[2]/div/div/input'
    element = driver.find_element(By.XPATH, mail_x)
    element.send_keys(mailID)
    time.sleep(0.5)

    phone_x = '/html/body/div/div[3]/div/div/div[1]/div/form/div[3]/div/div/input'
    element = driver.find_element(By.XPATH, phone_x)
    element.send_keys(mobileNO)
    time.sleep(0.5)

    passwd_x = '/html/body/div/div[3]/div/div/div[1]/div/form/div[4]/div/div/input'
    element = driver.find_element(By.XPATH, passwd_x)
    element.send_keys(password)
    time.sleep(0.5)

    cpasswd_x = '/html/body/div/div[3]/div/div/div[1]/div/form/div[5]/div/div/input'
    element = driver.find_element(By.XPATH, cpasswd_x)
    element.send_keys(Cpassword)
    time.sleep(0.5)

    try:
        button = '/html/body/div/div[3]/div/div/div[1]/div/form/div[7]/div/div/button'
        element = driver.find_element(By.XPATH, button)
        driver.execute_script("arguments[0].click();", element)
        #button = 'btn btn-primary login-btn'
        #element = driver.find_element(By.CLASS_NAME, button)
        print('Button Click')
        #printer.insert(END,"Button Click\n")
        time.sleep(3)
        #driver.refresh()
        print('Registred Succesfully!')
        printer.insert(END,"Registred Succesfully!")
    except:
        print("Session ID Error")
        printer.insert(END,"Session ID Error")
    driver.close()

def get_data():
    printer.insert(END,"\nProcessing..")
    password = "aq1234za"
    Cpassword = "aq1234za"
    namex = []
    mailx = []
    numberx = []

    for i in range(len(data.name)):
        namex.append(data.name[i])
    print('Names Appended')
    for i in range(len(data.mail)):
        mailx.append(data.mail[i])
    print('Mails appended')
    for i in range(len(data.number)):
        numberx.append(int(data.number[i]))
    print('Number Appended')

    for j in range(len(data.name)):
        sign_up(namex[j], mailx[j], str(numberx[j]), password, Cpassword)
        time.sleep(0.5)
        os.system('ipconfig /flushdns')
        time.sleep(1)
        print('DNS flushed')
        printer.insert(END,"DNS Flushed\n")
        c=j+1
        print('Registrations: ',c)
        printer.insert(END,"Total Registrations: \n")
        printer.insert(END,c)
        printer.insert(END,"\n")        

website = "https://my.learnwithcomics.org/register"

get_driver =Button(win,text="Select Driver",
                   width=10,height=1,command=get_chromedriver,
                   font=(font,12),fg="black",bg="#cccccc",activebackground="#aaaaaa",padx=10,pady=10)
get_driver.grid(row=0,column=0,padx=10, pady=10)

get_CSV =Button(win,text="Select CSV",
                height=1,width=10,command=get_csv,font=(font,12),
                fg="black",bg="#cccccc",activebackground="#aaaaaa",padx=10,pady=10)
get_CSV.grid(row=0,column=1,padx=10, pady=10)

start =Button(win,text="Start",
              width=10,height=1,command=get_data,font=(font,12),
              fg="black",bg="Red",activeforeground ="white",activebackground="green",padx=10,pady=10)
start.grid(row=0,column=2,padx=10, pady=10)
'''
printer = Label(win,text='Auto Signup',bg='black',fg='white', font=('calibri', 14),width=30, height=10,)
printer.grid(row=1,column=0,columnspan=3)
'''
printer = Text(win,bg='black',fg='white', font=(font, 12),width=40, height=10,)
printer.grid(row=1,column=0,columnspan=3)

printer.insert(END, 'Auto SignUp\nCSV Formate must be Name,Mail id, Phone No.\n')


#driver = webdriver.Chrome('C://Users//Mullaivendhan//Desktop/chromedriver.exe')
#data = pd.read_csv('C://Users//Mullaivendhan//Desktop//booklet.csv')
#get_data()
win.mainloop()
