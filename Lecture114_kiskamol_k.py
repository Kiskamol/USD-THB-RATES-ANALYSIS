from tkinter import *
import tkinter as tk
from statistics import *
from forex_python.converter import *
import datetime  
c = CurrencyRates()
Mainwindow  = Tk()

###Timedates###
today = datetime.date.today()
today_withtime = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
two_days_ago = yesterday - datetime.timedelta(days=1)
three_days_ago = two_days_ago - datetime.timedelta(days=1)
four_days_ago = three_days_ago - datetime.timedelta(days=1)
five_days_ago = four_days_ago - datetime.timedelta(days=1)
six_days_ago = five_days_ago - datetime.timedelta(days=1)

###USD to THB Currency###
usd_thb_today = c.get_rate('USD','THB')
usd_thb_today_2deci = round(usd_thb_today,2)
usd_thb_yesterday = c.get_rate('USD','THB',yesterday)
usd_thb_yesterday_2deci = round(usd_thb_yesterday,2)
usd_thb_twodaysago = c.get_rate('USD','THB',two_days_ago)
usd_thb_twodaysago_2deci = round(usd_thb_twodaysago,2)
usd_thb_threedaysago = c.get_rate('USD','THB',three_days_ago)
usd_thb_threedaysago_2deci = round(usd_thb_threedaysago,2)
usd_thb_fourdaysago = c.get_rate('USD','THB',four_days_ago)
usd_thb_fourdaysago_2deci = round(usd_thb_fourdaysago,2)
usd_thb_fivedaysago = c.get_rate('USD','THB',four_days_ago)
usd_thb_fivedaysago_2deci = round(usd_thb_fivedaysago,2)

###THB to USD Currency###
thb_usd_today = c.get_rate('THB','USD')
thb_usd_today_3deci = round(thb_usd_today,3)
thb_usd_yesterday = c.get_rate('THB','USD', yesterday)
thb_usd_yesterday_3deci = round(thb_usd_yesterday,3)
thb_usd_twodaysago = c.get_rate('THB','USD', two_days_ago)
thb_usd_twodaysago_3deci = round(thb_usd_twodaysago,3)
thb_usd_threedaysago = c.get_rate('THB','USD', three_days_ago)
thb_usd_threedaysago_3deci = round(thb_usd_threedaysago,3)
thb_usd_fourdaysago = c.get_rate('THB','USD', four_days_ago)
thb_usd_fourdaysago_3deci = round(thb_usd_fourdaysago,3)
thb_usd_fivedaysago = c.get_rate('THB','USD', five_days_ago)
thb_usd_fivedaysago_3deci = round(thb_usd_fivedaysago,3)

###USD to THB Currency###
def show_usdrates():
    text1 = "USD/THB Rates in "+ str(yesterday)+" : "+str(usd_thb_yesterday_2deci)+' ฿'+"\n"+"USD/THB Rates in "+ str(two_days_ago)+" : "+str(usd_thb_twodaysago_2deci)+' ฿'+"\n"+"USD/THB Rates in "+ str(three_days_ago)+" : "+str(usd_thb_threedaysago_2deci)+' ฿'+"\n"+"USD/THB Rates in "+ str(four_days_ago)+" : "+str(usd_thb_fourdaysago_2deci)+' ฿'+"\n"+"USD/THB Rates in "+ str(five_days_ago)+" : "+str(usd_thb_fivedaysago_2deci)+' ฿'
    label = tk.Label(Mainwindow, text= text1,font=('helvetica', 10, 'bold'))
    canvas1.create_window(160, 220, window=label)

def show_usd_avg_rates():
    usd_rates = (usd_thb_today,usd_thb_yesterday,usd_thb_twodaysago,usd_thb_threedaysago,usd_thb_fourdaysago,usd_thb_fivedaysago)
    usd_avg_usdrates = mean(usd_rates)
    usd_avg_usdrates_two = round(usd_avg_usdrates,3)
    text = str(usd_avg_usdrates_two) + ' ฿'
    label = tk.Label(Mainwindow, text= text,font=('helvetica', 10, 'bold'))
    canvas1.create_window(120, 335, window=label)

def show_usd_max_rates():
    usd_rates = (usd_thb_today,usd_thb_yesterday,usd_thb_twodaysago,usd_thb_threedaysago,usd_thb_fourdaysago,usd_thb_fivedaysago)
    usd_max_usdrates = max(usd_rates)
    usd_max_usdrates_two = round(usd_max_usdrates,3)
    usd_min_usdrates = min(usd_rates)
    usd_min_usdrates_two = round(usd_min_usdrates,3)
    text = "Maximum USD/THB Rates : "+str(usd_max_usdrates_two)+' ฿'+"\n"+"Minimum USD/THB Rates : "+str(usd_min_usdrates_two)+' ฿'
    label = tk.Label(Mainwindow, text= text,font=('helvetica', 10, 'bold'))
    canvas1.create_window(127, 410, window=label)

###THB to USD Currency###
def show_thbrates():
    text1 = "THB/USD Rates in "+ str(yesterday)+" : "+str(thb_usd_yesterday_3deci)+' $'+"\n"+"THB/USD Rates in "+ str(two_days_ago)+" : "+str(thb_usd_twodaysago_3deci)+' $'+"\n"+"THB/USD Rates in "+ str(three_days_ago)+" : "+str(thb_usd_threedaysago_3deci)+' $'+"\n"+"THB/USD Rates in "+ str(four_days_ago)+" : "+str(thb_usd_fourdaysago_3deci)+' $'+"\n"+"THB/USD Rates in "+ str(five_days_ago)+" : "+str(thb_usd_fivedaysago_3deci)+' $'
    label = tk.Label(Mainwindow, text= text1,font=('helvetica', 10, 'bold'))
    canvas1.create_window(450, 220, window=label)

def show_thb_avg_rates():
    thb_rates = (thb_usd_today,thb_usd_yesterday,thb_usd_twodaysago,thb_usd_threedaysago,thb_usd_fourdaysago,thb_usd_fivedaysago)
    thb_avg_rates = mean(thb_rates)
    usd_avg_rates_3deci = round(thb_avg_rates,3)
    text = str(usd_avg_rates_3deci) + ' $'
    label = tk.Label(Mainwindow, text= text,font=('helvetica', 10, 'bold'))
    canvas1.create_window(420, 335, window=label)

def show_thb_maxmin_rates():
    thb_rates = (thb_usd_today,thb_usd_yesterday,thb_usd_twodaysago,thb_usd_threedaysago,thb_usd_fourdaysago,thb_usd_fivedaysago)
    thb_max_rates = max(thb_rates)
    thb_max_rates_3deci = round(thb_max_rates,3)
    thb_min_rates = min(thb_rates)
    thb_min_rates_3deci = round(thb_min_rates,3)
    text = "Maximum THB/USD Rates : "+str(thb_max_rates_3deci)+' $'+"\n"+"Minimum THB/USD Rates : "+str(thb_min_rates_3deci)+' $'
    label = tk.Label(Mainwindow, text= text,font=('helvetica', 10, 'bold'))
    canvas1.create_window(427, 410, window=label)

canvas1 = tk.Canvas(Mainwindow, width = 600, height = 480)
canvas1.grid(row = 1, column = 0)   

label1 = tk.Label(Mainwindow, text='USD($) & THB(฿) Currency Rates Analysis')
label1.config(font=('helvetica', 14),bg = 'white')
canvas1.create_window(290, 40, window=label1)

label2 = tk.Label(Mainwindow, text=today_withtime)
label2.config(font=('helvetica', 14),bg = 'white')
canvas1.create_window(290, 70, window=label2)

usd_rates_today = "USD/THB Rates Today ("+ str(today)+") : "+str(usd_thb_today_2deci)+' ฿'
label3 = tk.Label(Mainwindow, text= usd_rates_today,font=('helvetica', 10, 'bold'),bg = 'white')
canvas1.create_window(145, 110, window=label3)

usd_rates_today = "THB/USD Rates Today ("+ str(today)+") : "+str(thb_usd_today_3deci)+' ฿'
label3 = tk.Label(Mainwindow, text= usd_rates_today,font=('helvetica', 10, 'bold'),bg = 'white')
canvas1.create_window(450, 110, window=label3)
            
Mainwindow.title("USD&THB RATES ANALYSIS")

button_1 = tk.Button(text='Show USD/TH Currency Rates\n (In the past 5 days)',command = show_usdrates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(125, 150, window=button_1)

button_2 = tk.Button(text='Show Average USD/TH Rates \n (In the past 5 days)',command = show_usd_avg_rates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(125, 300, window=button_2)

button_3 = tk.Button(text='Show Max&Min USD/TH Rates \n (In the past 5 days)',command = show_usd_max_rates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(127, 370, window=button_3)

button_4 = tk.Button(text='Show USD/TH Currency Rates\n (In the past 5 days)',command = show_thbrates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(425, 150, window=button_4)

button_5 = tk.Button(text='Show Average USD/TH Rates \n (In the past 5 days)',command = show_thb_avg_rates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(425, 300, window=button_5)

button_6 = tk.Button(text='Show Max&Min USD/TH Rates \n (In the past 5 days)',command = show_thb_maxmin_rates, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(427, 370, window=button_6)

button7 = tk.Button(text='Quit',command=Mainwindow.quit, bg='red', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(280, 455, window=button7)
Mainwindow.mainloop()
























































