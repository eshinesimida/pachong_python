# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:26:11 2019

@author: lenovo
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import random
import pymysql
import requests
from lxml import etree

connect = pymysql.Connect(
    host='rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='zd45+3=48',
    db='ctrip_gengxin',
    use_unicode=1,
    charset='utf8'
)
_css_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

Cookie = {'Cookie':'GANJISESSID=mal0ipes41v7k5mr9nmae3hei6; cityDomain=gz; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1571735042; Hm_lvt_acb0293cec76b2e30e511701c9bf2390=1571735042; lg=1; ganji_uuid=9176246665805161286300; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A61442912169%7D; __utma=32156897.928759174.1571735043.1571735043.1571735043.1; __utmc=32156897; __utmz=32156897.1571735043.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ganji_xuuid=9fbf6802-beb5-4b9d-e988-8230c8ec26cd.1571735043162; xxzl_deviceid=gEwsMOBBY9xSnC6PYlL5onCndIDB9SWdyLaw6WhffbEGINR7UKS1kg2E7eUi0yKa; sscode=VWW0wrdUIwqYia7OVWe6goJO; GanjiUserName=eshine12345; GanjiUserInfo=%7B%22user_id%22%3A811087461%2C%22email%22%3A%22%22%2C%22username%22%3A%22eshine12345%22%2C%22user_name%22%3A%22eshine12345%22%2C%22nickname%22%3A%22%22%7D; bizs=%5B%5D; supercookie=BQRkZQt3AQLkWQx4ZTV2LJD0AQHkLzL0AmuzLGR2BGRlLJMuMwIuAQAyL2AzAmV2ATD%3D; username_login_n=eshine12345; GanjiLoginType=0; xxzl_smartid=2243bc03cff31333024445bb2ae67d26; xzfzqtoken=LqLDE1Hu8TJ0fwickxM%2Fj26%2BZKwksoiKb%2BsMwYnE8d75eP6D6Z36omE47tWwzTS7in35brBb%2F%2FeSODvMgkQULA%3D%3D; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1571736055; __utmt=1; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1571736377; __utmb=32156897.10.10.1571735043; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1571736570; Hm_lpvt_acb0293cec76b2e30e511701c9bf2390=1571736570; ganji_login_act=1571736570166'}
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
#url = 'http://gz.ganji.com/qzshichangyingxiao/'

url = 'http://gz.ganji.com/qzshichangyingxiao/o31/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(30)

#eshine12345
#lxb454656783

crawlxiecheng()

 def crawlxiecheng():
    loopNum = 0
    ifHandle = False
    time.sleep(30)
        
    pageNum = 2800
    while(pageNum>=1):
            # 循环次数加1
        loopNum = loopNum + 1
            #if (len(re.findall('pkg_page',self.driver.page_source)) == 0):
              #  break

        target = driver.find_element_by_class_name(
                'pageBox')
        y = target.location['y']
            # print y
        y = y - 100
        print(y)

        js = "var q=document.documentElement.scrollTop=" + str(y)
        driver.execute_script(js)

        time.sleep(5)
         
        if u"下一页" in driver.page_source:

            if ifHandle == False:
                #doc = get_conment_page(page_source = driver.page_source,font_dict = font_dict)
                a = crawllianjie(driver.page_source)
                if(a ==2):
                    break
                ifHandle = True

            try:
                    #print u"下一页" in self.driver.page_source
                if u"下一页" in driver.page_source:
                    pageNum = pageNum - 1
                        #self.driver.maximize_window()
                        #self.driver.implicitly_wait(30)
                    driver.find_element_by_partial_link_text("下一页").click()
                        #self.driver.find_element_by_xpath("//div[@class='weiboitem active']/div[@class='comment_ctrip']/div[@class='ttd_pager cf']/div[@class='pager_v1']/a[@class='nextpage']").click()
                    ifHandle = False
                    loopNum = 0

                    time.sleep(3)
                    print ("页数：" + str(pageNum))
                        #print 'num =' + num, type(int(num))
                    num1 = 2800 - pageNum + 1
                    print ('num1 = ' + str(num1))


            except:
                pageNum = pageNum + 1
    return False if pageNum > 1 else True

def crawllianjie(doc = driver.page_source):
    response1 = HtmlResponse(url="my HTML string", body=doc, encoding="utf-8")

    A = response1.xpath("//dl[@class='list-noimg job-j-list clearfix job-new-list']")
    
    for B in A:
        ID = B.xpath('@pt').extract()[0]
        
        href = B.xpath('a/@href').extract()[0]
        href = 'http://gz.ganji.com' + href
        name = B.xpath('a/dt[@class = "fl per-info"]/div/div[@class="basic-info"]/span[@class="name"]/text()').extract()[0]
        sex = B.xpath('a/dt[@class = "fl per-info"]/div/div[@class="basic-info"]/span[2]/text()').extract()[0]
        age = B.xpath('a/dt[@class = "fl per-info"]/div/div[@class="basic-info"]/span[3]/text()').extract()[0]
        xueli = B.xpath('a/dt[@class = "fl per-info"]/div/div[@class="basic-info"]/span[4]/text()').extract()
        if(xueli):
            xueli = xueli[0]
        else:
            xueli = 'none'
        jingli = B.xpath('a/dt[@class = "fl per-info"]/div/div[@class="basic-info"]/span[5]/text()').extract()
        if(jingli):
            jingli = jingli[0]
        else:
            jingli = 'none'
        
        address = B.xpath('a/div[@class="fl district-salary"]/p[@class="district"]/text()').extract()[0]
        salary = B.xpath('a/div[@class="fl district-salary"]/p[@class="salary"]/text()').extract()[0]
        address = address.strip()
        salary = salary.strip()
        time1 = B.xpath('a/div[@class="order fr"]/text()').extract()[0]
        time1 = time1.strip()
        
        
        time.sleep(7)
        res = requests.get(href, headers=head, cookies = Cookie)
        html = res.text
        
        doc = etree.HTML(str(html))
        try:
            A1 = doc.xpath('//div[@class="tend-line clearfix"]/b/a')
            qiuzhi = []
            for B1 in A1:
                i = B1.xpath('text()')
                if(i):
                    i = i[0]
                else:
                    i = 'none'
                
                qiuzhi.append(i)
            qiuzhi = ','.join(qiuzhi)
        except:
            qiuzhi = 'none'
        
        try:
            work_exp1 = doc.xpath('//div[@class="experience-block"]/p/text()')
            exp = []
            if(work_exp1):
                work_exp1 = work_exp1[0]
                exp.append(work_exp1)
                didian = doc.xpath('//div[@class="experience-block"]/b')
                content = doc.xpath('//div[@class="experience-block"]/ul')
                for m,n in zip(didian,content):
                    company = m.xpath('text()')[0]
                    time2 = n.xpath('li[1]/p/text()')[0]
                    time3 = n.xpath('li[1]/p/i/text()')[0]
                    
                    zhiwei = n.xpath('li[2]/p/text()')[0]
                    work_content = n.xpath('li[3]/p/text()')
                    if(work_content):
                        work_content = work_content[0]
                    else:
                        work_content = 'none'
                    he = ','.join([company,time2,time3,zhiwei,work_content])
                    exp.append(he)
                exp = ','.join(exp)
            else:
                exp = 'none'
        except:
            exp = 'none'
        #print(exp)
        
        try:
            edu = doc.xpath('//div[@class="education-block"]/table/tbody/tr')
            if(edu):
                edu1 = []
                for a in edu:
                    i1 = a.xpath('td[1]/text()')[0]
                    i2 = a.xpath('td[2]/text()')
                    if(i2):
                        i2 = i2[0]
                    else:
                        i2 = 'none'
                    i3 = a.xpath('td[3]/text()')
                    if(i3):
                        i3 = i3[0]
                    else:
                        i3 = 'none'
                    i4 = ','.join([i1,i2,i3])
                    edu1.append(i4)
                edu1 = ','.join(edu1)
            else:
                edu1 = 'none'
        except:
            edu1 = 'none'
            
        
        try:    
            zhengshu = doc.xpath('//div[@class="project-block"]/table/tbody/tr')
            if(zhengshu):
                zhengshu1 = []
                for a in zhengshu:
                    i1 = a.xpath('td[1]/text()')[0]
                    i2 = a.xpath('td[2]/text()')
                    if(i2):
                        i2 = i2[0]
                    else:
                        i2 = 'none'
                    i3 = a.xpath('td[3]/text()')
                    if(i3):
                        i3 = i3[0]
                    else:
                        i3 = 'none'
                    i4 = ','.join([i1,i2,i3])
                    zhengshu1.append(i4)
                zhengshu1 = ','.join(zhengshu1)
            else:
                zhengshu1 = 'none'
        except:
            zhengshu1 = 'none'
            
        self1 = doc.xpath('//div[@class="self-block"]/div/text()')
        if(self1):
            self1 = self1[0]
        else:
            self1 = 'none'
            
        print(name,time1,qiuzhi)
        #print(ID,name,sex,age,xueli,jingli,address,salary,time1, href,
          #    exp, edu1, zhengshu1, self1)
        
        cursor = connect.cursor()

       
        sql = "INSERT IGNORE INTO ganji(ID,name,sex,age,xueli,jingli,address,salary,time1, href, exp, edu1, zhengshu1, self1,qiuzhi) VALUES ( '%s', '%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s', '%s','%s','%s', '%s','%s'  )"
        data = (ID,name,sex,age,xueli,jingli,address,salary,time1, href,
              exp, edu1, zhengshu1, self1, qiuzhi)
        try:
            cursor.execute(sql % data)
        except:
            print(ID)

        connect.commit()
    
        