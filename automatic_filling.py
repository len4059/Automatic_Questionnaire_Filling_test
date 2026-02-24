"""
This is a testing code written by Enoch Lu

Version - 3.1 (2026/02/24)

Disclaimer:
This script is provided "as is", without any warranty. 
The author assumes no responsibility for any damage, loss, 
or issues caused by using this script. Use at your own risk.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException, StaleElementReferenceException,
    ElementClickInterceptedException, JavascriptException
)

import tkinter as tk
from tkinter import font, messagebox

import time
from datetime import datetime, date

import os
import sys

EXPIRY_DATE = date(2026, 7, 31) 

age_hint = "不得小於18或大於99"
date_hint = "月/日/年（勿超過今日日期）"
times_hint = "執行完後自動關閉"

def enforce_expiry():
    today = date.today()
    if today > EXPIRY_DATE:
        os._exit(0)

enforce_expiry()

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")  
        entry.config(fg='black')

def on_focusout(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

RETRY_EXCEPTIONS = (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    JavascriptException
)

def do(driver, action, max_retry=20, wait_time=5):
    for attempt in range(1, max_retry + 1):
        try:
            return action()
        except RETRY_EXCEPTIONS as e:
            if attempt == max_retry:
                driver.refresh()
                raise  
            time.sleep(wait_time)  


def submit():
    global age, visit_date, times
    try:
        age = int(age_entry.get())
        if not 18 <= age <= 99:
            raise ValueError
        visit_date = date_entry.get()
        times = int(times_entry.get())
        if times <= 0:
            raise ValueError
    except ValueError:
        tk.messagebox.showerror("輸入錯誤", "請確認年齡、日期與次數")
        return
    window.destroy()
    auto()         


def auto():
    global times
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)       

    survey_url = "https://survey.medallia.com/?lego-retail-lcs&store=retail_20077&lng=zh_TW&fbclid=IwY2xjawE058NleHRuA2FlbQIxMAABHb4npEtLA9viddKcuL_4cbNwmejJgOiw0vRGnE6xrUBzS2aRZo5aCas8IA_aem_Cw0cH4HFZz7j31bIGqmXMA"

    driver.get(survey_url)

    while times > 0:

        driver.delete_all_cookies()

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonBegin")))
    
        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonBegin"))
        ).click())

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "spl_q_lego_global_age_txt")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "spl_q_lego_global_age_txt"))
        ).send_keys(age))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "cal_q_lego_retail_transaction_date_")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "cal_q_lego_retail_transaction_date_"))
        ).send_keys(str(visit_date)))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        do(driver, lambda: driver.execute_script("""
            const el = document.getElementById(arguments[0]);
            if (!el) { throw new Error('radio not ready'); }
            el.checked = true;
            el.dispatchEvent(new Event('change', {bubbles:true}));
        """, "onf_q_lego_global_ltr10_11"))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        do(driver, lambda: driver.execute_script("""
            const xpath = arguments[0];
            const el = document.evaluate(xpath, document, null,
                                        XPathResult.FIRST_ORDERED_NODE_TYPE, null
                                        ).singleNodeValue;
            if (!el) { throw new Error('noContact span not ready'); }
            el.scrollIntoView({block:'center'});
            el.click();
        """, '/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[3]/div/div/div/div[2]/span'))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        do(driver, lambda: driver.execute_script("""
            const xp = '/html/body/div/div/form/div/div[2]/div/fieldset/div/div/ul/li[1]/div/div/div/div[2]/span';
            const el = document.evaluate(xp, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (!el) { throw new Error('willing span not ready'); }
            el.scrollIntoView({block:'center'});
            el.click();
        """))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        SAT_IDS = [
            'onf_q_lego_retail_fun_in_store_sat10_11',
            'onf_q_lego_retail_greeting_recieved_sat10_11',
            'onf_q_lego_retail_timely_assistance_sat10_11',
            'onf_q_lego_retail_friendliness_staff_sat10_11',
            'onf_q_lego_retail_knowledgeable_staff_sat10_11',
            'onf_q_lego_retail_efficient_checkout_sat10_11',
            'onf_q_lego_retail_navigation_sat10_11',
            'onf_q_lego_retail_product_availability_sat10_11',
        ]

        def check_radio_by_id(driver, rid):
            # 等 radio 真正存在再動手
            el = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, rid))
            )
            driver.execute_script("""
                arguments[0].checked = true;
                arguments[0].dispatchEvent(new Event('change', {bubbles:true}));
            """, el)

        for rid in SAT_IDS:
            do(driver, lambda rid=rid: check_radio_by_id(driver, rid))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonNext"))
        ).click())

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonNext")))

        do(driver, lambda: WebDriverWait(driver, 60)
            .until(EC.element_to_be_clickable((By.ID, "buttonNext")))
            .click())

        time.sleep(0.5)

        do(driver, lambda: driver.execute_script("""
            const xp = '/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[2]/div/div/div/div[2]/span';
            const el = document.evaluate(xp, document, null,
                                        XPathResult.FIRST_ORDERED_NODE_TYPE, null
                                        ).singleNodeValue;
            if (!el) { throw new Error('no‑willing span not ready'); }
            el.scrollIntoView({block:'center'});
            el.click();
        """))

        time.sleep(0.5)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "buttonFinish")))

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonFinish"))
        ).click())

        time.sleep(0.5)

        do(driver, lambda: driver.execute_script(
            "window.location.href = arguments[0];", survey_url
        ))

        time.sleep(2)

        do(driver, lambda: WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "buttonBegin"))))

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