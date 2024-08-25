### This is a testing code written by Enoch
#Version 1.0

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tkinter as tk
from tkinter import messagebox
from tkinter import font

import time

age_hint = "不得小於18或大於99"
date_hint = "月/日/年（勿超過今日日期）"
times_hint = "執行完後自動關閉"

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")  
        entry.config(fg='black')

def on_focusout(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def submit():
    global age, date, times
    age = int(age_entry.get())
    date = date_entry.get()
    times = int(times_entry.get())
    window.destroy()
    auto()


def auto():
    global times
    service = Service(exctable_path = "chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service)

    survey_url = "https://survey.medallia.com/?lego-retail-lcs&store=retail_20077&lng=zh_TW&fbclid=IwY2xjawE058NleHRuA2FlbQIxMAABHb4npEtLA9viddKcuL_4cbNwmejJgOiw0vRGnE6xrUBzS2aRZo5aCas8IA_aem_Cw0cH4HFZz7j31bIGqmXMA"

    driver.get(survey_url)

    while times > 0:
    
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonBegin"))
        )

        start_button.click()

        age_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "spl_q_lego_global_age_txt"))
        )

        age_input.send_keys(age)

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cal_q_lego_retail_transaction_date_"))
        )

        date_input.send_keys(date)

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        driver.execute_script("document.getElementById('onf_q_lego_global_ltr10_11').checked = true;")

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        no_contact = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[3]/div/div/div/div[2]/span'))
        )

        driver.execute_script("arguments[0].click();", no_contact)

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        willing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/div/div[2]/div/fieldset/div/div/ul/li[1]/div/div/div/div[2]/span'))
        )

        driver.execute_script("arguments[0].click();", willing)

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        driver.execute_script("document.getElementById('onf_q_lego_retail_fun_in_store_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_greeting_recieved_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_timely_assistance_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_friendliness_staff_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_knowledgeable_staff_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_efficient_checkout_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_navigation_sat10_11').checked = true;")
        driver.execute_script("document.getElementById('onf_q_lego_retail_product_availability_sat10_11').checked = true;")

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        )

        next_button.click()

        no_willing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[2]/div/div/div/div[2]/span'))
        )

        driver.execute_script("arguments[0].click();", no_willing)

        finish = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonFinish"))
        )

        finish.click()

        time.sleep(1)

        driver.execute_script("window.location.href='https://survey.medallia.com/?lego-retail-lcs&store=retail_20077&lng=zh_TW&fbclid=IwY2xjawE058NleHRuA2FlbQIxMAABHb4npEtLA9viddKcuL_4cbNwmejJgOiw0vRGnE6xrUBzS2aRZo5aCas8IA_aem_Cw0cH4HFZz7j31bIGqmXMA';")

        times -= 1

    driver.quit()

window = tk.Tk()
window.title("User Input")

label_font = font.Font(family='Helvetica', size=16, weight='bold')
entry_font = font.Font(family='Helvetica', size=14)
button_font = font.Font(family='Helvetica', size=14, weight='bold')

frame = tk.LabelFrame(window, text="請輸入自訂參數：", padx=20, pady=20, font=label_font, bg="#FFFFFF")
frame.grid(row=0, column=0, padx=20, pady=20)

tk.Label(frame, text = "填卷者年齡：", font=label_font, bg="#FFFFFF").grid(row = 0, column = 0, sticky = "e", pady = 10)
age_entry = tk.Entry(frame, font=entry_font, width=25)
age_entry.insert(0, age_hint)
age_entry.config(fg='grey') 
age_entry.bind('<FocusIn>', lambda event: on_entry_click(event, age_entry, age_hint))
age_entry.bind('<FocusOut>', lambda event: on_focusout(event, age_entry, age_hint))
age_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

tk.Label(frame, text="到訪日期 (MM/DD/YYYY)：", font=label_font, bg="#FFFFFF").grid(row=1, column=0, sticky = "e", pady = 10)
date_entry = tk.Entry(frame, font=entry_font, width=25)
date_entry.insert(0, date_hint)
date_entry.config(fg='grey')
date_entry.bind('<FocusOut>', lambda event: on_focusout(event, date_entry, date_hint))
date_entry.bind('<FocusIn>', lambda event: on_entry_click(event, date_entry, date_hint))
date_entry.grid(row=1, column=1, padx = 10, pady = 10)

tk.Label(frame, text="重複次數：", font=label_font, bg="#FFFFFF").grid(row=2, column=0, sticky = "e", pady = 10)
times_entry = tk.Entry(frame, font=entry_font, width=25)
times_entry.insert(0, times_hint)
times_entry.config(fg='grey')
times_entry.bind('<FocusIn>', lambda event: on_entry_click(event, times_entry, times_hint))
times_entry.bind('<FocusOut>', lambda event: on_focusout(event, times_entry, times_hint))
times_entry.grid(row=2, column=1, padx = 10, pady = 10)

submit_button = tk.Button(frame, text="送出", command=submit, font=button_font, bg="#003060", fg="white", width=10)
submit_button.grid(row = 3, column = 1, pady = 10)

window.mainloop()