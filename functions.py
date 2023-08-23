import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

def getDataNum(driver):
    sleep(30)
    data = driver.find_elements(By.CLASS_NAME, 'etd_e')[1]
    num = data.text.replace(" ", "")
    return int(num)

def getOneData(driver, page_num, cookie, writer, system):
    print("=" * 66)
    # 這個就是每筆資料點進去的頁面連結
    print("send cookie: ", cookie)
    driver.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd={}/record?r1={}&h1=1'.format(cookie, page_num))
    print("send request url: ", 'https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd={}/record?r1={}&h1=1'.format(cookie, page_num))
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    # 論文名稱
    try:
        title = soup.find(text="論文名稱:").find_next('td').text
    except:
        title = ''
    print("論文名稱：" + title)
    
    # 學位類別
    try:
        degree = soup.find(text="學位類別:").find_next('td').text
    except:
        degree = ''
    print("學位類別：" + degree)

    # 研究生（作者）
    try:
        author = soup.find(text="研究生:").find_next('td').text
    except:
        author = ''
    print("作者：" + author)

    # 論文出版年
    try:
        year = soup.find(text="論文出版年:").find_next('td').text
    except:
        year = ""
    print("論文出版年：" + year)

    # 校系
    try:
        school = soup.find(text="校院名稱:").find_next('td').text
        department = soup.find(text="系所名稱:").find_next('td').text
    except:
        school = ''
        department = ''
    schoolDepartment = school + department
    print("校系：" + schoolDepartment)

    # 永久網址
    try:
        url = soup.find('input',{'id':'fe_text1'})['value']
    except:
        url = ''
    print("url：" + url)
    if(degree == '碩士'):
        degree = '04 學位論文-碩士'
    else:
        degree = '04 學位論文-博士'
    content = author + '（' + year + '）。' + title + '。' + schoolDepartment + '。取自網址：' + url
    row = ['', system.get_csv_name(), '臺灣', title, degree, author, '中文', year, schoolDepartment, '', '', 'URL', url, content]
    writer.writerow(row)

def crawlOneSystem(system, csvDir, cnt_all):
    cnt = 1
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get('https://ndltd.ncl.edu.tw/')
    sleep(2)
    driver.find_element(By.XPATH, '//a[@title="指令查詢"]').click()
    driver.find_element(By.ID, 'ysearchinput0').send_keys(system.get_req())
    driver.find_element(By.ID, 'gs32search').click()
    num = getDataNum(driver)

    # get the cookie whose key is "ccd"
    cookie = re.findall(r'ccd=(.*?)/', driver.current_url)[0]

    f = open(csvDir + system.get_csv_name()  + '.csv', 'w')
    writer = csv.writer(f)
    cookie_cnt = 0
    # crawl all data from one system result
    while cnt <= num:
        # get new cookie after too much request
        if cookie_cnt > 200:
            driver.get('https://ndltd.ncl.edu.tw/')
            sleep(2)
            driver.find_element(By.XPATH, '//a[@title="指令查詢"]').click()
            driver.find_element(By.ID, 'ysearchinput0').send_keys(system.get_req())
            driver.find_element(By.ID, 'gs32search').click()
            num = getDataNum(driver)
            # get the cookie whose key is "ccd"
            cookie = re.findall(r'ccd=(.*?)/', driver.current_url)[0]
            cookie_cnt = 0

        getOneData(driver, cnt, cookie, writer, system)
        cnt += 1
        cookie_cnt += 1
        cnt_all += 1
    f.close()
    driver.close()
    return cnt_all