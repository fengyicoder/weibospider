# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:57:31 2018

@author: flyfree
"""


import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re





import logging

logging.getLogger().setLevel(logging.INFO)


param = {}
param['username'] = input('请输入用户名/邮箱/电话:')
param['password'] = input('请输入密码:')

def weibospyder(aim):
    
    url = 'https://weibo.com/u/%d?is_all=1' %aim
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    
    #填写账号与密码
    driver.find_element_by_xpath("//ul[@class='gn_login_list']/li/a[@node-type='loginBtn']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys(param["username"])
    driver.find_element_by_name("password").send_keys(param["password"])
    #暂停10s，填写验证码
    flag = 1
    while flag:
        time.sleep(10)
        try:
            driver.find_element_by_xpath("//a[@class='W_btn_a btn_34px']").click()
        finally:
            time.sleep(5)
        try:
            driver.find_element_by_name("username") #判断是否正确登录
        except NoSuchElementException:
            flag = 0
    #微博昵称、微博数、粉丝数、关注数       
    aimname = driver.find_element_by_xpath("//div[@class='pf_username']/h1").text
    print(u'昵称： '+aimname)
    foll_num = driver.find_elements_by_tag_name("strong")[0].text
    print(u'关注数： '+foll_num)
    fan_num = driver.find_elements_by_tag_name("strong")[1].text
    print(u'粉丝数： '+fan_num)
    num = driver.find_elements_by_tag_name("strong")[2].text
    print(u'微博数： '+num)
    
    #获取微博内容及发布时间
    flag1 = 1
    ct = 1
    while flag1:
        try:
            driver.find_element_by_xpath('//a[@class="page next S_txt1 S_line1"]')
            break
        except:
            driver.execute_script('window.scrollBy(0,%d)' %(3000*ct))
            time.sleep(5)
            ct += 1
    driver.execute_script("document.getElementsByClassName('layer_menu_list W_scroll')[0].style.display='block'")
    page = driver.find_element_by_xpath('//div[@class="layer_menu_list W_scroll"]/ul/li[1]/a').text
    page_num = re.findall('\d+',page)
    pretime = []
    content = []
    for n in range(0,int(page_num[0])+1):
        driver.get(url+'&page=%d' %(n+1))
        flag1 = 1
        ct = 1
        while flag1:
            try:
                driver.find_element_by_xpath('//div[@class="W_pages"]/a[@class="page next S_txt1 S_line1"]')
                break
            except:
                driver.execute_script('window.scrollBy(0,%d)' %(3000*ct))
                time.sleep(3)
                ct += 1
                if ct == 5:   #到了尾页，跳出循环，经验判断，一页不会下拉到5次之多
                    break
                
        iter1 = driver.find_elements_by_xpath('//div[@class="WB_detail"]')
        for i in range(0,len(iter1)):
            pretime1 = iter1[i].find_element_by_xpath('div[@class="WB_from S_txt2"]/a[1]').text
            pretime.append(pretime1)
            print(u'发布时间: '+pretime1)
            content1 = iter1[i].find_element_by_xpath('div[@class="WB_text W_f14"]').text
            content.append(content1)
            print(u'发布内容: '+content1)
            
            
    #存储数据在文本中
    formation = '昵称：'+aimname+'\n' +'关注数:'+foll_num +','+'粉丝数:'+fan_num +','+'微博数:'+num+'\n'
    f = open('weibo.txt', "w",encoding='utf-8')
    f.write(formation)
    for k in range(len(content)):
        f.write("时间："+pretime[k]+'\n')
        f.write("内容："+content[k]+'\n')
    f.close()

    driver.close()
    
weibospyder(3979933883)




